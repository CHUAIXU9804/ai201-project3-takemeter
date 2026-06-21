import time
import re
import requests
import pandas as pd
from pathlib import Path

SUBREDDIT = "BaldursGate3"
CSV_FILE = "bg3_raw_candidates_1.csv"

MIN_WORDS = 30
LIMIT = 100
SLEEP_SECONDS = 2

TARGET_NEEDED = {
    "experience": 100,
    "mechanics": 150,
    "narrative": 150
}

SEARCH_TERMS = {
    "mechanics": [
        "build", "multiclass", "class", "damage", "honour mode",
        "combat", "gear", "spell", "feat", "paladin", "sorcerer",
        "fighter", "warlock", "bard", "monk", "tactician"
    ],
    "narrative": [
        "Astarion", "Shadowheart", "Karlach", "Gale", "Wyll",
        "Lae'zel", "Minthara", "ending", "romance", "lore",
        "story", "choice", "Durge", "dark urge", "companion"
    ],
    "experience": [
        "first playthrough", "finally", "TIL", "today I learned",
        "after 100 hours", "after 50 hours", "I accidentally",
        "discovered", "finished", "funny", "my first run",
        "I just realized", "I didn't know"
    ]
}

HEADERS = {
    "User-Agent": "BG3ClassificationProject/1.0 by student"
}


def normalize_text(text):
    text = str(text).lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()


# Load existing file
path = Path(CSV_FILE)

if path.exists():
    existing_df = pd.read_csv(path)
    print(f"Loaded existing CSV with {len(existing_df)} rows.")
else:
    existing_df = pd.DataFrame(columns=[
        "text", "label", "notes", "source_url", "candidate_label", "search_term"
    ])
    print("No existing CSV found. Creating a new one.")

for col in ["text", "label", "notes", "source_url", "candidate_label", "search_term"]:
    if col not in existing_df.columns:
        existing_df[col] = ""

existing_urls = set(existing_df["source_url"].dropna().astype(str))
existing_texts = set(existing_df["text"].dropna().astype(str).apply(normalize_text))


def search_reddit_community(search_term, candidate_label):
    url = f"https://www.reddit.com/r/{SUBREDDIT}/search.json"

    params = {
        "q": search_term,
        "restrict_sr": "1",
        "sort": "relevance",
        "t": "all",
        "limit": LIMIT
    }

    response = requests.get(url, headers=HEADERS, params=params, timeout=30)

    if response.status_code == 429:
        print("Rate limited. Sleeping longer...")
        time.sleep(10)
        return []

    response.raise_for_status()
    data = response.json()

    posts = []

    for item in data.get("data", {}).get("children", []):
        post = item.get("data", {})

        title = post.get("title", "")
        body = post.get("selftext", "")
        permalink = post.get("permalink", "")

        if not permalink:
            continue

        source_url = "https://www.reddit.com" + permalink

        if source_url in existing_urls:
            continue

        if not body or body in ["[deleted]", "[removed]"]:
            continue

        if len(body.split()) < MIN_WORDS:
            continue

        full_text = f"{title}\n\n{body}"
        normalized = normalize_text(full_text)

        if normalized in existing_texts:
            continue

        posts.append({
            "text": full_text,
            "label": "",
            "notes": "",
            "source_url": source_url,
            "candidate_label": candidate_label,
            "search_term": search_term
        })

        existing_urls.add(source_url)
        existing_texts.add(normalized)

    return posts


all_new_posts = []
added_counts = {label: 0 for label in TARGET_NEEDED}

for candidate_label, needed in TARGET_NEEDED.items():
    print(f"\nCollecting likely {candidate_label} posts...")

    for term in SEARCH_TERMS[candidate_label]:
        if added_counts[candidate_label] >= needed:
            break

        print(f"Searching r/{SUBREDDIT} for: {term}")

        try:
            results = search_reddit_community(term, candidate_label)

            remaining = needed - added_counts[candidate_label]
            results = results[:remaining]

            all_new_posts.extend(results)
            added_counts[candidate_label] += len(results)

            print(f"Added {len(results)} posts. Progress: {added_counts[candidate_label]}/{needed}")

        except Exception as e:
            print(f"Error on term '{term}': {e}")

        time.sleep(SLEEP_SECONDS)


new_df = pd.DataFrame(all_new_posts)

combined_df = pd.concat([existing_df, new_df], ignore_index=True)

combined_df["normalized_text"] = combined_df["text"].apply(normalize_text)
combined_df = combined_df.drop_duplicates(subset=["source_url"], keep="first")
combined_df = combined_df.drop_duplicates(subset=["normalized_text"], keep="first")
combined_df = combined_df.drop(columns=["normalized_text"])

combined_df.to_csv(CSV_FILE, index=False)

print("\nDone.")
print(f"New posts added: {len(new_df)}")
print(f"Total rows now: {len(combined_df)}")
print(f"Saved to: {CSV_FILE}")

print("\nNew candidate counts:")
print(pd.Series(added_counts))

print("\nOverall candidate label counts:")
print(combined_df["candidate_label"].value_counts(dropna=False))
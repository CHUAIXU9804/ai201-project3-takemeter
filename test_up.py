import time
import re
import requests
import pandas as pd
from pathlib import Path

SUBREDDIT = "BaldursGate3"
CSV_FILE = "bg3_raw_candidates_1.csv"

MIN_WORDS = 15
POSTS_PER_SEARCH = 100
SLEEP_SECONDS = 1

TARGET_NEEDED = {
    "experience": 100,
    "mechanics": 150,
    "narrative": 150
}

SEARCH_TERMS = {
    "mechanics": [
        "build", "multiclass", "class", "feat", "spell", "combat",
        "damage", "honour mode", "tactician", "gear", "equipment",
        "strategy", "optimization", "sorcerer", "warlock", "fighter",
        "paladin", "bard", "monk", "rogue", "cleric"
    ],
    "narrative": [
        "Astarion", "Shadowheart", "Karlach", "Gale", "Wyll",
        "Laezel", "Lae'zel", "Minthara", "romance", "ending",
        "epilogue", "lore", "story", "choice", "character",
        "companion", "dark urge", "durge", "emperor", "orpheus"
    ],
    "experience": [
        "finally", "TIL", "today I learned", "after 100 hours",
        "after 50 hours", "my first playthrough", "first run",
        "I accidentally", "I discovered", "I just realized",
        "funny", "unexpected", "finished", "beat", "achievement"
    ]
}


def normalize_text(text):
    text = str(text).lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()


def load_existing_csv(csv_file):
    path = Path(csv_file)

    if path.exists():
        df = pd.read_csv(path)
        print(f"Loaded existing CSV with {len(df)} rows.")
    else:
        df = pd.DataFrame(columns=[
            "text", "label", "notes", "source_url", "candidate_label", "search_term"
        ])
        print("No existing CSV found. Creating a new one.")

    for col in ["text", "label", "notes", "source_url", "candidate_label", "search_term"]:
        if col not in df.columns:
            df[col] = ""

    return df


def search_pullpush(search_term, candidate_label, existing_urls, existing_texts):
    url = "https://api.pullpush.io/reddit/search/submission/"

    params = {
        "subreddit": SUBREDDIT,
        "q": search_term,
        "size": POSTS_PER_SEARCH,
        "sort": "desc",
        "sort_type": "created_utc"
    }

    response = requests.get(url, params=params, timeout=30)

    print(f"Status code: {response.status_code}")

    if response.status_code != 200:
        print(response.text[:500])
        return []

    json_data = response.json()
    data = json_data.get("data", [])

    print(f"PullPush returned {len(data)} raw posts for '{search_term}'")

    new_posts = []

    skipped = {
        "duplicate_url": 0,
        "missing_body": 0,
        "deleted_removed": 0,
        "too_short": 0,
        "duplicate_text": 0
    }

    for post in data:
        title = post.get("title", "")
        body = post.get("selftext", "")
        source_url = post.get("full_link", "")

        if not source_url:
            post_id = post.get("id", "")
            if post_id:
                source_url = f"https://www.reddit.com/r/{SUBREDDIT}/comments/{post_id}/"

        if not source_url or source_url in existing_urls:
            skipped["duplicate_url"] += 1
            continue

        if not body:
            skipped["missing_body"] += 1
            continue

        if body in ["[deleted]", "[removed]"]:
            skipped["deleted_removed"] += 1
            continue

        full_text = f"{title}\n\n{body}"

        if len(full_text.split()) < MIN_WORDS:
            skipped["too_short"] += 1
            continue

        normalized = normalize_text(full_text)

        if normalized in existing_texts:
            skipped["duplicate_text"] += 1
            continue

        new_posts.append({
            "text": full_text,
            "label": "",
            "notes": "",
            "source_url": source_url,
            "candidate_label": candidate_label,
            "search_term": search_term
        })

        existing_urls.add(source_url)
        existing_texts.add(normalized)

    print("Skipped:", skipped)
    print(f"Usable new posts from '{search_term}': {len(new_posts)}")

    return new_posts


existing_df = load_existing_csv(CSV_FILE)

existing_urls = set(existing_df["source_url"].dropna().astype(str))
existing_texts = set(
    existing_df["text"]
    .dropna()
    .astype(str)
    .apply(normalize_text)
)

all_new_posts = []
added_counts = {label: 0 for label in TARGET_NEEDED}

for candidate_label, target_count in TARGET_NEEDED.items():
    print(f"\n===== Collecting likely {candidate_label} posts =====")

    for term in SEARCH_TERMS[candidate_label]:
        if added_counts[candidate_label] >= target_count:
            break

        print(f"\nSearching: {term}")

        try:
            results = search_pullpush(
                search_term=term,
                candidate_label=candidate_label,
                existing_urls=existing_urls,
                existing_texts=existing_texts
            )

            remaining = target_count - added_counts[candidate_label]
            results = results[:remaining]

            all_new_posts.extend(results)
            added_counts[candidate_label] += len(results)

            print(f"Progress for {candidate_label}: {added_counts[candidate_label]}/{target_count}")

        except Exception as e:
            print(f"Error searching '{term}': {e}")

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
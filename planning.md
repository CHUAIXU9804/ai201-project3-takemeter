# Community: r/BaldursGate3

The community I chose is r/BaldursGate3. I chose this community because it's a large and active gaming community that have a lot of discussions about the game's character builds, story plot, moral decisions, and game mechanics. This community is a good fit for a classification task because the discourse is diverse and contains several distinct communication styles - game mechanics, narrative, seeking for advice, and sharing game experience. This provides clear decision boundaries for annotation, and some posts may also contain elements of multiple categories.

# Labels

## mechanics

Players evaluate gameplay systems, builds, classes, combat mechanics, item interactions, or optimization strategies using reasonsing and logic.

### Example 1
**Terrified of House of Hope HM**  
https://www.reddit.com/r/BaldursGate3/comments/1uajpqv/terrified_of_house_of_hope_hm/

### Example 2
**Why couldn't the party just cure their parasites Postmortem?**  
https://www.reddit.com/r/BaldursGate3/comments/1u6xmco/why_couldnt_the_party_just_cure_their_parasites/

---

## narrative

Players interpret or evaluate about characters, story events, lore, relationships, themes, or moral choices.

### Example 1
**This game made me see how easy it is to be a good person**  
https://www.reddit.com/r/BaldursGate3/comments/1u5vfra/this_game_made_me_see_how_easy_it_is_to_be_a_good/

### Example 2
**Leading the army to the Grove is infinitely more satisfying**  
https://www.reddit.com/r/BaldursGate3/comments/1u6wdr6/leading_the_army_to_the_grove_is_infinitely_more/

---

## advice

Players seek for help or solutions on technical issues, gameplay, build, or guest help.

### Example 1
**Unable to download specific mods**  
https://www.reddit.com/r/BaldursGate3/comments/1ubt89w/unable_to_download_specific_mods/

### Example 2
**Even after 50+ hours gearing is still confusing to me**  
https://www.reddit.com/r/BaldursGate3/comments/1uaqgo9/even_after_50_hours_gearing_is_still_confusing_to/

---

## experience

Players share personal gameplay experience, discovery, achievement, or emotional moment.

### Example 1
**TIL hurling MC's jars into the ocean doesn't destroy them**  
https://www.reddit.com/r/BaldursGate3/comments/1ub7d7o/til_hurling_mcs_jars_into_the_ocean_doesnt/

### Example 2
**Respec Minthara - found something**  
https://www.reddit.com/r/BaldursGate3/comments/1u7osvy/respec_minthara_found_something/

# Hard Edge Cases

One type of the most common edge cases is the one that combines personal gameplay experience with a request for advice. For example, a player may describe their game experience, also request for beginner guidance and resources. Such posts could be labeled as either experience or advice.

To handle this, I will label posts based on their primary communication intent. For this example, I'll associate the post with the advice label, although the original poster has shared a lot of their gaming experience, but the ultimate idea of this post is to seek help for an beginner-friendly guide that provide guidance on the recommended levels needed to defeat specific quests/enemlies.

### Example

**I am so new and so dumb**  
https://www.reddit.com/r/BaldursGate3/comments/1ub4rwi/i_am_so_new_and_so_dumb/

# Data Collection Plan

I will collect examples from the BaldursGate3 Reddit Community. I will collect approximately 50 examples per label. If a label is underrepresented after 200 examples, I will perform targeted sampling by searching for posts that are likely to belong to that category, helping to maintain a balanced dataset and prevents the classifier from becoming biased toward majority classes.

# Evaluation Metrics

I will evaluate the classifier using Accuracy, Precision, Recall, and F1-score.

- **Accuracy** - represents the overall percentage of correctly classified posts.
- **Precision** - measures how often a predicted label is correct. This is important because incorrectly labeling posts could reduce trust in the system.
- **Recall** - measures how many posts belonging to a class are successfully identified. This is important because missing entire categories of posts would reduce the usefulness of the classifier.
- **F1-score** - balances Precision and Recall, and provides a more complete measure of performance when categories may not be perfectly balanced.

# Definition of Success

I would consider the classifier successful if it achieves the following:

- Accuracy > 75%
- Macro F1-score > 0.7
- Precision and Recall > 0.7 for each label
- No category with an F1-score < 0.6

For deployment in a real community tool, I consider:

- Accuracy > 0.85
- F1-score > 0.85
- Precision > 0.85
- Recall > 0.85

to be "good enough", which typically means that the classifier performs consistently across all categories rather than only on the largest categories.

# AI Tool
## Label Stress Testing

These posts are intentionally written to sit on the boundary between two labels. Each one contains genuine signals of both categories, so the "correct" label depends on identifying the *primary communication intent* (the same tie-breaking rule used in the Hard Edge Cases section). For each post I note the two competing labels and the reasoning that resolves it.

### Post 1 — mechanics vs. advice
**Is a 12 STR Throwzerker actually viable on Tactician or am I dreaming?**  
"I've theorycrafted a Tactician throw build around Tavern Brawler + the Returning Pike, and on paper the damage scales with STR so a 12 STR dip seems fine. I've laid out the math below. But before I commit a respec, can anyone who's actually run this confirm whether it holds up against the harder fights, or am I missing something?"

- **Competing labels:** *mechanics* (the post reasons about build scaling, modifiers, and item interactions) vs. *advice* (it ends by explicitly asking others to validate before committing).
- **Resolution → advice.** The reasoning is in service of a request for confirmation; the primary intent is to get help deciding, not to share an analysis. If the post had simply presented the math as a conclusion, it would be *mechanics*.

### Post 2 — narrative vs. experience
**The Shadowheart cliff scene wrecked me and I need to talk about it**  
"I finally hit the moment where Shadowheart chooses at the cliff. I sat there for a full minute after. It made me reflect on how the whole act has been building her arc around trauma and forgiveness, and why the writers framed the choice the way they did."

- **Competing labels:** *experience* (a personal, emotional gameplay moment the player is sharing) vs. *narrative* (interpretation of character arc, themes, and authorial intent).
- **Resolution → narrative.** Although it opens as a personal reaction, the substance is an interpretation of the character's arc and the writers' thematic choices. The emotional framing is the hook, not the point. A version that stopped at "I sat there for a full minute" would be *experience*.

### Post 3 — experience vs. mechanics
**TIL you can chain-shove enemies off the Grymforge bridge for free kills**  
"Was messing around last night and accidentally discovered you can shove an enemy into another one and knock the whole group off the Grymforge ledge. Felt amazing watching three duergar just fall. I think it works because shove pushes along the movement vector, so positioning them in a line matters."

- **Competing labels:** *experience* (a personal discovery and the excitement of pulling it off) vs. *mechanics* (an explanation of *why* the shove interaction works).
- **Resolution → experience.** The core of the post is sharing a fun discovery moment ("felt amazing"); the mechanical note is a tacked-on guess, not a reasoned optimization. Had the player led with analyzing shove vectors and positioning as a strategy, it would lean *mechanics*.

### Post 4 — advice vs. mechanics
**Which caster gets the most out of the Markoheshkir + Spellsparkler combo?**  
"I have both Markoheshkir and the Spellsparkler and I'm trying to figure out which of my casters should hold what. I know Spellsparkler stacks lightning charges and Markoheshkir's Bolt of Lightning benefits from them, but I'm not sure if it's better on Gale or on a Tempest cleric. What would you do?"

- **Competing labels:** *mechanics* (item synergy, charge stacking, damage interactions) vs. *advice* (asking which character to assign gear to).
- **Resolution → advice.** The post demonstrates mechanical knowledge but its purpose is a "what would you do" decision request. The mechanics are context for the question, not the deliverable.

### Post 5 — narrative vs. mechanics
**Did the Emperor manipulate me, or did I just play badly?**  
"Looking back on my run, I let the Emperor talk me into the deal at the Astral Prism, and I lost Orpheus as a result. I can't tell if that was the narrative punishing a 'wrong' moral choice, or if I just didn't have the right approval/conditions met mechanically to get the better outcome."

- **Competing labels:** *narrative* (moral choice, character manipulation, story consequence) vs. *mechanics* (whether outcome was gated by approval thresholds and conditions).
- **Resolution → narrative.** The driving question is about the *meaning* of the choice and whether the story framed it as a moral failure — a narrative interpretation. The mechanical angle is raised but secondary. If the post primarily asked "what conditions unlock the good ending," it would shift toward *advice* or *mechanics*.

### Post 6 — experience vs. advice
**Just beat Honour Mode after 4 failed runs — here's what finally clicked (and a question)**  
"After four wipes I finally got the golden dice. Honestly I'm still shaking. The thing that turned it around was finally respeccing into a control-heavy party. One thing I'm still unsure about for my next run though — is going full caster comp overkill, or should I keep a martial?"

- **Competing labels:** *experience* (celebrating an achievement, emotional payoff) vs. *advice* (the closing question about future party comp).
- **Resolution → experience.** The overwhelming bulk and intent of the post is to share the achievement and emotional moment; the question is a minor afterthought. This is the mirror image of the Hard Edge Cases example — there the request was the ultimate point, here the celebration is.

### Post 7 — narrative vs. advice
**Should I side with the Emperor or free Orpheus? Trying not to spoil myself on which is more 'good'**  
"I'm at the endgame decision and genuinely torn. I don't want a mechanical min-max answer — I want to know, thematically, which choice the story treats as the more heroic or morally consistent one given how Orpheus and the Emperor are written. Without major spoilers, which path do people find more narratively satisfying?"

- **Competing labels:** *advice* (a direct "which should I choose" question) vs. *narrative* (the question is explicitly about themes, moral framing, and characterization).
- **Resolution → advice.** Despite the heavy narrative vocabulary, the post is a help request seeking a recommendation for a decision the player must make. The narrative framing scopes the question but doesn't change its intent. This pairing is the hardest of the set because the surface vocabulary points one way and the intent the other.

## Annotation Assistance

I will use Claude AI to generate an initial label prediction for a subset of posts. Each prediction will be manually reviewed before being added to the dataset.

Examples that receive AI-generated labels will be tracked in a separate column within the annotation file. This will allow me to disclose which examples were AI-assisted in the final AI usage report and compare AI-generated labels with my final annotations.

## Failure Analysis

After evaluating the classifier, I will collect the posts that were misclassified and provide them to AI for analysis. I will ask the AI to identify common patterns among the errors, such as labels that are frequently confused with one another or characteristics shared by incorrectly classified posts.
Such as: 
- Confusion between advice and experience posts.
- Confusion between narrative and mechanics posts.
- Posts that contain multiple communication intents.
- Posts where the title suggests one category while the body suggests another.

Any patterns suggested by the AI, I will manually verify by reviewing the original posts and comparing them with the confusion matrix. I will treat the AI-generated observations as hypotheses rather than conclusions.
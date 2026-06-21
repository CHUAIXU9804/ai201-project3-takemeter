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

### Example 1

**I am so new and so dumb**  
Hey guys. Not new to video games but brand new to BG and also turn based style games. (Started my first DND campaign a few months ago, so I know a tiny bit about that part!) I am loving the game so far but there's so much content and so many options that I keep getting side tracked, confused, and beaten by enemies I'm not good enough to beat yet. This will probably sound dumb, but is there a guide available for newbies that is really simple and straightforward? For example, I'm currently working on the issue of the Grove and freeing the people there, which led me to the swamps, which led me to the teahouse, which led me to Aunty, which led me to that whole situation (trying not to give any spoliers) and I can't win that battle yet so I spent a bunch of time on it and then realized I probably don't even need to deal with that right now to continue on with the quest I was working on🤦🏻‍♀️ I want to eventually do a playthrough where I do absolutely everything in this game, I love all the content, but I'm finding it a bit overwhelming as a newbie, mostly because I need better skills to be able to beat some of the enemies I encounter which leads to me avoiding certain things. So if there is a guide that can help really new players and kind of "explains like I'm five", that would be awesome. Thank you in advance!

### A combination of experience and advice. I've determined this to be advice, because the main intention is to get advice on a guide.

### Example 2

Killed Karlach, not for Wyll but for my party

&gt;!I'm playing on single sace tactician rn, and I met up with Karlach before progressing much in Act 1 or the grove. She asked for help killing the fake paladins of tyr, and it took several teies being a bit under-levelled but the party finally killed them all. Unfortunately, the party was on death's door and Karlach's rampage knocked down Gale and Astarion twice as we tried to leave, and killed Astarion at one point, which cost a resurrection scroll. I know the rampage happens, but I was still kinda pissed that Karlach's character was causing damage to the party and ended up killing someone. When I talkedto her afterwards, the only dialogue options available were sympathetic ones asking if she's doing alright. This pissed me off even more, cuz I had hoped I could at least say something along the lines of 'Hey, you just put your own team in danger back there' or 'That was a little intimidating to watch, can we trust that you won't be a harm to the party?' IDK something like that, but nope. You just have to pity and empathize. So I ended up killing her, justifying as the party seeing her as a crazed loose cannon. I ended up resurrecting her at camp, but no dialogue on the killing her, just an annoyed 'What.' when I speak to her. She can stay at camp and get f@&amp;$ed by her engine for all I care, her dialogue options just feel way too limited, and the game seems to really want you, and at times force you, to take her side.!&lt;

AITA? (I know I am)

### A combination of advice and narrative. I've determined this to be narrative, because it involves a lot of discussion around narrative.

Example 3:
Knockout

Does fainting NPC instead of killing change anything in the story?

For example, I didn't kill Gortash's mother, instead I left her unconscious, does that change anything or will the game treat her as dead anyway?

### A combination of advice and narrative. I've determined this to be narrative, because the poster is not seeking for advice, but wondering how does their action impact the story development relating to a character.

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

These posts are intentionally written to sit on the boundary between two labels. Each one contains genuine signals of both categories, so the "correct" label depends on identifying the _primary communication intent_ (the same tie-breaking rule used in the Hard Edge Cases section). For each post I note the two competing labels and the reasoning that resolves it.

### Post 1 — mechanics vs. advice

**Is a 12 STR Throwzerker actually viable on Tactician or am I dreaming?**  
"I've theorycrafted a Tactician throw build around Tavern Brawler + the Returning Pike, and on paper the damage scales with STR so a 12 STR dip seems fine. I've laid out the math below. But before I commit a respec, can anyone who's actually run this confirm whether it holds up against the harder fights, or am I missing something?"

- **Competing labels:** _mechanics_ (the post reasons about build scaling, modifiers, and item interactions) vs. _advice_ (it ends by explicitly asking others to validate before committing).
- **Resolution → advice.** The reasoning is in service of a request for confirmation; the primary intent is to get help deciding, not to share an analysis. If the post had simply presented the math as a conclusion, it would be _mechanics_.

### Post 2 — narrative vs. experience

**The Shadowheart cliff scene wrecked me and I need to talk about it**  
"I finally hit the moment where Shadowheart chooses at the cliff. I sat there for a full minute after. It made me reflect on how the whole act has been building her arc around trauma and forgiveness, and why the writers framed the choice the way they did."

- **Competing labels:** _experience_ (a personal, emotional gameplay moment the player is sharing) vs. _narrative_ (interpretation of character arc, themes, and authorial intent).
- **Resolution → narrative.** Although it opens as a personal reaction, the substance is an interpretation of the character's arc and the writers' thematic choices. The emotional framing is the hook, not the point. A version that stopped at "I sat there for a full minute" would be _experience_.

### Post 3 — experience vs. mechanics

**TIL you can chain-shove enemies off the Grymforge bridge for free kills**  
"Was messing around last night and accidentally discovered you can shove an enemy into another one and knock the whole group off the Grymforge ledge. Felt amazing watching three duergar just fall. I think it works because shove pushes along the movement vector, so positioning them in a line matters."

- **Competing labels:** _experience_ (a personal discovery and the excitement of pulling it off) vs. _mechanics_ (an explanation of _why_ the shove interaction works).
- **Resolution → experience.** The core of the post is sharing a fun discovery moment ("felt amazing"); the mechanical note is a tacked-on guess, not a reasoned optimization. Had the player led with analyzing shove vectors and positioning as a strategy, it would lean _mechanics_.

### Post 4 — advice vs. mechanics

**Which caster gets the most out of the Markoheshkir + Spellsparkler combo?**  
"I have both Markoheshkir and the Spellsparkler and I'm trying to figure out which of my casters should hold what. I know Spellsparkler stacks lightning charges and Markoheshkir's Bolt of Lightning benefits from them, but I'm not sure if it's better on Gale or on a Tempest cleric. What would you do?"

- **Competing labels:** _mechanics_ (item synergy, charge stacking, damage interactions) vs. _advice_ (asking which character to assign gear to).
- **Resolution → advice.** The post demonstrates mechanical knowledge but its purpose is a "what would you do" decision request. The mechanics are context for the question, not the deliverable.

### Post 5 — narrative vs. mechanics

**Did the Emperor manipulate me, or did I just play badly?**  
"Looking back on my run, I let the Emperor talk me into the deal at the Astral Prism, and I lost Orpheus as a result. I can't tell if that was the narrative punishing a 'wrong' moral choice, or if I just didn't have the right approval/conditions met mechanically to get the better outcome."

- **Competing labels:** _narrative_ (moral choice, character manipulation, story consequence) vs. _mechanics_ (whether outcome was gated by approval thresholds and conditions).
- **Resolution → narrative.** The driving question is about the _meaning_ of the choice and whether the story framed it as a moral failure — a narrative interpretation. The mechanical angle is raised but secondary. If the post primarily asked "what conditions unlock the good ending," it would shift toward _advice_ or _mechanics_.

### Post 6 — experience vs. advice

**Just beat Honour Mode after 4 failed runs — here's what finally clicked (and a question)**  
"After four wipes I finally got the golden dice. Honestly I'm still shaking. The thing that turned it around was finally respeccing into a control-heavy party. One thing I'm still unsure about for my next run though — is going full caster comp overkill, or should I keep a martial?"

- **Competing labels:** _experience_ (celebrating an achievement, emotional payoff) vs. _advice_ (the closing question about future party comp).
- **Resolution → experience.** The overwhelming bulk and intent of the post is to share the achievement and emotional moment; the question is a minor afterthought. This is the mirror image of the Hard Edge Cases example — there the request was the ultimate point, here the celebration is.

### Post 7 — narrative vs. advice

**Should I side with the Emperor or free Orpheus? Trying not to spoil myself on which is more 'good'**  
"I'm at the endgame decision and genuinely torn. I don't want a mechanical min-max answer — I want to know, thematically, which choice the story treats as the more heroic or morally consistent one given how Orpheus and the Emperor are written. Without major spoilers, which path do people find more narratively satisfying?"

- **Competing labels:** _advice_ (a direct "which should I choose" question) vs. _narrative_ (the question is explicitly about themes, moral framing, and characterization).
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

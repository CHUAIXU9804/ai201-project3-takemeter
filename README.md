# Baldur's Gate 3 Reddit Classification Project

## Community Choice and Reasoning

### Community Choice

**r/BaldursGate3**

### Reasoning

I chose this community because it's a large and active gaming community that have a lot of discussions about the game's character builds, story plot, moral decisions, and game mechanics. This community is a good fit for a classification task because the discourse is diverse and contains several distinct communication styles - game mechanics, narrative, seeking for advice, and sharing game experience. This provides clear decision boundaries for annotation, and some posts may also contain elements of multiple categories.

---

## Label Taxonomy

### Mechanics

Players evaluate gameplay systems, builds, classes, combat mechanics, item interactions, or optimization strategies using reasonsing and logic.

#### Example 1

**Terrified of House of Hope HM**  
https://www.reddit.com/r/BaldursGate3/comments/1uajpqv/terrified_of_house_of_hope_hm/

#### Example 2

**Why couldn't the party just cure their parasites Postmortem?**  
https://www.reddit.com/r/BaldursGate3/comments/1u6xmco/why_couldnt_the_party_just_cure_their_parasites/

---

### Narrative

Players interpret or evaluate about characters, story events, lore, relationships, themes, or moral choices.

#### Example 1

**This game made me see how easy it is to be a good person**  
https://www.reddit.com/r/BaldursGate3/comments/1u5vfra/this_game_made_me_see_how_easy_it_is_to_be_a_good/

#### Example 2

**Leading the army to the Grove is infinitely more satisfying**  
https://www.reddit.com/r/BaldursGate3/comments/1u6wdr6/leading_the_army_to_the_grove_is_infinitely_more/

---

### Advice

Players seek for help or solutions on technical issues, gameplay, build, or guest help.

#### Example 1

**Unable to download specific mods**  
https://www.reddit.com/r/BaldursGate3/comments/1ubt89w/unable_to_download_specific_mods/

#### Example 2

**Even after 50+ hours gearing is still confusing to me**  
https://www.reddit.com/r/BaldursGate3/comments/1uaqgo9/even_after_50_hours_gearing_is_still_confusing_to/

---

### Experience

Players share personal gameplay experience, discovery, achievement, or emotional moment.

#### Example 1

**TIL hurling MC's jars into the ocean doesn't destroy them**  
https://www.reddit.com/r/BaldursGate3/comments/1ub7d7o/til_hurling_mcs_jars_into_the_ocean_doesnt/

#### Example 2

**Respec Minthara - found something**  
https://www.reddit.com/r/BaldursGate3/comments/1u7osvy/respec_minthara_found_something/

---

## Data Collection Source

r/BaldursGate3 Reddit Posts

---

## Labeling Process

Posts were collected from the r/BaldursGate3 Reddit community and manually annotated into one of four categories: mechanics, narrative, advice, and experience.

Each post was assigned exactly one label based on its primary communication intent. For ambiguous cases, the label was determined by the poster's main purpose. For example, a post describing a personal experience while asking for help was labeled as advice because the primary goal was to seek assistance.

---

## Label Distribution

| Label | Count |
|---------|---------:|
| mechanics | 41 |
| narrative | 48 |
| advice | 66 |
| experience | 57 |
| **Total** | **212** |

---

## 3 Difficult-to-Label Examples With Your Decisions

### Example 1

**I am so new and so dumb**

>Hey guys. Not new to video games but brand new to BG and also turn based style games. (Started my first DND campaign a few months ago, so I know a tiny bit about that part!) I am loving the game so far but there's so much content and so many options that I keep getting side tracked, confused, and beaten by enemies I'm not good enough to beat yet. This will probably sound dumb, but is there a guide available for newbies that is really simple and straightforward? For example, I'm currently working on the issue of the Grove and freeing the people there, which led me to the swamps, which led me to the teahouse, which led me to Aunty, which led me to that whole situation (trying not to give any spoliers) and I can't win that battle yet so I spent a bunch of time on it and then realized I probably don't even need to deal with that right now to continue on with the quest I was working on🤦🏻‍♀️ I want to eventually do a playthrough where I do absolutely everything in this game, I love all the content, but I'm finding it a bit overwhelming as a newbie, mostly because I need better skills to be able to beat some of the enemies I encounter which leads to me avoiding certain things. So if there is a guide that can help really new players and kind of "explains like I'm five", that would be awesome. Thank you in advance!

**Decision:**  
A combination of experience and advice. I've determined this to be advice, because the main intention is to get advice on a guide.

---

### Example 2

**Killed Karlach, not for Wyll but for my party**

>I'm playing on single sace tactician rn, and I met up with Karlach before progressing much in Act 1 or the grove. She asked for help killing the fake paladins of tyr, and it took several teies being a bit under-levelled but the party finally killed them all. Unfortunately, the party was on death's door and Karlach's rampage knocked down Gale and Astarion twice as we tried to leave, and killed Astarion at one point, which cost a resurrection scroll. I know the rampage happens, but I was still kinda pissed that Karlach's character was causing damage to the party and ended up killing someone. When I talkedto her afterwards, the only dialogue options available were sympathetic ones asking if she's doing alright. This pissed me off even more, cuz I had hoped I could at least say something along the lines of 'Hey, you just put your own team in danger back there' or 'That was a little intimidating to watch, can we trust that you won't be a harm to the party?' IDK something like that, but nope. You just have to pity and empathize. So I ended up killing her, justifying as the party seeing her as a crazed loose cannon. I ended up resurrecting her at camp, but no dialogue on the killing her, just an annoyed 'What.' when I speak to her. She can stay at camp and get f@&$ed by her engine for all I care, her dialogue options just feel way too limited, and the game seems to really want you, and at times force you, to take her side.

>AITA? (I know I am)

**Decision:**  
A combination of advice and narrative. I've determined this to be narrative, because it involves a lot of discussion around narrative.

---

### Example 3

**Knockout**

>Does fainting NPC instead of killing change anything in the story?

>For example, I didn't kill Gortash's mother, instead I left her unconscious, does that change anything or will the game treat her as dead anyway?

**Decision:**  
A combination of advice and narrative. I've determined this to be narrative, because the poster is not seeking for advice, but wondering how does their action impact the story development relating to a character.

---

## Fine-Tuning Approach

**Base model:** distilbert-base-uncased

### Hyperparameter Decision

| Parameter | Value |
|------------|--------|
| num_train_epochs | 3 |
| learning_rate | 2e-5 |
| per_device_train_batch_size | 16 |

---

## Baseline Description

### Prompt Used

```text
You are classifying posts from r/BaldursGate3.

Assign exactly ONE label.

Labels:

narrative
Definition:
Players interpret or evaluate about characters, story events, lore, relationships, themes, or moral choices.

Example:
"Astarion's character arc is one of the strongest redemption stories in the game because his growth feels earned."

mechanics
Definition:
Players evaluate gameplay systems, builds, classes, combat mechanics, item interactions, or optimization strategies using reasonsing and logic.

Example:
"Why is Sorcerer/Warlock multiclass stronger than pure Sorcerer for Honour Mode?"

experience
Definition:
Players share personal gameplay experience, discovery, achievement, or emotional moment.

Example:
"After 120 hours I finally discovered a hidden dialogue option with Karlach."

advice
Definition:
Players seek for help or solutions on technical issues, gameplay, build, or guest help.

Example:
"I'm stuck on the Myrkul fight. What level should I be before attempting it?"

Respond with ONLY the label name.
Do not explain your reasoning.

Valid labels:
narrative
mechanics
experience
advice
```

### How Results Were Collected

Results were collected using Baseline comparison, then Baseline metrics were calculated to give the statistical results.

---

## Full Evaluation Report

### Zero-Shot Baseline Using llama-3.3-70b-versatile Model

🎯 Baseline accuracy: **0.812**

#### Per-class metrics (baseline)

|              | Precision | Recall | F1-Score | Support |
|--------------|:---------:|:------:|:--------:|:-------:|
| experience   | 0.73 | 0.89 | 0.80 | 9 |
| advice       | 0.90 | 0.90 | 0.90 | 10 |
| narrative    | 0.80 | 0.57 | 0.67 | 7 |
| mechanics    | 0.83 | 0.83 | 0.83 | 6 |
| **accuracy** | | | 0.81 | 32 |
| macro avg    | 0.82 | 0.80 | 0.80 | 32 |
| weighted avg | 0.82 | 0.81 | 0.81 | 32 |

---

### Fine-Tuned Model

🎯 Fine-tuned model accuracy: **0.344**

#### Per-class metrics (fine-tuned model)

|              | Precision | Recall | F1-Score | Support |
|--------------|:---------:|:------:|:--------:|:-------:|
| experience   | 0.29 | 0.56 | 0.38 | 9 |
| advice       | 0.40 | 0.60 | 0.48 | 10 |
| narrative    | 0.00 | 0.00 | 0.00 | 7 |
| mechanics    | 0.00 | 0.00 | 0.00 | 6 |
| **accuracy** | | | 0.34 | 32 |
| macro avg    | 0.17 | 0.29 | 0.22 | 32 |
| weighted avg | 0.21 | 0.34 | 0.26 | 32 |

---

### Confusion Matrix

|              | experience | advice | narrative | mechanics |
|--------------|:----------:|:------:|:---------:|:---------:|
| **experience** | 5 | 4 | 0 | 0 |
| **advice** | 4 | 6 | 0 | 0 |
| **narrative** | 6 | 1 | 0 | 0 |
| **mechanics** | 2 | 4 | 0 | 0 |

Rows = true label, columns = predicted label

---

## Wrong Examples

### Example #1

**True:** narrative  
**Predicted:** experience (confidence: 0.28)

**Text:** Shadowheart's scar on her face

>I just finished the Original Shadowheart storyline, this time I saved her parents and learned the details of the night she was kidnapped from her father. But now the scar is unclear.

>Her father is a werewolf, and he was followed his daughter during the ritual to make sure she was safe. His daughter didn't recognize him and thought he was a normal wolf attacking, so her fear of wolves is understandable. But her father was in control of himself in his wolf form, and he wouldn't hurt his child. So how did she get that wound and scar?

**Analysis:** This model predicts the post as experience instead of narrative. It might be because the post is written in first person perspective and opens with a gameplay action, which structurally looks identical to an experience post. The actual content is a lore analysis of Shadowheart's backstory and a question about story consistency.

### Example #2

**True:** experience  
**Predicted:** advice (confidence: 0.27)

**Text:** Need motivation for act 3

>I get that it's a story driven game, but there's so much talk no jutsu in act 3 compared to 1 and 2. I've finished the game before but during my second playthrough and after building all party members with act2 "end game" items, all my excitement in trying out the new builds disappeared after imagining all the dialogue I have to go through for each fight.

>I also get it's not that kinda game but I just need motivation.

**Analysis:** The model predicts this post with label advice when it should be experience. The model might get confused on the title "Need motivation", but the actual content is the poster expressing their thoughts and emotions, not seeking for advice. It might have to do with boundary definition distinctions.

### Example #3

**True:** experience  
**Predicted:** advice (confidence: 0.27)

**Text:** Tactical Moonrise tower

>Doing tactical run as my first playthrough, game's much more fair compared to other bs crpgs can be on harder difficulties (looking at you pathfinder...) i fucked up and got "selunite" shadowheart before doing moonrise and all the harpers + jaheira (since i didnt want her in my party) just get obliterated at that first fight lol. i finally gave and jumped in behind the reinforcements on the rafters and killed all of the enemies by sniping them. but good god not having an option that says something to the effect of "go away harper fodder" is sad lol.

**Analysis:** The model predicts this post with label advice when it should be experience. The model might get confused because the poster pointed out a problem they are facing "got "selunite" shadowheart before doing moonrise", but the actual content is not to seek for advice, but to share experience. The issue might be related to boundary definition distinctions.

---

## Sample Classifications

| Text | Predicted Label | Confidence Score | Why Prediction is Reasonable |
|------|----------------|-----------------|------------------------------|
| Shadowheart's scar on her face | experience | 0.28 | Incorrect |
| Need motivation for act 3 | advice | 0.27 | Incorrect |
| Tactical Moonrise tower | advice | 0.27 | Incorrect |
| Looking for more elaborate Illithid armour | advice | 0.28 | It’s correct and reasonable because the post content is to seek for suggestions for mods that enhance the looks of Illithid armours., so the expected prediction and the actual prediction matches |

---

## Reflection

### What the Model Learned

The model learned to match First-person past tense to experience label. Any post opening with "I just…", "I finally…", or "I fucked up…" was pulled toward experience, regardless of whether the subject was a player action, a story reflection, or a build breakdown.

Any post that have a title or closing lines with Request-like phrasing such as "Need…", "How to…", or "Is this…" were predicted as advice, even when the body contained no actual ask. As well as any post that have a problem description without visible resolution, such as posts that described a failed fight, a mod conflict, a confusing build were pulled toward advice if they didn't explicitly state that the problem was solved.

### What I Intended

The model is supposed to reflect the purpose of a post from 4 dimensions - experience, advice, narrative, and mechanics, understand why someone wrote it and what they wanted from the community. An experience post shares a personal gameplay moment; advice seeks help from others; narrative reflects on story, character, or lore; and mechanics discusses game systems, builds, or tactics. The intended decision boundary was semantic and intentional — what is the communication intent of this post?

---

## Spec Reflection

One way the spec helped me is to identify what kind of posts should be used during data collection process that align to the 4 labels. However, one way the implementation diverged from it is that the fine-tuned model learned to use certain words and phrasing from the post content to assign labels instead of reading through the complete content, for example, when the post is using first person point of view, the model might consider it as sharing experience, but in fact, the main content of the post is around narrative discussion.

---

## AI Usage Section

I used AI to conduct label stress testing before collecting data, as well as during the data collection process, used AI to pre-label a batch of examples before reviewing them myself.

Reference: [Model Training][https://colab.research.google.com/drive/1qAguQd5p3lZd8VH6Ncv4UTcu8S0MHa3U]

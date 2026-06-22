## Community choice and reasoning

## Label taxonomy:

definitions and 2 examples per label

## Data collection source

## labeling process

## label distribution

## 3 difficult-to-label examples with your decisions

## Fine-tuning approach:

base model, training setup, and at least one hyperparameter decision

## Baseline description:

prompt used and how results were collected

## Full evaluation report:

metrics for both models (accuracy + per-class), confusion matrix (written as a markdown table in the README, not only the committed image), 3 specific wrong predictions with analysis, and a sample-classifications table (3–5 posts with predicted label and confidence, one correct example explained)

### zero-shot baseline using llama-3.3-70b-versatile Model
🎯 Baseline accuracy: 0.812

Per-class metrics (baseline):
              precision    recall  f1-score   support

  experience       0.73      0.89      0.80         9
      advice       0.90      0.90      0.90        10
   narrative       0.80      0.57      0.67         7
   mechanics       0.83      0.83      0.83         6

    accuracy                           0.81        32
   macro avg       0.82      0.80      0.80        32
weighted avg       0.82      0.81      0.81        32

### Fine-Tuned Model
🎯 Baseline accuracy: 0.812

Per-class metrics (baseline):
              precision    recall  f1-score   support

  experience       0.73      0.89      0.80         9
      advice       0.90      0.90      0.90        10
   narrative       0.80      0.57      0.67         7
   mechanics       0.83      0.83      0.83         6

    accuracy                           0.81        32
   macro avg       0.82      0.80      0.80        32
weighted avg       0.82      0.81      0.81        32


### Confusion Matrix
## Confusion Matrix — Fine-Tuned Model (Test Set)

|              | experience | advice | narrative | mechanics |
|--------------|:----------:|:------:|:---------:|:---------:|
| **experience** |     5      |   4    |     0     |     0     |
| **advice**     |     4      |   6    |     0     |     0     |
| **narrative**  |     6      |   1    |     0     |     0     |
| **mechanics**  |     2      |   4    |     0     |     0     |

Rows = true label, columns = predicted label


## Reflection:

what the model learned vs. what you intended

## Spec reflection:

one way the spec helped you, one way implementation diverged from it and why

## AI usage section:

at least 2 specific instances describing what you directed the AI to do and what you revised or overrode; disclose any annotation assistance

# Generating Test Data
To generate training data, I used Mistral-7B-Instruct-v0.3 (https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)
## Prompt
"You are a research assistant generating question-answer pairs from scientific paper abstracts.

Title: {title}

Abstract: {abstract}

Generate 2 to 3 QA pairs based only on the abstract. Respond in JSON format:
```
[
  {{
    "question": "...",
    "answer": "..."
  }},
  ...
]
```
"

Based on this prompt, the model generate 2 - 3 questions.

## Data
For test data, I used ISCA 2022 - 2024 paper.
## Colab Link
https://colab.research.google.com/drive/1u261rF0L5K8ohHM_TyE_fzr66rRuIq7Z#scrollTo=r_3mp48tZpRC


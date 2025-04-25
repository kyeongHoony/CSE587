# Generating Test Data
To generate test data, I used Mistral-7B-Instruct-v0.3 (https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)
## Prompt
```
"You are a research assistant generating question-answer pairs from scientific paper abstracts.

Title: {title}

Abstract: {abstract}

Generate 2 to 3 QA pairs based only on the abstract. Respond in JSON format:

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

# Generating Training Data
To create training data, I used Gemma2-2b-it (https://huggingface.co/google/gemma-2-2b-it)
## Prompt
```
"""You are a research assistant.

Given the following abstract of a scientific paper, generate 2 to 3 diverse and meaningful question-answer (QA) pairs that can be answered solely based on the abstract.

Respond ONLY in valid JSON format with a list of dictionaries. DO NOT include explanations, notes, or formatting outside the JSON.

Title: {title}

Abstract: {abstract}

Your response:
"""
```
Based on this prompt, the model creates question-answer pairs.
## Data
For training data, I used ISCA 2005 - 2021 paper.
## Colab Link
https://colab.research.google.com/drive/1Yj4SEY0UaeaFKS7oPFabtQqWq6IqVECF#scrollTo=ol-0sF7Bgt52

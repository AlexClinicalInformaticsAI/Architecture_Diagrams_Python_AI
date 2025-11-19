# GamELY - LLM Evaluation Framework Architecture

## Overview

GamELY is a Python package from PyPI (`pip install GamELY`) that evaluates language model outputs using other LLMs as judges. This architecture diagram visualizes the complete evaluation workflow and component structure.

## What is GamELY?

GamELY allows developers to assess LLM-generated responses against reference answers using state-of-the-art LLMs as evaluators. It provides automated scoring across 17 built-in criteria or custom evaluation metrics.

### Key Features

- **Automatic Provider Detection**: Simply specify a model name; GamELY automatically detects and configures the correct API provider
- **Batch Processing**: Efficiently evaluate multiple responses simultaneously via pandas DataFrames
- **Multi-Provider Support**: Integrates with OpenAI, Anthropic, and DeepSeek APIs
- **Built-in Criteria**: 17 default evaluation criteria covering accuracy, bias, toxicity, hallucination, and more
- **Custom Criteria**: Define your own evaluation metrics tailored to specific use cases

## Architecture Components

### 1. Input Layer
- **pandas DataFrame**: 2-column format (reference text + generated text)
- **Model Selection**: Choose from 23+ supported models across 3 providers
- **API Key**: Authentication for the selected provider
- **Evaluation Criteria**: Use built-in 17 criteria or define custom ones

### 2. Core Components

**GamELY Class**:
- Main evaluator instance
- Handles initialization, validation, and orchestration

**Provider Mapper**:
- `MODEL_PROVIDER_MAP`: Maps 23 models to their providers
- `get_provider()`: Automatically detects provider from model name

**Authentication**:
- `validate_api_key()`: Validates credentials against provider APIs
- `_setup_client()`: Initializes appropriate API client (OpenAI/Anthropic/DeepSeek)

### 3. Supported LLM Providers

**OpenAI** (via OpenAI API):
- GPT-3.5-turbo
- GPT-4, GPT-4-turbo
- GPT-4o, GPT-4o-mini
- O1, O1-mini

**Anthropic** (via Anthropic API):
- Claude 2
- Claude 3 Haiku, Sonnet, Opus
- Claude 3.5 latest variants

**DeepSeek** (via DeepSeek API):
- deepseek-chat
- deepseek-reasoner

### 4. Evaluation Pipeline

The evaluation follows this sequence for each DataFrame row:

1. **Build Prompt**: Constructs evaluation prompt with reference, generated text, and criterion
2. **Call Provider**: Makes API request to selected LLM judge
3. **Parse Response**: Extracts numerical score (1-5) or NaN from LLM response
4. **Aggregate**: Compiles all scores into output DataFrame

### 5. Scoring System

Each criterion receives a score based on a 5-point Likert scale:

- **1** = Strongly Disagree
- **2** = Disagree
- **3** = Neutral
- **4** = Agree
- **5** = Strongly Agree
- **NaN** = Criterion is irrelevant or not applicable

### 6. Default Evaluation Criteria (17)

1. **Accuracy**: Is the LLM generated response accurate?
2. **Comprehension**: Is the response correct in comprehension?
3. **Reasoning**: Does the response mirror the context's reasoning?
4. **Helpfulness**: Is the response helpful to the user?
5. **Topic Coverage**: Does it cover all needed topics?
6. **Key Aspects**: Does it cover all key aspects?
7. **Completeness**: Is it missing significant parts?
8. **Fluency**: Is the response fluent?
9. **Grammar**: Is it grammatically correct?
10. **Organization**: Is it well-organized?
11. **Bias Detection**: Does it contain bias?
12. **Toxicity**: Does it contain toxicity?
13. **Privacy**: Does it violate privacy?
14. **Hallucination**: Does it contain hallucinations?
15. **Human Distinguishability**: Is it distinguishable from human response?
16. **Human Comparison**: How does it compare with human response?
17. **LLM Comparison**: How does it compare to other LLM responses?

## Usage Example

```python
import pandas as pd
import GamELY

# Prepare data
df = pd.DataFrame({
    'reference': [
        'The capital of France is Paris.',
        'Water boils at 100°C at sea level.'
    ],
    'generated': [
        'Paris is the capital city of France.',
        'Water boils at approximately 212°F or 100°C.'
    ]
})

# Evaluate using GPT-4 as judge
results = GamELY.evaluate_responses(
    dataframe=df,
    model_name='gpt-4',
    api_key='sk-your-openai-key-here'
)

# results DataFrame now contains original columns + 17 criterion score columns
print(results)
```

### Custom Criteria Example

```python
custom_criteria = [
    'Does the response use technical terminology correctly?',
    'Is the response concise and to the point?',
    'Does the response cite sources?'
]

results = GamELY.evaluate_responses(
    dataframe=df,
    model_name='claude-3-5-sonnet-latest',
    api_key='your-anthropic-key',
    criteria=custom_criteria
)
```

## Output Format

The `evaluate_responses()` function returns a pandas DataFrame with:
- Original 2 columns: `reference` and `generated`
- Additional columns: One per evaluation criterion
- Cell values: Numerical scores (1.0-5.0) or NaN

Example output structure:

| reference | generated | Is the LLM response accurate? | Is the response fluent? | ... |
|-----------|-----------|--------------------------------|------------------------|-----|
| ref1      | gen1      | 5.0                            | 4.0                    | ... |
| ref2      | gen2      | 3.0                            | 5.0                    | ... |

## Architecture Diagram

The generated diagram (`gamely_architecture.png`) illustrates:

1. **Data Flow**: From user input through provider selection to final scored output
2. **Component Relationships**: How provider mapper, validator, and evaluator interact
3. **API Integration**: Connections to OpenAI, Anthropic, and DeepSeek services
4. **Processing Pipeline**: Step-by-step evaluation workflow for each DataFrame row

## Technical Details

- **Package**: GamELY v0.1.0 (PyPI)
- **Python Version**: 3.9+ required
- **Dependencies**: pandas, openai, anthropic, requests, numpy
- **License**: MIT
- **API Costs**: Usage incurs costs from LLM provider based on API pricing

## Installation

```bash
pip install GamELY
```

## PyPI Package

- **Package**: https://pypi.org/project/GamELY/
- **Current Version**: 0.1.0
- **Status**: Active development

## Related Resources

- Python `diagrams` library documentation: https://diagrams.mingrammer.com/
- OpenAI API: https://platform.openai.com/docs/api-reference
- Anthropic API: https://docs.anthropic.com/
- DeepSeek API: https://platform.deepseek.com/

## Diagram Generation

This architecture diagram was generated using:

```bash
python Arch_Diagrams/gamely_architecture.py
```

Output files:
- `diagrams/gamely_architecture.png` - Visual diagram (377KB)
- `diagrams/gamely_architecture.dot` - GraphViz source (20KB)
- `diagrams/gamely_architecture.drawio` - Draw.io format (if graphviz2drawio installed)

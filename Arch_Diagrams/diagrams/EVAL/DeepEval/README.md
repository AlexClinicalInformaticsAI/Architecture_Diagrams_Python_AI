# DeepEval - The LLM Evaluation Framework

## Overview

DeepEval is a simple-to-use, open-source evaluation framework for LLM applications. It's like **Pytest for LLMs** - providing unit testing capabilities specifically designed for evaluating large language model outputs.

**Repository**: https://github.com/confident-ai/deepeval  
**PyPI**: `pip install deepeval`  
**License**: Apache 2.0  
**Language**: Python 3.9+

## What is DeepEval?

DeepEval makes it easy to test LLM applications with a familiar pytest-style interface. It includes 14+ research-backed metrics that use LLMs, statistical methods, or NLP models running locally on your machine.

### Key Philosophy

**Unit Testing for LLMs**: Bring software testing best practices to LLM development:
- Write test cases like pytest
- Run evaluations locally
- Integrate with CI/CD
- Track results over time

## Key Features

### 1. Pytest Integration
```python
import deepeval
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric

@deepeval.pytest_mark
def test_answer_relevancy():
    test_case = LLMTestCase(
        input="What is the capital of France?",
        actual_output="Paris is the capital of France.",
        expected_output="Paris"
    )
    metric = AnswerRelevancyMetric(threshold=0.7)
    assert_test(test_case, [metric])
```

### 2. Comprehensive Metrics

#### RAG Metrics
- **Answer Relevancy**: Is the answer relevant to the question?
- **Faithfulness**: Is the answer faithful to the context?
- **Contextual Recall**: Did we retrieve all relevant context?
- **Contextual Precision**: Is the retrieved context precise?
- **Contextual Relevancy**: Is the context relevant?
- **RAGAS**: Combined RAG assessment score

#### Agentic Metrics
- **Task Completion**: Did the agent complete the task?
- **Tool Correctness**: Did the agent use tools correctly?

#### General Metrics
- **G-Eval**: Customizable LLM-as-judge metric
- **Hallucination**: Does output contain hallucinations?
- **Summarization**: Quality of summaries
- **Bias**: Detect biased outputs
- **Toxicity**: Identify toxic content

#### Conversational Metrics
- **Knowledge Retention**: Does the bot remember context?
- **Conversation Completeness**: Is the conversation complete?
- **Conversation Relevancy**: Are responses relevant?
- **Role Adherence**: Does the bot stay in character?

### 3. Synthetic Data Generation
```python
from deepeval.synthesizer import Synthesizer

synthesizer = Synthesizer()
synthetic_data = synthesizer.generate_goldens(
    contexts=[...],  # Your knowledge base
    num_goldens=100
)
```

### 4. Custom Metrics
```python
from deepeval.metrics import BaseMetric

class CustomMetric(BaseMetric):
    def __init__(self, threshold: float = 0.5):
        self.threshold = threshold
    
    def measure(self, test_case: LLMTestCase):
        # Your custom logic
        score = self.calculate_score(test_case.actual_output)
        self.success = score >= self.threshold
        self.score = score
        return self.score
```

### 5. Confident AI Platform Integration
- Upload test results to cloud
- Compare iterations
- Generate reports
- Team collaboration

## Architecture Components

### Core Components

#### 1. Test Case System
```python
from deepeval.test_case import LLMTestCase, ConversationalTestCase

# Single turn
test_case = LLMTestCase(
    input="User question",
    actual_output="LLM response",
    expected_output="Expected response",
    context=["Relevant context"],
    retrieval_context=["Retrieved docs"]
)

# Multi-turn conversation
conv_test_case = ConversationalTestCase(
    turns=[
        LLMTestCase(input="Hi", actual_output="Hello!"),
        LLMTestCase(input="How are you?", actual_output="I'm good!")
    ]
)
```

#### 2. Metric System
All metrics inherit from `BaseMetric`:
- `measure()`: Calculate score
- `is_successful()`: Pass/fail determination
- `score`: Numerical result
- `reason`: Explanation of score

#### 3. Evaluation Engine
- Parallel execution
- Caching
- Progress tracking
- Result aggregation

#### 4. Dataset Management
```python
from deepeval.dataset import EvaluationDataset

dataset = EvaluationDataset(test_cases=[...])
dataset.evaluate(metrics=[...])
```

### Workflow Architecture

```
┌─────────────────┐
│  Define Tests   │
│  (pytest style) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Create Test    │
│  Cases          │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Select Metrics │
│  (14+ built-in) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Run Evaluation │
│  (Local/LLM)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Assert Results │
│  (Pass/Fail)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Generate       │
│  Report         │
└────────┬────────┘
         │
         ├──────────────┐
         │              │
         ▼              ▼
┌─────────────┐  ┌─────────────┐
│  Local      │  │  Confident  │
│  Results    │  │  AI Cloud   │
└─────────────┘  └─────────────┘
```

## Usage Examples

### Basic Evaluation

```python
from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

# Define test case
test_case = LLMTestCase(
    input="What is machine learning?",
    actual_output="Machine learning is a subset of AI...",
    expected_output="ML is a type of artificial intelligence"
)

# Define metric
metric = AnswerRelevancyMetric(threshold=0.7)

# Evaluate
evaluate([test_case], [metric])
```

### Pytest Integration

```python
# test_llm.py
import pytest
import deepeval
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    HallucinationMetric
)

@pytest.mark.parametrize(
    "input,output,context",
    [
        ("What is AI?", "AI is...", ["AI definition"]),
        ("Explain ML", "ML is...", ["ML definition"]),
    ]
)
def test_rag_pipeline(input, output, context):
    test_case = LLMTestCase(
        input=input,
        actual_output=output,
        context=context
    )
    
    metrics = [
        AnswerRelevancyMetric(threshold=0.7),
        FaithfulnessMetric(threshold=0.8),
        HallucinationMetric(threshold=0.3)
    ]
    
    assert_test(test_case, metrics)

# Run with: pytest test_llm.py
```

### RAG Evaluation

```python
from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    ContextualRecallMetric,
    ContextualPrecisionMetric
)

# Your RAG pipeline
def rag_pipeline(query):
    # 1. Retrieve context
    retrieved_docs = retriever.search(query)
    
    # 2. Generate answer
    answer = llm.generate(query, context=retrieved_docs)
    
    return answer, retrieved_docs

# Test it
query = "What is quantum computing?"
answer, context = rag_pipeline(query)

test_case = LLMTestCase(
    input=query,
    actual_output=answer,
    retrieval_context=context,
    expected_output="Quantum computing uses quantum mechanics..."
)

metrics = [
    AnswerRelevancyMetric(),
    FaithfulnessMetric(),
    ContextualRecallMetric(),
    ContextualPrecisionMetric()
]

evaluate([test_case], metrics)
```

### Agent Evaluation

```python
from deepeval.metrics import TaskCompletionMetric, ToolCorrectnessMetric
from deepeval.test_case import LLMTestCase

# Your agent
def agent_execute(task):
    # Agent logic
    result = agent.run(task)
    tools_used = agent.get_tools_used()
    return result, tools_used

# Test
task = "Book a flight to Paris"
result, tools = agent_execute(task)

test_case = LLMTestCase(
    input=task,
    actual_output=result,
    tools_used=tools,
    expected_tools=["search_flights", "book_flight"]
)

metrics = [
    TaskCompletionMetric(threshold=0.8),
    ToolCorrectnessMetric(threshold=0.9)
]

evaluate([test_case], metrics)
```

### Custom Metric

```python
from deepeval.metrics import BaseMetric
from deepeval.test_case import LLMTestCase

class LengthMetric(BaseMetric):
    def __init__(self, min_length: int = 50, max_length: int = 200):
        self.min_length = min_length
        self.max_length = max_length
        self.threshold = 1.0
    
    def measure(self, test_case: LLMTestCase):
        length = len(test_case.actual_output)
        
        if self.min_length <= length <= self.max_length:
            self.success = True
            self.score = 1.0
            self.reason = f"Length {length} is within range"
        else:
            self.success = False
            self.score = 0.0
            self.reason = f"Length {length} is outside range"
        
        return self.score
    
    def is_successful(self):
        return self.success
    
    @property
    def __name__(self):
        return "Length Check"

# Use it
metric = LengthMetric(min_length=100, max_length=500)
evaluate([test_case], [metric])
```

### Synthetic Data Generation

```python
from deepeval.synthesizer import Synthesizer

# Your knowledge base
contexts = [
    "Paris is the capital of France.",
    "The Eiffel Tower is in Paris.",
    "France is in Europe."
]

# Generate test data
synthesizer = Synthesizer()
goldens = synthesizer.generate_goldens(
    contexts=contexts,
    num_goldens=50,
    include_expected_output=True
)

# Use generated data
for golden in goldens:
    test_case = LLMTestCase(
        input=golden.input,
        actual_output=your_llm(golden.input),
        expected_output=golden.expected_output,
        context=golden.context
    )
    evaluate([test_case], metrics)
```

### Confident AI Integration

```python
import deepeval

# Login to Confident AI
deepeval.login()

# Run tests and upload results
@deepeval.pytest_mark
def test_with_upload():
    # Your tests
    pass

# Results automatically uploaded to Confident AI platform
# View at: https://confident-ai.com
```

## Metric Details

### G-Eval
Customizable LLM-as-judge metric:
```python
from deepeval.metrics import GEval

metric = GEval(
    name="Creativity",
    criteria="Is the response creative and original?",
    evaluation_steps=[
        "Check for unique ideas",
        "Assess novelty",
        "Evaluate originality"
    ],
    evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT]
)
```

### DAG (Deep Acyclic Graph)
Complex evaluation workflows:
```python
from deepeval.metrics import DAGMetric

# Define evaluation graph
dag = DAGMetric(
    nodes=[
        ("relevancy", AnswerRelevancyMetric()),
        ("faithfulness", FaithfulnessMetric()),
        ("final", CustomCombinedMetric())
    ],
    edges=[
        ("relevancy", "final"),
        ("faithfulness", "final")
    ]
)
```

## Integration Examples

### With LangChain

```python
from langchain import OpenAI, PromptTemplate
from deepeval.integrations.langchain import DeepEvalCallbackHandler

# Add DeepEval callback
callback = DeepEvalCallbackHandler()

llm = OpenAI(callbacks=[callback])
result = llm("What is AI?")

# Automatically tracked in DeepEval
```

### With LlamaIndex

```python
from llama_index import VectorStoreIndex
from deepeval.integrations.llama_index import DeepEvalCallbackHandler

# Add callback
callback = DeepEvalCallbackHandler()

index = VectorStoreIndex.from_documents(
    documents,
    callback_manager=CallbackManager([callback])
)

# Queries automatically tracked
```

### CI/CD Integration

```yaml
# .github/workflows/test.yml
name: LLM Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Install dependencies
        run: |
          pip install deepeval pytest
      
      - name: Run DeepEval tests
        run: |
          deepeval test run
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

## Performance Characteristics

### Speed
- **Local Metrics**: Instant (toxicity, bias)
- **LLM Metrics**: Depends on API latency
- **Parallel Execution**: Multiple tests simultaneously

### Cost
- **Local Metrics**: Free
- **LLM Metrics**: API costs apply
- **Caching**: Reduces redundant calls

## Best Practices

1. **Start with Built-in Metrics**: Use research-backed metrics
2. **Combine Multiple Metrics**: Comprehensive evaluation
3. **Set Appropriate Thresholds**: Based on your requirements
4. **Use Synthetic Data**: Generate test cases at scale
5. **Integrate with CI/CD**: Catch regressions early
6. **Track Over Time**: Monitor improvements
7. **Custom Metrics**: For domain-specific needs

## Comparison with Other Tools

### vs Promptfoo
- **DeepEval**: Python, pytest-style, metric-focused
- **Promptfoo**: TypeScript, config-based, red teaming

### vs LangFuse
- **DeepEval**: Testing and evaluation
- **LangFuse**: Production monitoring

### vs CleanLab
- **DeepEval**: LLM output evaluation
- **CleanLab**: Training data quality

## Resources

- **Documentation**: https://deepeval.com/docs/
- **GitHub**: https://github.com/confident-ai/deepeval
- **Discord**: https://discord.gg/3SEyvpgu2f
- **Platform**: https://confident-ai.com

## Installation

```bash
# Basic installation
pip install deepeval

# With all dependencies
pip install "deepeval[all]"

# Verify
deepeval --version
```

## Community

- **GitHub Stars**: 3.5K+
- **Active Development**: Regular updates
- **Discord**: 500+ members
- **Open Source**: Apache 2.0

---

*Architecture diagram generated by: `python deepeval_architecture.py`*

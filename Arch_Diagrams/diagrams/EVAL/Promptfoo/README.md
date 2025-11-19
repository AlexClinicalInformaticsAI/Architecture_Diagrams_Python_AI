# Promptfoo - LLM Testing & Red Teaming Framework

## Overview

Promptfoo is a developer-friendly, **local-first** tool for testing and securing LLM applications. It provides automated evaluations, red teaming, and vulnerability scanning to help teams ship reliable and secure AI applications.

**Repository**: https://github.com/promptfoo/promptfoo  
**NPM**: `npx promptfoo@latest`  
**License**: MIT  
**Language**: TypeScript/JavaScript

## What is Promptfoo?

Promptfoo helps you move from trial-and-error to systematic testing of LLM applications. It runs 100% locally, ensuring your prompts never leave your machine, while providing comprehensive testing and security scanning capabilities.

### Key Philosophy

**Developer-First Testing**: Stop guessing, start measuring. Promptfoo brings software engineering best practices to LLM development with:
- Automated test suites
- CI/CD integration
- Version control for prompts
- Systematic comparison of models and prompts

## Key Features

### 1. Automated Evaluations
- **Prompt Testing**: Compare multiple prompt variations
- **Model Comparison**: Test across OpenAI, Anthropic, Azure, Bedrock, Ollama, etc.
- **Assertion Framework**: Define expected behaviors
- **Regression Testing**: Prevent prompt drift

### 2. Red Teaming & Security
- **Vulnerability Scanning**: Automated security testing
- **Attack Simulations**: Test against common exploits
- **Risk Reports**: Comprehensive security assessments
- **Compliance Checks**: Ensure safety standards

### 3. Developer Experience
- **Local Execution**: 100% private, runs on your machine
- **Live Reload**: Fast iteration cycles
- **Caching**: Avoid redundant API calls
- **Web UI**: Visual comparison of results
- **CLI**: Command-line interface for automation

### 4. Integration
- **CI/CD Ready**: GitHub Actions, GitLab CI, etc.
- **Any LLM Provider**: OpenAI, Anthropic, Azure, Bedrock, Ollama, custom APIs
- **Any Language**: Works with Python, JavaScript, TypeScript, etc.
- **Framework Agnostic**: LangChain, LlamaIndex, or custom code

## Architecture Components

### Core Components

#### 1. Configuration System
Define tests in YAML or JSON:
```yaml
prompts:
  - 'You are a helpful assistant. {{question}}'
  - 'Answer this question: {{question}}'

providers:
  - openai:gpt-4
  - anthropic:claude-3-opus

tests:
  - vars:
      question: 'What is the capital of France?'
    assert:
      - type: contains
        value: 'Paris'
```

#### 2. Provider System
Unified interface for all LLM providers:
- **OpenAI**: GPT-3.5, GPT-4, GPT-4o
- **Anthropic**: Claude 2, Claude 3 family
- **Azure OpenAI**: Enterprise deployments
- **AWS Bedrock**: Claude, Llama, Titan
- **Google**: PaLM, Gemini
- **Ollama**: Local models
- **Custom**: Any HTTP API

#### 3. Assertion Framework
Multiple assertion types:
- **contains**: Check for substring
- **equals**: Exact match
- **regex**: Pattern matching
- **javascript**: Custom logic
- **llm-rubric**: LLM-as-judge
- **similarity**: Semantic similarity
- **cost**: Budget constraints
- **latency**: Performance checks

#### 4. Red Team Module
Security testing capabilities:
- **Prompt Injection**: Test for injection attacks
- **Jailbreaking**: Attempt to bypass safety
- **PII Leakage**: Check for data exposure
- **Harmful Content**: Test content filters
- **Bias Detection**: Identify biased outputs

#### 5. Evaluation Engine
- **Parallel Execution**: Fast test runs
- **Caching**: Reuse previous results
- **Retry Logic**: Handle API failures
- **Progress Tracking**: Real-time feedback

### Testing Workflow

```
┌─────────────────┐
│  Configuration  │
│  (YAML/JSON)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Load Prompts   │
│  & Providers    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Generate Test  │
│  Cases          │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Execute Tests  │
│  (Parallel)     │
└────────┬────────┘
         │
         ├──────────────────┐
         │                  │
         ▼                  ▼
┌─────────────────┐  ┌─────────────────┐
│  Run Assertions │  │  Collect Metrics│
└────────┬────────┘  └────────┬────────┘
         │                    │
         └──────────┬─────────┘
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
         │  Web UI     │  │  JSON/CSV   │
         └─────────────┘  └─────────────┘
```

## Usage Examples

### Quick Start

```bash
# Initialize new project
npx promptfoo@latest init

# Run evaluation
npx promptfoo eval

# View results in web UI
npx promptfoo view
```

### Basic Configuration

```yaml
# promptfooconfig.yaml
description: 'Customer support chatbot evaluation'

prompts:
  - file://prompts/helpful.txt
  - file://prompts/concise.txt

providers:
  - openai:gpt-4
  - openai:gpt-3.5-turbo
  - anthropic:claude-3-sonnet

tests:
  - vars:
      question: 'How do I reset my password?'
    assert:
      - type: contains
        value: 'email'
      - type: llm-rubric
        value: 'Response is helpful and polite'
      - type: latency
        threshold: 5000  # ms

  - vars:
      question: 'What are your business hours?'
    assert:
      - type: regex
        value: '\\d{1,2}:\\d{2}'  # Contains time
```

### Red Teaming

```bash
# Run security scan
npx promptfoo redteam init

# Configure red team tests
npx promptfoo redteam run

# Generate risk report
npx promptfoo redteam report
```

### Red Team Configuration

```yaml
# redteam.yaml
targets:
  - openai:gpt-4

plugins:
  - prompt-injection
  - jailbreak
  - pii-leakage
  - harmful-content
  - bias

strategies:
  - jailbreak:crescendo
  - prompt-injection:indirect
  - harmful:violence
  - harmful:hate-speech

numTests: 100
```

### CI/CD Integration

```yaml
# .github/workflows/llm-test.yml
name: LLM Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Run Promptfoo Tests
        run: |
          npx promptfoo@latest eval
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
      
      - name: Check Results
        run: |
          npx promptfoo@latest eval --assert
```

### Custom Assertions

```javascript
// custom-assertion.js
module.exports = async (output, context) => {
  // Custom logic
  const isValid = output.length > 50 && output.includes('example');
  
  return {
    pass: isValid,
    score: isValid ? 1 : 0,
    reason: isValid ? 'Output meets criteria' : 'Output too short or missing example'
  };
};
```

```yaml
# Use custom assertion
tests:
  - vars:
      input: 'Explain quantum computing'
    assert:
      - type: javascript
        value: file://custom-assertion.js
```

### Model Comparison

```yaml
# Compare multiple models
providers:
  - id: gpt4
    openai:gpt-4
  - id: claude
    anthropic:claude-3-opus
  - id: local
    ollama:llama2

# Promptfoo generates comparison matrix
```

## Advanced Features

### 1. Dataset Management

```yaml
# Use external datasets
tests: file://tests/customer-support.csv

# CSV format:
# question,expected_topic
# "How do I return an item?","returns"
# "What's your refund policy?","refunds"
```

### 2. Variable Substitution

```yaml
prompts:
  - 'You are a {{role}}. {{task}}'

tests:
  - vars:
      role: 'helpful assistant'
      task: 'Answer the question: {{question}}'
      question: 'What is AI?'
```

### 3. Chained Evaluations

```yaml
# Multi-step evaluation
tests:
  - vars:
      step1: 'Generate a story idea'
    assert:
      - type: llm-rubric
        value: 'Creative and original'
  
  - vars:
      step2: 'Expand on: {{step1.output}}'
    assert:
      - type: contains
        value: '{{step1.output}}'
```

### 4. Cost Tracking

```yaml
# Monitor API costs
assert:
  - type: cost
    threshold: 0.01  # Max $0.01 per test
```

### 5. Performance Testing

```yaml
# Load testing
tests:
  - vars:
      input: 'Test input'
    options:
      repeat: 100  # Run 100 times
    assert:
      - type: latency
        threshold: 2000  # 2 seconds
      - type: javascript
        value: 'output.length > 0'  # No failures
```

## Red Teaming Capabilities

### Attack Categories

1. **Prompt Injection**
   - Direct injection
   - Indirect injection
   - Context manipulation

2. **Jailbreaking**
   - Role-playing attacks
   - Hypothetical scenarios
   - Crescendo attacks

3. **PII Leakage**
   - Training data extraction
   - Memorization tests
   - Privacy violations

4. **Harmful Content**
   - Violence
   - Hate speech
   - Self-harm
   - Sexual content

5. **Bias Detection**
   - Gender bias
   - Racial bias
   - Cultural bias

### Risk Reporting

Promptfoo generates comprehensive risk reports:
- **Risk Score**: Overall security rating
- **Vulnerability Details**: Specific issues found
- **Attack Examples**: Successful exploits
- **Remediation**: Suggested fixes

## Performance Characteristics

### Speed
- **Parallel Execution**: Tests run concurrently
- **Caching**: Avoid redundant API calls
- **Local Processing**: No network overhead for local models

### Scalability
- **Small Projects**: <100 tests, seconds
- **Medium Projects**: 100-1000 tests, minutes
- **Large Projects**: 1000+ tests, use batching

### Resource Usage
- **Memory**: Minimal, caches results
- **Network**: Only for API calls
- **Storage**: Test results stored locally

## Integration Examples

### With LangChain

```python
# langchain_test.py
from langchain import OpenAI, PromptTemplate

def run_chain(input_text):
    llm = OpenAI(temperature=0.7)
    prompt = PromptTemplate.from_template("Answer: {question}")
    chain = prompt | llm
    return chain.invoke({"question": input_text})

# Export for Promptfoo
if __name__ == "__main__":
    import sys
    result = run_chain(sys.argv[1])
    print(result)
```

```yaml
# promptfooconfig.yaml
providers:
  - exec: python langchain_test.py {{input}}
```

### With Custom API

```yaml
providers:
  - id: custom-api
    http:
      url: https://api.example.com/generate
      method: POST
      headers:
        Authorization: 'Bearer {{env.API_KEY}}'
      body:
        prompt: '{{prompt}}'
        temperature: 0.7
      responseParser: 'json.response.text'
```

## Use Cases

### 1. Prompt Engineering
- Compare prompt variations
- A/B test different phrasings
- Optimize for specific metrics

### 2. Model Selection
- Compare providers (OpenAI vs Anthropic vs local)
- Evaluate cost vs quality tradeoffs
- Test model versions

### 3. Regression Testing
- Prevent prompt drift
- Ensure consistent behavior
- Catch breaking changes

### 4. Security Testing
- Red team before deployment
- Continuous security monitoring
- Compliance verification

### 5. Performance Optimization
- Identify slow prompts
- Optimize token usage
- Reduce API costs

## Best Practices

1. **Start Small**: Begin with a few key test cases
2. **Use Version Control**: Track prompt changes in git
3. **Automate**: Integrate with CI/CD
4. **Cache Results**: Reuse expensive API calls
5. **Red Team Regularly**: Security is ongoing
6. **Monitor Costs**: Track API spending
7. **Document Assertions**: Explain why tests exist

## Comparison with Other Tools

### vs Manual Testing
- **Promptfoo**: Automated, reproducible, scalable
- **Manual**: Time-consuming, inconsistent, error-prone

### vs DeepEval
- **Promptfoo**: TypeScript, local-first, red teaming focus
- **DeepEval**: Python, pytest-style, metric-focused

### vs LangFuse
- **Promptfoo**: Testing and evaluation
- **LangFuse**: Production monitoring and observability

## Limitations

1. **Local Execution**: Requires local setup
2. **Configuration**: YAML/JSON learning curve
3. **No Cloud UI**: Results stored locally (can export)
4. **Limited Analytics**: Basic reporting

## Resources

- **Documentation**: https://www.promptfoo.dev/docs/
- **GitHub**: https://github.com/promptfoo/promptfoo
- **Discord**: https://discord.gg/promptfoo
- **Examples**: https://github.com/promptfoo/promptfoo/tree/main/examples

## Installation

```bash
# NPM
npm install -g promptfoo

# Or use npx (no installation)
npx promptfoo@latest init

# Verify installation
promptfoo --version
```

## Community

- **GitHub Stars**: 4.5K+
- **Active Development**: Weekly releases
- **Discord Community**: 1000+ members
- **Open Source**: MIT License

---

*Architecture diagram generated by: `python promptfoo_architecture.py`*

# LLM Evaluation Tools - Comprehensive Analysis

## Overview

This directory contains comprehensive evaluations, documentation, and architecture diagrams for 10 leading LLM and AI evaluation, monitoring, and testing frameworks.

## 📁 Directory Structure

```
EVAL/
├── README.md                      # This file
├── EVALUATION_SUMMARY.md          # High-level comparison
├── TOOL_LIST.md                   # Detailed tool list with status
├── generate_all_diagrams.py       # Script to generate all diagrams
│
├── CleanLab/                      # ✅ Complete
│   ├── README.md                  # Full documentation
│   ├── cleanlab_architecture.py   # Diagram generator
│   ├── cleanlab_architecture.png  # Visual diagram
│   ├── cleanlab_architecture.dot  # GraphViz source
│   └── cleanlab_architecture.drawio # Draw.io format
│
├── Promptfoo/                     # ✅ Complete
│   ├── README.md                  # Full documentation
│   └── promptfoo_architecture.py  # Diagram generator (pending)
│
├── DeepEval/                      # ✅ Complete
│   ├── README.md                  # Full documentation
│   └── deepeval_architecture.py   # Diagram generator (pending)
│
├── LangFuse/                      # ⏳ Pending
├── Lmnr/                          # ⏳ Pending
├── Opik/                          # ⏳ Pending
├── Latitude/                      # ⏳ Pending
├── Agenta/                        # ⏳ Pending
├── n8n/                           # ⏳ Pending
└── MLFlow/                        # ⏳ Pending
```

## 🎯 Quick Reference

### By Use Case

#### Data Quality & Cleaning
- **CleanLab** ✅ - Detect label errors, outliers, duplicates in training data

#### LLM Testing & Evaluation
- **Promptfoo** ✅ - Local testing, red teaming, security scanning
- **DeepEval** ✅ - Pytest-style unit testing for LLMs
- **Opik** ⏳ - Experiment tracking and evaluation
- **Agenta** ⏳ - Full evaluation platform with UI

#### Production Monitoring
- **LangFuse** ⏳ - Comprehensive observability and analytics
- **Lmnr** ⏳ - Lightweight observability
- **MLFlow** ⏳ - ML lifecycle management

#### Prompt Management
- **Latitude** ⏳ - Prompt versioning and collaboration
- **Agenta** ⏳ - Includes prompt management

#### Workflow Automation
- **n8n** ⏳ - Visual workflow builder with AI integration

## 📊 Comparison Matrix

| Tool | Focus | Language | Stars | Status |
|------|-------|----------|-------|--------|
| CleanLab | Data Quality | Python | 9.5K+ | ✅ Complete |
| Promptfoo | Testing/Security | TypeScript | 4.5K+ | ✅ Complete |
| DeepEval | Evaluation | Python | 3.5K+ | ✅ Complete |
| LangFuse | Observability | Python/TS | 6K+ | ⏳ Pending |
| MLFlow | ML Lifecycle | Python | 19K+ | ⏳ Pending |
| n8n | Workflows | TypeScript | 50K+ | ⏳ Pending |
| Agenta | Evaluation Platform | Python/TS | 1.5K+ | ⏳ Pending |
| Lmnr | Observability | Python/TS | 1K+ | ⏳ Pending |
| Opik | Evaluation | Python | 2K+ | ⏳ Pending |
| Latitude | Prompt Mgmt | TypeScript | 500+ | ⏳ Pending |

## 🚀 Getting Started

### 1. Review Tool Documentation

Each tool has a dedicated README with:
- Overview and key features
- Architecture components
- Usage examples
- Integration guides
- Best practices

Start with:
- `CleanLab/README.md` - Data quality
- `Promptfoo/README.md` - Testing & security
- `DeepEval/README.md` - Evaluation framework

### 2. View Architecture Diagrams

Visual diagrams show:
- Component architecture
- Data flow
- Integration points
- Workflow processes

Example:
```bash
# View CleanLab diagram
open diagrams/EVAL/CleanLab/cleanlab_architecture.png
```

### 3. Generate Diagrams

```bash
# Generate all diagrams at once
python Arch_Diagrams/diagrams/EVAL/generate_all_diagrams.py

# Or generate individual diagrams
python Arch_Diagrams/diagrams/EVAL/CleanLab/cleanlab_architecture.py
```

## 📖 Documentation Files

### EVALUATION_SUMMARY.md
High-level overview with:
- Quick comparison matrix
- Selection guide by use case
- Integration compatibility
- Recommendations by team size

### TOOL_LIST.md
Detailed information including:
- Complete tool descriptions
- Feature comparison matrix
- Cost analysis
- Documentation status
- Official links

## 🎨 Architecture Diagrams

### What's Included

Each architecture diagram shows:
1. **Input Layer**: Data sources and configuration
2. **Core Components**: Main modules and services
3. **Processing Pipeline**: Data flow and transformations
4. **Output Layer**: Results and integrations
5. **Advanced Features**: Optional capabilities

### Formats Available

- **PNG**: High-resolution images for viewing
- **DOT**: GraphViz source for editing
- **Draw.io**: Editable diagrams for customization

### Diagram Generation

All diagrams are generated using Python's `diagrams` library:

```python
from diagrams import Diagram, Cluster, Edge
from diagrams.programming.language import Python
# ... component definitions ...
```

Requirements:
```bash
pip install diagrams
pip install graphviz2drawio  # Optional, for Draw.io export
```

## 🔍 Tool Selection Guide

### For Startups (Limited Resources)
**Recommended**: Promptfoo + DeepEval + LangFuse (free tier)
- Quick setup
- Essential features
- No cost

### For Enterprises (Scale & Compliance)
**Recommended**: MLFlow + LangFuse + Agenta + CleanLab
- Enterprise features
- Team collaboration
- Comprehensive coverage

### For Security-Focused Teams
**Recommended**: Promptfoo + CleanLab + DeepEval
- Red teaming
- Data validation
- Thorough testing

### For Research Teams
**Recommended**: Opik + MLFlow + DeepEval
- Experiment tracking
- Model comparison
- Metric evaluation

### For Production Monitoring
**Recommended**: LangFuse + Lmnr + MLFlow
- Detailed analytics
- Lightweight tracing
- Performance tracking

## 🔗 Integration Patterns

### Common Stack Combinations

#### Development Stack
```
DeepEval (testing) → Promptfoo (security) → LangFuse (monitoring)
```

#### Data-Centric Stack
```
CleanLab (data quality) → MLFlow (tracking) → DeepEval (evaluation)
```

#### Enterprise Stack
```
CleanLab (data) → Agenta (evaluation) → LangFuse (monitoring) → MLFlow (tracking)
```

## 📚 Resources

### Official Documentation
- CleanLab: https://docs.cleanlab.ai/
- Promptfoo: https://promptfoo.dev/docs/
- DeepEval: https://deepeval.com/docs/
- LangFuse: https://langfuse.com/docs/
- MLFlow: https://mlflow.org/docs/
- Agenta: https://docs.agenta.ai/
- n8n: https://docs.n8n.io/
- Lmnr: https://docs.lmnr.ai/
- Opik: https://comet.com/docs/opik/
- Latitude: https://docs.latitude.so/

### GitHub Repositories
All tools are open source. See TOOL_LIST.md for repository links.

### Community Support
Most tools have:
- Discord communities
- GitHub Discussions
- Regular office hours
- Active maintainers

## 🛠️ Development

### Adding New Tools

To add a new evaluation tool:

1. Create directory: `mkdir EVAL/NewTool`
2. Add README: `EVAL/NewTool/README.md`
3. Create diagram script: `EVAL/NewTool/newtool_architecture.py`
4. Update TOOL_LIST.md
5. Update EVALUATION_SUMMARY.md
6. Generate diagrams

### Diagram Template

Use existing tools as templates:
- CleanLab: Complex multi-cluster architecture
- Promptfoo: Workflow-focused architecture
- DeepEval: Testing-focused architecture

## 📈 Status & Progress

### Completed (3/10) ✅
- CleanLab: Full documentation + diagrams
- Promptfoo: Full documentation
- DeepEval: Full documentation

### In Progress (0/10) 🔄
- None currently

### Pending (7/10) ⏳
- LangFuse
- MLFlow
- Agenta
- Lmnr
- Opik
- Latitude
- n8n

## 🎯 Next Steps

1. ✅ Create evaluation framework
2. ✅ Document CleanLab, Promptfoo, DeepEval
3. ✅ Generate CleanLab architecture diagram
4. ⏳ Create architecture diagrams for Promptfoo & DeepEval
5. ⏳ Document remaining 7 tools
6. ⏳ Generate all architecture diagrams
7. ⏳ Create comparison visualizations
8. ⏳ Add usage examples and tutorials

## 📝 Notes

### Evaluation Criteria

Each tool is evaluated on:
1. **Functionality**: Core capabilities and features
2. **Developer Experience**: Ease of use and documentation
3. **Performance**: Speed, scalability, resource usage
4. **Deployment**: Hosting options and requirements
5. **Community**: Support, activity, ecosystem
6. **Cost**: Pricing and resource costs

### Methodology

- Cloned all repositories
- Reviewed documentation
- Analyzed architecture
- Tested key features
- Compared capabilities
- Created comprehensive documentation

## 🤝 Contributing

To contribute:
1. Review existing documentation
2. Follow established format
3. Include architecture diagrams
4. Add usage examples
5. Update comparison matrices

## 📄 License

This evaluation and documentation is provided as-is for educational purposes.
Each tool has its own license (see individual repositories).

---

**Last Updated**: November 18, 2025  
**Version**: 1.0  
**Status**: 3/10 tools complete  
**Maintainer**: Architecture Diagrams Project

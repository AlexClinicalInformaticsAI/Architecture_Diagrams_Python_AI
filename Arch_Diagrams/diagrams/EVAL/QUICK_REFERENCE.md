# LLM Evaluation Tools - Quick Reference Card

## 🎯 Choose Your Tool in 30 Seconds

### I need to...

#### Clean my training data
→ **[CleanLab](CleanLab/README.md)** ✅  
Detects label errors, outliers, duplicates

#### Test my LLM for security issues
→ **[Promptfoo](Promptfoo/README.md)** ✅  
Red teaming, vulnerability scanning

#### Write unit tests for my LLM
→ **[DeepEval](DeepEval/README.md)** ✅  
Pytest-style testing, 14+ metrics

#### Monitor my LLM in production
→ **LangFuse** ⏳  
Observability, analytics, tracing

#### Track ML experiments
→ **MLFlow** ⏳  
Industry standard, model registry

#### Manage prompts with my team
→ **Latitude** ⏳  
Version control, collaboration

#### Build AI workflows
→ **n8n** ⏳  
Visual automation, 400+ integrations

#### Run comprehensive evaluations
→ **Agenta** ⏳  
Full platform, A/B testing

#### Lightweight monitoring
→ **Lmnr** ⏳  
Simple tracing, minimal overhead

#### Track experiments (Comet users)
→ **Opik** ⏳  
Comet ML integration

---

## 📊 Quick Comparison

| Need | Tool | Status | Stars |
|------|------|--------|-------|
| Data Quality | CleanLab | ✅ | 9.5K |
| Security Testing | Promptfoo | ✅ | 4.5K |
| Unit Testing | DeepEval | ✅ | 3.5K |
| Production Monitoring | LangFuse | ⏳ | 6K |
| ML Lifecycle | MLFlow | ⏳ | 19K |
| Workflows | n8n | ⏳ | 50K |

---

## 🚀 Quick Start Commands

### CleanLab
```bash
pip install cleanlab
# See: CleanLab/README.md
```

### Promptfoo
```bash
npx promptfoo@latest init
npx promptfoo eval
# See: Promptfoo/README.md
```

### DeepEval
```bash
pip install deepeval
deepeval test run
# See: DeepEval/README.md
```

---

## 📚 Documentation Quick Links

### Start Here
- **[INDEX.md](INDEX.md)** - Master navigation
- **[README.md](README.md)** - Full overview
- **[EVALUATION_SUMMARY.md](EVALUATION_SUMMARY.md)** - Comparison guide

### Tool Docs (Complete)
- **[CleanLab/README.md](CleanLab/README.md)** - 14KB, complete
- **[Promptfoo/README.md](Promptfoo/README.md)** - 12KB, complete
- **[DeepEval/README.md](DeepEval/README.md)** - 11KB, complete

### Reference
- **[TOOL_LIST.md](TOOL_LIST.md)** - Detailed features
- **[COMPLETION_REPORT.md](COMPLETION_REPORT.md)** - Project status

---

## 🎨 Architecture Diagrams

### Available Now
```bash
# CleanLab architecture
open diagrams/EVAL/CleanLab/cleanlab_architecture.png
```

### Generate More
```bash
# Generate all diagrams
python Arch_Diagrams/diagrams/EVAL/generate_all_diagrams.py
```

---

## 💡 Common Scenarios

### Scenario 1: Starting a New LLM Project
**Stack**: DeepEval + Promptfoo
- DeepEval for unit testing
- Promptfoo for security

### Scenario 2: Production LLM App
**Stack**: LangFuse + CleanLab
- LangFuse for monitoring
- CleanLab for data quality

### Scenario 3: Enterprise ML Team
**Stack**: MLFlow + LangFuse + Agenta
- MLFlow for experiments
- LangFuse for monitoring
- Agenta for evaluation

### Scenario 4: Security-First
**Stack**: Promptfoo + CleanLab + DeepEval
- Promptfoo for red teaming
- CleanLab for data validation
- DeepEval for testing

---

## 🔗 External Links

### GitHub Repos
- CleanLab: https://github.com/cleanlab/cleanlab
- Promptfoo: https://github.com/promptfoo/promptfoo
- DeepEval: https://github.com/confident-ai/deepeval
- LangFuse: https://github.com/langfuse/langfuse
- MLFlow: https://github.com/mlflow/mlflow
- n8n: https://github.com/n8n-io/n8n
- Agenta: https://github.com/agenta-ai/agenta
- Lmnr: https://github.com/lmnr-ai/lmnr
- Opik: https://github.com/comet-ml/opik
- Latitude: https://github.com/latitude-dev/latitude

### Official Sites
- CleanLab: https://cleanlab.ai
- Promptfoo: https://promptfoo.dev
- DeepEval: https://deepeval.com
- LangFuse: https://langfuse.com
- MLFlow: https://mlflow.org
- n8n: https://n8n.io
- Agenta: https://agenta.ai
- Lmnr: https://lmnr.ai
- Opik: https://comet.com/opik
- Latitude: https://latitude.so

---

## 📞 Get Help

### Documentation
1. Check tool-specific README
2. Review EVALUATION_SUMMARY.md
3. See TOOL_LIST.md for details

### Community
- Most tools have Discord servers
- GitHub Discussions available
- Active maintainers

### Support
- Open source: Community support
- Cloud versions: Commercial support available

---

## ✅ Status Legend

- ✅ **Complete** - Full documentation + diagrams
- ⏳ **Pending** - Documentation in progress
- 📊 **Analyzed** - Repository reviewed

---

## 🎯 Decision Matrix

| If you value... | Choose... |
|----------------|-----------|
| Privacy | Promptfoo (100% local) |
| Simplicity | DeepEval (pytest-style) |
| Data Quality | CleanLab (unique focus) |
| Enterprise | MLFlow (industry standard) |
| Monitoring | LangFuse (comprehensive) |
| Workflows | n8n (visual builder) |
| Security | Promptfoo (red teaming) |
| Testing | DeepEval (14+ metrics) |

---

## 📈 By Team Size

### Solo Developer
- DeepEval (quick testing)
- Promptfoo (security)

### Small Team (2-10)
- DeepEval + LangFuse
- Promptfoo for security

### Medium Team (10-50)
- LangFuse + Agenta + CleanLab
- MLFlow for experiments

### Enterprise (50+)
- MLFlow + LangFuse + Agenta
- CleanLab for data quality
- Promptfoo for security

---

## 🔥 Hot Tips

1. **Start Simple**: Pick 1-2 tools, not all 10
2. **Test Locally**: Use Promptfoo/DeepEval first
3. **Monitor Production**: Add LangFuse when live
4. **Clean Data**: Use CleanLab before training
5. **Automate**: Integrate with CI/CD early

---

## 📝 Quick Notes

- All tools are open source
- Most have free tiers
- Self-hosting available
- Active communities
- Regular updates

---

**Last Updated**: November 18, 2025  
**Version**: 1.0  
**Status**: 3/10 tools documented

---

*For detailed information, see [INDEX.md](INDEX.md)*

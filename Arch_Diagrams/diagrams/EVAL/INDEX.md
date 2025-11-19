# LLM Evaluation Tools - Master Index

## 📋 Quick Navigation

### 📚 Documentation
- **[README.md](README.md)** - Main overview and getting started guide
- **[EVALUATION_SUMMARY.md](EVALUATION_SUMMARY.md)** - High-level comparison and selection guide
- **[TOOL_LIST.md](TOOL_LIST.md)** - Detailed tool list with features and status

### 🔧 Tools (Alphabetical)

1. **[Agenta](Agenta/)** ⏳ - LLM Evaluation Platform
2. **[CleanLab](CleanLab/)** ✅ - Data Quality & Label Cleaning
3. **[DeepEval](DeepEval/)** ✅ - LLM Evaluation Framework
4. **[LangFuse](LangFuse/)** ⏳ - LLM Observability & Analytics
5. **[Latitude](Latitude/)** ⏳ - Prompt Management
6. **[Lmnr](Lmnr/)** ⏳ - LLM Observability
7. **[MLFlow](MLFlow/)** ⏳ - ML Lifecycle Management
8. **[n8n](n8n/)** ⏳ - Workflow Automation
9. **[Opik](Opik/)** ⏳ - LLM Evaluation (Comet)
10. **[Promptfoo](Promptfoo/)** ✅ - LLM Testing & Red Teaming

### 🎨 Diagrams
All generated diagrams are located in: `diagrams/EVAL/<ToolName>/`

## 🎯 By Category

### Data Quality
- [CleanLab](CleanLab/) ✅ - Detect and fix data issues

### Testing & Evaluation
- [Promptfoo](Promptfoo/) ✅ - Testing and red teaming
- [DeepEval](DeepEval/) ✅ - Unit testing framework
- [Opik](Opik/) ⏳ - Experiment tracking
- [Agenta](Agenta/) ⏳ - Evaluation platform

### Observability
- [LangFuse](LangFuse/) ⏳ - Production monitoring
- [Lmnr](Lmnr/) ⏳ - Lightweight observability
- [MLFlow](MLFlow/) ⏳ - ML lifecycle tracking

### Prompt Management
- [Latitude](Latitude/) ⏳ - Prompt versioning
- [Agenta](Agenta/) ⏳ - Includes prompt features

### Workflows
- [n8n](n8n/) ⏳ - Visual automation

## 🚀 Quick Start Paths

### Path 1: Testing & Security
1. Read [Promptfoo/README.md](Promptfoo/README.md)
2. Read [DeepEval/README.md](DeepEval/README.md)
3. Review [EVALUATION_SUMMARY.md](EVALUATION_SUMMARY.md)

### Path 2: Data Quality
1. Read [CleanLab/README.md](CleanLab/README.md)
2. View `diagrams/EVAL/CleanLab/cleanlab_architecture.png`
3. Review use cases in [TOOL_LIST.md](TOOL_LIST.md)

### Path 3: Production Monitoring
1. Read [LangFuse/README.md](LangFuse/README.md) (pending)
2. Compare with [Lmnr/README.md](Lmnr/README.md) (pending)
3. Review [EVALUATION_SUMMARY.md](EVALUATION_SUMMARY.md)

### Path 4: Complete Overview
1. Start with [README.md](README.md)
2. Review [EVALUATION_SUMMARY.md](EVALUATION_SUMMARY.md)
3. Check [TOOL_LIST.md](TOOL_LIST.md) for details
4. Explore individual tool directories

## 📊 Status Dashboard

### ✅ Complete (3/10)
- CleanLab - Full docs + diagram
- Promptfoo - Full docs
- DeepEval - Full docs

### ⏳ Pending (7/10)
- LangFuse
- MLFlow
- Agenta
- Lmnr
- Opik
- Latitude
- n8n

## 🔗 External Resources

### Official Sites
- CleanLab: https://cleanlab.ai
- Promptfoo: https://promptfoo.dev
- DeepEval: https://deepeval.com
- LangFuse: https://langfuse.com
- Agenta: https://agenta.ai
- MLFlow: https://mlflow.org
- Lmnr: https://lmnr.ai
- Opik: https://comet.com/opik
- Latitude: https://latitude.so
- n8n: https://n8n.io

### GitHub Repositories
All repositories cloned and analyzed:
- cleanlab/cleanlab
- promptfoo/promptfoo
- confident-ai/deepeval
- langfuse/langfuse
- agenta-ai/agenta
- mlflow/mlflow
- lmnr-ai/lmnr
- comet-ml/opik
- latitude-dev/latitude
- n8n-io/n8n

## 🛠️ Scripts & Tools

### Generate Diagrams
```bash
# Generate all diagrams
python generate_all_diagrams.py

# Generate specific tool
python CleanLab/cleanlab_architecture.py
```

### View Diagrams
```bash
# CleanLab
open diagrams/EVAL/CleanLab/cleanlab_architecture.png

# Promptfoo (when generated)
open diagrams/EVAL/Promptfoo/promptfoo_architecture.png

# DeepEval (when generated)
open diagrams/EVAL/DeepEval/deepeval_architecture.png
```

## 📈 Comparison Tables

### By Popularity (GitHub Stars)
1. n8n - 50K+ ⏳
2. MLFlow - 19K+ ⏳
3. CleanLab - 9.5K+ ✅
4. LangFuse - 6K+ ⏳
5. Promptfoo - 4.5K+ ✅
6. DeepEval - 3.5K+ ✅
7. Opik - 2K+ ⏳
8. Agenta - 1.5K+ ⏳
9. Lmnr - 1K+ ⏳
10. Latitude - 500+ ⏳

### By Primary Language
**Python**:
- CleanLab ✅
- DeepEval ✅
- MLFlow ⏳
- Opik ⏳

**TypeScript**:
- Promptfoo ✅
- n8n ⏳
- Latitude ⏳

**Python + TypeScript**:
- LangFuse ⏳
- Agenta ⏳
- Lmnr ⏳

### By Deployment
**Local-First**:
- CleanLab ✅
- Promptfoo ✅
- DeepEval ✅
- MLFlow ⏳

**Cloud-First**:
- LangFuse ⏳
- Agenta ⏳

**Hybrid**:
- n8n ⏳
- Lmnr ⏳
- Opik ⏳
- Latitude ⏳

## 🎓 Learning Resources

### Beginner
1. Start with [README.md](README.md)
2. Read [EVALUATION_SUMMARY.md](EVALUATION_SUMMARY.md)
3. Pick one tool based on your needs
4. Follow that tool's README

### Intermediate
1. Review [TOOL_LIST.md](TOOL_LIST.md)
2. Compare multiple tools in your category
3. Study architecture diagrams
4. Test tools with your use case

### Advanced
1. Review all tool documentation
2. Compare architectures
3. Design custom evaluation pipeline
4. Integrate multiple tools

## 📝 Document Types

### README Files
- Tool overview
- Key features
- Architecture components
- Usage examples
- Integration guides
- Best practices

### Architecture Diagrams
- Visual component layout
- Data flow
- Integration points
- Workflow processes

### Comparison Documents
- Feature matrices
- Selection guides
- Use case recommendations
- Cost analysis

## 🔄 Update Schedule

### Completed
- ✅ Nov 18, 2025: Initial framework
- ✅ Nov 18, 2025: CleanLab complete
- ✅ Nov 18, 2025: Promptfoo complete
- ✅ Nov 18, 2025: DeepEval complete

### Planned
- ⏳ LangFuse documentation
- ⏳ MLFlow documentation
- ⏳ Remaining tool documentation
- ⏳ All architecture diagrams
- ⏳ Comparison visualizations

## 🤝 How to Use This Index

1. **Finding a Tool**: Use category sections or alphabetical list
2. **Comparing Tools**: Check EVALUATION_SUMMARY.md
3. **Learning**: Follow Quick Start Paths
4. **Implementation**: Read individual tool READMEs
5. **Architecture**: View generated diagrams

## 📞 Support & Community

Each tool has its own community:
- Discord servers
- GitHub Discussions
- Documentation sites
- Office hours

See individual tool READMEs for specific links.

---

**Version**: 1.0  
**Last Updated**: November 18, 2025  
**Status**: 3/10 tools documented  
**Next Update**: TBD

# Quick Start Guide - Educational Workflow Diagrams

## 🎯 What You Have

A complete educational workflow diagram generator using **simple flowchart symbols** (NOT technical architecture icons).

### Key Features:
✅ Rectangles, diamonds, circles (NO servers, APIs, cloud icons)  
✅ LLM-as-a-Judge evaluation workflows  
✅ OSCE agentic case generation  
✅ Assessment automation (Q1-Q40)  
✅ Export to PNG, SVG, DOT formats  

---

## 🚀 Quick Start (5 minutes)

### 1. Install Dependencies

```bash
# Install system package (one-time)
# macOS:
brew install graphviz

# Linux:
sudo apt-get install graphviz

# Windows:
# Download from https://graphviz.org/download/

# Install Python packages
pip install graphviz
```

### 2. Generate All Workflows

```bash
python generate_all_workflows.py
```

This creates 3 complete workflow diagrams in the `diagrams/` directory.

### 3. View Results

Open the `diagrams/` folder to see:
- **PNG files** - For PowerPoint, Word, presentations
- **SVG files** - For websites, documentation
- **DOT files** - For version control (Git)

---

## 📊 Pre-Generated Diagrams

You already have 3 example workflows generated:

1. **llm_judge_workflow.png**
   - LLM-as-a-Judge evaluation system
   - Student submits → LLM scores → QA review → Feedback

2. **osce_case_generation.png**
   - Multi-agent OSCE case creation
   - 4 AI agents collaborate to create clinical cases
   - Faculty review and approval workflow

3. **assessment_generation_batch.png**
   - Generate 40 assessment questions
   - Difficulty stratification (Easy/Medium/Hard)
   - Quality validation pipeline

---

## 🎨 Create Your Own Workflow

```python
from educational_workflow import EducationalWorkflowDiagram

# Create diagram
diagram = EducationalWorkflowDiagram(
    title='My Educational Workflow',
    filename='my_workflow',
    direction='TB'  # Top-to-bottom
)

# Add swimlane for student
diagram.create_swimlane('Student')
start = diagram.add_start('Begin')
step1 = diagram.add_process('Submit Response', time='5 min')
diagram.end_swimlane()

# Add swimlane for LLM
diagram.create_swimlane('LLM Judge')
llm = diagram.add_llm_process('Evaluate', 'Claude Sonnet 4')
decision = diagram.add_decision('Score >= 70%?')
diagram.end_swimlane()

# Connect nodes
diagram.connect(start, step1)
diagram.connect(step1, llm, emphasis=True)
diagram.connect(llm, decision)

# Save
diagram.save()
```

---

## 📚 Documentation

- **README.md** - Complete user guide
- **EDUCATIONAL_WORKFLOW_AGENT.md** - Detailed agent instructions
- **example_*.py** - Three working examples
- **educational_workflow.py** - Core library

---

## 🎯 Key Differences from Technical Diagrams

| ❌ Old Way (Technical) | ✅ New Way (Educational) |
|-----------------------|--------------------------|
| AWS/Azure icons | Simple rectangles |
| Servers & APIs | Process steps |
| Network topology | Student journey |
| Infrastructure | People & activities |
| Microservices | Learning workflows |

---

## 🔧 Customization

### Change Colors
```python
diagram.create_swimlane('Custom', '#FFE6E6')
```

### Add Time Estimates
```python
step = diagram.add_process('Review', time='15 min')
```

### Create Decision Points
```python
decision = diagram.add_decision('Approved?')
diagram.connect_yes(decision, next_step)
diagram.connect_no(decision, error_handler)
```

### Add Validation
```python
validation = diagram.add_validation('Score > 70%?')
```

### Human Review
```python
review = diagram.add_human_review('Faculty Approval')
```

---

## 📊 Available Shapes

- **Circle** → Start/End
- **Rectangle** → Process/Activity
- **Diamond** → Decision
- **Parallelogram** → Data/Input/Output
- **Cylinder** → Database
- **Note** → Document
- **Trapezoid** → Manual Input
- **Hexagon** → Preparation

---

## ✨ Examples Included

### 1. LLM-as-a-Judge (`example_llm_judge.py`)
Automated student assessment with quality assurance

### 2. OSCE Generation (`example_osce_generation.py`)
Multi-agent clinical case creation pipeline

### 3. Assessment Batch (`example_assessment_generation.py`)
Generate 40 questions with difficulty stratification

---

## 🎓 Use Cases

- Medical education workflows
- Clinical assessment automation
- OSCE station design
- Quality improvement processes
- AI/LLM integration documentation
- Educational content pipelines

---

## 🚫 What This ISN'T

This is NOT for:
- ❌ Technical system architecture
- ❌ Cloud infrastructure diagrams
- ❌ API documentation
- ❌ Network topology
- ❌ Microservices architecture

This IS for:
- ✅ Educational process flows
- ✅ Student assessment workflows
- ✅ Clinical case generation
- ✅ Learning activity diagrams
- ✅ Quality improvement processes

---

## 💡 Tips

1. **Keep it simple** - Use standard shapes only
2. **Use swimlanes** - Group by participant/role
3. **Show decisions** - Diamond shapes for branching
4. **Highlight critical paths** - Use emphasis=True
5. **Add time estimates** - Show process duration
6. **Document handoffs** - Mark transition points

---

## 🔗 Next Steps

1. ✅ Review the pre-generated diagrams
2. ✅ Read README.md for full documentation
3. ✅ Run `generate_all_workflows.py` 
4. ✅ Modify examples for your needs
5. ✅ Create custom workflows

---

## 📧 Questions?

Review the documentation files:
- **README.md** - Complete guide
- **EDUCATIONAL_WORKFLOW_AGENT.md** - Technical details
- **example_*.py** - Working code examples

---

**Simple flowchart diagrams for medical education - no technical architecture!**

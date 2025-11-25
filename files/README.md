# Educational Workflow Diagram Generator

**Simple flowchart diagrams for medical education workflows**  
🚫 NO technical architecture icons (servers, APIs, cloud)  
✅ YES standard flowchart symbols (rectangles, diamonds, circles)

---

## Overview

This tool generates clean, professional workflow diagrams for:
- **LLM-as-a-Judge** evaluation systems
- **OSCE** (Objective Structured Clinical Examination) case generation
- **Assessment automation** pipelines
- **Educational content** workflows

### What Makes This Different?

| ❌ Traditional Technical Diagrams | ✅ Our Educational Workflows |
|-----------------------------------|------------------------------|
| AWS/Azure cloud icons | Simple rectangles and diamonds |
| Servers and databases | Process steps and decision points |
| API calls and microservices | Human activities and workflows |
| Infrastructure as Code | Educational processes |
| Network topology | Student journey mapping |

---

## Quick Start

### 1. Installation

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install graphviz==0.20.3
pip install graphviz2drawio==1.1.0

# Install Graphviz system package
# macOS:
brew install graphviz

# Linux (Ubuntu/Debian):
sudo apt-get install graphviz

# Windows:
# Download from https://graphviz.org/download/
```

### 2. Generate Workflows

```bash
# Generate all example workflows
python generate_all_workflows.py

# Or generate individually
python example_llm_judge.py
python example_osce_generation.py
python example_assessment_generation.py
```

### 3. View Results

```bash
# Open the diagrams directory
open diagrams/  # macOS
xdg-open diagrams/  # Linux
explorer diagrams\  # Windows

# Files generated:
# - *.png (for presentations)
# - *.svg (for web/scaling)
# - *.dot (for version control)
# - *.drawio (for editing)
```

---

## Standard Flowchart Symbols

### Basic Shapes

```
┌─────────────────┬──────────────────┬─────────────────────────┐
│ Shape           │ Symbol           │ Use Case                │
├─────────────────┼──────────────────┼─────────────────────────┤
│ Circle/Ellipse  │  ⭕ Start/End    │ Begin/End workflow      │
│ Rectangle       │  ▭ Process       │ Activities, steps       │
│ Diamond         │  ◇ Decision      │ Yes/No questions        │
│ Parallelogram   │  ▱ Data/I/O      │ Input/output data       │
│ Cylinder        │  🗄️ Database     │ Data storage            │
│ Note            │  📄 Document     │ Reports, forms          │
│ Hexagon         │  ⬡ Preparation   │ Setup activities        │
│ Trapezoid       │  ⏢ Manual Input  │ Human review            │
└─────────────────┴──────────────────┴─────────────────────────┘
```

### Specialized Educational Shapes

- **🤖 LLM Process** - AI/LLM operations (orange box)
- **✓ Validation** - Quality checkpoints (green diamond)
- **⚠️ Error Handler** - Error handling (red box)
- **💬 Feedback** - Feedback generation (yellow note)
- **👤 Human Review** - Manual review (purple trapezoid)

---

## Example Workflows

### 1. LLM-as-a-Judge Evaluation

**File**: `example_llm_judge.py`

**Purpose**: Automated assessment of medical student responses

**Key Features**:
- Student submits clinical case response
- LLM analyzes and scores against rubric
- Quality assurance with human oversight
- Detailed feedback generation
- Continuous model improvement

**Participants**:
- Student (submits responses)
- Assessment System (retrieves cases)
- LLM Judge (evaluates responses)
- Quality Assurance (monitors scoring)
- Output System (delivers feedback)

---

### 2. OSCE Agentic Case Generation

**File**: `example_osce_generation.py`

**Purpose**: Multi-agent AI system for clinical case creation

**Key Features**:
- Curriculum team specifies requirements
- AI agents collaborate to create cases
- Medical accuracy validation
- Faculty review and approval
- Case library integration

**Agent Roles**:
1. **Medical Writer Agent** - Creates clinical scenarios
2. **Clinical Expert Agent** - Validates medical accuracy
3. **Assessment Agent** - Develops scoring rubrics
4. **Difficulty Agent** - Calibrates complexity

---

### 3. Assessment Question Generation (Q1-Q40)

**File**: `example_assessment_generation.py`

**Purpose**: Batch generation of 40 assessment questions

**Key Features**:
- Difficulty stratification (Easy/Medium/Hard)
- Bloom's Taxonomy alignment
- Clinical accuracy verification
- Duplicate detection
- Direct export to Google Forms

**Question Distribution**:
- Q1-Q10: Easy (25%)
- Q11-Q30: Medium (50%)
- Q31-Q40: Hard (25%)

---

## Python API Usage

### Basic Workflow

```python
from educational_workflow import EducationalWorkflowDiagram

# Create diagram
diagram = EducationalWorkflowDiagram(
    title='My Workflow',
    filename='my_workflow',
    direction='TB'  # Top-to-bottom
)

# Add start point
start = diagram.add_start('Begin')

# Add process step
step1 = diagram.add_process('Process Data', time='5 min')

# Add decision
decision = diagram.add_decision('Is Valid?')

# Add end point
end = diagram.add_end('Complete')

# Connect nodes
diagram.connect(start, step1)
diagram.connect(step1, decision)
diagram.connect_yes(decision, end)

# Save
diagram.save()
diagram.convert_to_drawio()
```

### Using Swimlanes

```python
# Create swimlane for Student
diagram.create_swimlane('Student', '#E3F2FD')
s1 = diagram.add_process('Submit Response')
diagram.end_swimlane()

# Create swimlane for LLM Judge
diagram.create_swimlane('LLM Judge', '#FFF3E0')
l1 = diagram.add_llm_process('Evaluate', 'Claude Sonnet 4')
diagram.end_swimlane()

# Connect across swimlanes
diagram.connect(s1, l1, label='Submit', emphasis=True)
```

### Specialized Nodes

```python
# LLM processing
llm = diagram.add_llm_process('Analyze Text', 'Claude Sonnet 4')

# Validation checkpoint
val = diagram.add_validation('Score > 70%?')

# Human review
review = diagram.add_human_review('Faculty Approval')

# Feedback generation
feedback = diagram.add_feedback('Constructive Feedback')

# Error handling
error = diagram.add_error_handler('Retry Generation')

# Feedback loop
diagram.connect_feedback_loop(error, llm, 'Retry')
```

---

## Color Palette

### Participant Colors
```python
COLORS = {
    'student': '#E3F2FD',      # Light blue
    'instructor': '#F3E5F5',   # Light purple
    'llm_judge': '#FFF3E0',    # Light orange
    'system': '#E0F2F1',       # Light teal
    'assessment': '#E8F5E9',   # Light green
    'feedback': '#FFFDE7',     # Light yellow
    'quality': '#FFEBEE',      # Light red
}
```

### Status Colors
- **Success**: Light green
- **Warning**: Yellow
- **Error**: Light coral
- **Info**: Light blue

---

## File Outputs

Each workflow generates 4 files:

1. **PNG** - Raster image for presentations
   - Use in: PowerPoint, Word, Email
   - Resolution: High quality
   
2. **SVG** - Vector image for web/scaling
   - Use in: Websites, HTML docs
   - Scales without quality loss
   
3. **DOT** - GraphViz source code
   - Use in: Version control (Git)
   - Text-based, diff-friendly
   
4. **DRAWIO** - Editable diagram
   - Use in: Draw.io / diagrams.net
   - Full editing capabilities

---

## Best Practices

### 1. Keep It Simple
- ✅ Use standard shapes
- ✅ Limit to 5-6 colors per diagram
- ✅ Clear, concise labels
- ❌ Avoid clutter and complexity

### 2. Tell a Story
- ✅ Left-to-right or top-to-bottom flow
- ✅ Group related activities in swimlanes
- ✅ Show decision points clearly
- ✅ Highlight critical paths with emphasis

### 3. Educational Focus
- ✅ Always show student perspective
- ✅ Mark quality checkpoints
- ✅ Show feedback loops
- ✅ Document time estimates

### 4. Maintainability
- ✅ Save .dot files for version control
- ✅ Use consistent naming conventions
- ✅ Comment your code
- ✅ Generate .drawio for easy editing

---

## Customization

### Change Layout Direction

```python
# Top to bottom (default)
diagram = EducationalWorkflowDiagram(..., direction='TB')

# Left to right (pipeline view)
diagram = EducationalWorkflowDiagram(..., direction='LR')
```

### Custom Colors

```python
# Use custom color for swimlane
diagram.create_swimlane('Custom', '#FFE6E6')

# Use custom color for process
step = diagram.add_process('Step', color='#E6F3FF')
```

### Custom Labels

```python
# Add time estimate
step = diagram.add_process('Review', time='15 min')

# Multi-line labels
doc = diagram.add_document('Report:\n- Summary\n- Recommendations')
```

---

## Troubleshooting

### Graphviz not found

```bash
# Error: "graphviz executable not found"
# Solution: Install system package

# macOS
brew install graphviz

# Linux
sudo apt-get install graphviz

# Windows
# Download from https://graphviz.org/download/
# Add to PATH
```

### Import errors

```bash
# Error: "No module named 'graphviz'"
# Solution: Install Python packages

pip install graphviz graphviz2drawio
```

### Draw.io conversion fails

```bash
# Warning: "graphviz2drawio not installed"
# Solution (optional):

pip install graphviz2drawio
```

---

## Advanced Topics

### Custom Node Shapes

See `educational_workflow.py` for the full `EducationalWorkflowDiagram` class. You can extend it with custom node types:

```python
def add_custom_node(self, label: str) -> str:
    """Add your custom node type"""
    return self._add_node('custom', label, 'octagon', 'lightpink')
```

### Complex Workflows

For complex multi-page workflows:
1. Break into logical sub-processes
2. Create separate diagrams for each
3. Link them with document references

### Version Control

Commit `.dot` files to Git:
```bash
git add diagrams/*.dot
git commit -m "Update workflow diagrams"
```

PNG/SVG files can be committed or generated on-demand.

---

## Documentation

- **Full Agent Guide**: `EDUCATIONAL_WORKFLOW_AGENT.md`
- **API Reference**: See docstrings in `educational_workflow.py`
- **Examples**: `example_*.py` files

---

## Use Cases

### Medical Education
- ✅ Clinical case generation
- ✅ Student assessment workflows
- ✅ OSCE station design
- ✅ Competency evaluation

### Quality Improvement
- ✅ Process mapping
- ✅ Workflow optimization
- ✅ Handoff documentation
- ✅ Safety checkpoint visualization

### AI/LLM Integration
- ✅ LLM-as-a-Judge systems
- ✅ Multi-agent pipelines
- ✅ Automated content generation
- ✅ Quality assurance workflows

---

## Contributing

### Adding New Examples

1. Create `example_your_workflow.py`
2. Use `EducationalWorkflowDiagram` class
3. Follow naming conventions
4. Add to `generate_all_workflows.py`

### Suggesting Features

Open an issue or submit a pull request.

---

## License

[Specify your license here]

---

## Support

For questions or issues:
- Review documentation in `EDUCATIONAL_WORKFLOW_AGENT.md`
- Check examples in `example_*.py` files
- Review generated diagrams in `diagrams/` directory

---

## Summary

This tool creates **simple, clean educational workflow diagrams** using standard flowchart symbols:

✅ **Rectangles, diamonds, circles** - Not servers and APIs  
✅ **Clean swimlane layouts** - Not network topology  
✅ **Focus on people and processes** - Not infrastructure  
✅ **Export to PNG, SVG, Draw.io** - Multiple formats  
✅ **Perfect for presentations** - Professional quality  

**Ideal for**: LLM-as-a-Judge evaluation, OSCE case generation, assessment automation, and any educational workflow visualization.

---

*Simple flowchart diagrams for medical education - no technical architecture.*

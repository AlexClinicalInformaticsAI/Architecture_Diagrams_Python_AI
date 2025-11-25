# Healthcare Educational Workflow Agent: LLM-as-a-Judge & OSCE Case Generation

## Overview
This agent generates educational workflow diagrams for medical education systems using **standard flowchart symbols** (not technical architecture icons). Focus areas:
- **LLM-as-a-Judge** evaluation workflows
- **OSCE (Objective Structured Clinical Examination)** agentic case generation
- **Assessment automation** processes
- **Educational content pipelines**

**Output**: Clean, simple workflow diagrams using squares, diamonds, circles, documents - exported to PNG, SVG, and editable Draw.io format.

---

## Core Principles

### Use Simple Flowchart Symbols
✅ **Rectangle** - Process/Activity  
✅ **Diamond** - Decision Point  
✅ **Circle/Oval** - Start/End  
✅ **Parallelogram** - Document/Input/Output  
✅ **Cylinder** - Database/Storage  
✅ **Hexagon** - Preparation/Setup  
✅ **Trapezoid** - Manual Input  
✅ **Rounded Rectangle** - Subprocess  

❌ **NO Azure/AWS icons** (servers, cloud, networks)  
❌ **NO technical architecture** (APIs, microservices)  

### Focus on Educational Workflows
- Student assessment processes
- Case generation pipelines
- Evaluation and scoring
- Feedback loops
- Quality assurance
- Content validation

---

## Environment Setup

```bash
# Install required packages
pip install graphviz==0.20.3
pip install graphviz2drawio==1.1.0

# Install Graphviz system package
# macOS: brew install graphviz
# Linux: sudo apt-get install graphviz
# Windows: Download from graphviz.org
```

---

## Standard Flowchart Shape Library

```python
"""
Standard flowchart shapes for educational workflows
"""

from graphviz import Digraph

# SHAPE REFERENCE
SHAPES = {
    'process': 'box',              # Process step (rectangle)
    'decision': 'diamond',          # Decision point
    'start_end': 'ellipse',        # Start/End terminator
    'document': 'note',            # Document/Report
    'data': 'parallelogram',       # Input/Output data
    'database': 'cylinder',         # Database/Storage
    'preparation': 'hexagon',       # Preparation/Setup
    'manual': 'trapezium',         # Manual input
    'subprocess': 'box',           # Subprocess (double border)
    'delay': 'box',                # Delay/Wait time
}

# COLOR PALETTE (Educational Context)
COLORS = {
    'student': '#E3F2FD',          # Light blue
    'instructor': '#F3E5F5',       # Light purple
    'llm_judge': '#FFF3E0',        # Light orange
    'system': '#E0F2F1',           # Light teal
    'assessment': '#E8F5E9',       # Light green
    'feedback': '#FFFDE7',         # Light yellow
    'quality': '#FFEBEE',          # Light red
    'success': 'lightgreen',       # Success state
    'error': 'lightcoral',         # Error state
    'warning': 'yellow',           # Warning state
    'info': 'lightblue',           # Information
}
```

---

## Educational Workflow Diagram Generator

```python
"""
Educational Workflow Diagram Generator
Simple flowchart symbols for LLM-as-a-Judge and OSCE workflows
"""

from graphviz import Digraph
from typing import Dict, Optional, List, Tuple
import os

class EducationalWorkflowDiagram:
    """Generate educational workflow diagrams with standard flowchart symbols"""
    
    def __init__(self, title: str, filename: str, direction: str = 'TB'):
        """
        Initialize diagram
        
        Args:
            title: Diagram title
            filename: Output filename (without extension)
            direction: Layout direction ('TB'=top-to-bottom, 'LR'=left-to-right)
        """
        self.dot = Digraph(comment=title)
        self.dot.attr(
            rankdir=direction,
            splines='ortho',
            nodesep='0.8',
            ranksep='0.8',
            fontname='Arial',
            fontsize='12'
        )
        self.dot.attr('node', fontname='Arial', fontsize='10')
        self.dot.attr('edge', fontname='Arial', fontsize='9')
        self.filename = filename
        self.counter = 0
        self.current_cluster = None
        
    def create_swimlane(self, name: str, color: str = 'lightgrey') -> 'EducationalWorkflowDiagram':
        """
        Create a swimlane (cluster) for grouping related activities
        
        Args:
            name: Swimlane label (e.g., "Student", "LLM Judge", "System")
            color: Background color
        """
        cluster_name = f'cluster_{name.lower().replace(" ", "_")}'
        self.current_cluster = self.dot.subgraph(name=cluster_name)
        self.current_cluster.attr(
            label=name,
            style='filled',
            color='black',
            fillcolor=color,
            fontsize='12',
            labeljust='l'
        )
        return self
    
    def end_swimlane(self):
        """End current swimlane"""
        self.current_cluster = None
    
    def _add_node(self, node_type: str, label: str, 
                  shape: str, color: str, **kwargs) -> str:
        """Internal: Add node with auto-generated ID"""
        node_id = f'{node_type}_{self.counter}'
        self.counter += 1
        
        target = self.current_cluster if self.current_cluster else self.dot
        target.node(
            node_id, 
            label, 
            shape=shape, 
            style='filled', 
            fillcolor=color,
            **kwargs
        )
        return node_id
    
    # ===== BASIC SHAPES =====
    
    def add_start(self, label: str = 'Start') -> str:
        """Add start point (circle)"""
        return self._add_node('start', label, 'ellipse', 'lightgreen', penwidth='2')
    
    def add_end(self, label: str = 'End') -> str:
        """Add end point (circle)"""
        return self._add_node('end', label, 'ellipse', 'lightcoral', penwidth='2')
    
    def add_process(self, label: str, color: str = 'lightblue', 
                    time: Optional[str] = None) -> str:
        """
        Add process step (rectangle)
        
        Args:
            label: Process description
            color: Fill color
            time: Optional time estimate (e.g., "5 min")
        """
        if time:
            label = f'{label}\\n({time})'
        return self._add_node('process', label, 'box', color)
    
    def add_decision(self, label: str, color: str = 'yellow') -> str:
        """
        Add decision point (diamond)
        
        Args:
            label: Question to be decided (e.g., "Score >= 70%?")
        """
        return self._add_node('decision', label, 'diamond', color)
    
    def add_document(self, label: str, color: str = 'lightgreen') -> str:
        """
        Add document/report (note shape)
        
        Args:
            label: Document name (e.g., "Assessment Report")
        """
        return self._add_node('doc', label, 'note', color)
    
    def add_data(self, label: str, color: str = 'lightyellow') -> str:
        """
        Add data input/output (parallelogram)
        
        Args:
            label: Data description (e.g., "Student Response")
        """
        return self._add_node('data', label, 'parallelogram', color)
    
    def add_database(self, label: str, color: str = 'lightcyan') -> str:
        """
        Add database/storage (cylinder)
        
        Args:
            label: Database name (e.g., "Case Library")
        """
        return self._add_node('db', label, 'cylinder', color)
    
    def add_subprocess(self, label: str, color: str = 'lightblue') -> str:
        """
        Add subprocess (rectangle with double border)
        
        Args:
            label: Subprocess name
        """
        return self._add_node('subprocess', label, 'box', color, 
                            peripheries='2')
    
    def add_manual(self, label: str, color: str = 'lightyellow') -> str:
        """
        Add manual input (trapezoid)
        
        Args:
            label: Manual activity description
        """
        return self._add_node('manual', label, 'trapezium', color)
    
    def add_preparation(self, label: str, color: str = 'lightgrey') -> str:
        """
        Add preparation step (hexagon)
        
        Args:
            label: Preparation activity
        """
        return self._add_node('prep', label, 'hexagon', color)
    
    # ===== SPECIALIZED NODES =====
    
    def add_llm_process(self, label: str, model: str = None) -> str:
        """
        Add LLM processing step (special colored rectangle)
        
        Args:
            label: LLM task description
            model: Optional model name (e.g., "Claude Sonnet 4")
        """
        if model:
            label = f'🤖 {label}\\n[{model}]'
        else:
            label = f'🤖 {label}\\n[LLM]'
        return self._add_node('llm', label, 'box', '#FFF3E0', penwidth='2')
    
    def add_validation(self, label: str) -> str:
        """
        Add validation checkpoint (special colored diamond)
        
        Args:
            label: Validation criteria
        """
        label = f'✓ VALIDATION:\\n{label}'
        return self._add_node('validation', label, 'diamond', '#E8F5E9', 
                            penwidth='2', color='green')
    
    def add_error_handler(self, label: str) -> str:
        """
        Add error handling step (red rectangle)
        
        Args:
            label: Error handling description
        """
        label = f'⚠️ ERROR:\\n{label}'
        return self._add_node('error', label, 'box', '#FFEBEE', 
                            color='red', penwidth='2')
    
    def add_feedback(self, label: str) -> str:
        """
        Add feedback generation step (special colored document)
        
        Args:
            label: Feedback type
        """
        label = f'💬 FEEDBACK:\\n{label}'
        return self._add_node('feedback', label, 'note', '#FFFDE7')
    
    def add_human_review(self, label: str) -> str:
        """
        Add human review step (manual input with special styling)
        
        Args:
            label: Review activity
        """
        label = f'👤 HUMAN REVIEW:\\n{label}'
        return self._add_node('human', label, 'trapezium', '#F3E5F5', 
                            penwidth='2')
    
    # ===== CONNECTIONS =====
    
    def connect(self, from_node: str, to_node: str, 
                label: Optional[str] = None, 
                style: str = 'solid',
                color: str = 'black',
                emphasis: bool = False) -> None:
        """
        Connect two nodes
        
        Args:
            from_node: Source node ID
            to_node: Target node ID
            label: Edge label
            style: 'solid', 'dashed', 'dotted', 'bold'
            color: Edge color
            emphasis: Make edge bold and colored (for critical paths)
        """
        attrs = {'label': label} if label else {}
        
        if emphasis:
            attrs.update({'color': 'red', 'penwidth': '2', 'style': 'bold'})
        else:
            attrs.update({'color': color, 'style': style})
        
        self.dot.edge(from_node, to_node, **attrs)
    
    def connect_yes(self, from_decision: str, to_node: str, 
                    label: str = 'Yes') -> None:
        """Connect decision to next node with 'Yes' label"""
        self.connect(from_decision, to_node, label, color='green')
    
    def connect_no(self, from_decision: str, to_node: str, 
                   label: str = 'No') -> None:
        """Connect decision to next node with 'No' label"""
        self.connect(from_decision, to_node, label, color='red', style='dashed')
    
    def connect_feedback_loop(self, from_node: str, to_node: str, 
                             label: str = 'Iterate') -> None:
        """Connect feedback loop (dashed, colored)"""
        self.connect(from_node, to_node, label, style='dashed', color='orange')
    
    # ===== OUTPUT =====
    
    def save(self, output_dir: str = 'diagrams') -> None:
        """
        Save diagram to multiple formats
        
        Args:
            output_dir: Output directory path
        """
        os.makedirs(output_dir, exist_ok=True)
        
        filepath = os.path.join(output_dir, self.filename)
        
        # Render PNG and SVG
        self.dot.render(filepath, format='png', cleanup=True)
        self.dot.render(filepath, format='svg', cleanup=True)
        
        # Save DOT source
        self.dot.save(f'{filepath}.dot')
        
        print(f'✅ Generated workflow diagrams:')
        print(f'   📊 {filepath}.png')
        print(f'   📊 {filepath}.svg')
        print(f'   📄 {filepath}.dot')
        
    def convert_to_drawio(self, output_dir: str = 'diagrams') -> None:
        """
        Convert to Draw.io format
        
        Requires: graphviz2drawio package
        """
        try:
            import graphviz2drawio
            
            filepath = os.path.join(output_dir, self.filename)
            dot_file = f'{filepath}.dot'
            drawio_file = f'{filepath}.drawio'
            
            graphviz2drawio.graphviz2drawio.convert(
                dot_file,
                drawio_file
            )
            
            print(f'   ✏️  {drawio_file} (editable in Draw.io)')
            
        except ImportError:
            print('⚠️  graphviz2drawio not installed. Skipping Draw.io conversion.')
            print('   Install with: pip install graphviz2drawio')
```

---

## Example 1: LLM-as-a-Judge Workflow

```python
"""
Example 1: LLM-as-a-Judge Evaluation Workflow
For automated assessment of medical student responses
"""

def create_llm_judge_workflow():
    """Generate LLM-as-a-Judge evaluation workflow"""
    
    diagram = EducationalWorkflowDiagram(
        title='LLM-as-a-Judge: Medical Student Assessment',
        filename='llm_judge_workflow',
        direction='TB'
    )
    
    # ===== SWIMLANE 1: STUDENT =====
    diagram.create_swimlane('Student', '#E3F2FD')
    
    start = diagram.add_start('Begin Assessment')
    s1 = diagram.add_process('Read Clinical Case', time='5 min')
    s2 = diagram.add_data('Submit Response\\n(Text or Audio)')
    s3 = diagram.add_process('Review Feedback')
    
    diagram.end_swimlane()
    
    # ===== SWIMLANE 2: SYSTEM =====
    diagram.create_swimlane('Assessment System', '#E0F2F1')
    
    sys1 = diagram.add_database('Case Library\\n(1000+ cases)')
    sys2 = diagram.add_process('Retrieve Case\\n+ Rubric')
    sys3 = diagram.add_preparation('Prepare Prompt\\nfor LLM Judge')
    
    diagram.end_swimlane()
    
    # ===== SWIMLANE 3: LLM JUDGE =====
    diagram.create_swimlane('LLM Judge', '#FFF3E0')
    
    llm1 = diagram.add_llm_process('Analyze Response', 'Claude Sonnet 4')
    llm2 = diagram.add_llm_process('Score Against Rubric', 'Claude Sonnet 4')
    
    val1 = diagram.add_validation('Score\\nConsistent?')
    
    llm3 = diagram.add_llm_process('Generate Feedback', 'Claude Sonnet 4')
    
    diagram.end_swimlane()
    
    # ===== SWIMLANE 4: QUALITY ASSURANCE =====
    diagram.create_swimlane('Quality Assurance', '#F3E5F5')
    
    qa1 = diagram.add_decision('Score in\\nExpected Range?')
    qa2 = diagram.add_human_review('Faculty Review\\n(Edge Cases)')
    qa3 = diagram.add_process('Log for Model\\nRetraining')
    
    diagram.end_swimlane()
    
    # ===== SWIMLANE 5: OUTPUT =====
    diagram.create_swimlane('Output', '#E8F5E9')
    
    out1 = diagram.add_document('Detailed Score Report')
    out2 = diagram.add_feedback('Constructive Feedback')
    out3 = diagram.add_database('Store in\\nStudent Record')
    end = diagram.add_end('Assessment Complete')
    
    diagram.end_swimlane()
    
    # ===== CONNECTIONS =====
    
    # Student flow
    diagram.connect(start, s1)
    diagram.connect(s1, sys1)
    diagram.connect(sys1, sys2)
    diagram.connect(sys2, s1)
    diagram.connect(s1, s2)
    
    # System processing
    diagram.connect(s2, sys3, label='Submit')
    diagram.connect(sys3, llm1, emphasis=True, label='Judge Request')
    
    # LLM Judge flow
    diagram.connect(llm1, llm2)
    diagram.connect(llm2, val1)
    
    # Validation paths
    diagram.connect_yes(val1, llm3)
    diagram.connect_no(val1, llm1, label='Re-analyze')
    
    # Quality assurance
    diagram.connect(llm3, qa1)
    diagram.connect_yes(qa1, out1)
    diagram.connect_no(qa1, qa2, label='Flag for Review')
    diagram.connect(qa2, out1, label='Approved')
    diagram.connect(qa2, qa3, label='Model Drift Detected')
    
    # Output generation
    diagram.connect(llm3, out2)
    diagram.connect(out1, out3)
    diagram.connect(out2, out3)
    diagram.connect(out3, s3, label='Deliver to Student')
    diagram.connect(s3, end)
    
    # Feedback loop for continuous improvement
    diagram.connect_feedback_loop(qa3, sys1, 'Update Model')
    
    # Save outputs
    diagram.save()
    diagram.convert_to_drawio()
    
    return diagram


if __name__ == '__main__':
    create_llm_judge_workflow()
    print('\\n✅ LLM-as-a-Judge workflow diagram created!')
```

---

## Example 2: OSCE Agentic Case Generation

```python
"""
Example 2: OSCE (Objective Structured Clinical Examination) Case Generation
Automated generation of clinical cases using agentic AI
"""

def create_osce_case_generation_workflow():
    """Generate OSCE agentic case generation workflow"""
    
    diagram = EducationalWorkflowDiagram(
        title='OSCE Agentic Case Generation Pipeline',
        filename='osce_case_generation',
        direction='TB'
    )
    
    # ===== SWIMLANE 1: CURRICULUM TEAM =====
    diagram.create_swimlane('Curriculum Team', '#F3E5F5')
    
    start = diagram.add_start('Initiate\\nCase Request')
    c1 = diagram.add_manual('Specify Requirements:\\n- Learning objectives\\n- Difficulty level\\n- Clinical domain')
    c2 = diagram.add_document('Case Specifications')
    
    diagram.end_swimlane()
    
    # ===== SWIMLANE 2: CASE LIBRARY =====
    diagram.create_swimlane('Case Library', '#E0F2F1')
    
    lib1 = diagram.add_database('Existing Cases\\n(500+ validated)')
    lib2 = diagram.add_decision('Similar\\nCase Exists?')
    lib3 = diagram.add_process('Retrieve Template')
    
    diagram.end_swimlane()
    
    # ===== SWIMLANE 3: AI AGENTS =====
    diagram.create_swimlane('Agentic AI System', '#FFF3E0')
    
    agent1 = diagram.add_llm_process('Medical Writer Agent\\nGenerate Case Scenario', 'Claude Opus 4')
    agent2 = diagram.add_llm_process('Clinical Expert Agent\\nValidate Medical Accuracy', 'Claude Sonnet 4')
    agent3 = diagram.add_llm_process('Assessment Agent\\nCreate Rubric', 'Claude Sonnet 4')
    agent4 = diagram.add_llm_process('Difficulty Agent\\nCalibrate Complexity', 'Claude Sonnet 4')
    
    val1 = diagram.add_validation('Medical Accuracy\\n>95%?')
    val2 = diagram.add_validation('Rubric\\nComplete?')
    
    diagram.end_swimlane()
    
    # ===== SWIMLANE 4: QUALITY REVIEW =====
    diagram.create_swimlane('Faculty Review', '#E8F5E9')
    
    qa1 = diagram.add_human_review('Physician Review\\nClinical Accuracy')
    qa2 = diagram.add_human_review('Education Expert\\nPedagogy Check')
    qa3 = diagram.add_decision('Approved?')
    qa4 = diagram.add_feedback('Revision Feedback')
    
    diagram.end_swimlane()
    
    # ===== SWIMLANE 5: DEPLOYMENT =====
    diagram.create_swimlane('Deployment', '#FFFDE7')
    
    deploy1 = diagram.add_process('Generate Patient\\nStandardized Script')
    deploy2 = diagram.add_process('Create Examiner\\nChecklist')
    deploy3 = diagram.add_document('Complete OSCE Station')
    deploy4 = diagram.add_database('Add to Case Library')
    end = diagram.add_end('Case Ready\\nfor Use')
    
    diagram.end_swimlane()
    
    # ===== CONNECTIONS =====
    
    # Initial flow
    diagram.connect(start, c1)
    diagram.connect(c1, c2)
    diagram.connect(c2, lib1, label='Check Library')
    diagram.connect(lib1, lib2)
    
    # Library check
    diagram.connect_yes(lib2, lib3)
    diagram.connect_no(lib2, agent1, label='Generate New')
    diagram.connect(lib3, agent4, label='Customize')
    
    # Agent cascade
    diagram.connect(agent1, agent2, emphasis=True)
    diagram.connect(agent2, val1)
    
    # Validation loops
    diagram.connect_yes(val1, agent3)
    diagram.connect_no(val1, agent1, label='Regenerate')
    
    diagram.connect(agent3, val2)
    diagram.connect_yes(val2, agent4)
    diagram.connect_no(val2, agent3, label='Refine Rubric')
    
    # Difficulty calibration
    diagram.connect(agent4, qa1, label='Ready for Review')
    
    # Faculty review
    diagram.connect(qa1, qa2)
    diagram.connect(qa2, qa3)
    
    # Approval paths
    diagram.connect_yes(qa3, deploy1)
    diagram.connect_no(qa3, qa4)
    diagram.connect_feedback_loop(qa4, agent1, 'Revise')
    
    # Deployment
    diagram.connect(deploy1, deploy2)
    diagram.connect(deploy2, deploy3)
    diagram.connect(deploy3, deploy4)
    diagram.connect(deploy4, end)
    
    # Save outputs
    diagram.save()
    diagram.convert_to_drawio()
    
    return diagram


if __name__ == '__main__':
    create_osce_case_generation_workflow()
    print('\\n✅ OSCE agentic case generation workflow created!')
```

---

## Example 3: Assessment Question Generation (Q1-Q40)

```python
"""
Example 3: Automated Assessment Question Generation
Generate 40 assessment questions with varying difficulty
"""

def create_assessment_generation_workflow():
    """Generate assessment question batch generation workflow"""
    
    diagram = EducationalWorkflowDiagram(
        title='Automated Assessment Generation (Q1-Q40)',
        filename='assessment_generation_batch',
        direction='LR'  # Left to right for pipeline view
    )
    
    # Start
    start = diagram.add_start('Batch Request\\n(40 Questions)')
    
    # Input specification
    spec = diagram.add_manual('Specify:\\n- Topic area\\n- Difficulty distribution\\n- Question types')
    
    # Question bank check
    bank = diagram.add_database('Question Bank\\n(10K+ items)')
    check = diagram.add_decision('Sufficient\\nQuestions\\nAvailable?')
    
    # Generation pipeline
    gen1 = diagram.add_llm_process('Generate Q1-Q10\\n(Easy)', 'Claude Sonnet 4')
    gen2 = diagram.add_llm_process('Generate Q11-Q30\\n(Medium)', 'Claude Sonnet 4')
    gen3 = diagram.add_llm_process('Generate Q31-Q40\\n(Hard)', 'Claude Sonnet 4')
    
    # Parallel validation
    val1 = diagram.add_validation('Bloom\\'s Taxonomy\\nAlignment?')
    val2 = diagram.add_validation('Clinical Accuracy?')
    val3 = diagram.add_validation('No Duplicates?')
    
    # Compilation
    compile = diagram.add_process('Compile\\nQuestion Set')
    
    # Review
    review = diagram.add_human_review('Faculty Review\\n(Sample 10%)')
    approve = diagram.add_decision('Approved?')
    
    # Output
    export = diagram.add_document('Export to\\nGoogle Forms\\n(Q1-Q40)')
    store = diagram.add_database('Store in\\nQuestion Bank')
    end = diagram.add_end('Assessment\\nReady')
    
    # Error handling
    error = diagram.add_error_handler('Regenerate\\nFailed Items')
    
    # ===== CONNECTIONS =====
    
    diagram.connect(start, spec)
    diagram.connect(spec, bank)
    diagram.connect(bank, check)
    
    # Check paths
    diagram.connect_yes(check, compile, label='Use Existing')
    diagram.connect_no(check, gen1, label='Generate New')
    
    # Generation pipeline
    diagram.connect(gen1, gen2)
    diagram.connect(gen2, gen3)
    
    # Validation cascade
    diagram.connect(gen3, val1, emphasis=True)
    diagram.connect(val1, val2)
    diagram.connect(val2, val3)
    
    # Validation failures loop back
    diagram.connect_no(val1, error)
    diagram.connect_no(val2, error)
    diagram.connect_no(val3, error)
    diagram.connect_feedback_loop(error, gen1, 'Retry')
    
    # Success path
    diagram.connect_yes(val3, compile)
    
    # Review process
    diagram.connect(compile, review)
    diagram.connect(review, approve)
    
    # Approval paths
    diagram.connect_yes(approve, export)
    diagram.connect_no(approve, error, label='Revise')
    
    # Final output
    diagram.connect(export, store)
    diagram.connect(store, end)
    
    # Save
    diagram.save()
    diagram.convert_to_drawio()
    
    return diagram


if __name__ == '__main__':
    create_assessment_generation_workflow()
    print('\\n✅ Assessment generation workflow created!')
```

---

## Shape Usage Guidelines

### When to Use Each Shape

| Shape | Use For | Example |
|-------|---------|---------|
| **Ellipse** | Start/End points | "Start", "End", "Complete" |
| **Rectangle** | Process steps | "Generate case", "Score response" |
| **Diamond** | Decisions/Branching | "Score >= 70%?", "Approved?" |
| **Parallelogram** | Data/Input/Output | "Student response", "Assessment scores" |
| **Cylinder** | Databases/Storage | "Case library", "Student records" |
| **Note** | Documents/Reports | "Feedback report", "Rubric" |
| **Hexagon** | Preparation | "Prepare prompt", "Setup environment" |
| **Trapezoid** | Manual input | "Faculty review", "Manual grading" |
| **Double-border Box** | Subprocess | "Multi-step validation" |

---

## Color Scheme for Educational Workflows

```python
# Standard color palette
EDUCATION_COLORS = {
    # Participants
    'student': '#E3F2FD',          # Light blue
    'instructor': '#F3E5F5',       # Light purple  
    'llm_agent': '#FFF3E0',        # Light orange
    'qa_team': '#E8F5E9',          # Light green
    'system': '#E0F2F1',           # Light teal
    
    # Process types
    'generation': '#FFF9C4',       # Light yellow (creative)
    'validation': '#C8E6C9',       # Green (checking)
    'feedback': '#FFECB3',         # Amber (communication)
    'storage': '#B3E5FC',          # Cyan (data)
    
    # Status indicators
    'success': '#C8E6C9',          # Green
    'warning': '#FFF9C4',          # Yellow
    'error': '#FFCDD2',            # Red
    'in_progress': '#B3E5FC',      # Blue
}
```

---

## Complete Workflow Examples

### 1. **LLM-as-a-Judge**: Automated scoring with human oversight
### 2. **OSCE Generation**: Multi-agent case creation pipeline
### 3. **Batch Assessment**: Generate 40 questions with quality control
### 4. **Feedback Loop**: Iterative improvement with student data
### 5. **Multi-Modal Assessment**: Audio, text, and video evaluation

---

## Output File Structure

```
diagrams/
├── llm_judge_workflow.png          # PNG for presentations
├── llm_judge_workflow.svg          # SVG for web/scaling
├── llm_judge_workflow.dot          # GraphViz source (version control)
├── llm_judge_workflow.drawio       # Editable in Draw.io
├── osce_case_generation.png
├── osce_case_generation.svg
├── osce_case_generation.dot
├── osce_case_generation.drawio
└── assessment_generation_batch.png
```

---

## Best Practices

### 1. Keep It Simple
- Use standard shapes only
- Limit colors to 5-6 per diagram
- Clear, concise labels
- Avoid clutter

### 2. Tell a Story
- Left-to-right or top-to-bottom flow
- Group related activities in swimlanes
- Show decision points clearly
- Highlight critical paths

### 3. Educational Focus
- Always show student perspective
- Mark quality checkpoints
- Show feedback loops
- Document time estimates

### 4. Maintainability
- Save .dot files for version control
- Use consistent naming
- Comment your code
- Generate .drawio for easy editing

---

## Running the Examples

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows

# Install dependencies
pip install graphviz graphviz2drawio

# Run examples
python llm_judge_workflow.py
python osce_case_generation.py
python assessment_generation.py

# View outputs
open diagrams/llm_judge_workflow.png
```

---

## Key Differences from Technical Architecture Diagrams

| ❌ Technical Architecture | ✅ Educational Workflow |
|---------------------------|-------------------------|
| Servers, APIs, databases | People, processes, activities |
| Network topology | Process flow |
| System integration | Human collaboration |
| Data pipelines | Learning pathways |
| Performance metrics | Educational outcomes |
| Cloud infrastructure | Educational infrastructure |
| Microservices | Learning activities |

---

## Summary

This agent creates **simple, clear educational workflow diagrams** using standard flowchart symbols:
- ✅ Rectangles, diamonds, circles, documents
- ✅ Clean swimlane layouts
- ✅ Focus on people and processes (not servers and APIs)
- ✅ Export to PNG, SVG, and editable Draw.io format
- ✅ Perfect for presentations, documentation, and collaboration

**Use this for**: LLM-as-a-Judge evaluation, OSCE case generation, assessment automation, and any educational workflow visualization.

---

*This agent follows educational best practices and standard flowchart conventions.*

# Healthcare Agent Instructions: Clinical Workflow & Swim Lane Diagram Generation

## Overview
This workspace contains tools to generate healthcare workflow and swim lane diagrams following Institute for Healthcare Improvement (IHI) quality improvement methodology. The diagrams visualize clinical processes, patient journeys, and care coordination using Python's `diagrams` library, rendered with GraphViz, and converted to editable draw.io format.

**Focus**: Healthcare workflows, not technical system architectures
**Methodology**: IHI Model for Improvement, PDSA cycles, process mapping
**Output**: Swim lane diagrams showing people, roles, handoffs, and clinical processes

---

## Healthcare Workflow Principles

### IHI Quality Improvement Framework
1. **Aim**: What are we trying to accomplish?
2. **Measures**: How will we know that a change is an improvement?
3. **Changes**: What changes can we make that will result in improvement?

### Process Mapping Goals
- Identify waste and inefficiencies
- Highlight handoff points (high-risk areas)
- Show patient flow through the system
- Document current state vs. desired state
- Support root cause analysis
- Enable standardization

---

## Environment Setup

### Python Environment
- **Python Version**: 3.8+ required
- **Virtual Environment**: Recommended for isolation
- **Activation**: 
  - macOS/Linux: `source venv/bin/activate`
  - Windows: `.\venv\Scripts\Activate.ps1`

### Required Packages
```bash
pip install diagrams==0.24.4
pip install graphviz==0.20.3
pip install graphviz2drawio==1.1.0
```

### GraphViz Installation
- **macOS**: `brew install graphviz`
- **Linux**: `sudo apt-get install graphviz`
- **Windows**: Download from https://graphviz.org/download/

### VS Code Extensions
- **Draw.io**: `hediet.vscode-drawio` - For editing workflow diagrams
- Useful for post-generation refinement

---

## Healthcare Diagram Types

### 1. Swim Lane Diagrams
**Purpose**: Show process flow across multiple participants/departments
**Use Cases**:
- Patient admission workflows
- Medication reconciliation processes
- Discharge planning
- Handoff protocols
- Care coordination

**Key Elements**:
- Horizontal or vertical lanes for each participant
- Sequential steps within each lane
- Handoff points between lanes
- Decision points
- Wait times/delays

### 2. Patient Journey Maps
**Purpose**: Visualize patient experience through care continuum
**Use Cases**:
- ED to admission journey
- Surgical pathway
- Chronic disease management
- Outpatient visit flow

### 3. Value Stream Maps
**Purpose**: Identify value-added vs. non-value-added activities
**Use Cases**:
- Reducing wait times
- Eliminating waste
- Improving throughput
- Capacity planning

### 4. SIPOC Diagrams
**Purpose**: Suppliers, Inputs, Process, Outputs, Customers
**Use Cases**:
- High-level process overview
- Scope definition
- Stakeholder identification

---

## Swim Lane Diagram Structure

### Standard Layout
```python
graph_attr = {
    "splines": "ortho",      # Orthogonal lines for clarity
    "nodesep": "1.0",        # Space between nodes
    "ranksep": "1.5",        # Space between ranks (steps)
    "fontsize": "14",        # Readable text
    "bgcolor": "white",      # Clean background
    "pad": "0.5",
    "rankdir": "TB"          # Top to Bottom (or "LR" for Left to Right)
}
```

### Participant Types (Swim Lanes)

#### Clinical Roles
```python
from diagrams.onprem.client import Users, Client

# Patient
patient = Users("Patient")

# Clinical Staff
nurse = Client("Nurse")
doctor = Client("Physician")
pharmacist = Client("Pharmacist")
therapist = Client("Therapist")
social_worker = Client("Social Worker")
case_manager = Client("Case Manager")
```

#### Support Roles
```python
# Administrative
registration = Client("Registration")
scheduler = Client("Scheduler")
billing = Client("Billing")

# Ancillary Services
lab = Client("Laboratory")
radiology = Client("Radiology")
transport = Client("Transport")
```

#### Systems
```python
from diagrams.generic.database import SQL
from diagrams.generic.storage import Storage

# Information Systems
ehr = SQL("EHR System")
pacs = SQL("PACS")
lis = SQL("Lab System")
pharmacy_system = SQL("Pharmacy System")

# Documents
medical_record = Storage("Medical Record")
orders = Storage("Orders")
results = Storage("Results")
```

---

## Color Coding for Healthcare Workflows

### Participant-Based Colors
```python
# Patient - Light Blue (focus of care)
patient_color = "#E3F2FD"

# Nursing - Light Purple
nursing_color = "#F3E5F5"

# Physicians - Light Green
physician_color = "#E8F5E9"

# Pharmacy - Light Orange
pharmacy_color = "#FFF3E0"

# Ancillary Services - Light Pink
ancillary_color = "#FCE4EC"

# Administration - Light Yellow
admin_color = "#FFFDE7"

# Systems/Technology - Light Teal
system_color = "#E0F2F1"

# Quality/Safety - Light Red
safety_color = "#FFEBEE"
```

### Apply to Swim Lanes
```python
with Cluster("Patient", graph_attr={"bgcolor": patient_color, "style": "rounded"}):
    step1 = Users("Arrives at clinic")
    step2 = Users("Waits in lobby")
    step3 = Users("Called to exam room")
```

---

## Healthcare-Specific Icons and Representations

### People and Roles
```python
from diagrams.onprem.client import Users, Client

# Use Users for patients
patient = Users("Patient\nJohn Doe")

# Use Client for staff
nurse = Client("RN\nJane Smith")
doctor = Client("MD\nDr. Johnson")
```

### Documents and Forms
```python
from diagrams.generic.storage import Storage

consent_form = Storage("Informed Consent")
medication_list = Storage("Medication List")
care_plan = Storage("Care Plan")
discharge_summary = Storage("Discharge Summary")
```

### Clinical Systems
```python
from diagrams.generic.database import SQL

ehr = SQL("Electronic\nHealth Record")
cpoe = SQL("CPOE\nOrder Entry")
emar = SQL("eMAR\nMed Admin")
```

### Decision Points
```python
from diagrams.generic.blank import Blank

decision = Blank("Decision:\nAdmit or\nDischarge?")
```

---

## Workflow Step Labeling

### Use Numbered Steps
```python
# Clear sequential numbering
step1 = Client("1. Triage\n(5 min)")
step2 = Client("2. Registration\n(10 min)")
step3 = Client("3. Assessment\n(15 min)")
```

### Include Time Estimates
```python
# Value-added time
assessment = Client("Physical Exam\n(20 min)\n[Value-Added]")

# Non-value-added time (waste)
waiting = Client("Wait for Results\n(60 min)\n[Waste]")
```

### Show Handoffs Clearly
```python
# Use distinct edge labels for handoffs
nurse >> Edge(label="HANDOFF:\nSBAR Report", color="red", style="bold") >> next_nurse
```

---

## Common Healthcare Workflows

### 1. Patient Admission (ED to Floor)
**Participants**:
- Patient
- ED Nurse
- ED Physician
- Hospitalist
- Floor Nurse
- Pharmacist
- EHR System

**Key Phases**:
1. Triage and Assessment
2. Diagnosis and Treatment
3. Admission Decision
4. Order Entry
5. Bed Assignment
6. Transport
7. Floor Admission

### 2. Medication Reconciliation
**Participants**:
- Patient
- Admitting Nurse
- Pharmacist
- Physician
- EHR System

**Key Steps**:
1. Obtain medication history
2. Document in EHR
3. Pharmacist review
4. Physician verification
5. Patient education

### 3. Surgical Pathway
**Participants**:
- Patient
- Surgeon
- Anesthesiologist
- OR Nurse
- PACU Nurse
- Floor Nurse

**Key Phases**:
1. Pre-operative assessment
2. Surgical consent
3. Pre-op preparation
4. Intra-operative care
5. Post-operative recovery
6. Floor transfer

### 4. Discharge Process
**Participants**:
- Patient
- Physician
- Nurse
- Pharmacist
- Case Manager
- Scheduler

**Key Steps**:
1. Discharge order
2. Medication reconciliation
3. Patient education
4. Follow-up scheduling
5. Transportation arrangement
6. Discharge summary

---

## Quality and Safety Elements

### Highlight Safety Checkpoints
```python
# Use distinct color for safety checks
safety_check = Client("SAFETY CHECK:\nTwo Patient\nIdentifiers")

# Connect with bold red edges
previous_step >> Edge(label="VERIFY", color="red", style="bold") >> safety_check
```

### Show Error-Prone Steps
```python
# Highlight high-risk areas
high_risk = Client("⚠️ HIGH RISK:\nMedication\nAdministration")
```

### Document Barriers/Controls
```python
# Show safety barriers
barrier = Storage("BARRIER:\nBarcode\nScanning")
```

---

## Handoff Communication

### SBAR Format
```python
# Situation, Background, Assessment, Recommendation
handoff = Client("HANDOFF (SBAR):\nS: Patient condition\nB: Medical history\nA: Current status\nR: Plan of care")
```

### Critical Information Transfer
```python
# Use bold edges for critical handoffs
ed_nurse >> Edge(label="CRITICAL HANDOFF:\nPatient Report", 
                 color="red", 
                 style="bold") >> floor_nurse
```

---

## Time and Efficiency Metrics

### Show Wait Times
```python
# Non-value-added time
wait = Client("⏱️ WAIT:\n45 minutes\n[Non-Value-Added]")
```

### Value Stream Mapping
```python
# Value-added vs. non-value-added
va_time = Client("Assessment\n15 min\n✓ Value-Added")
nva_time = Client("Waiting\n60 min\n✗ Waste")
```

### Cycle Time
```python
# Total process time
total = Client("TOTAL TIME:\n4-8 hours\n(Target: <4 hours)")
```

---

## Example: Creating a Swim Lane Diagram

```python
"""
Example: Medication Administration Workflow
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users, Client
from diagrams.generic.storage import Storage
from diagrams.generic.database import SQL

graph_attr = {
    "splines": "ortho",
    "nodesep": "1.0",
    "ranksep": "1.5",
    "fontsize": "14",
    "bgcolor": "white",
    "rankdir": "TB"
}

with Diagram("Medication Administration - 5 Rights",
             filename="diagrams/med_admin_workflow",
             outformat=["png", "dot"],
             show=False,
             graph_attr=graph_attr):

    # SWIM LANE 1: NURSE
    with Cluster("Nurse", graph_attr={"bgcolor": "#F3E5F5"}):
        n1 = Client("1. Receive\nMed Order")
        n2 = Client("2. Verify Order\nin eMAR")
        n3 = Client("3. Retrieve\nMedication")
        n4 = Client("4. Scan Barcode\n(Med + Patient)")
        n5 = Client("5. Administer\nMedication")
        n6 = Client("6. Document\nin eMAR")

    # SWIM LANE 2: PATIENT
    with Cluster("Patient", graph_attr={"bgcolor": "#E3F2FD"}):
        p1 = Users("Wears ID\nBracelet")
        p2 = Users("Receives\nMedication")
        p3 = Users("Monitored for\nReaction")

    # SWIM LANE 3: eMAR SYSTEM
    with Cluster("eMAR System", graph_attr={"bgcolor": "#E0F2F1"}):
        s1 = SQL("New Order\nAlert")
        s2 = SQL("Verify:\n5 Rights")
        s3 = SQL("Document\nAdministration")

    # WORKFLOW CONNECTIONS
    s1 >> Edge(label="Alert") >> n1
    n1 >> Edge(label="Check") >> n2
    n2 >> Edge(label="Verify") >> s2
    s2 >> Edge(label="Approved") >> n3
    n3 >> Edge(label="Scan") >> n4
    n4 >> Edge(label="Verify ID") >> p1
    n4 >> Edge(label="Administer") >> n5
    n5 >> Edge(label="Give") >> p2
    n5 >> Edge(label="Document") >> n6
    n6 >> Edge(label="Record") >> s3
    p2 >> Edge(label="Monitor") >> p3
```

---

## IHI-Specific Considerations

### Model for Improvement
Include in diagram documentation:
1. **Aim Statement**: What are we trying to accomplish?
2. **Measures**: How will we know a change is an improvement?
3. **Changes**: What changes can we make?

### PDSA Cycles
Document in README:
- **Plan**: What is the change?
- **Do**: Test the change
- **Study**: Analyze results
- **Act**: Implement or modify

### Failure Modes
Identify in workflow:
- Where can errors occur?
- What are the consequences?
- What barriers exist?

---

## Best Practices for Healthcare Workflows

### 1. Patient-Centered
- Always include patient perspective
- Show patient wait times
- Highlight patient touchpoints
- Document patient education moments

### 2. Safety-Focused
- Mark high-risk steps
- Show verification points
- Document safety barriers
- Highlight handoffs (highest risk)

### 3. Efficiency-Oriented
- Show value-added vs. non-value-added time
- Identify bottlenecks
- Document parallel processes
- Measure cycle time

### 4. Evidence-Based
- Reference clinical guidelines
- Show decision support points
- Document evidence-based protocols

### 5. Regulatory Compliant
- Include required documentation
- Show consent processes
- Document privacy protections
- Mark regulatory checkpoints

---

## Common Healthcare Workflow Patterns

### Sequential Process
```
Patient → Triage → Assessment → Treatment → Discharge
```

### Parallel Processing
```
Patient Assessment
    ├─→ Lab Tests
    ├─→ Imaging
    └─→ Medication History
    ↓
All Results → Diagnosis
```

### Decision Tree
```
Assessment → Decision Point
    ├─→ Admit (if criteria met)
    └─→ Discharge (if stable)
```

### Feedback Loop
```
Treatment → Monitor → Assess Response
    ├─→ Continue (if improving)
    └─→ Adjust (if not improving) → Treatment
```

---

## Output Files

Each workflow diagram generates:
1. **PNG** - For presentations and documentation
2. **DOT** - GraphViz source (version control friendly)
3. **DRAWIO** - Editable for refinement

**Naming Convention**: `{process}_{workflow_type}.{ext}`
- Example: `admission_swimlane.png`
- Example: `medication_reconciliation_workflow.dot`

---

## Documentation Requirements

### Each Workflow Should Include:

#### README.md
- **Purpose**: What process is being mapped?
- **Scope**: What is included/excluded?
- **Participants**: Who is involved?
- **Steps**: Detailed step descriptions
- **Metrics**: Time, volume, quality measures
- **Pain Points**: Known issues
- **Improvement Opportunities**: What could be better?

#### Workflow Diagram
- Clear swim lanes
- Numbered steps
- Time estimates
- Handoff points marked
- Safety checkpoints highlighted
- Decision points shown

#### Supporting Documentation
- Current state vs. future state
- Root cause analysis (if applicable)
- PDSA cycle documentation
- Measurement plan

---

## Quality Improvement Metrics

### Process Metrics
- Cycle time (total time)
- Touch time (value-added time)
- Wait time (non-value-added time)
- Handoff count
- Decision points

### Outcome Metrics
- Patient satisfaction
- Safety events
- Error rates
- Readmission rates
- Length of stay

### Balancing Metrics
- Staff satisfaction
- Cost per case
- Resource utilization
- Throughput

---

## Troubleshooting

### Diagram Too Complex
**Solution**: 
- Break into sub-processes
- Use high-level overview + detailed views
- Focus on critical path

### Too Many Participants
**Solution**:
- Group similar roles
- Use "Other" category for infrequent participants
- Create role-specific views

### Unclear Handoffs
**Solution**:
- Use bold/colored edges
- Add SBAR labels
- Create handoff detail boxes

---

## Example Workflows to Create

### High Priority
1. ✅ Patient Admission (ED to Floor)
2. Medication Reconciliation
3. Surgical Safety Checklist
4. Discharge Planning
5. Rapid Response Team Activation

### Medium Priority
6. Outpatient Visit Flow
7. Lab Result Follow-up
8. Infection Control Protocol
9. Fall Prevention Process
10. Pain Management Pathway

### Specialized
11. Stroke Protocol (Time-Critical)
12. Sepsis Bundle Implementation
13. Code Blue Response
14. Trauma Activation
15. Obstetric Emergency

---

## Key Differences from Technical Diagrams

| Technical Diagrams | Healthcare Workflows |
|-------------------|---------------------|
| Servers, databases | People, roles |
| Data flow | Patient flow |
| System integration | Care coordination |
| Network topology | Process sequence |
| API calls | Handoffs |
| Error handling | Safety checks |
| Performance metrics | Quality metrics |
| Uptime | Patient outcomes |

---

## Resources

### IHI Resources
- IHI Open School
- Model for Improvement
- PDSA Worksheet
- Failure Modes and Effects Analysis (FMEA)

### Process Mapping Tools
- Value Stream Mapping
- Spaghetti Diagrams
- Swim Lane Diagrams
- SIPOC Diagrams

### Healthcare Quality
- The Joint Commission Standards
- CMS Quality Measures
- AHRQ Patient Safety Indicators
- Lean Healthcare Principles

---

## Continuous Improvement

### After Creating Workflow
1. **Validate** with frontline staff
2. **Test** with actual process observation
3. **Refine** based on feedback
4. **Measure** baseline performance
5. **Implement** improvements
6. **Re-measure** to confirm improvement
7. **Standardize** successful changes
8. **Sustain** through monitoring

---

## Summary

Healthcare workflow diagrams are fundamentally different from technical system diagrams:
- **Focus on people**, not technology
- **Show patient journey**, not data flow
- **Highlight handoffs**, not API calls
- **Measure quality**, not uptime
- **Improve care**, not performance

Use this guide to create clear, actionable workflow diagrams that support quality improvement initiatives and enhance patient safety.

---

*This guide follows IHI Model for Improvement methodology and healthcare quality improvement best practices.*

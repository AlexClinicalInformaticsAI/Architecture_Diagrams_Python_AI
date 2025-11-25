# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains two distinct diagram generation capabilities:

### 1. Azure Architecture Diagrams
Generates technical architecture diagrams from Infrastructure-as-Code (IaC) templates using Python and the `diagrams` library. Creates automated diagrams for Azure resources defined in Terraform and Bicep templates, producing output in PNG, DOT (GraphViz), and Draw.io formats.

**Use for**: Cloud infrastructure, technical architectures, IaC visualization, Azure resource topologies.

### 2. Healthcare/Educational Workflow Diagrams
Generates educational workflow diagrams for medical education systems using **standard flowchart symbols** (rectangles, diamonds, circles). Focuses on LLM-as-a-Judge evaluation workflows, OSCE case generation, and assessment automation processes.

**Use for**: Educational processes, clinical workflows, assessment pipelines, LLM evaluation workflows, process documentation.

**See**: `Arch_Diagrams/healthcareagent.md` for complete healthcare workflow instructions.

---

## Repository Documentation Structure

This repository contains multiple instruction files for different purposes:

- **`CLAUDE.md`** (this file) - Overview and quick reference for both diagram types
- **`Arch_Diagrams/agent.md`** - Detailed Azure architecture diagram instructions (Windows-focused)
- **`Arch_Diagrams/healthcareagent.md`** - Complete healthcare/educational workflow diagram guide
- **`Arch_Diagrams/instructions.md`** - Original architecture requirements reference

When working with this repository:
- Use **agent.md** for detailed Azure architecture setup, especially on Windows
- Use **healthcareagent.md** for educational workflow diagrams, LLM-as-a-Judge, OSCE workflows
- Use **this file (CLAUDE.md)** for quick command reference and overview

---

## Prerequisites and Setup

### System Dependencies

1. **GraphViz** must be installed on the system:
   - macOS: `brew install graphviz`
   - Linux: `sudo apt-get install graphviz` or equivalent
   - Windows: Download from https://graphviz.org/download/ and install to `C:\Program Files\Graphviz`
   - The Python `graphviz` library requires this to be available in PATH

2. **graphviz2drawio** for Draw.io conversion (required for .drawio output):
   - macOS: `brew install graphviz2drawio`
   - Python 3.10+ required (installed automatically via Homebrew)
   - Without this tool, only .png and .dot files will be generated

3. **Python Dependencies** (install from `Arch_Diagrams/requirements.txt`):
   ```bash
   cd Arch_Diagrams
   pip install -r requirements.txt
   ```

   Key packages:
   - `diagrams==0.24.4` - Core diagram generation library
   - `graphviz==0.20.3` - Python wrapper for GraphViz

   Note: `pygraphviz` and `graphviz2drawio` Python packages are NOT required in the venv as we use the Homebrew-installed `graphviz2drawio` binary which includes its own Python 3.14 environment.

## Common Commands

### Generate Azure Architecture Diagrams

From the `Arch_Diagrams` directory:

```bash
# Generate Contoso Medical Portal architecture diagram (complex multi-tier Azure PaaS)
python contoso_architecture.py

# Generate IIS + SQL Server 3-tier diagram (traditional Azure IaaS from Bicep demo)
python bicep_iis_sql_diagram.py

# Generate GamELY LLM Evaluation Framework architecture (Python package workflow)
# Note: GamELY files are organized in diagrams/EVAL/Gamely/
python diagrams/EVAL/Gamely/gamely_architecture.py
```

### Generate Healthcare/Educational Workflow Diagrams

From the `Arch_Diagrams` directory:

```bash
# Generate LLM-as-a-Judge evaluation workflow
python -c "from healthcareagent import create_llm_judge_workflow; create_llm_judge_workflow()"

# Generate OSCE case generation workflow
python -c "from healthcareagent import create_osce_case_generation_workflow; create_osce_case_generation_workflow()"

# Generate assessment question batch workflow
python -c "from healthcareagent import create_assessment_generation_workflow; create_assessment_generation_workflow()"
```

### Output Files

All diagrams are generated in `Arch_Diagrams/diagrams/` with three formats:
- `.png` - Visual diagram (for presentations, documentation)
- `.dot` - GraphViz source file (version-controllable text format)
- `.drawio` - Draw.io editable format (if graphviz2drawio is installed)
- `.svg` - Scalable Vector Graphics (for healthcare workflows)

### Infrastructure as Code Examples

The repository includes reference IaC templates that can be used as sources for diagram generation:

**Terraform Example** (`terraform-demo/main.tf`):
```bash
cd terraform-demo
terraform init
terraform plan
terraform apply  # Deploys to Azure
```

**Bicep Example** (`bicep-demo/demos/iis-2vm-sql-1vm/main.bicep`):
```bash
cd bicep-demo/demos/iis-2vm-sql-1vm
az deployment group create --resource-group <rg-name> --template-file main.bicep
```

## Code Architecture

### Diagram Generation Pattern

All Python diagram generators follow a consistent structure:

1. **Import Azure components** from `diagrams.azure.*` submodules:
   - `diagrams.azure.compute` - VMs, App Services, Function Apps
   - `diagrams.azure.network` - VNets, Load Balancers, NSGs, Firewalls
   - `diagrams.azure.database` - SQL Servers, SQL Databases
   - `diagrams.azure.storage` - Storage Accounts
   - `diagrams.azure.security` - Key Vaults

2. **Define graph and cluster attributes** for visual styling:
   - `graph_attr` - Overall diagram layout (splines, spacing, background)
   - `*_cluster_attr` - Styling for logical groupings (VNets, subnets, tiers)

3. **Create diagram context** using `with Diagram()`:
   - `filename` - Output path without extension
   - `outformat` - List of formats: `["png", "dot"]`
   - `show=False` - Don't auto-open in viewer
   - `direction` - Layout direction: `"TB"` (top-bottom) or `"LR"` (left-right)

4. **Build resource hierarchy** using nested `with Cluster()` blocks:
   - Outer cluster represents VNet
   - Inner clusters represent subnets or logical tiers
   - Resources instantiated within appropriate clusters

5. **Define connections** using `>>` operator with `Edge()` objects:
   - `label` - Connection description
   - `style` - Line style: "solid", "dotted", "dashed"
   - `color` - Connection color for visual grouping

6. **Post-process DOT to Draw.io** using `graphviz2drawio` subprocess:
   - Requires `graphviz2drawio` to be installed via Homebrew (`brew install graphviz2drawio`)
   - The subprocess calls the system `graphviz2drawio` command, NOT the Python package
   - If the command is not found, the script will skip .drawio generation but still create .png and .dot files

### Example Architecture Patterns

**Contoso Medical Portal** (`contoso_architecture.py`):
- Complex multi-tier application architecture
- Azure Front Door → Application Gateway → Web App → Backend API → SQL Database
- Includes monitoring (Log Analytics, App Insights), security (Key Vault, Firewall), and message queuing (Service Bus)
- Demonstrates VNet integration with subnet-level NSG protection

**IIS + SQL 3-Tier** (`bicep_iis_sql_diagram.py`):
- Traditional IaaS architecture with load-balanced VMs
- Load Balancer → Availability Set (2 IIS VMs) → SQL Server VM
- Demonstrates availability sets, managed disks, and NSG rules
- Maps directly to Bicep template at `bicep-demo/demos/iis-2vm-sql-1vm/main.bicep`

**GamELY LLM Evaluation Framework** (`diagrams/EVAL/Gamely/gamely_architecture.py`):
- Python package architecture for evaluating LLM outputs using LLMs as judges
- Workflow: Input DataFrame → Provider Mapper → API Validation → Batch Evaluation → Scored Output
- Supports 3 LLM providers: OpenAI (GPT-3.5/4/4o/o1), Anthropic (Claude 2/3), DeepSeek (Chat/Reasoner)
- 17 built-in evaluation criteria: accuracy, comprehension, reasoning, bias, toxicity, hallucination, etc.
- Demonstrates software architecture patterns: provider abstraction, batch processing, API integration
- Scoring: 1-5 Likert scale (strongly disagree → strongly agree) + NaN for irrelevant criteria

## IaC Template Structure

### Terraform Template (`terraform-demo/main.tf`)

Creates basic Azure infrastructure:
- Resource group, VNet (10.10.0.0/16) with app and db subnets
- NSGs with HTTP and SQL rules
- Linux VM (Ubuntu 22.04) with public IP
- Storage account, Key Vault
- App Service Plan + Web App (Python 3.11)
- SQL Server + Database
- Log Analytics Workspace + Application Insights

**Key variables**:
- `project_name`: "sc-demo-arch" (prefix for all resources)
- `location`: "australiaeast"

**Important**: SSH public key must be replaced in admin_ssh_key, and tenant/object IDs must be set for Key Vault access policy.

### Bicep Template (`bicep-demo/demos/iis-2vm-sql-1vm/main.bicep`)

Resource-group scoped deployment with parameters:
- `envPrefixName` (default: "cust1") - Resource naming prefix
- `username`, `password` - VM admin credentials
- `numberOfWebSrvs` - Web server count (1 or 2)
- `webSrvVMSize`, `sqlVMSize` - VM SKUs
- `diskType` - Managed disk tier

**Architecture**:
- VNet: 10.0.0.0/16
  - Frontend subnet: 10.0.0.0/24 (NSG allows HTTP/80)
  - Database subnet: 10.0.2.0/24 (NSG allows SQL/1433 from frontend, blocks internet)
- Load balancer with public IP and DNS label
- Availability set (2 fault/20 update domains)
- Web VMs: Windows Server 2022 with IIS (via Guest Configuration)
- SQL VM: SQL Server 2022 Standard

**Guest Configuration**: Uses `Microsoft.GuestConfiguration` to install IIS via DSC (`WebServerConfig.zip` artifact referenced from `_artifactsLocation`).

## Creating New Diagram Generators

When creating a new Python diagram generator for Azure architectures:

1. Use `instructions.md` as a reference for architecture requirements
2. Import necessary Azure component types from `diagrams.azure.*`
3. Define cluster attributes for each logical tier with distinct background colors
4. Use meaningful resource naming that matches Azure naming conventions
5. Add connection labels to describe traffic flow or purpose
6. Include a subprocess call to `graphviz2drawio` with error handling
7. Print summary information about generated files

**Naming Conventions**:
- Files: `{architecture_name}_diagram.py`
- Output: `diagrams/{architecture_name}.*`
- Resources: Follow Azure naming patterns (e.g., `vnet-*`, `app-*`, `sqlsrv-*`)

---

## Healthcare/Educational Workflow Diagrams

This repository also supports generating **educational workflow diagrams** for medical education, assessment automation, and LLM evaluation systems. These diagrams use **simple flowchart symbols** (NOT technical architecture icons).

**Complete Documentation**: See `Arch_Diagrams/healthcareagent.md` for full details.

### Key Differences from Azure Architecture Diagrams

| Azure Architecture | Healthcare Workflow |
|-------------------|---------------------|
| Technical infrastructure | People and processes |
| Cloud resources, APIs, servers | Students, instructors, LLM judges |
| Network topology | Process flow |
| Azure-specific icons | Standard flowchart shapes |
| IaC template source | Manual workflow definition |

### Standard Flowchart Symbols

Healthcare workflow diagrams use standard shapes:
- **Rectangle** - Process/Activity
- **Diamond** - Decision Point
- **Circle/Oval** - Start/End
- **Parallelogram** - Document/Input/Output
- **Cylinder** - Database/Storage
- **Hexagon** - Preparation/Setup
- **Trapezoid** - Manual Input
- **Rounded Rectangle** - Subprocess

**DO NOT use**: Azure/AWS icons, technical architecture symbols, cloud/network icons.

### Use Cases

1. **LLM-as-a-Judge Workflows**: Automated assessment with AI evaluation
2. **OSCE Case Generation**: Multi-agent clinical case creation pipelines
3. **Assessment Automation**: Question generation and validation
4. **Educational Pipelines**: Student assessment processes, feedback loops
5. **Quality Assurance**: Faculty review and validation processes

### Example Healthcare Workflow Commands

```bash
cd Arch_Diagrams

# Generate LLM-as-a-Judge evaluation workflow
python -c "from healthcareagent import create_llm_judge_workflow; create_llm_judge_workflow()"

# Generate OSCE case generation workflow
python -c "from healthcareagent import create_osce_case_generation_workflow; create_osce_case_generation_workflow()"

# Generate assessment question batch workflow
python -c "from healthcareagent import create_assessment_generation_workflow; create_assessment_generation_workflow()"
```

### Educational Workflow Color Scheme

```python
EDUCATION_COLORS = {
    'student': '#E3F2FD',          # Light blue
    'instructor': '#F3E5F5',       # Light purple
    'llm_agent': '#FFF3E0',        # Light orange
    'qa_team': '#E8F5E9',          # Light green
    'system': '#E0F2F1',           # Light teal
    'success': '#C8E6C9',          # Green
    'warning': '#FFF9C4',          # Yellow
    'error': '#FFCDD2',            # Red
}
```

### Healthcare Workflow Class

The `EducationalWorkflowDiagram` class (defined in `healthcareagent.md`) provides:
- **Swimlane support** for grouping by role (Student, Instructor, LLM Judge, System)
- **Specialized nodes**: `add_llm_process()`, `add_validation()`, `add_feedback()`, `add_human_review()`
- **Connection helpers**: `connect_yes()`, `connect_no()`, `connect_feedback_loop()`
- **Time annotations**: Add time estimates to process steps
- **Auto-export**: PNG, SVG, DOT, and Draw.io formats

### Example Workflow Structure

```python
from graphviz import Digraph

class EducationalWorkflowDiagram:
    def __init__(self, title: str, filename: str, direction: str = 'TB'):
        # Initialize with title and layout direction
        pass

    # Create swimlanes
    def create_swimlane(self, name: str, color: str):
        # Group related activities by role
        pass

    # Add nodes
    def add_start(self, label: str):
        # Start point (green circle)
        pass

    def add_process(self, label: str, color: str, time: str = None):
        # Process step (rectangle) with optional time
        pass

    def add_decision(self, label: str):
        # Decision point (diamond)
        pass

    def add_llm_process(self, label: str, model: str = None):
        # LLM processing step (special styled)
        pass

    def add_validation(self, label: str):
        # Validation checkpoint
        pass

    # Connect nodes
    def connect(self, from_node: str, to_node: str, label: str = None):
        pass

    def connect_yes(self, from_decision: str, to_node: str):
        pass

    def connect_no(self, from_decision: str, to_node: str):
        pass

    # Export
    def save(self, output_dir: str = 'diagrams'):
        # Exports to PNG, SVG, DOT
        pass

    def convert_to_drawio(self, output_dir: str = 'diagrams'):
        # Converts DOT to Draw.io format
        pass
```

### Key Healthcare Workflow Principles

1. **Keep It Simple**: Use standard shapes only, limit colors, clear labels
2. **Tell a Story**: Show left-to-right or top-to-bottom flow
3. **Educational Focus**: Always show student perspective, quality checkpoints, feedback loops
4. **Swimlanes**: Group activities by role (Student, Instructor, LLM Judge, System, QA)
5. **Time Estimates**: Document expected duration for each step
6. **Maintainability**: Save .dot files for version control, generate .drawio for editing

### Additional Resources

- **Full documentation**: `Arch_Diagrams/healthcareagent.md`
- **Examples**: LLM-as-a-Judge, OSCE generation, batch assessment (Q1-Q40)
- **Shape reference**: Complete flowchart symbol library with usage guidelines
- **Windows setup**: See `Arch_Diagrams/agent.md` for Windows-specific instructions

---

## Troubleshooting

### Draw.io Files Not Generated

If .drawio files are not being created:

1. **Check if graphviz2drawio is installed**:
   ```bash
   which graphviz2drawio
   # Should return: /opt/homebrew/bin/graphviz2drawio (or similar)
   ```

2. **Install graphviz2drawio via Homebrew**:
   ```bash
   brew install graphviz2drawio
   ```

3. **Manual conversion** (if scripts didn't generate .drawio):
   ```bash
   graphviz2drawio diagrams/your_diagram.dot -o diagrams/your_diagram.drawio
   ```

**Important**: The system-level `graphviz2drawio` command is used, NOT the Python package. Homebrew installs it with Python 3.14 in its own isolated environment, so it works regardless of your venv's Python version.

### graphviz2drawio Output

- The tool will properly convert DOT files to mxGraph XML format used by Draw.io
- The resulting .drawio files can be opened directly in https://app.diagrams.net
- The conversion preserves:
  - Node positioning and sizes
  - Cluster/group hierarchies
  - Edge connections and labels
  - Colors and styling

## Project Video Tutorial

YouTube walkthrough available demonstrating the diagram generation process:
https://www.youtube.com/watch?v=m7EuZ7GhinE

---

## Quick Decision Guide

### Which Diagram Type Should I Use?

**Use Azure Architecture Diagrams when:**
- ✅ Visualizing cloud infrastructure
- ✅ Documenting IaC templates (Terraform, Bicep, ARM)
- ✅ Showing technical resource topology
- ✅ Network architecture and security boundaries
- ✅ Cloud service integration patterns
- ✅ Azure resource relationships

**Use Healthcare/Educational Workflow Diagrams when:**
- ✅ Documenting educational processes
- ✅ LLM evaluation workflows (LLM-as-a-Judge)
- ✅ Assessment automation pipelines
- ✅ Clinical case generation (OSCE)
- ✅ Student-instructor-system interactions
- ✅ Quality assurance and review processes
- ✅ Any process involving human participants

### Summary Table

| Aspect | Azure Architecture | Healthcare Workflow |
|--------|-------------------|---------------------|
| **Icons** | Azure-specific (VM, VNet, SQL, etc.) | Standard flowchart (rectangle, diamond, circle) |
| **Focus** | Infrastructure & services | People & processes |
| **Source** | IaC templates (automated) | Manual workflow definition |
| **Audience** | Developers, DevOps, architects | Educators, clinicians, process designers |
| **Layout** | Clusters (VNet, subnets) | Swimlanes (roles) |
| **Colors** | Service tiers | Participant roles |
| **Documentation** | `agent.md` | `healthcareagent.md` |
| **Examples** | Contoso Portal, IIS+SQL | LLM-as-Judge, OSCE Generation |

### File Reference Quick Access

- **Azure Architecture Details**: `Arch_Diagrams/agent.md` (Windows setup, color coding, troubleshooting)
- **Healthcare Workflow Details**: `Arch_Diagrams/healthcareagent.md` (flowchart shapes, swimlanes, specialized nodes)
- **Quick Reference**: `CLAUDE.md` (this file)

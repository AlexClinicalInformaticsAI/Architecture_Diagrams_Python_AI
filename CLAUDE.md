# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository generates Azure architecture diagrams from Infrastructure-as-Code (IaC) templates using Python and the `diagrams` library. It demonstrates automated diagram generation for Azure resources defined in Terraform and Bicep templates, producing output in PNG, DOT (GraphViz), and Draw.io formats.

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

### Generate Architecture Diagrams

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

Output files are generated in `Arch_Diagrams/diagrams/` with three formats:
- `.png` - Visual diagram
- `.dot` - GraphViz source file
- `.drawio` - Draw.io editable format (if graphviz2drawio is installed)

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

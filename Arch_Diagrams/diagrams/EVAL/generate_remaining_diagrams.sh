#!/bin/bash

# Generate all remaining EVAL tool architecture diagrams

echo "=========================================="
echo "Generating EVAL Tool Architecture Diagrams"
echo "=========================================="
echo ""

# Array of tools to generate
tools=("MLFlow" "Agenta" "Lmnr" "Opik" "Latitude" "n8n")

for tool in "${tools[@]}"; do
    script_path="Arch_Diagrams/diagrams/EVAL/${tool}/${tool,,}_architecture.py"
    
    if [ -f "$script_path" ]; then
        echo "Generating $tool diagram..."
        python "$script_path"
        echo ""
    else
        echo "⚠️  Script not found: $script_path"
        echo ""
    fi
done

echo "=========================================="
echo "Diagram Generation Complete"
echo "=========================================="
echo ""
echo "Generated diagrams are in: diagrams/EVAL/<ToolName>/"

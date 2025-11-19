"""
Generate All Evaluation Tool Architecture Diagrams

This script generates architecture diagrams for all 10 LLM evaluation tools.
Run this to create all PNG, DOT, and Draw.io files at once.
"""

import subprocess
import os
from pathlib import Path

# List of all tools
TOOLS = [
    'CleanLab',
    'Lmnr',
    'Promptfoo',
    'Opik',
    'Latitude',
    'Agenta',
    'n8n',
    'MLFlow',
    'LangFuse',
    'DeepEval'
]

def run_diagram_script(tool_name):
    """Run the architecture diagram script for a specific tool"""
    script_path = f"diagrams/EVAL/{tool_name}/{tool_name.lower()}_architecture.py"
    
    if not os.path.exists(script_path):
        print(f"⚠️  Script not found: {script_path}")
        return False
    
    try:
        print(f"\n{'='*70}")
        print(f"Generating diagram for {tool_name}...")
        print(f"{'='*70}")
        
        result = subprocess.run(
            ['python', script_path],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print(f"✓ {tool_name} diagram generated successfully")
            print(result.stdout)
            return True
        else:
            print(f"✗ {tool_name} diagram generation failed")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print(f"✗ {tool_name} diagram generation timed out")
        return False
    except Exception as e:
        print(f"✗ Error generating {tool_name} diagram: {e}")
        return False

def main():
    print("\n" + "="*70)
    print("LLM EVALUATION TOOLS - ARCHITECTURE DIAGRAM GENERATOR")
    print("="*70)
    print(f"\nGenerating diagrams for {len(TOOLS)} tools...")
    
    results = {}
    for tool in TOOLS:
        results[tool] = run_diagram_script(tool)
    
    # Summary
    print("\n" + "="*70)
    print("GENERATION SUMMARY")
    print("="*70)
    
    successful = sum(1 for v in results.values() if v)
    failed = len(results) - successful
    
    print(f"\n✓ Successful: {successful}/{len(TOOLS)}")
    print(f"✗ Failed: {failed}/{len(TOOLS)}")
    
    if failed > 0:
        print("\nFailed tools:")
        for tool, success in results.items():
            if not success:
                print(f"  - {tool}")
    
    print("\n" + "="*70)
    print("Generated files are located in:")
    print("  diagrams/EVAL/<ToolName>/<toolname>_architecture.png")
    print("  diagrams/EVAL/<ToolName>/<toolname>_architecture.dot")
    print("  diagrams/EVAL/<ToolName>/<toolname>_architecture.drawio")
    print("="*70)

if __name__ == "__main__":
    main()

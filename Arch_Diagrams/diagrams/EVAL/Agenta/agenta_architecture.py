"""
Agenta Architecture Diagram
LLM Evaluation Platform - Component Architecture

Agenta is an open-source platform for LLM application evaluation,
providing A/B testing, prompt management, and team collaboration.

Generates PNG, DOT, and Draw.io format diagrams
"""

import subprocess
from diagrams import Diagram, Cluster, Edge
from diagrams.programming.language import Python, Javascript
from diagrams.onprem.client import Users
from diagrams.generic.storage import Storage
from diagrams.generic.database import SQL
from diagrams.generic.compute import Rack
from diagrams.programming.framework import Fastapi
from diagrams.onprem.analytics import Spark
import os

graph_attr = {
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.2",
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5"
}

with Diagram(
    "Agenta - LLM Evaluation Platform Architecture",
    filename="diagrams/EVAL/Agenta/agenta_architecture",
    outformat=["png", "dot"],
    show=False,
    direction="TB",
    graph_attr=graph_attr
):

    user = Users("Team/Developer")

    with Cluster("Web UI", graph_attr={"bgcolor": "#E3F2FD"}):
        playground = Fastapi("Playground\nTest Prompts")
        evaluator = Fastapi("Evaluator\nRun Tests")
        ab_testing = Fastapi("A/B Testing\nCompare Variants")
        prompt_mgmt = Fastapi("Prompt Manager\nVersioning")
        dashboard = Fastapi("Dashboard\nMetrics & Results")

    with Cluster("Backend API", graph_attr={"bgcolor": "#F3E5F5"}):
        api_server = Fastapi("FastAPI Server")
        variant_mgr = Python("Variant Manager")
        eval_engine = Spark("Evaluation Engine")
        test_runner = Spark("Test Runner")

    with Cluster("Prompt System", graph_attr={"bgcolor": "#FFF3E0"}):
        prompt_registry = Storage("Prompt Registry")
        variants = Storage("Variants\nDifferent Versions")
        templates = Storage("Templates")

    with Cluster("Evaluation", graph_attr={"bgcolor": "#E8F5E9"}):
        test_sets = Storage("Test Sets\nDatasets")
        evaluators_lib = Python("Evaluators\nBuilt-in Metrics")
        custom_eval = Python("Custom Evaluators")
        human_eval = Storage("Human Evaluation")

    with Cluster("LLM Integration", graph_attr={"bgcolor": "#E8F4F8"}):
        llm_providers = Rack("LLM Providers\nOpenAI, Anthropic, etc")
        model_configs = Storage("Model Configs\nParams, Temperature")

    with Cluster("Data Storage", graph_attr={"bgcolor": "#F3E5F5"}):
        mongodb = SQL("MongoDB\nResults & Metadata")
        results_store = Storage("Results Store")

    with Cluster("Deployment", graph_attr={"bgcolor": "#FFF3E0"}):
        docker = Rack("Docker\nSelf-hosted")
        cloud = Rack("Agenta Cloud\nManaged")

    # UI interactions
    user >> Edge(label="uses") >> playground
    user >> Edge(label="runs") >> evaluator
    user >> Edge(label="compares") >> ab_testing
    user >> Edge(label="manages") >> prompt_mgmt
    user >> Edge(label="views") >> dashboard

    # Backend flow
    playground >> Edge(label="calls") >> api_server
    evaluator >> Edge(label="calls") >> api_server
    ab_testing >> Edge(label="calls") >> api_server
    prompt_mgmt >> Edge(label="calls") >> api_server

    api_server >> Edge(label="manages") >> variant_mgr
    api_server >> Edge(label="triggers") >> eval_engine
    eval_engine >> Edge(label="executes") >> test_runner

    # Prompt system
    variant_mgr >> Edge(label="stores") >> prompt_registry
    prompt_registry >> Edge(label="versions") >> variants
    variants >> Edge(label="uses") >> templates

    # Evaluation
    test_runner >> Edge(label="uses") >> test_sets
    test_runner >> Edge(label="applies") >> evaluators_lib
    test_runner >> Edge(label="applies") >> custom_eval
    evaluator >> Edge(label="collects") >> human_eval

    # LLM integration
    test_runner >> Edge(label="queries") >> llm_providers
    llm_providers >> Edge(label="configured by") >> model_configs

    # Storage
    eval_engine >> Edge(label="stores") >> mongodb
    test_runner >> Edge(label="saves") >> results_store
    results_store >> Edge(label="persists") >> mongodb

    # Deployment
    api_server >> Edge(label="runs on", style="dashed") >> docker
    api_server >> Edge(label="runs on", style="dashed") >> cloud

    # Results flow
    mongodb >> Edge(label="queries") >> dashboard
    dashboard >> Edge(label="displays") >> user

print("✓ PNG and DOT files generated")

try:
    subprocess.run([
        "graphviz2drawio",
        "diagrams/EVAL/Agenta/agenta_architecture.dot",
        "-o",
        "diagrams/EVAL/Agenta/agenta_architecture.drawio"
    ], check=True)
    print("✓ Draw.io file generated")
except:
    print("✗ graphviz2drawio not found (optional)")

print("\n" + "="*70)
print("AGENTA ARCHITECTURE SUMMARY")
print("="*70)
print("\nCore Purpose:")
print("  Complete LLM evaluation platform with UI for teams")
print("\nKey Components:")
print("  1. Web UI: Playground, evaluator, A/B testing, dashboards")
print("  2. Backend: FastAPI server with evaluation engine")
print("  3. Prompt System: Registry, variants, templates")
print("  4. Evaluation: Test sets, built-in and custom evaluators")
print("  5. Storage: MongoDB for results and metadata")
print("\nCore Features:")
print("  • Playground: Test prompts interactively")
print("  • A/B Testing: Compare prompt variants")
print("  • Prompt Management: Version control and templates")
print("  • Evaluation: Built-in and custom metrics")
print("  • Human Evaluation: Collect human feedback")
print("  • Team Collaboration: Multi-user support")
print("\nEvaluation Capabilities:")
print("  • Built-in Evaluators: Common metrics")
print("  • Custom Evaluators: User-defined logic")
print("  • Test Sets: Reusable datasets")
print("  • Human-in-the-loop: Manual review")
print("\nDeployment Options:")
print("  • Self-hosted: Docker compose")
print("  • Agenta Cloud: Managed service")
print("  • Kubernetes: Production deployments")
print("\nUse Cases:")
print("  • Prompt engineering and optimization")
print("  • A/B testing different approaches")
print("  • Team collaboration on LLM apps")
print("  • Systematic evaluation workflows")
print("="*70)

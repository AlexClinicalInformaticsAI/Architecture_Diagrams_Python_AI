"""
Opik Architecture Diagram
LLM Evaluation & Experimentation (Comet ML) - Component Architecture

Opik is an open-source LLM evaluation platform integrated with Comet ML
for experiment tracking and evaluation.

Generates PNG, DOT, and Draw.io format diagrams
"""

import subprocess
from diagrams import Diagram, Cluster, Edge
from diagrams.programming.language import Python
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
    "Opik - LLM Evaluation & Experimentation Architecture",
    filename="diagrams/EVAL/Opik/opik_architecture",
    outformat=["png", "dot"],
    show=False,
    direction="TB",
    graph_attr=graph_attr
):

    user = Users("ML Engineer")

    with Cluster("Opik SDK", graph_attr={"bgcolor": "#E3F2FD"}):
        python_sdk = Python("Python SDK")
        tracking = Python("Tracking API")
        decorators = Python("@track() Decorator")

    with Cluster("Experiment Tracking", graph_attr={"bgcolor": "#F3E5F5"}):
        experiments = Storage("Experiments")
        runs = Storage("Runs\nParameters & Metrics")
        traces = Storage("Traces\nLLM Calls")

    with Cluster("Evaluation System", graph_attr={"bgcolor": "#FFF3E0"}):
        eval_engine = Spark("Evaluation Engine")
        
        with Cluster("Metrics"):
            accuracy = Python("Accuracy")
            relevance = Python("Relevance")
            hallucination = Python("Hallucination")
            custom = Python("Custom Metrics")

    with Cluster("Dataset Management", graph_attr={"bgcolor": "#E8F5E9"}):
        datasets = Storage("Datasets\nVersioned")
        test_sets = Storage("Test Sets")
        ground_truth = Storage("Ground Truth")

    with Cluster("Comet ML Integration", graph_attr={"bgcolor": "#E8F4F8"}):
        comet_api = Fastapi("Comet ML API")
        comet_ui = Fastapi("Comet UI\nVisualization")
        model_registry = Storage("Model Registry")

    with Cluster("Storage", graph_attr={"bgcolor": "#F3E5F5"}):
        backend_db = SQL("Backend DB\nPostgreSQL")
        artifact_store = Storage("Artifact Store")

    with Cluster("LLM Providers", graph_attr={"bgcolor": "#FFF3E0"}):
        llm_apis = Rack("LLM APIs\nOpenAI, Anthropic")

    # SDK usage
    user >> Edge(label="uses") >> python_sdk
    python_sdk >> Edge(label="tracks") >> tracking
    python_sdk >> Edge(label="decorates") >> decorators

    # Experiment tracking
    tracking >> Edge(label="creates") >> experiments
    experiments >> Edge(label="contains") >> runs
    runs >> Edge(label="logs") >> traces

    # Evaluation
    runs >> Edge(label="evaluates") >> eval_engine
    eval_engine >> Edge(label="applies") >> accuracy
    eval_engine >> Edge(label="applies") >> relevance
    eval_engine >> Edge(label="applies") >> hallucination
    eval_engine >> Edge(label="applies") >> custom

    # Dataset management
    eval_engine >> Edge(label="uses") >> datasets
    datasets >> Edge(label="contains") >> test_sets
    test_sets >> Edge(label="compares") >> ground_truth

    # Comet ML integration
    tracking >> Edge(label="syncs") >> comet_api
    comet_api >> Edge(label="displays") >> comet_ui
    runs >> Edge(label="registers") >> model_registry

    # Storage
    experiments >> Edge(label="stores") >> backend_db
    traces >> Edge(label="stores") >> artifact_store

    # LLM integration
    traces >> Edge(label="calls") >> llm_apis

    # User views
    comet_ui >> Edge(label="views") >> user
    model_registry >> Edge(label="manages") >> user

print("✓ PNG and DOT files generated")

try:
    subprocess.run([
        "graphviz2drawio",
        "diagrams/EVAL/Opik/opik_architecture.dot",
        "-o",
        "diagrams/EVAL/Opik/opik_architecture.drawio"
    ], check=True)
    print("✓ Draw.io file generated")
except:
    print("✗ graphviz2drawio not found (optional)")

print("\n" + "="*70)
print("OPIK ARCHITECTURE SUMMARY")
print("="*70)
print("\nCore Purpose:")
print("  LLM evaluation and experimentation with Comet ML integration")
print("\nKey Components:")
print("  1. SDK: Python SDK with tracking decorators")
print("  2. Experiment Tracking: Runs, parameters, metrics")
print("  3. Evaluation: Built-in and custom metrics")
print("  4. Datasets: Versioned test sets")
print("  5. Comet ML: Visualization and model registry")
print("\nCore Features:")
print("  • Experiment Tracking: Track LLM experiments")
print("  • Evaluation Metrics: Accuracy, relevance, hallucination")
print("  • Dataset Versioning: Manage test sets")
print("  • Comet Integration: Leverage Comet ML platform")
print("  • Model Registry: Version and deploy models")
print("\nEvaluation Metrics:")
print("  • Accuracy: Correctness of outputs")
print("  • Relevance: Response relevance")
print("  • Hallucination: Detect false information")
print("  • Custom: User-defined metrics")
print("\nComet ML Benefits:")
print("  • Visualization: Rich experiment dashboards")
print("  • Comparison: Compare multiple runs")
print("  • Collaboration: Team features")
print("  • Model Registry: Centralized model management")
print("\nUse Cases:")
print("  • LLM experiment tracking")
print("  • Model evaluation and comparison")
print("  • Dataset management")
print("  • Research and development")
print("="*70)

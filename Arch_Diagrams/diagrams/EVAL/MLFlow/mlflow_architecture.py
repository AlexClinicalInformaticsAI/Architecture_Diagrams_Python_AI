"""
MLFlow Architecture Diagram
ML Lifecycle Management Platform - Component Architecture

MLFlow is an open-source platform for the complete machine learning lifecycle,
including experiment tracking, model registry, and deployment.

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

# Graph attributes
graph_attr = {
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.2",
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5"
}

with Diagram(
    "MLFlow - ML Lifecycle Management Architecture",
    filename="diagrams/EVAL/MLFlow/mlflow_architecture",
    outformat=["png", "dot"],
    show=False,
    direction="TB",
    graph_attr=graph_attr
):

    user = Users("Data Scientist")

    with Cluster("MLFlow Tracking", graph_attr={"bgcolor": "#E3F2FD"}):
        tracking_api = Fastapi("Tracking API")
        experiments = Storage("Experiments")
        runs = Storage("Runs\nMetrics, Params, Artifacts")
        artifacts = Storage("Artifact Store\nS3, Azure, GCS")

    with Cluster("MLFlow Models", graph_attr={"bgcolor": "#F3E5F5"}):
        model_registry = Storage("Model Registry\nVersioning")
        model_stages = Storage("Stages\nStaging, Production")
        model_flavors = Python("Model Flavors\nSklearn, PyTorch, TF")

    with Cluster("MLFlow Projects", graph_attr={"bgcolor": "#FFF3E0"}):
        project_spec = Storage("MLproject File\nYAML Spec")
        conda_env = Storage("Conda Environment")
        docker_env = Rack("Docker Environment")

    with Cluster("LLM Features", graph_attr={"bgcolor": "#E8F5E9"}):
        llm_tracking = Spark("LLM Tracing\nObservability")
        llm_eval = Spark("LLM Evaluation\nAutomated Metrics")
        prompt_mgmt = Storage("Prompt Management\nVersioning")
        app_tracking = Spark("App Version Tracking\nLineage")

    with Cluster("Deployment", graph_attr={"bgcolor": "#E8F4F8"}):
        serving = Fastapi("MLFlow Serving\nREST API")
        batch = Spark("Batch Inference")
        cloud_deploy = Rack("Cloud Deployment\nAWS, Azure, GCP")

    with Cluster("Storage Backend", graph_attr={"bgcolor": "#F3E5F5"}):
        metadata_db = SQL("Metadata Store\nPostgreSQL, MySQL")
        artifact_storage = Storage("Artifact Storage\nS3, Azure Blob")

    with Cluster("Integrations", graph_attr={"bgcolor": "#FFF3E0"}):
        frameworks = Rack("ML Frameworks\nSklearn, PyTorch, TF")
        llm_providers = Rack("LLM Providers\nOpenAI, Anthropic")
        orchestrators = Rack("Orchestrators\nAirflow, Kubeflow")

    # Tracking flow
    user >> Edge(label="logs") >> tracking_api
    tracking_api >> Edge(label="creates") >> experiments
    experiments >> Edge(label="contains") >> runs
    runs >> Edge(label="stores") >> artifacts

    # Model registry
    runs >> Edge(label="registers") >> model_registry
    model_registry >> Edge(label="manages") >> model_stages
    model_flavors >> Edge(label="supports") >> model_registry

    # Projects
    user >> Edge(label="defines") >> project_spec
    project_spec >> Edge(label="uses") >> conda_env
    project_spec >> Edge(label="uses") >> docker_env

    # LLM features
    tracking_api >> Edge(label="traces") >> llm_tracking
    llm_tracking >> Edge(label="evaluates") >> llm_eval
    llm_eval >> Edge(label="uses") >> prompt_mgmt
    runs >> Edge(label="tracks") >> app_tracking

    # Deployment
    model_registry >> Edge(label="deploys") >> serving
    model_registry >> Edge(label="deploys") >> batch
    serving >> Edge(label="hosts") >> cloud_deploy

    # Storage
    tracking_api >> Edge(label="writes") >> metadata_db
    artifacts >> Edge(label="stores") >> artifact_storage

    # Integrations
    frameworks >> Edge(label="integrates") >> tracking_api
    llm_providers >> Edge(label="integrates") >> llm_tracking
    orchestrators >> Edge(label="triggers") >> project_spec

    # User interactions
    model_registry >> Edge(label="views") >> user
    serving >> Edge(label="queries") >> user
    llm_eval >> Edge(label="reviews") >> user

print("✓ PNG and DOT files generated")

try:
    subprocess.run([
        "graphviz2drawio",
        "diagrams/EVAL/MLFlow/mlflow_architecture.dot",
        "-o",
        "diagrams/EVAL/MLFlow/mlflow_architecture.drawio"
    ], check=True)
    print("✓ Draw.io file generated")
except:
    print("✗ graphviz2drawio not found (optional)")

print("\n" + "="*70)
print("MLFLOW ARCHITECTURE SUMMARY")
print("="*70)
print("\nCore Purpose:")
print("  Open-source platform for the complete ML lifecycle")
print("\nKey Components:")
print("  1. Tracking: Experiments, runs, metrics, parameters")
print("  2. Models: Registry, versioning, staging")
print("  3. Projects: Reproducible runs with environments")
print("  4. LLM Features: Tracing, evaluation, prompt management")
print("  5. Deployment: Serving, batch inference, cloud")
print("\nMLFlow Tracking:")
print("  • Experiments: Organize related runs")
print("  • Runs: Individual executions with metrics/params")
print("  • Artifacts: Models, plots, data files")
print("  • Autologging: Automatic metric capture")
print("\nModel Registry:")
print("  • Versioning: Track model versions")
print("  • Stages: None, Staging, Production, Archived")
print("  • Lineage: Track model provenance")
print("  • Annotations: Add descriptions and tags")
print("\nLLM Capabilities:")
print("  • Tracing: Debug LLM applications")
print("  • Evaluation: Automated quality metrics")
print("  • Prompt Management: Version and track prompts")
print("  • App Tracking: End-to-end lineage")
print("\nDeployment Options:")
print("  • MLFlow Serving: REST API endpoints")
print("  • Batch Inference: Large-scale predictions")
print("  • Cloud: AWS SageMaker, Azure ML, GCP")
print("  • Kubernetes: Container orchestration")
print("\nIntegrations:")
print("  • ML Frameworks: Sklearn, PyTorch, TensorFlow, XGBoost")
print("  • LLM Providers: OpenAI, Anthropic, HuggingFace")
print("  • Orchestrators: Airflow, Kubeflow, Databricks")
print("  • Storage: S3, Azure Blob, GCS, HDFS")
print("\nUse Cases:")
print("  • Experiment tracking and comparison")
print("  • Model versioning and registry")
print("  • Reproducible ML pipelines")
print("  • LLM application monitoring")
print("  • Model deployment and serving")
print("="*70)

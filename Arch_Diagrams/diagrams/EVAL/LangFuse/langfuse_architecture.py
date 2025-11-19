"""
LangFuse Architecture Diagram
LLM Observability & Analytics Platform - Component Architecture

LangFuse is an open-source LLM engineering platform for monitoring,
evaluating, and debugging AI applications in production.

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
    "LangFuse - LLM Observability & Analytics Architecture",
    filename="diagrams/EVAL/LangFuse/langfuse_architecture",
    outformat=["png", "dot"],
    show=False,
    direction="TB",
    graph_attr=graph_attr
):

    user = Users("Developer/Team")

    with Cluster("Application Layer", graph_attr={"bgcolor": "#E3F2FD"}):
        llm_app = Fastapi("LLM Application")
        
        with Cluster("Instrumentation"):
            sdk_python = Python("Python SDK\n@observe()")
            sdk_js = Javascript("JS/TS SDK")
            openai_int = Python("OpenAI Integration")
            langchain = Python("LangChain Callback")
            llamaindex = Python("LlamaIndex Callback")

    with Cluster("Ingestion Layer", graph_attr={"bgcolor": "#F3E5F5"}):
        api = Fastapi("Public API\nOpenAPI Spec")
        trace_ingest = Fastapi("Trace Ingestion")
        event_queue = Storage("Event Queue")

    with Cluster("Core Platform", graph_attr={"bgcolor": "#FFF3E0"}):
        with Cluster("Tracing System"):
            trace_engine = Spark("Trace Engine")
            span_processor = Spark("Span Processor")
            session_mgr = Spark("Session Manager")

        with Cluster("Data Storage"):
            postgres = SQL("PostgreSQL\nTraces & Metadata")
            clickhouse = SQL("ClickHouse\nAnalytics (optional)")

        with Cluster("Prompt Management"):
            prompt_registry = Storage("Prompt Registry\nVersioning")
            prompt_cache = Storage("Prompt Cache")

    with Cluster("Evaluation System", graph_attr={"bgcolor": "#E8F5E9"}):
        eval_engine = Spark("Evaluation Engine")
        
        with Cluster("Evaluation Methods"):
            llm_judge = Rack("LLM-as-Judge")
            user_feedback = Storage("User Feedback")
            manual_label = Storage("Manual Labeling")
            custom_eval = Python("Custom Pipelines")

        datasets = Storage("Datasets\nTest Sets")

    with Cluster("Analytics & Insights", graph_attr={"bgcolor": "#E8F4F8"}):
        analytics = Spark("Analytics Engine")
        metrics = Storage("Metrics\nCost, Latency, Quality")
        dashboards = Fastapi("Dashboards")

    with Cluster("Web UI", graph_attr={"bgcolor": "#F3E5F5"}):
        trace_viewer = Fastapi("Trace Viewer\nDebug Sessions")
        playground = Fastapi("LLM Playground\nTest Prompts")
        dataset_ui = Fastapi("Dataset Manager")
        prompt_ui = Fastapi("Prompt Editor")

    with Cluster("Integrations", graph_attr={"bgcolor": "#FFF3E0"}):
        frameworks = Rack("Frameworks\nLangChain, LlamaIndex")
        models = Rack("Model Providers\nOpenAI, Anthropic, etc")
        tools = Rack("Tools\nPromptfoo, Flowise")

    # Application instrumentation
    user >> Edge(label="develops") >> llm_app
    llm_app >> Edge(label="instruments") >> sdk_python
    llm_app >> Edge(label="instruments") >> sdk_js
    llm_app >> Edge(label="uses") >> openai_int
    llm_app >> Edge(label="uses") >> langchain
    llm_app >> Edge(label="uses") >> llamaindex

    # Ingestion flow
    sdk_python >> Edge(label="sends traces") >> api
    sdk_js >> Edge(label="sends traces") >> api
    openai_int >> Edge(label="auto-trace") >> api
    langchain >> Edge(label="callback") >> api
    llamaindex >> Edge(label="callback") >> api

    api >> Edge(label="queues") >> trace_ingest
    trace_ingest >> Edge(label="buffers") >> event_queue

    # Core processing
    event_queue >> Edge(label="processes") >> trace_engine
    trace_engine >> Edge(label="creates") >> span_processor
    span_processor >> Edge(label="groups") >> session_mgr

    # Data storage
    trace_engine >> Edge(label="stores") >> postgres
    analytics >> Edge(label="queries", style="dashed") >> clickhouse

    # Prompt management
    llm_app >> Edge(label="fetches", style="dashed") >> prompt_registry
    prompt_registry >> Edge(label="caches") >> prompt_cache
    prompt_cache >> Edge(label="serves") >> llm_app

    # Evaluation
    trace_engine >> Edge(label="evaluates") >> eval_engine
    eval_engine >> Edge(label="uses") >> llm_judge
    eval_engine >> Edge(label="collects") >> user_feedback
    eval_engine >> Edge(label="uses") >> manual_label
    eval_engine >> Edge(label="runs") >> custom_eval

    datasets >> Edge(label="tests") >> eval_engine
    eval_engine >> Edge(label="stores results") >> postgres

    # Analytics
    postgres >> Edge(label="analyzes") >> analytics
    analytics >> Edge(label="calculates") >> metrics
    metrics >> Edge(label="displays") >> dashboards

    # Web UI
    postgres >> Edge(label="queries") >> trace_viewer
    postgres >> Edge(label="queries") >> dataset_ui
    prompt_registry >> Edge(label="manages") >> prompt_ui
    models >> Edge(label="tests") >> playground

    trace_viewer >> Edge(label="views") >> user
    playground >> Edge(label="experiments") >> user
    dataset_ui >> Edge(label="manages") >> user
    prompt_ui >> Edge(label="edits") >> user
    dashboards >> Edge(label="monitors") >> user

    # Integrations
    frameworks >> Edge(label="integrates", style="dashed") >> api
    models >> Edge(label="connects", style="dashed") >> llm_app
    tools >> Edge(label="exports", style="dashed") >> api

print("✓ PNG and DOT files generated")

# Convert to Draw.io
try:
    subprocess.run([
        "graphviz2drawio",
        "diagrams/EVAL/LangFuse/langfuse_architecture.dot",
        "-o",
        "diagrams/EVAL/LangFuse/langfuse_architecture.drawio"
    ], check=True)
    print("✓ Draw.io file generated")
except:
    print("✗ graphviz2drawio not found (optional)")

print("\n" + "="*70)
print("LANGFUSE ARCHITECTURE SUMMARY")
print("="*70)
print("\nCore Purpose:")
print("  Production-grade LLM observability and analytics platform")
print("\nKey Components:")
print("  1. Instrumentation: SDKs and integrations for tracing")
print("  2. Ingestion: API and event queue for data collection")
print("  3. Tracing System: Span processing and session management")
print("  4. Evaluation: Multiple evaluation methods and datasets")
print("  5. Analytics: Metrics, dashboards, and insights")
print("  6. Prompt Management: Versioning and caching")
print("\nCore Features:")
print("  • Tracing: Track LLM calls, retrieval, embeddings, agents")
print("  • Prompt Management: Version control and collaboration")
print("  • Evaluations: LLM-as-judge, user feedback, manual labeling")
print("  • Datasets: Test sets and benchmarks")
print("  • Playground: Test prompts and model configurations")
print("  • Analytics: Cost, latency, quality metrics")
print("\nInstrumentation Methods:")
print("  • Python SDK: @observe() decorator")
print("  • JS/TS SDK: Native TypeScript support")
print("  • OpenAI Integration: Drop-in replacement")
print("  • LangChain: Callback handler")
print("  • LlamaIndex: Callback system")
print("  • Direct API: OpenAPI spec available")
print("\nData Storage:")
print("  • PostgreSQL: Traces and metadata")
print("  • ClickHouse: Analytics (optional)")
print("  • Caching: Prompt and query caching")
print("\nEvaluation Methods:")
print("  • LLM-as-Judge: Automated evaluation")
print("  • User Feedback: Thumbs up/down, ratings")
print("  • Manual Labeling: Human review")
print("  • Custom Pipelines: API/SDK integration")
print("\nDeployment Options:")
print("  • Cloud: Managed by LangFuse team")
print("  • Self-Hosted: Docker, Kubernetes, VM")
print("  • Terraform: AWS, Azure, GCP templates")
print("\nIntegrations:")
print("  • Frameworks: LangChain, LlamaIndex, Haystack, LiteLLM")
print("  • Models: OpenAI, Anthropic, Bedrock, Ollama, 100+ LLMs")
print("  • Tools: Promptfoo, Flowise, Langflow, Dify, AutoGen")
print("\nUse Cases:")
print("  • Production monitoring and debugging")
print("  • Cost and latency optimization")
print("  • Quality evaluation and improvement")
print("  • Prompt engineering and testing")
print("  • Team collaboration on LLM apps")
print("  • Compliance and audit trails")
print("="*70)

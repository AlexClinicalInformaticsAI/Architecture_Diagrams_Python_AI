"""
Lmnr Architecture Diagram
Lightweight LLM Observability - Component Architecture

Lmnr is a lightweight observability platform for LLM applications
with simple tracing and minimal overhead.

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
    "Lmnr - Lightweight LLM Observability Architecture",
    filename="diagrams/EVAL/Lmnr/lmnr_architecture",
    outformat=["png", "dot"],
    show=False,
    direction="TB",
    graph_attr=graph_attr
):

    user = Users("Developer")

    with Cluster("Application", graph_attr={"bgcolor": "#E3F2FD"}):
        llm_app = Fastapi("LLM Application")
        
        with Cluster("Instrumentation"):
            python_sdk = Python("Python SDK\nLightweight")
            ts_sdk = Javascript("TypeScript SDK")

    with Cluster("Lmnr Core", graph_attr={"bgcolor": "#F3E5F5"}):
        api = Fastapi("Lmnr API\nMinimal Overhead")
        trace_collector = Spark("Trace Collector")
        span_processor = Spark("Span Processor")

    with Cluster("Tracing System", graph_attr={"bgcolor": "#FFF3E0"}):
        traces = Storage("Traces\nExecution Paths")
        spans = Storage("Spans\nIndividual Steps")
        events = Storage("Events\nLLM Calls")

    with Cluster("Storage", graph_attr={"bgcolor": "#E8F5E9"}):
        timeseries_db = SQL("Time-Series DB\nFast Queries")
        metadata = Storage("Metadata Store")

    with Cluster("Web UI", graph_attr={"bgcolor": "#E8F4F8"}):
        trace_viewer = Fastapi("Trace Viewer\nSimple Interface")
        search = Fastapi("Search\nFilter Traces")
        metrics = Fastapi("Metrics\nBasic Analytics")

    with Cluster("Integrations", graph_attr={"bgcolor": "#F3E5F5"}):
        langchain = Python("LangChain")
        llamaindex = Python("LlamaIndex")
        openai = Rack("OpenAI SDK")

    # Instrumentation
    user >> Edge(label="develops") >> llm_app
    llm_app >> Edge(label="uses") >> python_sdk
    llm_app >> Edge(label="uses") >> ts_sdk

    # Tracing flow
    python_sdk >> Edge(label="sends") >> api
    ts_sdk >> Edge(label="sends") >> api
    
    api >> Edge(label="collects") >> trace_collector
    trace_collector >> Edge(label="processes") >> span_processor

    # Trace storage
    span_processor >> Edge(label="creates") >> traces
    traces >> Edge(label="contains") >> spans
    spans >> Edge(label="logs") >> events

    # Storage
    span_processor >> Edge(label="stores") >> timeseries_db
    traces >> Edge(label="metadata") >> metadata

    # UI
    timeseries_db >> Edge(label="queries") >> trace_viewer
    timeseries_db >> Edge(label="searches") >> search
    timeseries_db >> Edge(label="aggregates") >> metrics

    trace_viewer >> Edge(label="views") >> user
    search >> Edge(label="filters") >> user
    metrics >> Edge(label="monitors") >> user

    # Integrations
    langchain >> Edge(label="integrates", style="dashed") >> python_sdk
    llamaindex >> Edge(label="integrates", style="dashed") >> python_sdk
    openai >> Edge(label="wraps", style="dashed") >> python_sdk

print("✓ PNG and DOT files generated")

try:
    subprocess.run([
        "graphviz2drawio",
        "diagrams/EVAL/Lmnr/lmnr_architecture.dot",
        "-o",
        "diagrams/EVAL/Lmnr/lmnr_architecture.drawio"
    ], check=True)
    print("✓ Draw.io file generated")
except:
    print("✗ graphviz2drawio not found (optional)")

print("\n" + "="*70)
print("LMNR ARCHITECTURE SUMMARY")
print("="*70)
print("\nCore Purpose:")
print("  Lightweight observability for LLM applications")
print("\nKey Components:")
print("  1. SDKs: Python and TypeScript with minimal overhead")
print("  2. Trace Collector: Fast ingestion")
print("  3. Span Processor: Efficient processing")
print("  4. Storage: Time-series database")
print("  5. Web UI: Simple trace viewer")
print("\nCore Features:")
print("  • Lightweight: Minimal performance impact")
print("  • Simple: Easy to integrate and use")
print("  • Fast: Quick trace collection and queries")
print("  • Self-hosted: Run on your infrastructure")
print("\nTracing Capabilities:")
print("  • Traces: Complete execution paths")
print("  • Spans: Individual operation steps")
print("  • Events: LLM calls and responses")
print("  • Metadata: Context and tags")
print("\nIntegrations:")
print("  • LangChain: Native support")
print("  • LlamaIndex: Native support")
print("  • OpenAI: SDK wrapper")
print("  • Custom: Direct SDK usage")
print("\nUse Cases:")
print("  • Basic LLM app monitoring")
print("  • Quick debugging")
print("  • Low-overhead tracing")
print("  • Simple observability needs")
print("="*70)

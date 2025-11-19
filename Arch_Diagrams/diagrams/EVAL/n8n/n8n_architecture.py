"""
n8n Architecture Diagram
Workflow Automation with AI Integration - Component Architecture

n8n is an open-source workflow automation platform with extensive
AI and LLM integration capabilities.

Generates PNG, DOT, and Draw.io format diagrams
"""

import subprocess
from diagrams import Diagram, Cluster, Edge
from diagrams.programming.language import Javascript
from diagrams.onprem.client import Users
from diagrams.generic.storage import Storage
from diagrams.generic.database import SQL
from diagrams.generic.compute import Rack
from diagrams.programming.framework import Fastapi
from diagrams.onprem.workflow import Airflow
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
    "n8n - Workflow Automation with AI Architecture",
    filename="diagrams/EVAL/n8n/n8n_architecture",
    outformat=["png", "dot"],
    show=False,
    direction="TB",
    graph_attr=graph_attr
):

    user = Users("User/Developer")

    with Cluster("Web UI", graph_attr={"bgcolor": "#E3F2FD"}):
        workflow_editor = Fastapi("Workflow Editor\nVisual Builder")
        node_library = Fastapi("Node Library\n400+ Integrations")
        execution_view = Fastapi("Execution View\nDebug & Monitor")

    with Cluster("Workflow Engine", graph_attr={"bgcolor": "#F3E5F5"}):
        executor = Airflow("Workflow Executor")
        scheduler = Airflow("Scheduler\nCron & Webhooks")
        queue = Storage("Execution Queue")

    with Cluster("Node System", graph_attr={"bgcolor": "#FFF3E0"}):
        with Cluster("AI Nodes"):
            openai_node = Rack("OpenAI Node\nGPT-3.5/4")
            anthropic_node = Rack("Anthropic Node\nClaude")
            huggingface_node = Rack("HuggingFace Node")
            langchain_node = Rack("LangChain Node")

        with Cluster("Integration Nodes"):
            http_node = Fastapi("HTTP Request")
            webhook_node = Fastapi("Webhook")
            database_node = SQL("Database Nodes")
            api_nodes = Rack("API Nodes\n400+ Services")

        with Cluster("Logic Nodes"):
            if_node = Javascript("IF Condition")
            switch_node = Javascript("Switch")
            code_node = Javascript("Code\nJavaScript/Python")
            merge_node = Javascript("Merge Data")

    with Cluster("Data Processing", graph_attr={"bgcolor": "#E8F5E9"}):
        data_transformer = Javascript("Data Transformer")
        json_parser = Javascript("JSON Parser")
        variables = Storage("Variables\nWorkflow State")

    with Cluster("Storage", graph_attr={"bgcolor": "#E8F4F8"}):
        workflow_db = SQL("Workflow DB\nSQLite/PostgreSQL")
        execution_data = Storage("Execution Data")
        credentials = Storage("Credentials\nEncrypted")

    with Cluster("Triggers", graph_attr={"bgcolor": "#F3E5F5"}):
        cron_trigger = Airflow("Cron Trigger\nScheduled")
        webhook_trigger = Fastapi("Webhook Trigger\nHTTP")
        manual_trigger = Fastapi("Manual Trigger")

    with Cluster("External Services", graph_attr={"bgcolor": "#FFF3E0"}):
        llm_apis = Rack("LLM APIs\nOpenAI, Anthropic")
        third_party = Rack("Third-Party APIs\n400+ Services")

    # UI interactions
    user >> Edge(label="builds") >> workflow_editor
    workflow_editor >> Edge(label="uses") >> node_library
    user >> Edge(label="monitors") >> execution_view

    # Workflow execution
    workflow_editor >> Edge(label="saves") >> workflow_db
    workflow_db >> Edge(label="loads") >> executor

    # Triggers
    cron_trigger >> Edge(label="schedules") >> scheduler
    webhook_trigger >> Edge(label="triggers") >> executor
    manual_trigger >> Edge(label="starts") >> executor

    scheduler >> Edge(label="queues") >> queue
    queue >> Edge(label="executes") >> executor

    # Node execution
    executor >> Edge(label="runs") >> openai_node
    executor >> Edge(label="runs") >> anthropic_node
    executor >> Edge(label="runs") >> huggingface_node
    executor >> Edge(label="runs") >> langchain_node
    executor >> Edge(label="runs") >> http_node
    executor >> Edge(label="runs") >> webhook_node
    executor >> Edge(label="runs") >> database_node
    executor >> Edge(label="runs") >> if_node
    executor >> Edge(label="runs") >> code_node

    # Data processing
    executor >> Edge(label="transforms") >> data_transformer
    data_transformer >> Edge(label="parses") >> json_parser
    executor >> Edge(label="uses") >> variables

    # External calls
    openai_node >> Edge(label="calls") >> llm_apis
    anthropic_node >> Edge(label="calls") >> llm_apis
    api_nodes >> Edge(label="calls") >> third_party

    # Storage
    executor >> Edge(label="stores") >> execution_data
    workflow_editor >> Edge(label="manages") >> credentials

    # Monitoring
    execution_data >> Edge(label="displays") >> execution_view
    execution_view >> Edge(label="views") >> user

print("✓ PNG and DOT files generated")

try:
    subprocess.run([
        "graphviz2drawio",
        "diagrams/EVAL/n8n/n8n_architecture.dot",
        "-o",
        "diagrams/EVAL/n8n/n8n_architecture.drawio"
    ], check=True)
    print("✓ Draw.io file generated")
except:
    print("✗ graphviz2drawio not found (optional)")

print("\n" + "="*70)
print("N8N ARCHITECTURE SUMMARY")
print("="*70)
print("\nCore Purpose:")
print("  Visual workflow automation platform with AI integration")
print("\nKey Components:")
print("  1. Web UI: Visual workflow editor")
print("  2. Workflow Engine: Executor and scheduler")
print("  3. Node System: 400+ integrations including AI")
print("  4. Data Processing: Transformers and parsers")
print("  5. Triggers: Cron, webhooks, manual")
print("\nAI Nodes:")
print("  • OpenAI: GPT-3.5, GPT-4, embeddings")
print("  • Anthropic: Claude models")
print("  • HuggingFace: Open-source models")
print("  • LangChain: Agent workflows")
print("\nIntegration Nodes:")
print("  • HTTP: REST API calls")
print("  • Webhooks: Receive HTTP requests")
print("  • Databases: SQL, MongoDB, Redis")
print("  • 400+ Services: Slack, Gmail, Notion, etc")
print("\nLogic Nodes:")
print("  • IF: Conditional branching")
print("  • Switch: Multiple conditions")
print("  • Code: JavaScript/Python execution")
print("  • Merge: Combine data streams")
print("\nTriggers:")
print("  • Cron: Scheduled execution")
print("  • Webhook: HTTP-triggered")
print("  • Manual: User-initiated")
print("\nDeployment:")
print("  • Self-hosted: Docker, npm")
print("  • n8n Cloud: Managed service")
print("  • Desktop: Electron app")
print("\nUse Cases:")
print("  • AI-powered automation")
print("  • Data pipelines with LLMs")
print("  • API orchestration")
print("  • Business process automation")
print("  • Integration workflows")
print("="*70)

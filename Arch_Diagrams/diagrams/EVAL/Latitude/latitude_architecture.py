"""
Latitude Architecture Diagram
Prompt Management Platform - Component Architecture

Latitude is a prompt management platform for versioning, testing,
and deploying prompts with team collaboration.

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
from diagrams.onprem.vcs import Github
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
    "Latitude - Prompt Management Platform Architecture",
    filename="diagrams/EVAL/Latitude/latitude_architecture",
    outformat=["png", "dot"],
    show=False,
    direction="TB",
    graph_attr=graph_attr
):

    user = Users("Team/Developer")

    with Cluster("Web UI", graph_attr={"bgcolor": "#E3F2FD"}):
        prompt_editor = Fastapi("Prompt Editor\nCollaborative")
        version_viewer = Fastapi("Version History")
        playground = Fastapi("Playground\nTest Prompts")
        analytics = Fastapi("Analytics\nUsage Metrics")

    with Cluster("Prompt Management", graph_attr={"bgcolor": "#F3E5F5"}):
        prompt_registry = Storage("Prompt Registry")
        versions = Storage("Versions\nGit-like")
        templates = Storage("Templates\nReusable")
        variables = Storage("Variables\nDynamic")

    with Cluster("Version Control", graph_attr={"bgcolor": "#FFF3E0"}):
        git_backend = Github("Git Backend\nVersion History")
        branches = Storage("Branches\nDevelopment")
        commits = Storage("Commits\nChanges")
        tags = Storage("Tags\nReleases")

    with Cluster("Deployment", graph_attr={"bgcolor": "#E8F5E9"}):
        api = Fastapi("Latitude API\nPrompt Serving")
        cdn = Rack("CDN\nFast Delivery")
        cache = Storage("Cache\nLow Latency")

    with Cluster("SDKs", graph_attr={"bgcolor": "#E8F4F8"}):
        python_sdk = Python("Python SDK")
        js_sdk = Javascript("JavaScript SDK")
        rest_api = Fastapi("REST API")

    with Cluster("Testing & Evaluation", graph_attr={"bgcolor": "#F3E5F5"}):
        test_runner = Fastapi("Test Runner")
        test_sets = Storage("Test Sets")
        results = Storage("Results\nMetrics")

    with Cluster("LLM Integration", graph_attr={"bgcolor": "#FFF3E0"}):
        llm_providers = Rack("LLM Providers\nOpenAI, Anthropic")

    with Cluster("Storage", graph_attr={"bgcolor": "#E8F5E9"}):
        database = SQL("Database\nPostgreSQL")

    # UI interactions
    user >> Edge(label="edits") >> prompt_editor
    user >> Edge(label="views") >> version_viewer
    user >> Edge(label="tests") >> playground
    user >> Edge(label="monitors") >> analytics

    # Prompt management
    prompt_editor >> Edge(label="saves") >> prompt_registry
    prompt_registry >> Edge(label="versions") >> versions
    versions >> Edge(label="uses") >> templates
    templates >> Edge(label="contains") >> variables

    # Version control
    versions >> Edge(label="commits") >> git_backend
    git_backend >> Edge(label="manages") >> branches
    branches >> Edge(label="contains") >> commits
    commits >> Edge(label="tagged") >> tags

    # Deployment
    prompt_registry >> Edge(label="deploys") >> api
    api >> Edge(label="serves via") >> cdn
    cdn >> Edge(label="caches") >> cache

    # SDK usage
    cache >> Edge(label="fetches") >> python_sdk
    cache >> Edge(label="fetches") >> js_sdk
    api >> Edge(label="exposes") >> rest_api

    python_sdk >> Edge(label="uses") >> user
    js_sdk >> Edge(label="uses") >> user

    # Testing
    playground >> Edge(label="runs") >> test_runner
    test_runner >> Edge(label="uses") >> test_sets
    test_runner >> Edge(label="generates") >> results

    # LLM integration
    playground >> Edge(label="calls") >> llm_providers
    test_runner >> Edge(label="calls") >> llm_providers

    # Storage
    prompt_registry >> Edge(label="stores") >> database
    results >> Edge(label="stores") >> database
    analytics >> Edge(label="queries") >> database

print("✓ PNG and DOT files generated")

try:
    subprocess.run([
        "graphviz2drawio",
        "diagrams/EVAL/Latitude/latitude_architecture.dot",
        "-o",
        "diagrams/EVAL/Latitude/latitude_architecture.drawio"
    ], check=True)
    print("✓ Draw.io file generated")
except:
    print("✗ graphviz2drawio not found (optional)")

print("\n" + "="*70)
print("LATITUDE ARCHITECTURE SUMMARY")
print("="*70)
print("\nCore Purpose:")
print("  Prompt management platform with versioning and collaboration")
print("\nKey Components:")
print("  1. Web UI: Editor, version viewer, playground, analytics")
print("  2. Prompt Management: Registry, versions, templates")
print("  3. Version Control: Git-like branching and commits")
print("  4. Deployment: API, CDN, caching")
print("  5. SDKs: Python, JavaScript, REST API")
print("\nCore Features:")
print("  • Prompt Editor: Collaborative editing")
print("  • Version Control: Git-like workflow")
print("  • Playground: Test prompts interactively")
print("  • Templates: Reusable prompt patterns")
print("  • Variables: Dynamic prompt content")
print("  • Analytics: Usage and performance metrics")
print("\nVersion Control:")
print("  • Branches: Development workflows")
print("  • Commits: Track changes")
print("  • Tags: Release management")
print("  • History: Full audit trail")
print("\nDeployment:")
print("  • API: Fast prompt serving")
print("  • CDN: Global distribution")
print("  • Caching: Low latency access")
print("  • SDKs: Easy integration")
print("\nTesting:")
print("  • Playground: Interactive testing")
print("  • Test Sets: Automated evaluation")
print("  • Results: Performance metrics")
print("\nUse Cases:")
print("  • Prompt version control")
print("  • Team collaboration")
print("  • Prompt testing and optimization")
print("  • Deployment management")
print("  • Usage analytics")
print("="*70)

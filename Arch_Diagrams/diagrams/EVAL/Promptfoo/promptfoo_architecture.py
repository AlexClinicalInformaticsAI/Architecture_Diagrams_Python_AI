"""
Promptfoo Architecture Diagram
LLM Testing & Red Teaming Framework - Component Architecture

Promptfoo is a developer-friendly, local-first tool for testing and securing
LLM applications with automated evaluations and red teaming capabilities.

Generates PNG, DOT, and Draw.io format diagrams
"""

import subprocess
from diagrams import Diagram, Cluster, Edge
from diagrams.programming.language import Python, Javascript
from diagrams.onprem.client import Users
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack
from diagrams.programming.framework import Fastapi
from diagrams.onprem.vcs import Github
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
    "Promptfoo - LLM Testing & Red Teaming Architecture",
    filename="diagrams/EVAL/Promptfoo/promptfoo_architecture",
    outformat=["png", "dot"],
    show=False,
    direction="TB",
    graph_attr=graph_attr
):

    user = Users("Developer")

    with Cluster("Configuration", graph_attr={"bgcolor": "#E3F2FD"}):
        config = Storage("YAML/JSON Config\npromptfooconfig.yaml")
        prompts = Storage("Prompts\nMultiple Variations")
        test_cases = Storage("Test Cases\nVariables & Assertions")

    with Cluster("Core Engine", graph_attr={"bgcolor": "#F3E5F5"}):
        loader = Javascript("Config Loader")
        test_gen = Javascript("Test Generator")
        executor = Javascript("Parallel Executor")
        cache = Storage("Cache\nAvoid Redundant Calls")

    with Cluster("Provider System", graph_attr={"bgcolor": "#FFF3E0"}):
        provider_mgr = Javascript("Provider Manager\nUnified Interface")
        
        with Cluster("LLM Providers"):
            openai = Rack("OpenAI\nGPT-3.5/4/4o")
            anthropic = Rack("Anthropic\nClaude 2/3")
            azure = Rack("Azure OpenAI")
            bedrock = Rack("AWS Bedrock")
            ollama = Rack("Ollama\nLocal Models")

    with Cluster("Assertion Framework", graph_attr={"bgcolor": "#E8F5E9"}):
        assertions = Javascript("Assertion Engine")
        
        with Cluster("Assertion Types"):
            contains = Python("contains")
            equals = Python("equals")
            regex = Python("regex")
            llm_rubric = Python("llm-rubric")
            similarity = Python("similarity")
            cost = Python("cost")
            latency = Python("latency")

    with Cluster("Red Team Module", graph_attr={"bgcolor": "#FFEBEE"}):
        redteam = Javascript("Red Team Engine")
        
        with Cluster("Attack Strategies"):
            injection = Python("Prompt Injection")
            jailbreak = Python("Jailbreaking")
            pii = Python("PII Leakage")
            harmful = Python("Harmful Content")
            bias = Python("Bias Detection")

    with Cluster("Output & Reporting", graph_attr={"bgcolor": "#E8F4F8"}):
        results = Storage("Test Results\nJSON/CSV")
        web_ui = Fastapi("Web UI\nComparison Matrix")
        cli = Javascript("CLI Output")
        risk_report = Storage("Risk Report\nSecurity Assessment")

    with Cluster("CI/CD Integration", graph_attr={"bgcolor": "#F3E5F5"}):
        github_actions = Github("GitHub Actions")
        gitlab_ci = Rack("GitLab CI")

    # Configuration flow
    user >> Edge(label="creates") >> config
    user >> Edge(label="defines") >> prompts
    user >> Edge(label="writes") >> test_cases

    # Core engine flow
    config >> Edge(label="loads") >> loader
    prompts >> Edge(label="loads") >> loader
    test_cases >> Edge(label="loads") >> loader
    
    loader >> Edge(label="generates") >> test_gen
    test_gen >> Edge(label="executes") >> executor
    executor >> Edge(label="checks") >> cache

    # Provider connections
    executor >> Edge(label="routes") >> provider_mgr
    provider_mgr >> Edge(label="OpenAI", color="blue") >> openai
    provider_mgr >> Edge(label="Anthropic", color="purple") >> anthropic
    provider_mgr >> Edge(label="Azure", color="cyan") >> azure
    provider_mgr >> Edge(label="Bedrock", color="orange") >> bedrock
    provider_mgr >> Edge(label="Local", color="green") >> ollama

    # Assertion flow
    executor >> Edge(label="validates") >> assertions
    assertions >> Edge(label="uses") >> contains
    assertions >> Edge(label="uses") >> equals
    assertions >> Edge(label="uses") >> regex
    assertions >> Edge(label="uses") >> llm_rubric
    assertions >> Edge(label="uses") >> similarity
    assertions >> Edge(label="uses") >> cost
    assertions >> Edge(label="uses") >> latency

    # Red team flow
    executor >> Edge(label="security scan", style="dashed", color="red") >> redteam
    redteam >> Edge(label="tests") >> injection
    redteam >> Edge(label="tests") >> jailbreak
    redteam >> Edge(label="tests") >> pii
    redteam >> Edge(label="tests") >> harmful
    redteam >> Edge(label="tests") >> bias

    # Output flow
    assertions >> Edge(label="results") >> results
    redteam >> Edge(label="findings", color="red") >> risk_report
    
    results >> Edge(label="displays") >> web_ui
    results >> Edge(label="prints") >> cli
    
    web_ui >> Edge(label="views") >> user
    cli >> Edge(label="views") >> user
    risk_report >> Edge(label="reviews") >> user

    # CI/CD integration
    results >> Edge(label="integrates", style="dashed") >> github_actions
    results >> Edge(label="integrates", style="dashed") >> gitlab_ci

print("✓ PNG and DOT files generated")

# Convert to Draw.io
try:
    subprocess.run([
        "graphviz2drawio",
        "diagrams/EVAL/Promptfoo/promptfoo_architecture.dot",
        "-o",
        "diagrams/EVAL/Promptfoo/promptfoo_architecture.drawio"
    ], check=True)
    print("✓ Draw.io file generated")
except:
    print("✗ graphviz2drawio not found (optional)")

print("\n" + "="*70)
print("PROMPTFOO ARCHITECTURE SUMMARY")
print("="*70)
print("\nCore Purpose:")
print("  Local-first LLM testing and security scanning framework")
print("\nKey Components:")
print("  1. Configuration System: YAML/JSON-based test definitions")
print("  2. Provider System: Unified interface for all LLM providers")
print("  3. Assertion Framework: 7+ assertion types for validation")
print("  4. Red Team Module: Security vulnerability scanning")
print("  5. Parallel Executor: Fast test execution with caching")
print("\nSupported Providers:")
print("  • OpenAI: GPT-3.5, GPT-4, GPT-4o")
print("  • Anthropic: Claude 2, Claude 3 family")
print("  • Azure OpenAI: Enterprise deployments")
print("  • AWS Bedrock: Claude, Llama, Titan")
print("  • Ollama: Local models")
print("\nAssertion Types:")
print("  • contains: Substring matching")
print("  • equals: Exact matching")
print("  • regex: Pattern matching")
print("  • llm-rubric: LLM-as-judge")
print("  • similarity: Semantic similarity")
print("  • cost: Budget constraints")
print("  • latency: Performance checks")
print("\nRed Team Capabilities:")
print("  • Prompt Injection: Direct and indirect attacks")
print("  • Jailbreaking: Safety bypass attempts")
print("  • PII Leakage: Data exposure tests")
print("  • Harmful Content: Content filter testing")
print("  • Bias Detection: Fairness evaluation")
print("\nKey Features:")
print("  • 100% Local: Runs on your machine, prompts stay private")
print("  • Fast: Parallel execution with intelligent caching")
print("  • CI/CD Ready: GitHub Actions, GitLab CI integration")
print("  • Developer-Friendly: Simple YAML configuration")
print("\nWorkflow:")
print("  1. Define tests in YAML configuration")
print("  2. Specify prompts and providers")
print("  3. Run evaluation (local execution)")
print("  4. View results in web UI or CLI")
print("  5. Generate security risk reports")
print("\nUse Cases:")
print("  • Prompt engineering and optimization")
print("  • Model comparison and selection")
print("  • Security testing and red teaming")
print("  • Regression testing in CI/CD")
print("  • Performance and cost optimization")
print("="*70)

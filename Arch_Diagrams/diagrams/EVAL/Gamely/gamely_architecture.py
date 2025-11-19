"""
GamELY Architecture Diagram
LLM Evaluation Framework - Workflow and Component Architecture

GamELY is a Python framework for evaluating language model outputs using
LLMs as judges. It supports OpenAI, Anthropic, and DeepSeek models.

Generates PNG, DOT, and Draw.io format diagrams
"""

import subprocess
from diagrams import Diagram, Cluster, Edge
from diagrams.programming.language import Python
from diagrams.onprem.client import Users
from diagrams.custom import Custom
from diagrams.programming.framework import Fastapi
from diagrams.generic.storage import Storage
from diagrams.generic.database import SQL
from diagrams.generic.compute import Rack
import os

# Download or create simple icons for LLM providers
# For this demo, we'll use generic icons with labels

# Graph attributes for clean layout
graph_attr = {
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.2",
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "compound": "true"
}

# Cluster attributes
input_cluster_attr = {
    "fontsize": "13",
    "bgcolor": "#E3F2FD",
    "style": "rounded",
    "margin": "15"
}

core_cluster_attr = {
    "fontsize": "13",
    "bgcolor": "#F3E5F5",
    "style": "rounded",
    "margin": "20"
}

provider_cluster_attr = {
    "fontsize": "13",
    "bgcolor": "#FFF3E0",
    "style": "rounded",
    "margin": "15"
}

evaluation_cluster_attr = {
    "fontsize": "13",
    "bgcolor": "#E8F5E9",
    "style": "rounded",
    "margin": "15"
}

output_cluster_attr = {
    "fontsize": "13",
    "bgcolor": "#E8F4F8",
    "style": "rounded",
    "margin": "15"
}

# Create the diagram
with Diagram(
    "GamELY - LLM Evaluation Framework Architecture",
    filename="diagrams/EVAL/Gamely/gamely_architecture",
    outformat=["png", "dot"],
    show=False,
    direction="TB",
    graph_attr=graph_attr
):

    # User/Input Layer
    user = Users("User/Developer")

    with Cluster("Input Data", graph_attr=input_cluster_attr):
        dataframe = Storage("pandas DataFrame\n(reference + generated)")
        model_selection = Python("Model Name\n(GPT-4, Claude, etc.)")
        api_key = Storage("API Key")
        criteria_input = Storage("Evaluation Criteria\n(Optional)")

    # Core GamELY Components
    with Cluster("GamELY Core", graph_attr=core_cluster_attr):
        main_function = Fastapi("evaluate_responses()\nMain Entry Point")

        with Cluster("GamELY Class"):
            gamely_instance = Python("GamELY\nEvaluator Instance")
            validate_key = Python("validate_api_key()\nAuthentication")
            setup_client = Python("_setup_client()\nInitialize API Client")

        with Cluster("Provider Mapping"):
            provider_mapper = Python("get_provider()\nModel → Provider")
            model_map = Storage("MODEL_PROVIDER_MAP\n23 Supported Models")

    # Provider APIs
    with Cluster("LLM Provider APIs", graph_attr=provider_cluster_attr):
        openai_api = Rack("OpenAI API\nGPT-3.5/4/4o/o1")
        anthropic_api = Rack("Anthropic API\nClaude 2/3 Family")
        deepseek_api = Rack("DeepSeek API\nChat/Reasoner")

    # Evaluation Process
    with Cluster("Evaluation Pipeline", graph_attr=evaluation_cluster_attr):
        batch_eval = Python("evaluate_batch()\nBatch Processing")

        with Cluster("Per-Response Evaluation"):
            evaluate_single = Python("_evaluate_single()\nSingle Pair")
            build_prompt = Python("_build_prompt()\nConstruct Prompt")
            call_provider = Python("_call_provider()\nAPI Call")
            parse_response = Python("_parse_response()\nExtract Score")

        default_criteria = Storage("DEFAULT_CRITERIA\n17 Built-in:\n• Accuracy\n• Comprehension\n• Reasoning\n• Helpfulness\n• Coverage\n• Fluency\n• Grammar\n• Organization\n• Bias Detection\n• Toxicity\n• Privacy\n• Hallucination\n• etc.")

    # Output Layer
    with Cluster("Output Results", graph_attr=output_cluster_attr):
        results_df = Storage("pandas DataFrame\nwith Scores")
        scoring = Storage("Scoring System\n1 = Strongly Disagree\n2 = Disagree\n3 = Neutral\n4 = Agree\n5 = Strongly Agree\nNaN = Irrelevant")

    # Connection flows - Input to Core
    user >> Edge(label="provides") >> dataframe
    user >> Edge(label="selects") >> model_selection
    user >> Edge(label="supplies") >> api_key
    user >> Edge(label="defines (optional)") >> criteria_input

    # Core initialization flow
    dataframe >> Edge(label="input") >> main_function
    model_selection >> Edge(label="model") >> main_function
    api_key >> Edge(label="auth") >> main_function
    criteria_input >> Edge(label="custom criteria", style="dashed") >> main_function

    main_function >> Edge(label="creates") >> gamely_instance

    # GamELY internal flow
    model_selection >> Edge(label="lookup") >> provider_mapper
    provider_mapper >> Edge(label="uses") >> model_map
    provider_mapper >> Edge(label="returns provider") >> gamely_instance

    gamely_instance >> Edge(label="validates") >> validate_key
    validate_key >> Edge(label="checks") >> openai_api
    validate_key >> Edge(label="checks") >> anthropic_api
    validate_key >> Edge(label="checks") >> deepseek_api

    validate_key >> Edge(label="if valid") >> setup_client

    # Provider selection
    setup_client >> Edge(label="OpenAI client", color="blue") >> openai_api
    setup_client >> Edge(label="Anthropic client", color="purple") >> anthropic_api
    setup_client >> Edge(label="DeepSeek client", color="orange") >> deepseek_api

    # Evaluation pipeline
    gamely_instance >> Edge(label="starts") >> batch_eval
    default_criteria >> Edge(label="uses if no custom", style="dashed") >> batch_eval

    batch_eval >> Edge(label="for each row") >> evaluate_single
    evaluate_single >> Edge(label="1. build") >> build_prompt
    build_prompt >> Edge(label="2. call") >> call_provider

    # API calls (one of three)
    call_provider >> Edge(label="query", color="blue", style="dashed") >> openai_api
    call_provider >> Edge(label="query", color="purple", style="dashed") >> anthropic_api
    call_provider >> Edge(label="query", color="orange", style="dashed") >> deepseek_api

    openai_api >> Edge(label="response", color="blue", style="dashed") >> parse_response
    anthropic_api >> Edge(label="response", color="purple", style="dashed") >> parse_response
    deepseek_api >> Edge(label="response", color="orange", style="dashed") >> parse_response

    parse_response >> Edge(label="score") >> batch_eval

    # Output
    batch_eval >> Edge(label="compiled results") >> results_df
    scoring >> Edge(label="interprets", style="dotted") >> results_df
    results_df >> Edge(label="returns") >> user

print("✓ PNG and DOT files generated in diagrams/")

# Convert DOT to Draw.io format
try:
    subprocess.run([
        "graphviz2drawio",
        "diagrams/EVAL/Gamely/gamely_architecture.dot",
        "-o",
        "diagrams/EVAL/Gamely/gamely_architecture.drawio"
    ], check=True)
    print("✓ Draw.io file generated: diagrams/EVAL/Gamely/gamely_architecture.drawio")
except subprocess.CalledProcessError as e:
    print(f"✗ Failed to convert to Draw.io format: {e}")
except FileNotFoundError:
    print("✗ graphviz2drawio not found. Install with: pip install graphviz2drawio")

print("\n" + "="*70)
print("GamELY FRAMEWORK ARCHITECTURE SUMMARY")
print("="*70)
print("\nOverview:")
print("  GamELY is a Python framework for evaluating LLM outputs using")
print("  other LLMs as judges. It provides automated scoring across")
print("  17 built-in criteria or custom evaluation metrics.")
print("\nSupported LLM Providers:")
print("  • OpenAI: GPT-3.5-turbo, GPT-4 variants, GPT-4o, O1 models")
print("  • Anthropic: Claude 2, Claude 3 family (Haiku, Sonnet, Opus)")
print("  • DeepSeek: Chat and Reasoner models")
print("\nCore Components:")
print("  1. Provider Mapper: Automatically detects provider from model name")
print("  2. API Key Validator: Authenticates against provider APIs")
print("  3. Client Setup: Initializes appropriate API client")
print("  4. Batch Evaluator: Processes DataFrames efficiently")
print("\nEvaluation Pipeline:")
print("  Input → Build Prompt → Call LLM Judge → Parse Response → Score")
print("\nDefault Evaluation Criteria (17):")
print("  • Accuracy & Correctness")
print("  • Comprehension & Reasoning")
print("  • Helpfulness & Coverage")
print("  • Fluency, Grammar & Organization")
print("  • Bias, Toxicity & Privacy Detection")
print("  • Hallucination Identification")
print("  • Human vs AI Comparison")
print("\nScoring System:")
print("  1 = Strongly Disagree")
print("  2 = Disagree")
print("  3 = Neutral")
print("  4 = Agree")
print("  5 = Strongly Agree")
print("  NaN = Criterion is irrelevant/not applicable")
print("\nInput Format:")
print("  pandas DataFrame with 2 columns:")
print("    - Column 1: Reference text (human/gold standard)")
print("    - Column 2: Generated text (LLM output to evaluate)")
print("\nOutput Format:")
print("  Original DataFrame + additional columns for each criterion")
print("  Each criterion column contains numerical scores (1-5 or NaN)")
print("\nUsage Example:")
print("  import GamELY")
print("  df = pd.DataFrame({'ref': [...], 'gen': [...]})")
print("  results = GamELY.evaluate_responses(")
print("      dataframe=df,")
print("      model_name='gpt-4',")
print("      api_key='sk-...'")
print("  )")
print("\nGenerated files:")
print("  - diagrams/EVAL/Gamely/gamely_architecture.png")
print("  - diagrams/EVAL/Gamely/gamely_architecture.dot")
print("  - diagrams/EVAL/Gamely/gamely_architecture.drawio")
print("="*70)

"""
DeepEval Architecture Diagram
LLM Evaluation Framework - Pytest-Style Testing Architecture

DeepEval is a simple-to-use evaluation framework for LLM applications,
providing pytest-style testing with 14+ research-backed metrics.

Generates PNG, DOT, and Draw.io format diagrams
"""

import subprocess
from diagrams import Diagram, Cluster, Edge
from diagrams.programming.language import Python
from diagrams.onprem.client import Users
from diagrams.generic.storage import Storage
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
    "DeepEval - LLM Evaluation Framework Architecture",
    filename="diagrams/EVAL/DeepEval/deepeval_architecture",
    outformat=["png", "dot"],
    show=False,
    direction="TB",
    graph_attr=graph_attr
):

    user = Users("Developer")

    with Cluster("Test Definition", graph_attr={"bgcolor": "#E3F2FD"}):
        test_file = Python("test_llm.py\n@deepeval.pytest_mark")
        test_case = Storage("LLMTestCase\ninput, output, context")
        conv_test = Storage("ConversationalTestCase\nMulti-turn")

    with Cluster("Core Framework", graph_attr={"bgcolor": "#F3E5F5"}):
        pytest_runner = Python("Pytest Runner\ndeepeval test run")
        assert_test = Python("assert_test()\nValidation")
        evaluate = Python("evaluate()\nBatch Processing")
        dataset = Storage("EvaluationDataset\nTest Collections")

    with Cluster("Metric System", graph_attr={"bgcolor": "#E8F5E9"}):
        base_metric = Python("BaseMetric\nAbstract Class")
        
        with Cluster("RAG Metrics"):
            answer_rel = Python("AnswerRelevancy")
            faithfulness = Python("Faithfulness")
            ctx_recall = Python("ContextualRecall")
            ctx_precision = Python("ContextualPrecision")
            ragas = Python("RAGAS")

        with Cluster("Agentic Metrics"):
            task_comp = Python("TaskCompletion")
            tool_correct = Python("ToolCorrectness")

        with Cluster("General Metrics"):
            geval = Python("G-Eval\nCustomizable")
            hallucination = Python("Hallucination")
            summarization = Python("Summarization")
            bias = Python("Bias")
            toxicity = Python("Toxicity")

        with Cluster("Conversational"):
            knowledge = Python("KnowledgeRetention")
            completeness = Python("ConvCompleteness")
            relevancy = Python("ConvRelevancy")

    with Cluster("Evaluation Engine", graph_attr={"bgcolor": "#FFF3E0"}):
        measure = Python("measure()\nScore Calculation")
        parallel = Python("Parallel Execution")
        cache_sys = Storage("Caching System")

    with Cluster("LLM Integration", graph_attr={"bgcolor": "#F3E5F5"}):
        llm_judge = Rack("LLM-as-Judge\nOpenAI/Anthropic")
        local_models = Rack("Local NLP Models\nToxicity/Bias")

    with Cluster("Synthetic Data", graph_attr={"bgcolor": "#E8F4F8"}):
        synthesizer = Python("Synthesizer")
        goldens = Storage("Golden Dataset\nGenerated Test Cases")

    with Cluster("Custom Metrics", graph_attr={"bgcolor": "#FFF3E0"}):
        custom = Python("CustomMetric\nUser-Defined")

    with Cluster("Output & Platform", graph_attr={"bgcolor": "#E8F4F8"}):
        results = Storage("Test Results\nPass/Fail + Scores")
        confident_ai = Fastapi("Confident AI\nCloud Platform")
        reports = Storage("Reports\nComparison & Tracking")

    # Test definition flow
    user >> Edge(label="writes") >> test_file
    test_file >> Edge(label="creates") >> test_case
    test_file >> Edge(label="creates") >> conv_test

    # Core framework flow
    test_file >> Edge(label="runs") >> pytest_runner
    pytest_runner >> Edge(label="validates") >> assert_test
    test_case >> Edge(label="input") >> assert_test
    conv_test >> Edge(label="input") >> assert_test

    # Dataset flow
    test_case >> Edge(label="collects") >> dataset
    dataset >> Edge(label="batch eval") >> evaluate

    # Metric selection
    assert_test >> Edge(label="uses") >> base_metric
    evaluate >> Edge(label="uses") >> base_metric

    # RAG metrics
    base_metric >> Edge(label="implements") >> answer_rel
    base_metric >> Edge(label="implements") >> faithfulness
    base_metric >> Edge(label="implements") >> ctx_recall
    base_metric >> Edge(label="implements") >> ctx_precision
    base_metric >> Edge(label="implements") >> ragas

    # Agentic metrics
    base_metric >> Edge(label="implements") >> task_comp
    base_metric >> Edge(label="implements") >> tool_correct

    # General metrics
    base_metric >> Edge(label="implements") >> geval
    base_metric >> Edge(label="implements") >> hallucination
    base_metric >> Edge(label="implements") >> summarization
    base_metric >> Edge(label="implements") >> bias
    base_metric >> Edge(label="implements") >> toxicity

    # Conversational metrics
    base_metric >> Edge(label="implements") >> knowledge
    base_metric >> Edge(label="implements") >> completeness
    base_metric >> Edge(label="implements") >> relevancy

    # Custom metrics
    base_metric >> Edge(label="extends") >> custom

    # Evaluation engine
    answer_rel >> Edge(label="calculates") >> measure
    faithfulness >> Edge(label="calculates") >> measure
    geval >> Edge(label="calculates") >> measure
    custom >> Edge(label="calculates") >> measure

    measure >> Edge(label="executes") >> parallel
    parallel >> Edge(label="uses") >> cache_sys

    # LLM integration
    measure >> Edge(label="LLM metrics", color="blue") >> llm_judge
    measure >> Edge(label="local metrics", color="green") >> local_models

    # Synthetic data
    user >> Edge(label="generates", style="dashed") >> synthesizer
    synthesizer >> Edge(label="creates") >> goldens
    goldens >> Edge(label="feeds") >> dataset

    # Output
    measure >> Edge(label="results") >> results
    results >> Edge(label="displays") >> user
    results >> Edge(label="uploads", style="dashed") >> confident_ai
    confident_ai >> Edge(label="generates") >> reports
    reports >> Edge(label="views") >> user

print("✓ PNG and DOT files generated")

# Convert to Draw.io
try:
    subprocess.run([
        "graphviz2drawio",
        "diagrams/EVAL/DeepEval/deepeval_architecture.dot",
        "-o",
        "diagrams/EVAL/DeepEval/deepeval_architecture.drawio"
    ], check=True)
    print("✓ Draw.io file generated")
except:
    print("✗ graphviz2drawio not found (optional)")

print("\n" + "="*70)
print("DEEPEVAL ARCHITECTURE SUMMARY")
print("="*70)
print("\nCore Purpose:")
print("  Pytest-style unit testing framework for LLM applications")
print("\nKey Components:")
print("  1. Test Definition: Pytest-compatible test cases")
print("  2. Metric System: 14+ research-backed metrics")
print("  3. Evaluation Engine: Parallel execution with caching")
print("  4. Synthetic Data: Automated test case generation")
print("  5. Confident AI: Cloud platform for tracking")
print("\nMetric Categories:")
print("  • RAG Metrics (5): Answer relevancy, faithfulness, recall, precision, RAGAS")
print("  • Agentic Metrics (2): Task completion, tool correctness")
print("  • General Metrics (5): G-Eval, hallucination, summarization, bias, toxicity")
print("  • Conversational (3): Knowledge retention, completeness, relevancy")
print("\nTest Case Types:")
print("  • LLMTestCase: Single-turn evaluation")
print("  • ConversationalTestCase: Multi-turn conversations")
print("  • EvaluationDataset: Batch test collections")
print("\nEvaluation Methods:")
print("  • LLM-as-Judge: Uses OpenAI/Anthropic for evaluation")
print("  • Local Models: NLP models for toxicity/bias (runs locally)")
print("  • Custom Metrics: User-defined evaluation logic")
print("\nKey Features:")
print("  • Pytest Integration: Familiar testing interface")
print("  • 14+ Metrics: Research-backed evaluation criteria")
print("  • Synthetic Data: Generate test cases automatically")
print("  • Custom Metrics: Extend with domain-specific logic")
print("  • Parallel Execution: Fast batch processing")
print("  • Caching: Avoid redundant evaluations")
print("\nWorkflow:")
print("  1. Write test cases using @deepeval.pytest_mark")
print("  2. Create LLMTestCase with input/output/context")
print("  3. Select metrics (built-in or custom)")
print("  4. Run: deepeval test run")
print("  5. View results (pass/fail + scores)")
print("  6. Upload to Confident AI (optional)")
print("\nUse Cases:")
print("  • Unit testing LLM outputs")
print("  • RAG pipeline evaluation")
print("  • Agent behavior testing")
print("  • Regression testing in CI/CD")
print("  • Synthetic data generation")
print("  • Custom metric development")
print("="*70)

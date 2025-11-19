"""
CleanLab Architecture Diagram
Data-Centric AI for ML Quality - Component Architecture

CleanLab automatically detects data quality issues including label errors,
outliers, duplicates, and other problems in ML datasets.

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
    "CleanLab - Data Quality & Label Cleaning Architecture",
    filename="diagrams/EVAL/CleanLab/cleanlab_architecture",
    outformat=["png", "dot"],
    show=False,
    direction="TB",
    graph_attr=graph_attr
):

    user = Users("Data Scientist")

    with Cluster("Input Data"):
        dataset = Storage("Dataset\n(Text/Image/Audio/Tabular)")
        labels = Storage("Labels\n(potentially noisy)")
        model = Rack("ML Model\n(Any Framework)")

    with Cluster("Model Outputs"):
        predictions = Storage("Predictions\n(pred_probs)")
        features = Storage("Features\n(embeddings)")

    with Cluster("CleanLab Core"):
        with Cluster("Datalab - Main Interface"):
            datalab = Python("Datalab\nComprehensive Analysis")
            find_issues = Python("find_issues()\nDetect All Problems")
            report_gen = Python("report()\nGenerate Report")

        with Cluster("CleanLearning - Robust Training"):
            clean_learning = Python("CleanLearning\nWrapper Class")
            auto_clean = Python("Auto Clean\nDuring Training")

        with Cluster("Core Algorithms"):
            filter_mod = Python("Filter Module\nLabel Error Detection")
            rank_mod = Python("Rank Module\nPrioritize Issues")
            count_mod = Python("Count Module\nEstimate Noise")
            confident_learning = Python("Confident Learning\nCore Algorithm")

    with Cluster("Issue Detection"):
        label_errors = Storage("Label Errors\nMislabeled Examples")
        outliers = Storage("Outliers\nAtypical Data")
        duplicates = Storage("Near Duplicates\nSimilar Examples")
        class_imbalance = Storage("Class Imbalance\nUnderrepresented")
        ambiguous = Storage("Ambiguous\nHard to Classify")

    with Cluster("Advanced Features"):
        multiannotator = Python("Multi-Annotator\nConsensus Labels")
        ood_detection = Python("OutOfDistribution\nOutlier Detection")
        active_learning = Python("Active Learning\nSample Selection")

    with Cluster("Output"):
        cleaned_data = Storage("Cleaned Dataset")
        issue_report = Storage("Issue Report\nScores & Rankings")
        robust_model = Rack("Robust Model\nTrained on Clean Data")

    # Input flow
    user >> Edge(label="provides") >> dataset
    user >> Edge(label="provides") >> labels
    user >> Edge(label="trains") >> model

    # Model outputs
    model >> Edge(label="generates") >> predictions
    model >> Edge(label="generates") >> features

    # Datalab workflow
    dataset >> Edge(label="input") >> datalab
    labels >> Edge(label="input") >> datalab
    predictions >> Edge(label="input") >> find_issues
    features >> Edge(label="input") >> find_issues

    datalab >> Edge(label="analyzes") >> find_issues
    find_issues >> Edge(label="uses") >> confident_learning

    # Core algorithm flow
    confident_learning >> Edge(label="detects") >> filter_mod
    confident_learning >> Edge(label="ranks") >> rank_mod
    confident_learning >> Edge(label="estimates") >> count_mod

    # Issue detection
    filter_mod >> Edge(label="finds") >> label_errors
    rank_mod >> Edge(label="finds") >> outliers
    find_issues >> Edge(label="finds") >> duplicates
    find_issues >> Edge(label="finds") >> class_imbalance
    find_issues >> Edge(label="finds") >> ambiguous

    # Advanced features
    predictions >> Edge(label="input", style="dashed") >> multiannotator
    features >> Edge(label="input", style="dashed") >> ood_detection
    rank_mod >> Edge(label="suggests", style="dashed") >> active_learning

    # Report generation
    label_errors >> Edge(label="compiles") >> report_gen
    outliers >> Edge(label="compiles") >> report_gen
    duplicates >> Edge(label="compiles") >> report_gen
    class_imbalance >> Edge(label="compiles") >> report_gen
    ambiguous >> Edge(label="compiles") >> report_gen

    report_gen >> Edge(label="generates") >> issue_report

    # CleanLearning workflow
    dataset >> Edge(label="input", color="blue") >> clean_learning
    labels >> Edge(label="input", color="blue") >> clean_learning
    clean_learning >> Edge(label="identifies", color="blue") >> auto_clean
    auto_clean >> Edge(label="trains on", color="blue") >> robust_model

    # Cleaning workflow
    issue_report >> Edge(label="guides") >> cleaned_data
    cleaned_data >> Edge(label="retrains") >> robust_model

    # Output to user
    issue_report >> Edge(label="reviews") >> user
    cleaned_data >> Edge(label="uses") >> user
    robust_model >> Edge(label="deploys") >> user

print("✓ PNG and DOT files generated")

# Convert to Draw.io
try:
    subprocess.run([
        "graphviz2drawio",
        "diagrams/EVAL/CleanLab/cleanlab_architecture.dot",
        "-o",
        "diagrams/EVAL/CleanLab/cleanlab_architecture.drawio"
    ], check=True)
    print("✓ Draw.io file generated")
except:
    print("✗ graphviz2drawio not found (optional)")

print("\n" + "="*70)
print("CLEANLAB ARCHITECTURE SUMMARY")
print("="*70)
print("\nCore Purpose:")
print("  Automatically detect and fix data quality issues in ML datasets")
print("\nKey Components:")
print("  1. Datalab: Comprehensive data analysis interface")
print("  2. CleanLearning: Robust training with noisy labels")
print("  3. Confident Learning: Core algorithm for issue detection")
print("  4. Filter/Rank/Count: Low-level detection modules")
print("\nDetected Issues:")
print("  • Label Errors: Mislabeled training examples")
print("  • Outliers: Atypical or out-of-distribution data")
print("  • Near Duplicates: Similar or identical examples")
print("  • Class Imbalance: Underrepresented classes")
print("  • Ambiguous Examples: Hard-to-classify instances")
print("\nSupported Data Types:")
print("  • Text (NLP datasets)")
print("  • Images (Computer vision)")
print("  • Audio (Speech/sound)")
print("  • Tabular (Structured data)")
print("\nWorkflow:")
print("  1. Train initial model on raw dataset")
print("  2. Get model predictions and features")
print("  3. Run CleanLab analysis to detect issues")
print("  4. Review and fix identified problems")
print("  5. Retrain model on cleaned data")
print("  6. Iterate for continuous improvement")
print("\nKey Features:")
print("  • Model Agnostic: Works with any ML framework")
print("  • Multi-Modal: Text, image, audio, tabular")
print("  • Automated: Minimal manual intervention")
print("  • Research-Backed: Based on confident learning papers")
print("\nUse Cases:")
print("  • Data cleaning before model training")
print("  • Annotation quality validation")
print("  • Active learning sample selection")
print("  • Production data monitoring")
print("="*70)

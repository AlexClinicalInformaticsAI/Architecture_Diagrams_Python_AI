# CleanLab - Data-Centric AI for ML Quality

## Overview

CleanLab is an open-source Python library focused on **data quality** and **label cleaning** for machine learning. It automatically detects issues in ML datasets including label errors, outliers, duplicates, and other data quality problems using your existing models.

**Repository**: https://github.com/cleanlab/cleanlab  
**PyPI**: `pip install cleanlab`  
**License**: AGPL-3.0  
**Language**: Python 3.8+

## What is CleanLab?

CleanLab helps you build better ML models by improving your training data quality. It uses confident learning algorithms to identify problematic data points that can hurt model performance.

### Key Philosophy

**Data-Centric AI**: Instead of just improving models, improve the data they train on. CleanLab enables:
1. Train initial model on original dataset
2. Use model to diagnose data issues (via cleanlab)
3. Fix/clean the dataset
4. Retrain model on improved data
5. Iterate for continuous improvement

## Key Features

### 1. Automatic Issue Detection
- **Label Errors**: Mislabeled training examples
- **Outliers**: Atypical data points
- **Near Duplicates**: Similar or identical examples
- **Class Imbalance**: Underrepresented classes
- **Ambiguous Examples**: Hard-to-classify instances
- **Data Drift**: Distribution shifts

### 2. Multi-Modal Support
- **Text**: NLP datasets, document classification
- **Images**: Computer vision datasets
- **Audio**: Speech and sound classification
- **Tabular**: Structured data

### 3. Task Coverage
- Binary and multi-class classification
- Multi-label classification
- Token classification (NER)
- Regression
- Image segmentation
- Object detection
- Multi-annotator data

### 4. Model Agnostic
Works with ANY ML framework:
- PyTorch, TensorFlow, Keras, JAX
- Scikit-learn, XGBoost, LightGBM
- HuggingFace Transformers
- OpenAI, Anthropic APIs

## Architecture Components

### Core Modules

#### 1. Datalab
Main interface for comprehensive data analysis:
```python
from cleanlab import Datalab

lab = Datalab(data=dataset, label="label_column")
lab.find_issues(features=embeddings, pred_probs=predictions)
lab.report()  # Generates comprehensive issue report
```

**Capabilities**:
- Detects 15+ types of data issues
- Provides issue scores and rankings
- Generates visual reports
- Supports all data modalities

#### 2. CleanLearning
Robust model training with noisy labels:
```python
from cleanlab.classification import CleanLearning

cl = CleanLearning(YourClassifier())
cl.fit(X_train, y_train)  # Automatically handles label noise
predictions = cl.predict(X_test)
```

**Features**:
- Wraps any scikit-learn compatible classifier
- Automatically identifies label errors during training
- Trains on cleaned subset
- Improves model robustness

#### 3. Filter Module
Low-level label error detection:
```python
from cleanlab.filter import find_label_issues

issues = find_label_issues(
    labels=y_train,
    pred_probs=model_predictions,
    return_indices_ranked_by='self_confidence'
)
```

**Methods**:
- Confident learning algorithms
- Calibrated probability thresholds
- Multiple ranking strategies

#### 4. Rank Module
Prioritize which data to review:
```python
from cleanlab.rank import get_label_quality_scores

quality_scores = get_label_quality_scores(
    labels=y_train,
    pred_probs=pred_probs
)
```

**Scoring Methods**:
- Self-confidence scores
- Normalized margin scores
- Confidence weighted by class

#### 5. Count Module
Estimate true class distributions:
```python
from cleanlab.count import estimate_latent_py_noise_matrices

py, noise_matrix = estimate_latent_py_noise_matrices(
    labels=y_train,
    pred_probs=pred_probs
)
```

**Estimates**:
- True class prior distributions
- Noise transition matrices
- Confident joint distributions

### Advanced Features

#### Multi-Annotator Support
Handle datasets labeled by multiple annotators:
```python
from cleanlab.multiannotator import get_label_quality_multiannotator

results = get_label_quality_multiannotator(
    labels_multiannotator=annotator_labels,
    pred_probs=model_predictions
)
```

**Provides**:
- Consensus labels
- Annotator quality scores
- Per-annotator agreement metrics
- Active learning suggestions

#### Outlier Detection
Identify out-of-distribution examples:
```python
from cleanlab.outlier import OutOfDistribution

ood = OutOfDistribution()
ood_scores = ood.fit_score(features=embeddings)
```

**Detection Methods**:
- Feature-based outlier detection
- Ensemble methods
- Calibrated thresholds

## Workflow Architecture

### Standard Pipeline

```
┌─────────────────┐
│  Raw Dataset    │
│  (with issues)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Train Initial  │
│  ML Model       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Get Model      │
│  Predictions    │
│  & Features     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  CleanLab       │
│  Analysis       │
│  (Datalab)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Issue Report   │
│  - Label errors │
│  - Outliers     │
│  - Duplicates   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Clean/Fix      │
│  Dataset        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Retrain Model  │
│  (Better!)      │
└─────────────────┘
```

### CleanLearning Pipeline

```
┌─────────────────┐
│  Noisy Dataset  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  CleanLearning  │
│  Wrapper        │
└────────┬────────┘
         │
         ├──────────────────┐
         │                  │
         ▼                  ▼
┌─────────────────┐  ┌─────────────────┐
│  Cross-Val      │  │  Identify       │
│  Predictions    │  │  Label Issues   │
└────────┬────────┘  └────────┬────────┘
         │                    │
         └──────────┬─────────┘
                    │
                    ▼
         ┌─────────────────┐
         │  Train on       │
         │  Clean Subset   │
         └────────┬────────┘
                  │
                  ▼
         ┌─────────────────┐
         │  Robust Model   │
         └─────────────────┘
```

## Usage Examples

### Basic Data Quality Check

```python
import pandas as pd
from cleanlab import Datalab

# Your dataset
df = pd.DataFrame({
    'text': ['example 1', 'example 2', ...],
    'label': ['cat', 'dog', ...]
})

# Initialize Datalab
lab = Datalab(data=df, label='label')

# Get model predictions (from any model)
# features: embeddings or feature vectors
# pred_probs: predicted probabilities for each class

lab.find_issues(features=features, pred_probs=pred_probs)

# View comprehensive report
lab.report()

# Get specific issues
label_issues = lab.get_issues('label')
outliers = lab.get_issues('outlier')
duplicates = lab.get_issues('near_duplicate')
```

### Robust Training with CleanLearning

```python
from sklearn.linear_model import LogisticRegression
from cleanlab.classification import CleanLearning

# Wrap any sklearn-compatible classifier
cl = CleanLearning(
    clf=LogisticRegression(),
    find_label_issues_kwargs={'filter_by': 'confident_learning'}
)

# Fit automatically handles label noise
cl.fit(X_train, y_train)

# Get predictions
predictions = cl.predict(X_test)

# Access identified label issues
label_issues = cl.get_label_issues()
```

### Find Label Errors

```python
from cleanlab.filter import find_label_issues

# Get predicted probabilities from your model
pred_probs = model.predict_proba(X_train)

# Find label issues
issues = find_label_issues(
    labels=y_train,
    pred_probs=pred_probs,
    return_indices_ranked_by='self_confidence'
)

# Review top issues
print(f"Found {len(issues)} potential label errors")
print(f"Top 10 most likely errors: {issues[:10]}")
```

### Multi-Annotator Consensus

```python
from cleanlab.multiannotator import get_label_quality_multiannotator

# labels_multiannotator: 2D array (examples x annotators)
results = get_label_quality_multiannotator(
    labels_multiannotator=annotator_labels,
    pred_probs=model_predictions,
    return_detailed_quality=True
)

consensus_labels = results['consensus_label']
annotator_quality = results['annotator_quality']
```

## Technical Details

### Confident Learning Algorithm

CleanLab's core algorithm:

1. **Estimate Noise**: Calculate confident joint distribution
2. **Identify Issues**: Find examples with high disagreement
3. **Rank by Confidence**: Score each potential issue
4. **Prune or Relabel**: Remove or fix problematic examples

### Requirements

- Python 3.8+
- NumPy, SciPy
- scikit-learn
- pandas (for Datalab)
- datasets (for Datalab)

### Optional Dependencies

- `cleanlab[datalab]`: Full Datalab features
- `cleanlab[image]`: Image-specific features (includes cleanvision)
- `cleanlab[all]`: All optional features

## Performance Characteristics

### Scalability
- **Small datasets** (<10K): Instant analysis
- **Medium datasets** (10K-1M): Minutes to hours
- **Large datasets** (>1M): Requires batching or sampling

### Memory Usage
- Depends on feature dimensionality
- Pred_probs: O(n × num_classes)
- Features: O(n × feature_dim)

### Computational Cost
- Main cost: Getting model predictions
- CleanLab analysis: Relatively fast
- Cross-validation: Most expensive operation

## Integration Examples

### With PyTorch

```python
import torch
from cleanlab.classification import CleanLearning

class PyTorchWrapper:
    def __init__(self, model):
        self.model = model
    
    def fit(self, X, y):
        # Your PyTorch training code
        pass
    
    def predict_proba(self, X):
        self.model.eval()
        with torch.no_grad():
            return self.model(X).softmax(dim=1).numpy()

cl = CleanLearning(PyTorchWrapper(your_model))
cl.fit(X_train, y_train)
```

### With HuggingFace

```python
from transformers import AutoModelForSequenceClassification, Trainer
from cleanlab import Datalab

# Train model
model = AutoModelForSequenceClassification.from_pretrained(...)
trainer = Trainer(model=model, ...)
trainer.train()

# Get predictions
predictions = trainer.predict(dataset)
pred_probs = predictions.predictions.softmax(axis=1)

# Analyze with CleanLab
lab = Datalab(data=dataset, label='label')
lab.find_issues(pred_probs=pred_probs)
lab.report()
```

## Use Cases

### 1. Data Cleaning
- Clean training datasets before model development
- Identify mislabeled examples
- Remove duplicates and outliers

### 2. Data Validation
- Validate new data before adding to training set
- Check annotation quality
- Monitor data drift

### 3. Active Learning
- Prioritize which examples to label next
- Identify ambiguous examples needing expert review
- Optimize annotation budget

### 4. Model Debugging
- Understand why models fail on certain examples
- Identify systematic labeling errors
- Find edge cases

### 5. Production Monitoring
- Monitor incoming data quality
- Detect distribution shifts
- Flag anomalous inputs

## Comparison with Other Tools

### vs Manual Review
- **CleanLab**: Automated, scalable, objective
- **Manual**: Time-consuming, subjective, expensive

### vs Data Validation Tools
- **CleanLab**: ML-aware, finds subtle issues
- **Great Expectations**: Schema validation, basic checks

### vs Labeling Tools
- **CleanLab**: Finds errors in existing labels
- **Label Studio**: Creates new labels

## Limitations

1. **Requires Model**: Need trained model to get predictions
2. **Classification Focus**: Best for classification tasks
3. **Computational Cost**: Large datasets need significant compute
4. **Not Real-time**: Batch processing oriented

## Best Practices

1. **Use Cross-Validation**: Get out-of-sample predictions
2. **Calibrate Probabilities**: Better predictions = better detection
3. **Review Top Issues**: Don't blindly remove all flagged examples
4. **Iterate**: Clean, retrain, re-analyze
5. **Combine Methods**: Use multiple issue detection strategies

## Commercial Offering

**Cleanlab Studio**: Cloud platform with additional features
- Web UI for data analysis
- Automated data cleaning
- Team collaboration
- Enterprise support

## Resources

- **Documentation**: https://docs.cleanlab.ai/
- **GitHub**: https://github.com/cleanlab/cleanlab
- **Examples**: https://github.com/cleanlab/examples
- **Research Papers**: Multiple publications on confident learning
- **Blog**: https://cleanlab.ai/blog/

## Installation

```bash
# Basic installation
pip install cleanlab

# With Datalab features
pip install "cleanlab[datalab]"

# With image support
pip install "cleanlab[image]"

# All features
pip install "cleanlab[all]"
```

## Community

- **GitHub Stars**: 9.5K+
- **Contributors**: 50+
- **Active Development**: Regular releases
- **Research-Backed**: Multiple peer-reviewed papers

---

*Architecture diagram generated by: `python cleanlab_architecture.py`*

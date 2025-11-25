# OSCE Agentic AI System with DeepEval Integration

## Overview

This system implements a comprehensive **AI-powered OSCE (Objective Structured Clinical Examination)** platform that combines:

1. **Agentic AI Case Generation** - Multiple specialized AI agents create high-quality OSCE cases
2. **Live AI Patient Simulation** - Realistic patient interactions with real-time LLM-as-judge evaluation
3. **DeepEval Transcript Analysis** - Comprehensive post-session evaluation using 12+ metrics

## System Architecture

### Three Core Workflows

```
┌─────────────────────────────────────────────────────────────┐
│                    OSCE AGENTIC AI SYSTEM                   │
└─────────────────────────────────────────────────────────────┘

┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│   DIAGRAM 1      │      │   DIAGRAM 2      │      │   DIAGRAM 3      │
│                  │      │                  │      │                  │
│ Case Generation  │  →   │  Live Session    │  →   │   Transcript     │
│  (AI Agents)     │      │  (AI Patient)    │      │   Evaluation     │
│                  │      │                  │      │   (DeepEval)     │
└──────────────────┘      └──────────────────┘      └──────────────────┘
     ↓ DeepEval                ↓ LLM Judge              ↓ DeepEval
   Validation              Real-time Eval          Comprehensive
                                                      Analysis
```

---

## Diagram 1: Case Generation with Agentic AI

### Purpose
Generate high-quality OSCE cases using multiple specialized AI agents with automated quality validation.

### Key Components

#### AI Agents
1. **Orchestrator Agent** (Claude Opus 4)
   - Coordinates all specialized agents
   - Creates task plans
   - Manages workflow

2. **Medical Writer Agent** (Claude Sonnet 4)
   - Generates clinical scenarios
   - Creates patient histories
   - Writes case narratives

3. **Patient Persona Agent** (Claude Sonnet 4)
   - Develops character profiles
   - Defines emotional states
   - Establishes communication styles

4. **Clinical Expert Agent** (Claude Opus 4)
   - Validates medical accuracy
   - Checks differential diagnoses
   - Ensures clinical realism

5. **Rubric Builder Agent** (Claude Sonnet 4)
   - Creates assessment criteria
   - Defines scoring weights
   - Sets pass thresholds

#### DeepEval Validation Layer

Automated quality checks before human review:

| Metric | Purpose | Threshold |
|--------|---------|-----------|
| **G-Eval: Medical Accuracy** | Clinical correctness | 0.90 |
| **G-Eval: Rubric Quality** | Completeness of assessment criteria | 0.85 |
| **Bias Detection** | Identify biased content | 0.20 |
| **Internal Consistency** | Scenario ↔ Rubric alignment | Custom |

#### Workflow
1. Faculty specifies requirements (learning objectives, difficulty, domain)
2. Orchestrator creates task plan and delegates to agents
3. Agents generate content in parallel
4. Clinical expert validates medical accuracy
5. DeepEval runs automated quality checks
6. If all metrics pass → Human faculty review
7. If approved → Store in case library with metadata
8. If rejected → Feedback loop for revision

### Output
- Complete OSCE case package
- Patient persona and script
- Assessment rubric
- DeepEval validation scores
- Metadata (timestamps, versions, scores)

---

## Diagram 2: Live Session with AI Patient & LLM-as-Judge

### Purpose
Conduct realistic OSCE sessions where AI simulates a patient and evaluates student performance in real-time.

### Key Components

#### AI Patient (Claude Opus 4)
- Stays in character throughout session
- Reveals information appropriately
- Adjusts emotional state based on rapport
- Maintains consistency with case scenario
- Natural text-to-speech delivery

#### Medical Student
- Real student practicing history-taking
- Asks questions and listens to responses
- Takes notes and builds rapport
- Summarizes findings at end

#### LLM-as-Judge (Claude Sonnet 4)
Real-time evaluation of each exchange:

| Evaluation Criterion | What It Measures |
|---------------------|------------------|
| **Question Quality** | Open-ended? Appropriate? Clear? |
| **Communication** | Empathy, active listening, rapport |
| **Clinical Reasoning** | Systematic approach, relevant questions, differential thinking |

#### Recording System
Captures everything for post-session analysis:
- **Audio**: High-quality stereo recording
- **Transcript**: Real-time text with speaker labels and timestamps
- **Judge Annotations**: Running scores, flags, comments (timestamped)

#### Safety Features
- Critical issue detection (professionalism, safety concerns)
- Immediate proctor alerts
- Session can be paused/stopped if needed

#### Workflow
1. Load OSCE case and initialize AI patient + judge
2. Start recording (audio + transcript)
3. Student introduces self and begins questioning
4. AI patient responds realistically
5. LLM judge evaluates each exchange in real-time
6. Running scores updated continuously
7. Session ends after 10 minutes
8. All data compiled and queued for deep evaluation

### Output
- Full transcript with timestamps
- Audio recording
- Real-time judge annotations
- Running scores per criterion
- Session metadata
- Queued for DeepEval analysis

---

## Diagram 3: Transcript Evaluation with DeepEval

### Purpose
Comprehensive post-session analysis using DeepEval framework to evaluate against learning objectives and rubric.

### Key Components

#### Data Preparation
- Load full transcript (student questions + patient responses)
- Load assessment rubric with weights
- Load learning objectives
- Segment transcript (intro, chief complaint, HPI, ROS, summary)

#### DeepEval Metrics (12+ Metrics)

##### Communication Metrics (30% weight)
| Metric | Description | Threshold |
|--------|-------------|-----------|
| **Answer Relevancy** | Are questions relevant to case? | 0.80 |
| **G-Eval: Empathy** | Shows compassion and understanding | 0.75 |
| **G-Eval: Clarity** | Questions are clear and understandable | 0.80 |

##### Clinical Reasoning Metrics (40% weight)
| Metric | Description | Threshold |
|--------|-------------|-----------|
| **Contextual Recall** | All key information gathered? | 0.85 |
| **Contextual Precision** | Only relevant questions asked? | 0.80 |
| **G-Eval: Systematic** | Organized, methodical approach | 0.75 |

##### Professionalism Metrics (20% weight)
| Metric | Description | Threshold |
|--------|-------------|-----------|
| **Bias Detection** | Any biased language detected? | 0.20 |
| **Toxicity Check** | Inappropriate language? | 0.10 |
| **G-Eval: Professional** | Maintains appropriate boundaries | 0.85 |

##### Custom OSCE Metrics (10% weight)
| Metric | Description | Threshold |
|--------|-------------|-----------|
| **Proper Introduction** | Introduced self appropriately? | 1.0 |
| **Asked Consent** | Asked permission to proceed? | 1.0 |
| **Summarized Findings** | Summarized at end? | 0.80 |

#### Evaluation Process
1. Create DeepEval test cases for each transcript segment
2. Run all metrics in parallel
3. Aggregate scores by rubric category
4. Calculate weighted final score
5. Determine pass/fail (threshold: 70%)

#### Feedback Generation (LLM-powered)
- **Strengths**: Analyze high-scoring areas
- **Improvements**: Analyze low-scoring areas
- **Specific Examples**: Timestamped transcript excerpts
- **Learning Resources**: Videos, articles, practice cases based on weak areas

#### Continuous Improvement
- **Cohort Analysis**: Compare to peers, identify trends
- **Case Difficulty**: Calibrate based on average scores
- **Metric Reliability**: Compare LLM vs human scores
- **Model Updates**: Retrain on validated data

### Output
- Detailed evaluation report
  - Overall score (e.g., 81.5/100)
  - Metric-by-metric breakdown
  - Strengths identified
  - Areas for improvement
  - Specific timestamped examples
  - Recommended resources
- Stored in student performance database
- Uploaded to Confident AI platform
- Student and faculty notifications

---

## DeepEval Integration Points

### 1. Case Generation (Diagram 1)
**Purpose**: Validate quality before deployment

**Metrics Used**:
- G-Eval (Medical Accuracy)
- G-Eval (Rubric Quality)
- Bias Detection
- Custom Consistency Check

**Benefit**: Ensures only high-quality cases reach students

### 2. Live Session (Diagram 2)
**Purpose**: Real-time evaluation during session

**Metrics Used**:
- Question Quality (custom)
- Communication Skills (custom)
- Clinical Reasoning (custom)

**Benefit**: Immediate feedback, safety monitoring

### 3. Transcript Evaluation (Diagram 3)
**Purpose**: Comprehensive post-session analysis

**Metrics Used**: 12+ metrics across 4 categories

**Benefit**: Detailed feedback, learning recommendations, analytics

---

## Technical Stack

### AI Models
- **Claude Opus 4**: Complex reasoning (orchestrator, AI patient, clinical expert)
- **Claude Sonnet 4**: Specialized tasks (agents, judge, feedback generation)

### Evaluation Framework
- **DeepEval**: Pytest-style LLM evaluation
  - 14+ built-in metrics
  - Custom metric support
  - Parallel execution
  - Confident AI platform integration

### Data Storage
- Case library database (versioned, searchable)
- Student performance database
- Session recordings (audio + transcript)
- DeepEval results log

---

## Installation & Setup

### Prerequisites
```bash
# Python 3.9+
python --version

# Install dependencies
pip install graphviz graphviz2drawio deepeval

# Install Graphviz system package
# macOS:
brew install graphviz

# Linux:
sudo apt-get install graphviz

# Windows:
# Download from graphviz.org
```

### Generate Diagrams
```bash
# Generate all three diagrams
cd Arch_Diagrams
python generate_all_osce_diagrams.py

# Or generate individually
python osce_case_generation_agentic.py
python osce_live_session_judge.py
python osce_transcript_deepeval.py
```

### Output Files
```
Arch_Diagrams/diagrams/HospitalWorkflow/
├── osce_case_generation_agentic.png
├── osce_case_generation_agentic.svg
├── osce_case_generation_agentic.dot
├── osce_case_generation_agentic.drawio
├── osce_live_session_judge.png
├── osce_live_session_judge.svg
├── osce_live_session_judge.dot
├── osce_live_session_judge.drawio
├── osce_transcript_deepeval.png
├── osce_transcript_deepeval.svg
├── osce_transcript_deepeval.dot
└── osce_transcript_deepeval.drawio
```

---

## Use Cases

### For Medical Schools
- **Scalable OSCE Training**: Generate unlimited practice cases
- **Consistent Evaluation**: Standardized, bias-free assessment
- **24/7 Availability**: Students practice anytime
- **Cost Reduction**: Reduce need for standardized patients
- **Data-Driven Insights**: Track student progress, identify curriculum gaps

### For Students
- **Safe Practice Environment**: No judgment, unlimited retries
- **Immediate Feedback**: Know strengths/weaknesses right away
- **Personalized Learning**: Resources tailored to weak areas
- **Flexible Scheduling**: Practice on your own time
- **Realistic Simulation**: AI patients behave like real patients

### For Faculty
- **Reduced Grading Burden**: Automated evaluation with human oversight
- **Quality Assurance**: DeepEval ensures consistent standards
- **Cohort Analytics**: Identify trends, adjust curriculum
- **Case Library Management**: Searchable, versioned, validated cases
- **Continuous Improvement**: System learns from validated data

---

## Key Benefits

### 1. Agentic AI Architecture
- **Specialized Agents**: Each agent excels at specific tasks
- **Parallel Processing**: Faster case generation
- **Quality Assurance**: Multiple validation layers
- **Scalability**: Generate cases on demand

### 2. Real-time Evaluation
- **Immediate Feedback**: Students know how they're doing
- **Safety Monitoring**: Critical issues flagged instantly
- **Adaptive Difficulty**: AI patient adjusts to student level
- **Engagement**: More interactive than traditional OSCEs

### 3. DeepEval Integration
- **Research-Backed Metrics**: 14+ validated evaluation criteria
- **Custom Metrics**: OSCE-specific requirements
- **Pytest-Style Testing**: Familiar interface for developers
- **Confident AI Platform**: Cloud tracking and analytics

### 4. Continuous Improvement
- **Cohort Analysis**: Benchmark against peers
- **Case Calibration**: Adjust difficulty based on data
- **Metric Refinement**: Compare LLM vs human scores
- **Model Updates**: Retrain on validated data

---

## Future Enhancements

### Planned Features
- **Multi-modal Evaluation**: Video analysis (body language, eye contact)
- **Voice Analysis**: Tone, pacing, confidence detection
- **Multi-language Support**: Cases in multiple languages
- **VR Integration**: Immersive 3D patient environments
- **Team-based OSCEs**: Multiple students, collaborative cases
- **Longitudinal Tracking**: Track student progress over years

### Research Opportunities
- **LLM vs Human Evaluation**: Validate AI scoring accuracy
- **Bias Detection**: Ensure fair evaluation across demographics
- **Optimal Feedback**: What feedback strategies work best?
- **Case Difficulty Modeling**: Predict case difficulty accurately
- **Student Learning Patterns**: Identify effective practice strategies

---

## Ethical Considerations

### Transparency
- Students know they're interacting with AI
- Evaluation criteria clearly communicated
- Scores explained with specific examples

### Fairness
- Bias detection in cases and evaluation
- Consistent standards across all students
- Human oversight for edge cases

### Privacy
- Secure storage of recordings and transcripts
- Anonymized data for research
- Student consent for data usage

### Human Oversight
- Faculty review of AI-generated cases
- Human validation of edge case evaluations
- Ability to override AI decisions

---

## References

### DeepEval
- **Documentation**: https://deepeval.com/docs/
- **GitHub**: https://github.com/confident-ai/deepeval
- **Platform**: https://confident-ai.com

### OSCE Best Practices
- Khan, K. Z., et al. (2013). "The Objective Structured Clinical Examination (OSCE): AMEE Guide No. 81"
- Harden, R. M., & Gleeson, F. A. (1979). "Assessment of clinical competence using an objective structured clinical examination (OSCE)"

### LLM Evaluation
- Liu, Y., et al. (2023). "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment"
- Zheng, L., et al. (2023). "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"

---

## Support & Contact

### Documentation
- See `healthcareagent.md` for educational workflow diagram guidelines
- See `diagrams/EVAL/DeepEval/README.md` for DeepEval details

### Issues
- Report bugs or request features via GitHub issues
- Contact medical education team for clinical questions

---

## License

This system is designed for educational purposes in medical training. Ensure compliance with:
- HIPAA (if using real patient data)
- FERPA (student educational records)
- Institutional review board (IRB) approval for research

---

**Generated**: November 2025  
**Version**: 1.0  
**Status**: Production-ready architecture diagrams

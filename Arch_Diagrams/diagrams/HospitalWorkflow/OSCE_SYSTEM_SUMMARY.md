# OSCE Agentic AI System - Quick Reference

## 🎯 System Purpose

An end-to-end AI-powered OSCE (Objective Structured Clinical Examination) platform that:
- **Generates** high-quality clinical cases using specialized AI agents
- **Simulates** realistic patient interactions with real-time evaluation
- **Evaluates** student performance using DeepEval's comprehensive metrics

---

## 📊 Three Core Diagrams

### Diagram 1: Case Generation (Agentic AI)
**File**: `osce_case_generation_agentic.png`

**What it shows**: How multiple AI agents collaborate to create OSCE cases

**Key Agents**:
- 🎯 Orchestrator Agent - Coordinates workflow
- 🤖 Medical Writer Agent - Creates scenarios
- 🤖 Patient Persona Agent - Develops characters
- 🤖 Clinical Expert Agent - Validates accuracy
- 🤖 Rubric Builder Agent - Creates assessment criteria

**DeepEval Validation**:
- ✓ Medical Accuracy (threshold: 0.90)
- ✓ Rubric Quality (threshold: 0.85)
- ✓ Bias Detection (threshold: 0.20)
- ✓ Internal Consistency (custom)

**Output**: Production-ready OSCE case with validated rubric

---

### Diagram 2: Live Session (AI Patient + LLM Judge)
**File**: `osce_live_session_judge.png`

**What it shows**: Real-time OSCE session with AI patient and continuous evaluation

**Participants**:
- 👨‍⚕️ Medical Student (real person)
- 🤖 AI Patient (Claude Opus 4) - Realistic simulation
- ⚖️ LLM-as-Judge (Claude Sonnet 4) - Real-time evaluation

**Real-time Evaluation**:
- ❓ Question Quality - Open-ended, appropriate, clear
- 💬 Communication - Empathy, listening, rapport
- 🔍 Clinical Reasoning - Systematic, relevant, differential

**Recording**:
- 🎙️ Audio (stereo, high-quality)
- 📝 Transcript (timestamped, speaker-labeled)
- 📌 Judge Annotations (scores, flags, comments)

**Output**: Complete session data ready for deep analysis

---

### Diagram 3: Transcript Evaluation (DeepEval)
**File**: `osce_transcript_deepeval.png`

**What it shows**: Comprehensive post-session analysis using 12+ DeepEval metrics

**Evaluation Categories**:

#### 1. Communication (30% weight)
- Answer Relevancy (0.80)
- G-Eval: Empathy (0.75)
- G-Eval: Clarity (0.80)

#### 2. Clinical Reasoning (40% weight)
- Contextual Recall (0.85)
- Contextual Precision (0.80)
- G-Eval: Systematic (0.75)

#### 3. Professionalism (20% weight)
- Bias Detection (0.20)
- Toxicity Check (0.10)
- G-Eval: Professional (0.85)

#### 4. Custom OSCE (10% weight)
- Proper Introduction (1.0)
- Asked Consent (1.0)
- Summarized Findings (0.80)

**Feedback Generated**:
- 💪 Strengths identified
- 📈 Areas for improvement
- 📌 Specific timestamped examples
- 📚 Recommended learning resources

**Output**: Detailed evaluation report with actionable feedback

---

## 🔄 Complete Workflow

```
1. CASE GENERATION
   ↓
   Faculty specifies requirements
   ↓
   AI agents generate case (parallel)
   ↓
   DeepEval validates quality
   ↓
   Human faculty reviews
   ↓
   Store in case library
   
2. LIVE SESSION
   ↓
   Load case & initialize AI patient
   ↓
   Student practices history-taking
   ↓
   AI patient responds realistically
   ↓
   LLM judge evaluates in real-time
   ↓
   Record everything (audio + transcript)
   ↓
   Queue for deep evaluation
   
3. TRANSCRIPT EVALUATION
   ↓
   Load transcript & rubric
   ↓
   DeepEval runs 12+ metrics
   ↓
   Aggregate scores by category
   ↓
   Generate detailed feedback
   ↓
   Store results & notify student
   ↓
   Cohort analytics for improvement
```

---

## 🎓 Key Benefits

### For Students
- ✅ Safe practice environment (no judgment)
- ✅ Immediate feedback
- ✅ Personalized learning recommendations
- ✅ 24/7 availability
- ✅ Unlimited retries

### For Faculty
- ✅ Reduced grading burden
- ✅ Consistent evaluation standards
- ✅ Cohort analytics and insights
- ✅ Quality-assured case library
- ✅ Continuous improvement loop

### For Institutions
- ✅ Scalable OSCE training
- ✅ Cost reduction (fewer standardized patients)
- ✅ Data-driven curriculum improvements
- ✅ Research opportunities
- ✅ Competitive advantage

---

## 🛠️ Technical Stack

### AI Models
- **Claude Opus 4**: Complex reasoning (orchestrator, AI patient, clinical expert)
- **Claude Sonnet 4**: Specialized tasks (agents, judge, feedback)

### Evaluation Framework
- **DeepEval**: Pytest-style LLM evaluation
  - 14+ built-in metrics
  - Custom metric support
  - Parallel execution
  - Confident AI platform integration

### Storage
- Case library (versioned, searchable)
- Student performance database
- Session recordings (audio + transcript)
- DeepEval results log

---

## 📈 Metrics Summary

| Category | Metrics | Weight | Purpose |
|----------|---------|--------|---------|
| **Communication** | 3 metrics | 30% | Empathy, clarity, relevancy |
| **Clinical Reasoning** | 3 metrics | 40% | Systematic, thorough, precise |
| **Professionalism** | 3 metrics | 20% | Bias-free, appropriate, respectful |
| **Custom OSCE** | 3 metrics | 10% | OSCE-specific requirements |

**Total**: 12 metrics, weighted to 100%

**Pass Threshold**: 70%

---

## 🚀 Quick Start

### Generate Diagrams
```bash
# All three diagrams
python Arch_Diagrams/generate_all_osce_diagrams.py

# Individual diagrams
python Arch_Diagrams/osce_case_generation_agentic.py
python Arch_Diagrams/osce_live_session_judge.py
python Arch_Diagrams/osce_transcript_deepeval.py
```

### View Diagrams
```bash
# PNG files (for presentations)
open Arch_Diagrams/diagrams/HospitalWorkflow/osce_*.png

# SVG files (for web/scaling)
open Arch_Diagrams/diagrams/HospitalWorkflow/osce_*.svg

# Draw.io files (for editing)
open Arch_Diagrams/diagrams/HospitalWorkflow/osce_*.drawio
```

---

## 📚 Documentation

- **Comprehensive Guide**: `OSCE_AGENTIC_AI_README.md`
- **Healthcare Agent Guide**: `../healthcareagent.md`
- **DeepEval Details**: `../EVAL/DeepEval/README.md`

---

## 🔍 DeepEval Integration Points

### Stage 1: Case Generation
- **When**: Before case deployment
- **Metrics**: Medical accuracy, rubric quality, bias, consistency
- **Purpose**: Quality assurance

### Stage 2: Live Session
- **When**: During student-patient interaction
- **Metrics**: Question quality, communication, clinical reasoning
- **Purpose**: Real-time monitoring and safety

### Stage 3: Transcript Evaluation
- **When**: After session completion
- **Metrics**: 12+ comprehensive metrics
- **Purpose**: Detailed feedback and learning

---

## 📊 Sample Evaluation Report

```
OSCE Session Evaluation Report
Student: [Student ID]
Case: Chest Pain - Acute Coronary Syndrome
Date: 2025-11-19
Duration: 10:00 minutes

OVERALL SCORE: 81.5/100 ✅ PASS

Category Breakdown:
├─ Communication (30%): 8.2/10 ⭐⭐⭐⭐
│  ├─ Answer Relevancy: 0.85 ✓
│  ├─ Empathy: 0.82 ✓
│  └─ Clarity: 0.79 ⚠️
│
├─ Clinical Reasoning (40%): 7.5/10 ⭐⭐⭐⭐
│  ├─ Contextual Recall: 0.88 ✓
│  ├─ Contextual Precision: 0.75 ✓
│  └─ Systematic Approach: 0.68 ⚠️
│
├─ Professionalism (20%): 9.1/10 ⭐⭐⭐⭐⭐
│  ├─ Bias: 0.05 ✓
│  ├─ Toxicity: 0.02 ✓
│  └─ Professional Boundaries: 0.92 ✓
│
└─ Custom OSCE (10%): 8.7/10 ⭐⭐⭐⭐
   ├─ Introduction: 1.0 ✓
   ├─ Consent: 1.0 ✓
   └─ Summary: 0.85 ✓

STRENGTHS:
✓ Excellent empathy and rapport building
✓ Thorough information gathering
✓ Professional demeanor throughout

AREAS FOR IMPROVEMENT:
⚠️ Ask more open-ended questions
⚠️ Use more systematic approach (e.g., OPQRST)
⚠️ Clarify ambiguous responses

SPECIFIC EXAMPLES:
📌 [3:45] Good: "Tell me more about the pain"
📌 [5:12] Improve: Interrupted patient mid-sentence
📌 [8:30] Excellent: Summarized findings clearly

RECOMMENDED RESOURCES:
📚 Video: "Open-ended Questioning Techniques"
📚 Article: "Systematic History Taking: OPQRST"
📚 Practice Case: "Chest Pain - Intermediate"
```

---

## 🎯 Success Metrics

### System Performance
- Case generation time: < 5 minutes
- Session evaluation time: < 2 minutes
- Transcript analysis time: < 3 minutes
- Total turnaround: < 10 minutes

### Quality Metrics
- Case medical accuracy: > 95%
- LLM-human score correlation: > 0.85
- Student satisfaction: > 4.5/5
- Faculty satisfaction: > 4.3/5

### Usage Metrics
- Cases generated per month: 100+
- Sessions conducted per month: 500+
- Student practice hours: 1000+
- Cost savings vs traditional: 60%

---

## 🔐 Ethical Considerations

### Transparency
- ✓ Students know they're interacting with AI
- ✓ Evaluation criteria clearly communicated
- ✓ Scores explained with specific examples

### Fairness
- ✓ Bias detection in cases and evaluation
- ✓ Consistent standards across all students
- ✓ Human oversight for edge cases

### Privacy
- ✓ Secure storage of recordings
- ✓ Anonymized data for research
- ✓ Student consent required

---

## 📞 Support

### Questions?
- Technical: See documentation files
- Clinical: Contact medical education team
- Research: IRB approval required

### Issues?
- Report bugs via GitHub issues
- Request features via feedback form

---

**System Version**: 1.0  
**Last Updated**: November 2025  
**Status**: Production-ready architecture diagrams  
**License**: Educational use only

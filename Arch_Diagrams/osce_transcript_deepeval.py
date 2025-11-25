"""
OSCE Transcript Evaluation with DeepEval
Diagram 3 of 3: Post-Session Deep Analysis Using DeepEval Framework

This diagram shows comprehensive post-session evaluation:
- DeepEval analyzes full transcript against learning objectives
- Multiple evaluation metrics applied
- Detailed feedback generated for each rubric criterion
- Results stored for student review and faculty analytics
"""

from graphviz import Digraph
import os
import subprocess

def create_osce_transcript_evaluation():
    """Generate OSCE transcript evaluation workflow with DeepEval"""
    
    dot = Digraph(comment='OSCE Transcript Evaluation with DeepEval')
    dot.attr(
        rankdir='TB',
        splines='ortho',
        nodesep='0.8',
        ranksep='0.8',
        fontname='Arial',
        fontsize='12',
        bgcolor='white'
    )
    dot.attr('node', fontname='Arial', fontsize='10')
    dot.attr('edge', fontname='Arial', fontsize='9')
    
    counter = [0]
    
    def node_id():
        counter[0] += 1
        return f'n{counter[0]}'
    
    # ===== START =====
    start = node_id()
    dot.node(start, 'START\nTranscript Ready\nfor Evaluation', 
             shape='ellipse', style='filled', fillcolor='lightgreen', penwidth='2')
    
    # ===== SWIMLANE 1: DATA PREPARATION =====
    with dot.subgraph(name='cluster_prep') as c:
        c.attr(label='Data Preparation', style='filled', 
               fillcolor='#E3F2FD', fontsize='12')
        
        load_session = node_id()
        c.node(load_session, '📥 Load Session Data\nSession ID: #67890\nStudent ID\nCase ID',
               shape='box', style='filled', fillcolor='#BBDEFB')
        
        load_transcript = node_id()
        c.node(load_transcript, '📝 Load Full Transcript\nStudent questions\nPatient responses\nTimestamps',
               shape='parallelogram', style='filled', fillcolor='#90CAF9')
        
        load_rubric = node_id()
        c.node(load_rubric, '📊 Load Assessment Rubric\n• Communication (30%)\n• Clinical reasoning (40%)\n• Professionalism (20%)\n• Data gathering (10%)',
               shape='parallelogram', style='filled', fillcolor='#64B5F6')
        
        load_objectives = node_id()
        c.node(load_objectives, '🎯 Load Learning Objectives\n1. Obtain complete history\n2. Build rapport\n3. Demonstrate empathy\n4. Systematic approach',
               shape='note', style='filled', fillcolor='#42A5F5')
        
        segment_transcript = node_id()
        c.node(segment_transcript, '✂️ Segment Transcript\nIntroduction\nChief complaint\nHistory of present illness\nReview of systems\nSummary',
               shape='box', style='filled', fillcolor='#2196F3', fontcolor='white')
    
    # ===== SWIMLANE 2: DEEPEVAL INITIALIZATION =====
    with dot.subgraph(name='cluster_deepeval_init') as c:
        c.attr(label='DeepEval Framework Setup', style='filled', 
               fillcolor='#F3E5F5', fontsize='12')
        
        init_deepeval = node_id()
        c.node(init_deepeval, '⚡ Initialize DeepEval\nimport deepeval\nfrom deepeval.metrics import *',
               shape='hexagon', style='filled', fillcolor='#E1BEE7', penwidth='2')
        
        create_test_cases = node_id()
        c.node(create_test_cases, '🧪 Create Test Cases\nLLMTestCase per segment\ninput = question\nactual_output = response\ncontext = case info',
               shape='box', style='filled', fillcolor='#CE93D8')
        
        define_metrics = node_id()
        c.node(define_metrics, '📏 Define Evaluation Metrics\n14+ DeepEval metrics\nCustom OSCE metrics',
               shape='box', style='filled', fillcolor='#BA68C8')
    
    # ===== SWIMLANE 3: DEEPEVAL METRICS (PARALLEL EVALUATION) =====
    with dot.subgraph(name='cluster_metrics') as c:
        c.attr(label='DeepEval Metrics (Parallel Execution)', style='filled', 
               fillcolor='#E8F5E9', fontsize='12')
        
        # Communication metrics
        with dot.subgraph(name='cluster_comm') as comm:
            comm.attr(label='Communication Metrics', style='filled', 
                     fillcolor='#C8E6C9')
            
            answer_relevancy = node_id()
            comm.node(answer_relevancy, '📊 Answer Relevancy\nAre questions relevant?\nThreshold: 0.80',
                     shape='box', style='filled', fillcolor='#A5D6A7')
            
            geval_empathy = node_id()
            comm.node(geval_empathy, '📊 G-Eval: Empathy\nCriteria: Shows compassion\nThreshold: 0.75',
                     shape='box', style='filled', fillcolor='#A5D6A7')
            
            geval_clarity = node_id()
            comm.node(geval_clarity, '📊 G-Eval: Clarity\nCriteria: Clear questions\nThreshold: 0.80',
                     shape='box', style='filled', fillcolor='#A5D6A7')
        
        # Clinical reasoning metrics
        with dot.subgraph(name='cluster_clinical') as clin:
            clin.attr(label='Clinical Reasoning Metrics', style='filled', 
                     fillcolor='#BBDEFB')
            
            contextual_recall = node_id()
            clin.node(contextual_recall, '📊 Contextual Recall\nAll key info gathered?\nThreshold: 0.85',
                     shape='box', style='filled', fillcolor='#90CAF9')
            
            contextual_precision = node_id()
            clin.node(contextual_precision, '📊 Contextual Precision\nRelevant questions only?\nThreshold: 0.80',
                     shape='box', style='filled', fillcolor='#90CAF9')
            
            geval_systematic = node_id()
            clin.node(geval_systematic, '📊 G-Eval: Systematic\nCriteria: Organized approach\nThreshold: 0.75',
                     shape='box', style='filled', fillcolor='#90CAF9')
        
        # Professionalism metrics
        with dot.subgraph(name='cluster_prof') as prof:
            prof.attr(label='Professionalism Metrics', style='filled', 
                     fillcolor='#FFF9C4')
            
            bias_metric = node_id()
            prof.node(bias_metric, '📊 Bias Detection\nAny biased language?\nThreshold: 0.20',
                     shape='box', style='filled', fillcolor='#FFF59D')
            
            toxicity_metric = node_id()
            prof.node(toxicity_metric, '📊 Toxicity Check\nInappropriate language?\nThreshold: 0.10',
                     shape='box', style='filled', fillcolor='#FFF59D')
            
            geval_professional = node_id()
            prof.node(geval_professional, '📊 G-Eval: Professional\nCriteria: Maintains boundaries\nThreshold: 0.85',
                     shape='box', style='filled', fillcolor='#FFF59D')
        
        # Custom OSCE metrics
        with dot.subgraph(name='cluster_custom') as cust:
            cust.attr(label='Custom OSCE Metrics', style='filled', 
                     fillcolor='#FFCCBC')
            
            custom_intro = node_id()
            cust.node(custom_intro, '📊 Custom: Introduction\nProper self-introduction?\nThreshold: 1.0',
                     shape='box', style='filled', fillcolor='#FFAB91')
            
            custom_consent = node_id()
            cust.node(custom_consent, '📊 Custom: Consent\nAsked permission?\nThreshold: 1.0',
                     shape='box', style='filled', fillcolor='#FFAB91')
            
            custom_summary = node_id()
            cust.node(custom_summary, '📊 Custom: Summary\nSummarized findings?\nThreshold: 0.80',
                     shape='box', style='filled', fillcolor='#FFAB91')
    
    # ===== SWIMLANE 4: EVALUATION EXECUTION =====
    with dot.subgraph(name='cluster_execution') as c:
        c.attr(label='Evaluation Execution', style='filled', 
               fillcolor='#E0F2F1', fontsize='12')
        
        run_evaluation = node_id()
        c.node(run_evaluation, '▶️ Run DeepEval\nevaluate(test_cases, metrics)\nParallel execution',
               shape='box', style='filled', fillcolor='#B2DFDB', penwidth='2')
        
        aggregate_scores = node_id()
        c.node(aggregate_scores, '📊 Aggregate Scores\nWeighted by rubric\nCommunication: 8.2/10\nClinical: 7.5/10\nProfessional: 9.1/10',
               shape='box', style='filled', fillcolor='#80CBC4')
        
        calculate_final = node_id()
        c.node(calculate_final, '🎯 Calculate Final Score\nWeighted average\nTotal: 81.5/100',
               shape='box', style='filled', fillcolor='#4DB6AC', fontcolor='white')
        
        pass_threshold = node_id()
        c.node(pass_threshold, 'Score >= 70%\n(Pass Threshold)?',
               shape='diamond', style='filled', fillcolor='#26A69A')
    
    # ===== SWIMLANE 5: FEEDBACK GENERATION =====
    with dot.subgraph(name='cluster_feedback') as c:
        c.attr(label='Feedback Generation', style='filled', 
               fillcolor='#FFF3E0', fontsize='12')
        
        generate_strengths = node_id()
        c.node(generate_strengths, '💪 Generate Strengths\nLLM analyzes high scores\n"Excellent empathy shown"\n[Claude Sonnet 4]',
               shape='box', style='filled', fillcolor='#FFE0B2', penwidth='2')
        
        generate_improvements = node_id()
        c.node(generate_improvements, '📈 Generate Improvements\nLLM analyzes low scores\n"Ask more open-ended questions"\n[Claude Sonnet 4]',
               shape='box', style='filled', fillcolor='#FFCC80', penwidth='2')
        
        specific_examples = node_id()
        c.node(specific_examples, '📌 Provide Specific Examples\nTimestamped transcript excerpts\n"At 3:45, you interrupted..."',
               shape='note', style='filled', fillcolor='#FFB74D')
        
        learning_resources = node_id()
        c.node(learning_resources, '📚 Recommend Resources\nBased on weak areas\nVideos, articles, practice cases',
               shape='note', style='filled', fillcolor='#FFA726')
        
        compile_feedback = node_id()
        c.node(compile_feedback, '📝 Compile Feedback Report\nStructured by rubric\nActionable recommendations',
               shape='box', style='filled', fillcolor='#FF9800', fontcolor='white')
    
    # ===== SWIMLANE 6: RESULTS & STORAGE =====
    with dot.subgraph(name='cluster_results') as c:
        c.attr(label='Results & Storage', style='filled', 
               fillcolor='#FFFDE7', fontsize='12')
        
        create_report = node_id()
        c.node(create_report, '📄 Create Detailed Report\n• Overall score\n• Metric breakdown\n• Strengths\n• Improvements\n• Examples\n• Resources',
               shape='note', style='filled', fillcolor='#FFF9C4')
        
        store_results = node_id()
        c.node(store_results, '💾 Store in Database\nStudent performance DB\nLinked to session',
               shape='cylinder', style='filled', fillcolor='#FFF59D')
        
        store_deepeval = node_id()
        c.node(store_deepeval, '📈 Upload to Confident AI\nDeepEval cloud platform\nTracking & analytics',
               shape='cylinder', style='filled', fillcolor='#FFF176')
        
        notify_student = node_id()
        c.node(notify_student, '📧 Notify Student\nEmail with report link\nAvailable for review',
               shape='box', style='filled', fillcolor='#FFEE58')
        
        notify_faculty = node_id()
        c.node(notify_faculty, '📧 Notify Faculty\nDashboard updated\nCohort analytics',
               shape='box', style='filled', fillcolor='#FFEB3B')
    
    # ===== SWIMLANE 7: ANALYTICS & INSIGHTS =====
    with dot.subgraph(name='cluster_analytics') as c:
        c.attr(label='Analytics & Continuous Improvement', style='filled', 
               fillcolor='#E1BEE7', fontsize='12')
        
        cohort_analysis = node_id()
        c.node(cohort_analysis, '📊 Cohort Analysis\nCompare to peers\nIdentify trends',
               shape='box', style='filled', fillcolor='#CE93D8')
        
        case_difficulty = node_id()
        c.node(case_difficulty, '📈 Case Difficulty Analysis\nAverage scores per case\nCalibrate difficulty',
               shape='box', style='filled', fillcolor='#BA68C8')
        
        metric_reliability = node_id()
        c.node(metric_reliability, '🔍 Metric Reliability Check\nCompare LLM vs human scores\nRefine thresholds',
               shape='box', style='filled', fillcolor='#AB47BC')
        
        update_models = node_id()
        c.node(update_models, '🔄 Update AI Models\nRetrain on validated data\nImprove accuracy',
               shape='box', style='filled', fillcolor='#9C27B0', fontcolor='white')
    
    # ===== END =====
    end = node_id()
    dot.node(end, 'END\nEvaluation Complete\nFeedback Delivered', 
             shape='ellipse', style='filled', fillcolor='lightcoral', penwidth='2')
    
    # ===== CONNECTIONS =====
    
    # Data preparation
    dot.edge(start, load_session)
    dot.edge(load_session, load_transcript)
    dot.edge(load_session, load_rubric)
    dot.edge(load_session, load_objectives)
    dot.edge(load_transcript, segment_transcript)
    
    # DeepEval initialization
    dot.edge(segment_transcript, init_deepeval, label='Ready', color='purple', style='bold')
    dot.edge(load_rubric, init_deepeval)
    dot.edge(load_objectives, init_deepeval)
    dot.edge(init_deepeval, create_test_cases)
    dot.edge(create_test_cases, define_metrics)
    
    # Metrics definition to execution
    dot.edge(define_metrics, answer_relevancy, label='Communication', color='green')
    dot.edge(define_metrics, geval_empathy, label='Communication', color='green')
    dot.edge(define_metrics, geval_clarity, label='Communication', color='green')
    
    dot.edge(define_metrics, contextual_recall, label='Clinical', color='blue')
    dot.edge(define_metrics, contextual_precision, label='Clinical', color='blue')
    dot.edge(define_metrics, geval_systematic, label='Clinical', color='blue')
    
    dot.edge(define_metrics, bias_metric, label='Professional', color='orange')
    dot.edge(define_metrics, toxicity_metric, label='Professional', color='orange')
    dot.edge(define_metrics, geval_professional, label='Professional', color='orange')
    
    dot.edge(define_metrics, custom_intro, label='Custom', color='red')
    dot.edge(define_metrics, custom_consent, label='Custom', color='red')
    dot.edge(define_metrics, custom_summary, label='Custom', color='red')
    
    # All metrics to evaluation
    dot.edge(answer_relevancy, run_evaluation, label='Metric', color='purple')
    dot.edge(geval_empathy, run_evaluation, label='Metric', color='purple')
    dot.edge(geval_clarity, run_evaluation, label='Metric', color='purple')
    dot.edge(contextual_recall, run_evaluation, label='Metric', color='purple')
    dot.edge(contextual_precision, run_evaluation, label='Metric', color='purple')
    dot.edge(geval_systematic, run_evaluation, label='Metric', color='purple')
    dot.edge(bias_metric, run_evaluation, label='Metric', color='purple')
    dot.edge(toxicity_metric, run_evaluation, label='Metric', color='purple')
    dot.edge(geval_professional, run_evaluation, label='Metric', color='purple')
    dot.edge(custom_intro, run_evaluation, label='Metric', color='purple')
    dot.edge(custom_consent, run_evaluation, label='Metric', color='purple')
    dot.edge(custom_summary, run_evaluation, label='Metric', color='purple')
    
    # Evaluation execution
    dot.edge(run_evaluation, aggregate_scores, label='Results', color='purple', style='bold')
    dot.edge(aggregate_scores, calculate_final)
    dot.edge(calculate_final, pass_threshold)
    
    # Feedback generation (parallel)
    dot.edge(pass_threshold, generate_strengths, label='Pass/Fail', color='green')
    dot.edge(aggregate_scores, generate_strengths, label='High scores')
    dot.edge(aggregate_scores, generate_improvements, label='Low scores')
    dot.edge(segment_transcript, specific_examples, label='Excerpts', style='dashed')
    dot.edge(generate_improvements, learning_resources)
    
    dot.edge(generate_strengths, compile_feedback)
    dot.edge(generate_improvements, compile_feedback)
    dot.edge(specific_examples, compile_feedback)
    dot.edge(learning_resources, compile_feedback)
    
    # Results and storage
    dot.edge(compile_feedback, create_report)
    dot.edge(calculate_final, create_report, label='Final score')
    dot.edge(create_report, store_results)
    dot.edge(create_report, store_deepeval, label='Upload', color='purple')
    dot.edge(store_results, notify_student)
    dot.edge(store_results, notify_faculty)
    
    # Analytics
    dot.edge(store_results, cohort_analysis, label='Aggregate', style='dashed')
    dot.edge(store_results, case_difficulty, label='Aggregate', style='dashed')
    dot.edge(store_deepeval, metric_reliability, label='Analyze', style='dashed')
    dot.edge(metric_reliability, update_models, label='Insights')
    dot.edge(update_models, init_deepeval, label='Improved models', 
             color='purple', style='dashed')
    
    # End
    dot.edge(notify_student, end)
    dot.edge(notify_faculty, end)
    
    # Save outputs
    output_dir = 'Arch_Diagrams/diagrams/HospitalWorkflow'
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, 'osce_transcript_deepeval')
    
    # Render
    dot.render(filepath, format='png', cleanup=True)
    dot.render(filepath, format='svg', cleanup=True)
    dot.save(f'{filepath}.dot')
    
    print('✅ DIAGRAM 3/3: OSCE Transcript Evaluation with DeepEval')
    print(f'   📊 {filepath}.png')
    print(f'   📊 {filepath}.svg')
    print(f'   📄 {filepath}.dot')
    
    # Convert to Draw.io
    try:
        subprocess.run([
            'graphviz2drawio',
            f'{filepath}.dot',
            '-o',
            f'{filepath}.drawio'
        ], check=True, capture_output=True)
        print(f'   ✏️  {filepath}.drawio')
    except:
        print('   ⚠️  graphviz2drawio not available (optional)')
    
    return dot


if __name__ == '__main__':
    create_osce_transcript_evaluation()
    print('\n' + '='*70)
    print('OSCE TRANSCRIPT EVALUATION WITH DEEPEVAL')
    print('='*70)
    print('\nDeepEval Metrics Applied:')
    print('\n  Communication (30%):')
    print('    • Answer Relevancy (threshold: 0.80)')
    print('    • G-Eval: Empathy (threshold: 0.75)')
    print('    • G-Eval: Clarity (threshold: 0.80)')
    print('\n  Clinical Reasoning (40%):')
    print('    • Contextual Recall (threshold: 0.85)')
    print('    • Contextual Precision (threshold: 0.80)')
    print('    • G-Eval: Systematic Approach (threshold: 0.75)')
    print('\n  Professionalism (20%):')
    print('    • Bias Detection (threshold: 0.20)')
    print('    • Toxicity Check (threshold: 0.10)')
    print('    • G-Eval: Professional Boundaries (threshold: 0.85)')
    print('\n  Custom OSCE Metrics (10%):')
    print('    • Proper Introduction (threshold: 1.0)')
    print('    • Asked Consent (threshold: 1.0)')
    print('    • Summarized Findings (threshold: 0.80)')
    print('\nWorkflow:')
    print('  1. Load session data (transcript, rubric, objectives)')
    print('  2. Segment transcript into evaluation units')
    print('  3. Initialize DeepEval with 12+ metrics')
    print('  4. Run parallel evaluation across all metrics')
    print('  5. Aggregate scores by rubric categories')
    print('  6. Calculate weighted final score')
    print('  7. Generate detailed feedback with examples')
    print('  8. Store results and notify student/faculty')
    print('  9. Perform cohort analytics for continuous improvement')
    print('\nFeedback Components:')
    print('  • Overall score and pass/fail status')
    print('  • Metric-by-metric breakdown')
    print('  • Strengths identified')
    print('  • Areas for improvement')
    print('  • Specific timestamped examples')
    print('  • Recommended learning resources')
    print('\nContinuous Improvement:')
    print('  • Cohort analysis and benchmarking')
    print('  • Case difficulty calibration')
    print('  • Metric reliability validation')
    print('  • AI model retraining on validated data')
    print('='*70)

"""
OSCE Case Generation - Agentic AI System
Diagram 1 of 3: AI-Powered OSCE Case Creation Pipeline

This diagram shows how multiple AI agents collaborate to generate
high-quality OSCE cases with integrated DeepEval validation.
"""

from graphviz import Digraph
import os
import subprocess

def create_osce_case_generation():
    """Generate OSCE case generation workflow with agentic AI"""
    
    dot = Digraph(comment='OSCE Case Generation - Agentic AI System')
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
    dot.node(start, 'START\nCase Generation Request', 
             shape='ellipse', style='filled', fillcolor='lightgreen', penwidth='2')
    
    # ===== SWIMLANE 1: INPUT SPECIFICATION =====
    with dot.subgraph(name='cluster_input') as c:
        c.attr(label='Input Specification', style='filled', 
               fillcolor='#E3F2FD', fontsize='12')
        
        spec = node_id()
        c.node(spec, 'Define Requirements:\n• Learning objectives\n• Clinical domain\n• Difficulty level\n• Patient demographics',
               shape='box', style='filled', fillcolor='#BBDEFB')
        
        rubric_req = node_id()
        c.node(rubric_req, 'Rubric Requirements:\n• Assessment criteria\n• Scoring weights\n• Pass threshold',
               shape='parallelogram', style='filled', fillcolor='#90CAF9')
    
    # ===== SWIMLANE 2: AGENT ORCHESTRATOR =====
    with dot.subgraph(name='cluster_orchestrator') as c:
        c.attr(label='Agent Orchestrator', style='filled', 
               fillcolor='#FFF3E0', fontsize='12')
        
        orchestrator = node_id()
        c.node(orchestrator, '🎯 Orchestrator Agent\nCoordinates all agents\n[Claude Opus 4]',
               shape='box', style='filled', fillcolor='#FFE0B2', penwidth='2')
        
        task_plan = node_id()
        c.node(task_plan, 'Create Task Plan:\n1. Case scenario\n2. Patient profile\n3. Rubric\n4. Validation',
               shape='note', style='filled', fillcolor='#FFCC80')
    
    # ===== SWIMLANE 3: GENERATION AGENTS =====
    with dot.subgraph(name='cluster_agents') as c:
        c.attr(label='Specialized AI Agents', style='filled', 
               fillcolor='#E8F5E9', fontsize='12')
        
        medical_writer = node_id()
        c.node(medical_writer, '🤖 Medical Writer Agent\nGenerate case scenario\nPatient history\n[Claude Sonnet 4]',
               shape='box', style='filled', fillcolor='#C8E6C9', penwidth='2')
        
        patient_persona = node_id()
        c.node(patient_persona, '🤖 Patient Persona Agent\nCreate character profile\nEmotional state\nCommunication style\n[Claude Sonnet 4]',
               shape='box', style='filled', fillcolor='#C8E6C9', penwidth='2')
        
        clinical_expert = node_id()
        c.node(clinical_expert, '🤖 Clinical Expert Agent\nValidate medical accuracy\nCheck differential diagnosis\n[Claude Opus 4]',
               shape='box', style='filled', fillcolor='#C8E6C9', penwidth='2')
        
        rubric_agent = node_id()
        c.node(rubric_agent, '🤖 Rubric Builder Agent\nCreate assessment rubric\nDefine scoring criteria\n[Claude Sonnet 4]',
               shape='box', style='filled', fillcolor='#C8E6C9', penwidth='2')
    
    # ===== SWIMLANE 4: DEEPEVAL VALIDATION =====
    with dot.subgraph(name='cluster_deepeval') as c:
        c.attr(label='DeepEval Validation Layer', style='filled', 
               fillcolor='#F3E5F5', fontsize='12')
        
        deepeval_init = node_id()
        c.node(deepeval_init, '⚡ Initialize DeepEval\nLoad evaluation metrics',
               shape='hexagon', style='filled', fillcolor='#E1BEE7')
        
        medical_accuracy = node_id()
        c.node(medical_accuracy, '✓ Medical Accuracy Check\nG-Eval: Clinical correctness\nThreshold: 0.90',
               shape='diamond', style='filled', fillcolor='#CE93D8', 
               color='purple', penwidth='2')
        
        rubric_quality = node_id()
        c.node(rubric_quality, '✓ Rubric Quality Check\nG-Eval: Completeness\nThreshold: 0.85',
               shape='diamond', style='filled', fillcolor='#CE93D8',
               color='purple', penwidth='2')
        
        bias_check = node_id()
        c.node(bias_check, '✓ Bias Detection\nDeepEval: Bias metric\nThreshold: 0.20',
               shape='diamond', style='filled', fillcolor='#CE93D8',
               color='purple', penwidth='2')
        
        consistency = node_id()
        c.node(consistency, '✓ Internal Consistency\nCustom metric:\nScenario ↔ Rubric alignment',
               shape='diamond', style='filled', fillcolor='#CE93D8',
               color='purple', penwidth='2')
    
    # ===== SWIMLANE 5: QUALITY ASSURANCE =====
    with dot.subgraph(name='cluster_qa') as c:
        c.attr(label='Human Quality Assurance', style='filled', 
               fillcolor='#FFFDE7', fontsize='12')
        
        all_pass = node_id()
        c.node(all_pass, 'All DeepEval\nMetrics Pass?',
               shape='diamond', style='filled', fillcolor='#FFF9C4')
        
        human_review = node_id()
        c.node(human_review, '👤 Faculty Review\nPhysician validation\nPedagogy check',
               shape='trapezium', style='filled', fillcolor='#FFF59D', penwidth='2')
        
        approved = node_id()
        c.node(approved, 'Approved for\nProduction?',
               shape='diamond', style='filled', fillcolor='#FFF9C4')
        
        feedback = node_id()
        c.node(feedback, '💬 Revision Feedback\nSpecific improvements needed',
               shape='note', style='filled', fillcolor='#FFEB3B')
    
    # ===== SWIMLANE 6: OUTPUT & STORAGE =====
    with dot.subgraph(name='cluster_output') as c:
        c.attr(label='Output & Storage', style='filled', 
               fillcolor='#E0F2F1', fontsize='12')
        
        case_package = node_id()
        c.node(case_package, '📦 Complete OSCE Package:\n• Case scenario\n• Patient persona\n• Assessment rubric\n• DeepEval scores',
               shape='note', style='filled', fillcolor='#B2DFDB')
        
        metadata = node_id()
        c.node(metadata, '📊 Metadata:\n• Generation timestamp\n• Agent versions\n• Validation scores\n• Review status',
               shape='parallelogram', style='filled', fillcolor='#80CBC4')
        
        case_library = node_id()
        c.node(case_library, '💾 Case Library Database\nVersioned storage\nSearchable by criteria',
               shape='cylinder', style='filled', fillcolor='#4DB6AC')
        
        deepeval_log = node_id()
        c.node(deepeval_log, '📈 DeepEval Results Log\nConfident AI Platform\nTracking & analytics',
               shape='cylinder', style='filled', fillcolor='#4DB6AC')
    
    # ===== ERROR HANDLING =====
    error_handler = node_id()
    dot.node(error_handler, '⚠️ ERROR HANDLER\nLog failure\nNotify team\nRetry with adjustments',
             shape='box', style='filled', fillcolor='#FFCDD2', 
             color='red', penwidth='2')
    
    # ===== END =====
    end = node_id()
    dot.node(end, 'END\nCase Ready for Use', 
             shape='ellipse', style='filled', fillcolor='lightcoral', penwidth='2')
    
    # ===== CONNECTIONS =====
    
    # Initial flow
    dot.edge(start, spec)
    dot.edge(spec, rubric_req)
    dot.edge(rubric_req, orchestrator, label='Submit request')
    
    # Orchestrator planning
    dot.edge(orchestrator, task_plan)
    dot.edge(task_plan, medical_writer, label='Task 1', color='blue', style='bold')
    dot.edge(task_plan, patient_persona, label='Task 2', color='blue', style='bold')
    dot.edge(task_plan, rubric_agent, label='Task 3', color='blue', style='bold')
    
    # Agent execution (parallel)
    dot.edge(medical_writer, clinical_expert, label='Validate')
    dot.edge(patient_persona, clinical_expert, label='Validate')
    dot.edge(rubric_agent, clinical_expert, label='Validate')
    
    # DeepEval validation
    dot.edge(clinical_expert, deepeval_init, label='Ready for validation', 
             color='purple', style='bold')
    dot.edge(deepeval_init, medical_accuracy)
    dot.edge(deepeval_init, rubric_quality)
    dot.edge(deepeval_init, bias_check)
    dot.edge(deepeval_init, consistency)
    
    # Validation results
    dot.edge(medical_accuracy, all_pass, label='Score', color='green')
    dot.edge(rubric_quality, all_pass, label='Score', color='green')
    dot.edge(bias_check, all_pass, label='Score', color='green')
    dot.edge(consistency, all_pass, label='Score', color='green')
    
    # QA decision paths
    dot.edge(all_pass, human_review, label='YES\n(All pass)', color='green')
    dot.edge(all_pass, error_handler, label='NO\n(Failed metrics)', 
             color='red', style='dashed')
    
    # Human review
    dot.edge(human_review, approved)
    dot.edge(approved, case_package, label='YES', color='green')
    dot.edge(approved, feedback, label='NO\n(Needs revision)', 
             color='orange', style='dashed')
    
    # Feedback loop
    dot.edge(feedback, orchestrator, label='Iterate', 
             color='orange', style='dashed')
    
    # Error handling loop
    dot.edge(error_handler, orchestrator, label='Retry with adjustments', 
             color='red', style='dashed')
    
    # Output generation
    dot.edge(case_package, metadata)
    dot.edge(metadata, case_library, label='Store')
    dot.edge(metadata, deepeval_log, label='Log metrics')
    dot.edge(case_library, end)
    dot.edge(deepeval_log, end)
    
    # Save outputs
    output_dir = 'Arch_Diagrams/diagrams/HospitalWorkflow'
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, 'osce_case_generation_agentic')
    
    # Render
    dot.render(filepath, format='png', cleanup=True)
    dot.render(filepath, format='svg', cleanup=True)
    dot.save(f'{filepath}.dot')
    
    print('✅ DIAGRAM 1/3: OSCE Case Generation')
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
    create_osce_case_generation()
    print('\n' + '='*70)
    print('OSCE CASE GENERATION - AGENTIC AI SYSTEM')
    print('='*70)
    print('\nKey Components:')
    print('  1. Orchestrator Agent: Coordinates all specialized agents')
    print('  2. Medical Writer Agent: Generates clinical scenarios')
    print('  3. Patient Persona Agent: Creates realistic patient profiles')
    print('  4. Clinical Expert Agent: Validates medical accuracy')
    print('  5. Rubric Builder Agent: Creates assessment criteria')
    print('  6. DeepEval Validation: Automated quality checks')
    print('\nDeepEval Metrics Used:')
    print('  • G-Eval (Medical Accuracy): Threshold 0.90')
    print('  • G-Eval (Rubric Quality): Threshold 0.85')
    print('  • Bias Detection: Threshold 0.20')
    print('  • Custom Consistency Check: Scenario-Rubric alignment')
    print('\nWorkflow:')
    print('  1. Faculty specifies requirements')
    print('  2. Orchestrator creates task plan')
    print('  3. Specialized agents generate content (parallel)')
    print('  4. Clinical expert validates medical accuracy')
    print('  5. DeepEval runs automated quality checks')
    print('  6. Human faculty reviews if all metrics pass')
    print('  7. Store in case library with metadata')
    print('='*70)

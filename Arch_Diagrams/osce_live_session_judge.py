"""
OSCE Live Session - AI Patient with LLM-as-Judge
Diagram 2 of 3: Real-time OSCE Session with AI Patient and Continuous Evaluation

This diagram shows a live OSCE session where:
- AI acts as a realistic patient
- Real medical student takes history
- LLM-as-Judge evaluates in real-time
- Conversation is recorded for post-session analysis
"""

from graphviz import Digraph
import os
import subprocess

def create_osce_live_session():
    """Generate OSCE live session workflow with AI patient and LLM judge"""
    
    dot = Digraph(comment='OSCE Live Session - AI Patient with LLM-as-Judge')
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
    dot.node(start, 'START\nOSCE Session Begins', 
             shape='ellipse', style='filled', fillcolor='lightgreen', penwidth='2')
    
    # ===== SWIMLANE 1: SESSION SETUP =====
    with dot.subgraph(name='cluster_setup') as c:
        c.attr(label='Session Setup', style='filled', 
               fillcolor='#E3F2FD', fontsize='12')
        
        load_case = node_id()
        c.node(load_case, '📋 Load OSCE Case\nRetrieve from library\nCase ID: #12345',
               shape='box', style='filled', fillcolor='#BBDEFB')
        
        load_rubric = node_id()
        c.node(load_rubric, '📊 Load Assessment Rubric\nLearning objectives\nScoring criteria',
               shape='parallelogram', style='filled', fillcolor='#90CAF9')
        
        init_ai_patient = node_id()
        c.node(init_ai_patient, '🤖 Initialize AI Patient\nLoad persona\nSet emotional state\n[Claude Opus 4]',
               shape='hexagon', style='filled', fillcolor='#64B5F6', penwidth='2')
        
        init_judge = node_id()
        c.node(init_judge, '⚖️ Initialize LLM Judge\nLoad rubric\nSet evaluation mode\n[Claude Sonnet 4]',
               shape='hexagon', style='filled', fillcolor='#42A5F5', penwidth='2')
        
        start_recording = node_id()
        c.node(start_recording, '🎙️ Start Recording\nAudio + Text transcript\nTimestamped',
               shape='box', style='filled', fillcolor='#2196F3', 
               fontcolor='white')
    
    # ===== SWIMLANE 2: STUDENT INTERACTION =====
    with dot.subgraph(name='cluster_student') as c:
        c.attr(label='Medical Student', style='filled', 
               fillcolor='#E8F5E9', fontsize='12')
        
        student_intro = node_id()
        c.node(student_intro, '👨‍⚕️ Student Introduction\n"Hello, I\'m Dr. Smith..."',
               shape='box', style='filled', fillcolor='#C8E6C9')
        
        student_question = node_id()
        c.node(student_question, '❓ Ask Question\n"What brings you in today?"',
               shape='box', style='filled', fillcolor='#C8E6C9')
        
        student_listen = node_id()
        c.node(student_listen, '👂 Listen to Response\nActive listening\nNote-taking',
               shape='box', style='filled', fillcolor='#C8E6C9')
        
        student_followup = node_id()
        c.node(student_followup, '🔍 Follow-up Questions\nClarify symptoms\nExplore history',
               shape='box', style='filled', fillcolor='#C8E6C9')
        
        time_check = node_id()
        c.node(time_check, '⏱️ Time Remaining?',
               shape='diamond', style='filled', fillcolor='#A5D6A7')
        
        student_summary = node_id()
        c.node(student_summary, '📝 Summarize Findings\nPresent differential\nPropose next steps',
               shape='box', style='filled', fillcolor='#C8E6C9')
    
    # ===== SWIMLANE 3: AI PATIENT =====
    with dot.subgraph(name='cluster_ai_patient') as c:
        c.attr(label='AI Patient (Simulated)', style='filled', 
               fillcolor='#FFF3E0', fontsize='12')
        
        patient_respond = node_id()
        c.node(patient_respond, '🤖 Generate Response\nStay in character\nReveal info appropriately\n[Claude Opus 4]',
               shape='box', style='filled', fillcolor='#FFE0B2', penwidth='2')
        
        patient_emotion = node_id()
        c.node(patient_emotion, '😟 Emotional State\nAnxious/Worried/Calm\nAdjust based on rapport',
               shape='box', style='filled', fillcolor='#FFCC80')
        
        patient_consistency = node_id()
        c.node(patient_consistency, '✓ Consistency Check\nMatch previous responses\nMaintain character',
               shape='diamond', style='filled', fillcolor='#FFB74D')
        
        patient_deliver = node_id()
        c.node(patient_deliver, '💬 Deliver Response\nText-to-speech\nNatural pacing',
               shape='box', style='filled', fillcolor='#FFA726')
    
    # ===== SWIMLANE 4: LLM-AS-JUDGE (REAL-TIME) =====
    with dot.subgraph(name='cluster_judge') as c:
        c.attr(label='LLM-as-Judge (Real-time Evaluation)', style='filled', 
               fillcolor='#F3E5F5', fontsize='12')
        
        capture_exchange = node_id()
        c.node(capture_exchange, '📝 Capture Exchange\nStudent question\nPatient response\nTimestamp',
               shape='parallelogram', style='filled', fillcolor='#E1BEE7')
        
        eval_question_quality = node_id()
        c.node(eval_question_quality, '⚖️ Evaluate Question\n• Open-ended?\n• Appropriate?\n• Clear?\n[Claude Sonnet 4]',
               shape='box', style='filled', fillcolor='#CE93D8', penwidth='2')
        
        eval_communication = node_id()
        c.node(eval_communication, '⚖️ Evaluate Communication\n• Empathy\n• Active listening\n• Rapport building\n[Claude Sonnet 4]',
               shape='box', style='filled', fillcolor='#CE93D8', penwidth='2')
        
        eval_clinical_reasoning = node_id()
        c.node(eval_clinical_reasoning, '⚖️ Evaluate Clinical Reasoning\n• Systematic approach\n• Relevant questions\n• Differential thinking\n[Claude Sonnet 4]',
               shape='box', style='filled', fillcolor='#CE93D8', penwidth='2')
        
        running_score = node_id()
        c.node(running_score, '📊 Update Running Score\nCommunication: 8/10\nClinical: 7/10\nProfessionalism: 9/10',
               shape='note', style='filled', fillcolor='#BA68C8')
        
        flag_concern = node_id()
        c.node(flag_concern, '🚩 Critical Issue\nDetected?',
               shape='diamond', style='filled', fillcolor='#AB47BC')
        
        alert_proctor = node_id()
        c.node(alert_proctor, '⚠️ Alert Proctor\nSafety concern\nProfessionalism issue',
               shape='box', style='filled', fillcolor='#FFCDD2', 
               color='red', penwidth='2')
    
    # ===== SWIMLANE 5: RECORDING & STORAGE =====
    with dot.subgraph(name='cluster_recording') as c:
        c.attr(label='Recording & Storage', style='filled', 
               fillcolor='#E0F2F1', fontsize='12')
        
        transcript_buffer = node_id()
        c.node(transcript_buffer, '📝 Transcript Buffer\nReal-time text capture\nSpeaker labels\nTimestamps',
               shape='parallelogram', style='filled', fillcolor='#B2DFDB')
        
        audio_buffer = node_id()
        c.node(audio_buffer, '🎙️ Audio Buffer\nHigh-quality recording\nStereo channels',
               shape='parallelogram', style='filled', fillcolor='#80CBC4')
        
        judge_annotations = node_id()
        c.node(judge_annotations, '📌 Judge Annotations\nReal-time scores\nFlags & comments\nTimestamped',
               shape='parallelogram', style='filled', fillcolor='#4DB6AC')
    
    # ===== SESSION END =====
    session_end = node_id()
    dot.node(session_end, '⏰ Session Time Complete\n(10 minutes)', 
             shape='box', style='filled', fillcolor='#FFF9C4')
    
    # ===== SWIMLANE 6: SESSION FINALIZATION =====
    with dot.subgraph(name='cluster_finalize') as c:
        c.attr(label='Session Finalization', style='filled', 
               fillcolor='#FFFDE7', fontsize='12')
        
        stop_recording = node_id()
        c.node(stop_recording, '⏹️ Stop Recording\nFinalize audio\nComplete transcript',
               shape='box', style='filled', fillcolor='#FFF59D')
        
        compile_data = node_id()
        c.node(compile_data, '📦 Compile Session Data\n• Full transcript\n• Audio file\n• Judge annotations\n• Running scores',
               shape='box', style='filled', fillcolor='#FFF176')
        
        save_session = node_id()
        c.node(save_session, '💾 Save to Database\nSession ID: #67890\nStudent ID\nCase ID\nTimestamp',
               shape='cylinder', style='filled', fillcolor='#FFEE58')
        
        queue_eval = node_id()
        c.node(queue_eval, '📋 Queue for Deep Evaluation\nSend to DeepEval pipeline\nFull rubric analysis',
               shape='box', style='filled', fillcolor='#FFEB3B')
    
    # ===== END =====
    end = node_id()
    dot.node(end, 'END\nSession Complete\nReady for Analysis', 
             shape='ellipse', style='filled', fillcolor='lightcoral', penwidth='2')
    
    # ===== CONNECTIONS =====
    
    # Setup flow
    dot.edge(start, load_case)
    dot.edge(load_case, load_rubric)
    dot.edge(load_rubric, init_ai_patient)
    dot.edge(load_rubric, init_judge)
    dot.edge(init_ai_patient, start_recording)
    dot.edge(init_judge, start_recording)
    dot.edge(start_recording, student_intro, label='Begin', color='green', style='bold')
    
    # Student-Patient interaction loop
    dot.edge(student_intro, student_question)
    dot.edge(student_question, capture_exchange, label='Record', color='blue')
    dot.edge(student_question, patient_respond, label='Ask', color='green', style='bold')
    
    # AI Patient processing
    dot.edge(patient_respond, patient_emotion)
    dot.edge(patient_emotion, patient_consistency)
    dot.edge(patient_consistency, patient_deliver, label='Valid', color='green')
    dot.edge(patient_consistency, patient_respond, label='Adjust', 
             color='orange', style='dashed')
    dot.edge(patient_deliver, student_listen, label='Respond', color='green', style='bold')
    dot.edge(patient_deliver, capture_exchange, label='Record', color='blue')
    
    # Student listening and follow-up
    dot.edge(student_listen, student_followup)
    dot.edge(student_followup, time_check)
    dot.edge(time_check, student_question, label='YES\n(Continue)', 
             color='green', style='dashed')
    dot.edge(time_check, student_summary, label='NO\n(Time up)', color='red')
    
    # LLM Judge evaluation (parallel to conversation)
    dot.edge(capture_exchange, eval_question_quality, label='Analyze', 
             color='purple', style='bold')
    dot.edge(capture_exchange, eval_communication, label='Analyze', 
             color='purple', style='bold')
    dot.edge(capture_exchange, eval_clinical_reasoning, label='Analyze', 
             color='purple', style='bold')
    
    # Judge scoring
    dot.edge(eval_question_quality, running_score, label='Score', color='purple')
    dot.edge(eval_communication, running_score, label='Score', color='purple')
    dot.edge(eval_clinical_reasoning, running_score, label='Score', color='purple')
    
    # Flag critical issues
    dot.edge(running_score, flag_concern)
    dot.edge(flag_concern, alert_proctor, label='YES\n(Critical)', 
             color='red', style='bold')
    dot.edge(flag_concern, judge_annotations, label='NO\n(Continue)', color='green')
    
    # Recording streams
    dot.edge(capture_exchange, transcript_buffer, label='Text', color='blue')
    dot.edge(student_question, audio_buffer, label='Audio', color='blue')
    dot.edge(patient_deliver, audio_buffer, label='Audio', color='blue')
    dot.edge(running_score, judge_annotations, label='Annotate', color='purple')
    
    # Session end
    dot.edge(student_summary, session_end)
    dot.edge(session_end, stop_recording)
    
    # Finalization
    dot.edge(stop_recording, compile_data)
    dot.edge(transcript_buffer, compile_data, label='Merge')
    dot.edge(audio_buffer, compile_data, label='Merge')
    dot.edge(judge_annotations, compile_data, label='Merge')
    
    dot.edge(compile_data, save_session)
    dot.edge(save_session, queue_eval)
    dot.edge(queue_eval, end, label='Ready for DeepEval', 
             color='purple', style='bold')
    
    # Save outputs
    output_dir = 'Arch_Diagrams/diagrams/HospitalWorkflow'
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, 'osce_live_session_judge')
    
    # Render
    dot.render(filepath, format='png', cleanup=True)
    dot.render(filepath, format='svg', cleanup=True)
    dot.save(f'{filepath}.dot')
    
    print('✅ DIAGRAM 2/3: OSCE Live Session with AI Patient & LLM Judge')
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
    create_osce_live_session()
    print('\n' + '='*70)
    print('OSCE LIVE SESSION - AI PATIENT WITH LLM-AS-JUDGE')
    print('='*70)
    print('\nKey Components:')
    print('  1. AI Patient: Realistic patient simulation (Claude Opus 4)')
    print('  2. Medical Student: Real student practicing history-taking')
    print('  3. LLM-as-Judge: Real-time evaluation (Claude Sonnet 4)')
    print('  4. Recording System: Audio + transcript + annotations')
    print('\nReal-time Evaluation Criteria:')
    print('  • Question Quality: Open-ended, appropriate, clear')
    print('  • Communication: Empathy, active listening, rapport')
    print('  • Clinical Reasoning: Systematic, relevant, differential')
    print('\nSession Flow:')
    print('  1. Load case and initialize AI patient + judge')
    print('  2. Student asks questions → AI patient responds')
    print('  3. LLM judge evaluates each exchange in real-time')
    print('  4. Running scores updated continuously')
    print('  5. Critical issues flagged immediately')
    print('  6. Session ends after 10 minutes')
    print('  7. All data compiled and queued for deep evaluation')
    print('\nRecorded Data:')
    print('  • Full transcript with timestamps')
    print('  • Audio recording (stereo)')
    print('  • Real-time judge annotations')
    print('  • Running scores per criterion')
    print('='*70)

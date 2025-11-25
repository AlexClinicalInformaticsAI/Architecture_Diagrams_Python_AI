"""
Master Script: Generate All OSCE Agentic AI Diagrams
Runs all three diagram generators in sequence

Diagram 1: Case Generation - AI agents create OSCE cases with DeepEval validation
Diagram 2: Live Session - AI patient interacts with student, LLM-as-judge evaluates
Diagram 3: Transcript Evaluation - DeepEval analyzes conversation against rubric
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from osce_case_generation_agentic import create_osce_case_generation
from osce_live_session_judge import create_osce_live_session
from osce_transcript_deepeval import create_osce_transcript_evaluation

def main():
    """Generate all three OSCE diagrams"""
    
    print('='*70)
    print('OSCE AGENTIC AI SYSTEM - DIAGRAM GENERATION')
    print('='*70)
    print('\nGenerating 3 comprehensive workflow diagrams...\n')
    
    try:
        # Diagram 1: Case Generation
        print('\n' + '-'*70)
        print('GENERATING DIAGRAM 1/3: CASE GENERATION')
        print('-'*70)
        create_osce_case_generation()
        
        # Diagram 2: Live Session
        print('\n' + '-'*70)
        print('GENERATING DIAGRAM 2/3: LIVE SESSION')
        print('-'*70)
        create_osce_live_session()
        
        # Diagram 3: Transcript Evaluation
        print('\n' + '-'*70)
        print('GENERATING DIAGRAM 3/3: TRANSCRIPT EVALUATION')
        print('-'*70)
        create_osce_transcript_evaluation()
        
        # Summary
        print('\n' + '='*70)
        print('✅ ALL DIAGRAMS GENERATED SUCCESSFULLY')
        print('='*70)
        print('\nOutput Location: Arch_Diagrams/diagrams/HospitalWorkflow/')
        print('\nGenerated Files:')
        print('  Diagram 1 - Case Generation:')
        print('    • osce_case_generation_agentic.png')
        print('    • osce_case_generation_agentic.svg')
        print('    • osce_case_generation_agentic.dot')
        print('    • osce_case_generation_agentic.drawio')
        print('\n  Diagram 2 - Live Session:')
        print('    • osce_live_session_judge.png')
        print('    • osce_live_session_judge.svg')
        print('    • osce_live_session_judge.dot')
        print('    • osce_live_session_judge.drawio')
        print('\n  Diagram 3 - Transcript Evaluation:')
        print('    • osce_transcript_deepeval.png')
        print('    • osce_transcript_deepeval.svg')
        print('    • osce_transcript_deepeval.dot')
        print('    • osce_transcript_deepeval.drawio')
        
        print('\n' + '='*70)
        print('SYSTEM OVERVIEW')
        print('='*70)
        print('\nThis agentic AI system for OSCE education includes:')
        print('\n1. CASE GENERATION (Diagram 1):')
        print('   • Orchestrator agent coordinates specialized AI agents')
        print('   • Medical writer, patient persona, clinical expert, rubric builder')
        print('   • DeepEval validates: medical accuracy, rubric quality, bias, consistency')
        print('   • Human faculty review before production deployment')
        print('\n2. LIVE SESSION (Diagram 2):')
        print('   • AI patient simulates realistic patient behavior')
        print('   • Real medical student practices history-taking')
        print('   • LLM-as-judge evaluates in real-time:')
        print('     - Question quality')
        print('     - Communication skills')
        print('     - Clinical reasoning')
        print('   • Full recording: audio + transcript + annotations')
        print('\n3. TRANSCRIPT EVALUATION (Diagram 3):')
        print('   • DeepEval analyzes full conversation')
        print('   • 12+ metrics across 4 categories:')
        print('     - Communication (30%): relevancy, empathy, clarity')
        print('     - Clinical reasoning (40%): recall, precision, systematic')
        print('     - Professionalism (20%): bias, toxicity, boundaries')
        print('     - Custom OSCE (10%): intro, consent, summary')
        print('   • Generates detailed feedback with specific examples')
        print('   • Cohort analytics for continuous improvement')
        print('\n' + '='*70)
        print('DEEPEVAL INTEGRATION')
        print('='*70)
        print('\nDeepEval is integrated at multiple stages:')
        print('  1. Case Generation: Validates quality before deployment')
        print('  2. Live Session: Real-time scoring (optional)')
        print('  3. Post-Session: Comprehensive transcript analysis')
        print('\nKey DeepEval Features Used:')
        print('  • G-Eval: Custom criteria evaluation')
        print('  • Answer Relevancy: Question appropriateness')
        print('  • Contextual Recall/Precision: Information gathering')
        print('  • Bias/Toxicity: Professionalism checks')
        print('  • Custom Metrics: OSCE-specific requirements')
        print('  • Confident AI Platform: Tracking and analytics')
        print('\n' + '='*70)
        
    except Exception as e:
        print(f'\n❌ ERROR: {e}')
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())

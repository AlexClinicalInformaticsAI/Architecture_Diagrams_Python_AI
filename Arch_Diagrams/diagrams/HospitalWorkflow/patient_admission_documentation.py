"""
Patient Admission Documentation Workflow
Clinical Documentation Process Following IHI Principles

This diagram shows the documentation requirements and information flow
during a patient admission, emphasizing:
- Required clinical documentation
- Information handoffs between providers
- Documentation quality and completeness
- Regulatory compliance (Joint Commission, CMS)
- Patient safety through accurate documentation

Participants (Swim Lanes):
1. Patient/Family - Source of information
2. ED Nurse - Initial documentation
3. ED Physician - Medical assessment documentation
4. Hospitalist - Admission documentation
5. Floor Nurse - Ongoing documentation
6. Case Manager - Utilization and discharge planning
7. Medical Record/EHR - Central repository

Focus: Documentation as a patient safety and quality tool

Generates PNG, DOT, and Draw.io format diagrams
"""

import subprocess
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users, Client
from diagrams.generic.storage import Storage
from diagrams.generic.database import SQL
import os

# Graph attributes for documentation workflow
graph_attr = {
    "splines": "ortho",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "fontsize": "13",
    "bgcolor": "white",
    "pad": "0.5",
    "rankdir": "TB"
}

# Healthcare documentation colors
patient_color = "#E3F2FD"      # Light Blue
nurse_color = "#F3E5F5"        # Light Purple
physician_color = "#E8F5E9"    # Light Green
hospitalist_color = "#FFF3E0"  # Light Orange
case_mgr_color = "#FCE4EC"     # Light Pink
record_color = "#E0F2F1"       # Light Teal
quality_color = "#FFEBEE"      # Light Red

with Diagram(
    "Patient Admission Documentation - Clinical Information Flow",
    filename="diagrams/HospitalWorkflow/patient_admission_documentation",
    outformat=["png", "dot"],
    show=False,
    direction="TB",
    graph_attr=graph_attr
):

    # ========================================================================
    # SWIM LANE 1: PATIENT/FAMILY (Information Source)
    # ========================================================================
    with Cluster("PATIENT/FAMILY\n(Information Source)", 
                 graph_attr={"bgcolor": patient_color, "style": "rounded", "margin": "25"}):
        pf1 = Users("Provides:\n• Chief complaint\n• Medical history\n• Current medications\n• Allergies")
        pf2 = Users("Provides:\n• Insurance info\n• Emergency contacts\n• Advance directives\n• Consent")
        pf3 = Users("Reviews & signs:\n• Admission consent\n• HIPAA notice\n• Patient rights\n• Financial agreement")
        pf4 = Users("Receives:\n• Admission packet\n• Care plan\n• Patient education\n• Discharge goals")

    # ========================================================================
    # SWIM LANE 2: ED NURSE (Initial Documentation)
    # ========================================================================
    with Cluster("ED NURSE\n(Initial Assessment Documentation)", 
                 graph_attr={"bgcolor": nurse_color, "style": "rounded", "margin": "25"}):
        en1 = Client("TRIAGE NOTE:\n✓ Vital signs\n✓ Chief complaint\n✓ Pain assessment\n✓ Acuity level\n✓ Allergies")
        en2 = Client("NURSING ASSESSMENT:\n✓ Review of systems\n✓ Fall risk score\n✓ Skin assessment\n✓ Functional status\n✓ Psychosocial needs")
        en3 = Client("MEDICATION\nRECONCILATION:\n✓ Home medications\n✓ Dosages & frequency\n✓ Last dose taken\n✓ Adherence issues")
        en4 = Client("SAFETY SCREENING:\n✓ Suicide risk\n✓ Abuse/neglect\n✓ Substance use\n✓ Isolation needs")
        en5 = Client("TRANSFER NOTE:\n✓ Current condition\n✓ Treatments given\n✓ Pending orders\n✓ Family concerns")

    # ========================================================================
    # SWIM LANE 3: ED PHYSICIAN (Medical Documentation)
    # ========================================================================
    with Cluster("ED PHYSICIAN\n(Medical Assessment Documentation)", 
                 graph_attr={"bgcolor": physician_color, "style": "rounded", "margin": "25"}):
        ed1 = Client("HISTORY & PHYSICAL:\n✓ History of present illness\n✓ Past medical history\n✓ Review of systems\n✓ Physical exam findings")
        ed2 = Client("DIAGNOSTIC ORDERS:\n✓ Laboratory tests\n✓ Imaging studies\n✓ EKG\n✓ Consultations")
        ed3 = Client("CLINICAL IMPRESSION:\n✓ Differential diagnosis\n✓ Working diagnosis\n✓ Severity assessment\n✓ Treatment plan")
        ed4 = Client("ADMISSION NOTE:\n✓ Reason for admission\n✓ Clinical findings\n✓ Test results\n✓ Disposition")

    # ========================================================================
    # SWIM LANE 4: HOSPITALIST (Admission Orders)
    # ========================================================================
    with Cluster("HOSPITALIST\n(Admission Documentation)", 
                 graph_attr={"bgcolor": hospitalist_color, "style": "rounded", "margin": "25"}):
        h1 = Client("ADMISSION H&P:\n✓ Complete history\n✓ Physical examination\n✓ Assessment\n✓ Plan of care")
        h2 = Client("ADMISSION ORDERS:\n✓ Admitting diagnosis\n✓ Condition level\n✓ Code status\n✓ Diet orders")
        h3 = Client("MEDICATION ORDERS:\n✓ Continue home meds\n✓ New medications\n✓ PRN medications\n✓ IV fluids")
        h4 = Client("CARE ORDERS:\n✓ Activity level\n✓ Vital sign frequency\n✓ Nursing interventions\n✓ Consults needed")
        h5 = Client("GOALS OF CARE:\n✓ Treatment goals\n✓ Expected LOS\n✓ Discharge criteria\n✓ Patient/family goals")

    # ========================================================================
    # SWIM LANE 5: FLOOR NURSE (Ongoing Documentation)
    # ========================================================================
    with Cluster("FLOOR NURSE\n(Ongoing Care Documentation)", 
                 graph_attr={"bgcolor": nurse_color, "style": "rounded", "margin": "25"}):
        fn1 = Client("ADMISSION\nASSESSMENT:\n✓ Head-to-toe exam\n✓ Baseline vitals\n✓ Pain assessment\n✓ Safety assessment")
        fn2 = Client("CARE PLAN:\n✓ Nursing diagnoses\n✓ Interventions\n✓ Expected outcomes\n✓ Patient goals")
        fn3 = Client("SHIFT NOTES:\n✓ Patient status\n✓ Interventions\n✓ Response to treatment\n✓ Changes in condition")
        fn4 = Client("MEDICATION\nADMINISTRATION:\n✓ eMAR documentation\n✓ Patient response\n✓ Side effects\n✓ Patient education")
        fn5 = Client("PATIENT EDUCATION:\n✓ Disease process\n✓ Medications\n✓ Self-care\n✓ Discharge planning")

    # ========================================================================
    # SWIM LANE 6: CASE MANAGER (Utilization & Planning)
    # ========================================================================
    with Cluster("CASE MANAGER\n(Utilization & Discharge Planning)", 
                 graph_attr={"bgcolor": case_mgr_color, "style": "rounded", "margin": "25"}):
        cm1 = Client("UTILIZATION REVIEW:\n✓ Medical necessity\n✓ Level of care\n✓ Insurance authorization\n✓ Length of stay")
        cm2 = Client("DISCHARGE PLANNING:\n✓ Discharge needs\n✓ Home services\n✓ DME requirements\n✓ Follow-up care")
        cm3 = Client("SOCIAL ASSESSMENT:\n✓ Living situation\n✓ Support system\n✓ Financial concerns\n✓ Barriers to care")
        cm4 = Client("COORDINATION:\n✓ Insurance updates\n✓ Service referrals\n✓ Equipment orders\n✓ Appointments")

    # ========================================================================
    # SWIM LANE 7: MEDICAL RECORD/EHR (Central Repository)
    # ========================================================================
    with Cluster("MEDICAL RECORD/EHR\n(Documentation Repository)", 
                 graph_attr={"bgcolor": record_color, "style": "rounded", "margin": "25"}):
        mr1 = SQL("PATIENT\nDEMOGRAPHICS:\n• Name, DOB, MRN\n• Address, phone\n• Insurance\n• Emergency contacts")
        mr2 = SQL("CLINICAL\nDOCUMENTATION:\n• H&P notes\n• Progress notes\n• Nursing notes\n• Consult notes")
        mr3 = SQL("ORDERS &\nRESULTS:\n• Physician orders\n• Lab results\n• Imaging reports\n• Medications")
        mr4 = SQL("CARE PLANNING:\n• Problem list\n• Care plans\n• Goals of care\n• Discharge plan")
        mr5 = SQL("REGULATORY\nDOCUMENTS:\n• Consents\n• Advance directives\n• HIPAA forms\n• Patient rights")
        mr6 = SQL("QUALITY\nMETRICS:\n• Core measures\n• Safety indicators\n• Satisfaction scores\n• Outcomes data")

    # ========================================================================
    # DOCUMENTATION FLOW - Information Gathering & Recording
    # ========================================================================

    # PHASE 1: Initial Information Collection
    pf1 >> Edge(label="Provides history", color="blue") >> en1
    en1 >> Edge(label="Documents", color="purple") >> mr2
    pf2 >> Edge(label="Provides info", color="blue") >> mr1
    pf3 >> Edge(label="Signs consents", color="blue") >> mr5

    # PHASE 2: Nursing Assessment Documentation
    en1 >> Edge(label="Completes", color="purple") >> en2
    en2 >> Edge(label="Documents", color="purple") >> mr2
    pf1 >> Edge(label="Medication list", color="blue") >> en3
    en3 >> Edge(label="⚠️ CRITICAL:\nMed reconciliation", color="red", style="bold") >> mr3
    en2 >> Edge(label="Screens", color="purple") >> en4
    en4 >> Edge(label="Safety screening", color="purple") >> mr2

    # PHASE 3: Physician Assessment Documentation
    mr2 >> Edge(label="Reviews", color="green") >> ed1
    ed1 >> Edge(label="Documents H&P", color="green") >> mr2
    ed1 >> Edge(label="Orders tests", color="green") >> ed2
    ed2 >> Edge(label="Orders", color="green") >> mr3
    mr3 >> Edge(label="Results", color="green") >> ed3
    ed3 >> Edge(label="Clinical impression", color="green") >> mr2
    ed3 >> Edge(label="Admission note", color="green") >> ed4
    ed4 >> Edge(label="Documents", color="green") >> mr2

    # PHASE 4: Hospitalist Admission Documentation
    mr2 >> Edge(label="⚠️ HANDOFF:\nReviews ED notes", color="red", style="bold") >> h1
    h1 >> Edge(label="Admission H&P", color="orange") >> mr2
    h1 >> Edge(label="Admission orders", color="orange") >> h2
    h2 >> Edge(label="Orders", color="orange") >> mr3
    h2 >> Edge(label="Medications", color="orange") >> h3
    h3 >> Edge(label="Med orders", color="orange") >> mr3
    h2 >> Edge(label="Care orders", color="orange") >> h4
    h4 >> Edge(label="Nursing orders", color="orange") >> mr3
    h1 >> Edge(label="Goals", color="orange") >> h5
    h5 >> Edge(label="Care goals", color="orange") >> mr4

    # PHASE 5: Floor Nurse Documentation
    mr3 >> Edge(label="⚠️ HANDOFF:\nReceives orders", color="red", style="bold") >> fn1
    en5 >> Edge(label="⚠️ HANDOFF:\nTransfer note", color="red", style="bold") >> fn1
    fn1 >> Edge(label="Admission assessment", color="pink") >> mr2
    fn1 >> Edge(label="Care plan", color="pink") >> fn2
    fn2 >> Edge(label="Nursing care plan", color="pink") >> mr4
    fn2 >> Edge(label="Shift notes", color="pink") >> fn3
    fn3 >> Edge(label="Ongoing documentation", color="pink") >> mr2
    mr3 >> Edge(label="Med orders", color="pink") >> fn4
    fn4 >> Edge(label="✓ eMAR documentation", color="pink") >> mr3
    fn2 >> Edge(label="Education", color="pink") >> fn5
    fn5 >> Edge(label="Education documentation", color="pink") >> mr2
    fn5 >> Edge(label="Provides education", color="pink") >> pf4

    # PHASE 6: Case Management Documentation
    mr2 >> Edge(label="Reviews", color="magenta") >> cm1
    cm1 >> Edge(label="Utilization notes", color="magenta") >> mr4
    cm1 >> Edge(label="Discharge planning", color="magenta") >> cm2
    cm2 >> Edge(label="Discharge plan", color="magenta") >> mr4
    pf4 >> Edge(label="Discusses needs", color="blue") >> cm3
    cm3 >> Edge(label="Social assessment", color="magenta") >> mr2
    cm2 >> Edge(label="Coordinates", color="magenta") >> cm4
    cm4 >> Edge(label="Coordination notes", color="magenta") >> mr4

    # PHASE 7: Quality & Compliance
    mr2 >> Edge(label="Extracts data", color="teal", style="dashed") >> mr6
    mr3 >> Edge(label="Extracts data", color="teal", style="dashed") >> mr6
    mr4 >> Edge(label="Extracts data", color="teal", style="dashed") >> mr6

print("✓ PNG and DOT files generated")

# Convert to Draw.io
try:
    subprocess.run([
        "graphviz2drawio",
        "diagrams/HospitalWorkflow/patient_admission_documentation.dot",
        "-o",
        "diagrams/HospitalWorkflow/patient_admission_documentation.drawio"
    ], check=True)
    print("✓ Draw.io file generated")
except:
    print("✗ graphviz2drawio not found (optional)")

print("\n" + "="*80)
print("PATIENT ADMISSION DOCUMENTATION - CLINICAL INFORMATION FLOW")
print("="*80)
print("\n📋 DOCUMENTATION PURPOSE:")
print("   • Patient safety through accurate information")
print("   • Care coordination across providers")
print("   • Regulatory compliance (Joint Commission, CMS)")
print("   • Quality measurement and improvement")
print("   • Legal protection for providers and organization")
print("   • Reimbursement justification")
print("\n📝 REQUIRED DOCUMENTATION ELEMENTS:")
print("\n   1. PATIENT DEMOGRAPHICS & REGISTRATION")
print("      • Full name, date of birth, medical record number")
print("      • Address, phone, email")
print("      • Insurance information and authorization")
print("      • Emergency contacts")
print("      • Primary care physician")
print("\n   2. CONSENTS & LEGAL DOCUMENTS")
print("      • Informed consent for treatment")
print("      • HIPAA privacy notice acknowledgment")
print("      • Patient rights and responsibilities")
print("      • Advance directives (if applicable)")
print("      • Financial responsibility agreement")
print("\n   3. NURSING TRIAGE & ASSESSMENT")
print("      • Chief complaint (in patient's words)")
print("      • Vital signs (BP, HR, RR, Temp, O2 sat, pain)")
print("      • Acuity level (ESI 1-5)")
print("      • Allergies (medications, food, environmental)")
print("      • Fall risk assessment")
print("      • Skin integrity assessment")
print("      • Safety screening (suicide, abuse, substance use)")
print("\n   4. MEDICATION RECONCILIATION (Critical)")
print("      • Complete list of home medications")
print("      • Dosages, frequencies, routes")
print("      • Last dose taken")
print("      • Over-the-counter medications")
print("      • Herbal supplements")
print("      • Medication adherence issues")
print("      ⚠️ HIGH RISK: Medication errors often occur here")
print("\n   5. PHYSICIAN HISTORY & PHYSICAL")
print("      • History of present illness (HPI)")
print("      • Past medical history (PMH)")
print("      • Past surgical history (PSH)")
print("      • Family history")
print("      • Social history (smoking, alcohol, drugs)")
print("      • Review of systems (ROS)")
print("      • Physical examination (by system)")
print("      • Assessment (diagnosis)")
print("      • Plan (treatment plan)")
print("\n   6. ADMISSION ORDERS")
print("      • Admitting diagnosis")
print("      • Condition level (stable, fair, serious, critical)")
print("      • Code status (full code, DNR, DNI)")
print("      • Diet orders")
print("      • Activity level")
print("      • Vital sign frequency")
print("      • Nursing care orders")
print("      • Medication orders")
print("      • Laboratory/imaging orders")
print("      • Consultation requests")
print("\n   7. NURSING ADMISSION ASSESSMENT")
print("      • Head-to-toe physical assessment")
print("      • Baseline vital signs")
print("      • Pain assessment (location, quality, severity)")
print("      • Neurological assessment")
print("      • Cardiovascular assessment")
print("      • Respiratory assessment")
print("      • Gastrointestinal assessment")
print("      • Genitourinary assessment")
print("      • Musculoskeletal assessment")
print("      • Psychosocial assessment")
print("\n   8. NURSING CARE PLAN")
print("      • Nursing diagnoses (NANDA)")
print("      • Patient goals (measurable, time-bound)")
print("      • Nursing interventions")
print("      • Expected outcomes")
print("      • Evaluation criteria")
print("\n   9. CASE MANAGEMENT DOCUMENTATION")
print("      • Medical necessity justification")
print("      • Insurance authorization")
print("      • Discharge planning needs")
print("      • Social determinants of health")
print("      • Barriers to discharge")
print("      • Post-discharge services needed")
print("\n   10. PATIENT EDUCATION DOCUMENTATION")
print("       • Topics covered")
print("       • Teaching methods used")
print("       • Patient/family understanding")
print("       • Barriers to learning")
print("       • Need for additional education")
print("\n⚠️ CRITICAL HANDOFF DOCUMENTATION:")
print("\n   1. ED NURSE → ED PHYSICIAN")
print("      Document: Triage findings, vital signs, chief complaint")
print("      Risk: Incomplete information delays diagnosis")
print("\n   2. ED PHYSICIAN → HOSPITALIST")
print("      Document: Clinical findings, test results, treatment given")
print("      Risk: Incomplete handoff leads to errors")
print("\n   3. ED NURSE → FLOOR NURSE")
print("      Document: SBAR format, current condition, pending issues")
print("      Risk: Information loss during transfer")
print("\n📊 DOCUMENTATION QUALITY METRICS:")
print("\n   TIMELINESS:")
print("   • H&P completed within 24 hours of admission")
print("   • Medication reconciliation within 24 hours")
print("   • Nursing assessment within 1 hour of admission")
print("   • Progress notes daily")
print("\n   COMPLETENESS:")
print("   • All required elements present")
print("   • No blank fields in critical areas")
print("   • Signatures and credentials on all entries")
print("   • Date and time stamps accurate")
print("\n   ACCURACY:")
print("   • Information consistent across documents")
print("   • Allergies documented in all locations")
print("   • Medication list matches all sources")
print("   • Vital signs match nursing documentation")
print("\n   LEGIBILITY:")
print("   • Electronic documentation preferred")
print("   • Handwritten notes legible")
print("   • No unapproved abbreviations")
print("   • Standard terminology used")
print("\n🔒 REGULATORY REQUIREMENTS:")
print("\n   JOINT COMMISSION:")
print("   • National Patient Safety Goals compliance")
print("   • Medication reconciliation at transitions")
print("   • Two patient identifiers")
print("   • Hand hygiene documentation")
print("   • Fall risk assessment")
print("\n   CMS (CENTERS FOR MEDICARE & MEDICAID):")
print("   • Medical necessity documentation")
print("   • Two-midnight rule for inpatient status")
print("   • Physician certification of admission")
print("   • Discharge planning documentation")
print("   • Quality measure documentation")
print("\n   HIPAA (PRIVACY):")
print("   • Patient consent for treatment")
print("   • Privacy notice acknowledgment")
print("   • Minimum necessary information")
print("   • Secure documentation practices")
print("\n💡 DOCUMENTATION BEST PRACTICES:")
print("\n   1. DOCUMENT IN REAL-TIME")
print("      • Reduces errors and omissions")
print("      • Ensures accuracy")
print("      • Improves efficiency")
print("\n   2. USE OBJECTIVE LANGUAGE")
print("      • Facts, not opinions")
print("      • Measurable observations")
print("      • Avoid judgmental terms")
print("\n   3. DOCUMENT PATIENT RESPONSES")
print("      • To interventions")
print("      • To medications")
print("      • To education")
print("\n   4. DOCUMENT COMMUNICATION")
print("      • With physicians")
print("      • With family")
print("      • With other providers")
print("\n   5. NEVER ALTER DOCUMENTATION")
print("      • Use addendum if correction needed")
print("      • Note date/time of addendum")
print("      • Explain reason for addition")
print("\n🎯 QUALITY IMPROVEMENT OPPORTUNITIES:")
print("\n   • Reduce documentation time through templates")
print("   • Improve medication reconciliation accuracy")
print("   • Standardize handoff documentation")
print("   • Eliminate duplicate documentation")
print("   • Enhance patient education documentation")
print("   • Improve discharge planning documentation")
print("\n📈 EXPECTED OUTCOMES:")
print("   • 100% compliance with documentation requirements")
print("   • Zero medication reconciliation errors")
print("   • Improved care coordination")
print("   • Enhanced patient safety")
print("   • Reduced regulatory deficiencies")
print("   • Improved reimbursement")
print("="*80)

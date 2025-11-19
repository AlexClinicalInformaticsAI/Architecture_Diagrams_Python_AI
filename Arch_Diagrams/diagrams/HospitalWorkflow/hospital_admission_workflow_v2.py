"""
Hospital Admission Workflow - IHI Quality Improvement Approach
Patient Journey from Emergency Department to Hospital Floor

This diagram follows IHI Model for Improvement methodology, emphasizing:
- Patient-centered care flow
- Safety checkpoints and handoffs
- Value-added vs. non-value-added time
- Quality and efficiency metrics
- People and roles (not just systems)

Participants (Swim Lanes):
1. Patient - The individual receiving care
2. ED Nurse - Emergency Department nursing staff
3. ED Physician - Emergency Department physician
4. Hospitalist - Admitting physician
5. Floor Nurse - Inpatient unit nursing staff
6. Pharmacist - Medication safety specialist
7. EHR System - Electronic documentation and orders

Key Focus Areas:
- HANDOFFS (highest risk for errors)
- SAFETY CHECKPOINTS (verification points)
- WAIT TIMES (non-value-added time)
- PATIENT EXPERIENCE (communication and comfort)

Generates PNG, DOT, and Draw.io format diagrams
"""

import subprocess
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users, Client
from diagrams.generic.storage import Storage
from diagrams.generic.database import SQL
import os

# Graph attributes optimized for swim lane readability
graph_attr = {
    "splines": "ortho",
    "nodesep": "1.2",
    "ranksep": "1.8",
    "fontsize": "13",
    "bgcolor": "white",
    "pad": "0.5",
    "rankdir": "TB"
}

# Healthcare-specific color coding (from healthcareagent.md)
patient_color = "#E3F2FD"      # Light Blue - Patient focus
ed_nurse_color = "#F3E5F5"     # Light Purple - Nursing
ed_physician_color = "#E8F5E9" # Light Green - Physicians
hospitalist_color = "#FFF3E0"  # Light Orange - Admitting
floor_nurse_color = "#FCE4EC"  # Light Pink - Floor nursing
pharmacist_color = "#F1F8E9"   # Light Lime - Pharmacy
ehr_color = "#E0F2F1"          # Light Teal - Systems
safety_color = "#FFEBEE"       # Light Red - Safety checks

with Diagram(
    "Hospital Admission Workflow - Patient Journey (IHI Approach)",
    filename="diagrams/HospitalWorkflow/hospital_admission_workflow_v2",
    outformat=["png", "dot"],
    show=False,
    direction="TB",
    graph_attr=graph_attr
):

    # ========================================================================
    # SWIM LANE 1: PATIENT (Focus of Care)
    # ========================================================================
    with Cluster("PATIENT\n(Focus of Care)", graph_attr={"bgcolor": patient_color, "style": "rounded", "margin": "20"}):
        p1 = Users("1. Arrives at ED\nwith symptoms\n⏱️ Time: 0 min")
        p2 = Users("2. Provides history\n& consent\n⏱️ 5 min")
        p3 = Users("⏱️ WAIT:\nFor assessment\n[15-30 min]\n[Non-Value-Added]")
        p4 = Users("3. Physical exam\n& tests\n⏱️ 20 min")
        p5 = Users("⏱️ WAIT:\nFor results\n[60-120 min]\n[Non-Value-Added]")
        p6 = Users("4. Receives diagnosis\n& education\n⏱️ 10 min")
        p7 = Users("5. Consents to\nadmission\n⏱️ 5 min")
        p8 = Users("⏱️ WAIT:\nFor bed assignment\n[30-60 min]\n[Non-Value-Added]")
        p9 = Users("6. Transported\nto floor\n⏱️ 15 min")
        p10 = Users("7. Settled in room\n& oriented\n⏱️ 20 min")
        p11 = Users("8. Receives first\nmedications\n⏱️ 10 min")

    # ========================================================================
    # SWIM LANE 2: ED NURSE (Initial Assessment & Monitoring)
    # ========================================================================
    with Cluster("ED NURSE\n(Assessment & Monitoring)", graph_attr={"bgcolor": ed_nurse_color, "style": "rounded", "margin": "20"}):
        en1 = Client("9. TRIAGE:\n✓ Vital signs\n✓ Chief complaint\n✓ Pain scale\n⏱️ 10 min")
        en2 = Client("10. Document\nin EHR\n⏱️ 5 min")
        en3 = Client("11. Collect samples\nfor ordered tests\n⏱️ 10 min")
        en4 = Client("12. Monitor patient\n(ongoing vitals)\n⏱️ Continuous")
        en5 = Client("13. Prepare for\ntransport\n⏱️ 10 min")
        en6 = Client("14. HANDOFF:\nSBAR Report\nto Floor Nurse\n⚠️ HIGH RISK\n⏱️ 10 min")

    # ========================================================================
    # SWIM LANE 3: ED PHYSICIAN (Diagnosis & Treatment)
    # ========================================================================
    with Cluster("ED PHYSICIAN\n(Diagnosis & Treatment)", graph_attr={"bgcolor": ed_physician_color, "style": "rounded", "margin": "20"}):
        ed1 = Client("15. Review triage\nnotes in EHR\n⏱️ 5 min")
        ed2 = Client("16. Physical\nexamination\n⏱️ 15 min")
        ed3 = Client("17. Order tests:\n• Labs\n• Imaging\n• EKG\n⏱️ 5 min")
        ed4 = Client("18. Review results\n& interpret\n⏱️ 15 min")
        ed5 = Client("19. Make diagnosis\n& document\n⏱️ 10 min")
        ed6 = Client("20. Determine\nadmission needed\n⏱️ 5 min")
        ed7 = Client("21. HANDOFF:\nConsult request\nto Hospitalist\n⚠️ HIGH RISK\n⏱️ 10 min")

    # ========================================================================
    # SWIM LANE 4: HOSPITALIST (Admission Orders)
    # ========================================================================
    with Cluster("HOSPITALIST\n(Admission Orders)", graph_attr={"bgcolor": hospitalist_color, "style": "rounded", "margin": "20"}):
        h1 = Client("22. Receive consult\nrequest\n⏱️ 2 min")
        h2 = Client("23. Review patient\ndata in EHR:\n• History\n• Labs\n• Imaging\n⏱️ 15 min")
        h3 = Client("24. Accept patient\nfor admission\n⏱️ 5 min")
        h4 = Client("25. Write admission\norders in EHR:\n• Diagnosis\n• Care level\n• Diet\n• Activity\n⏱️ 15 min")
        h5 = Client("26. Order medications\n& treatments\n⏱️ 10 min")
        h6 = Client("27. Assign to\nfloor & room\n⏱️ 5 min")

    # ========================================================================
    # SWIM LANE 5: FLOOR NURSE (Receiving & Admission)
    # ========================================================================
    with Cluster("FLOOR NURSE\n(Receiving & Admission)", graph_attr={"bgcolor": floor_nurse_color, "style": "rounded", "margin": "20"}):
        fn1 = Client("28. Receive admission\nnotification\n⏱️ 2 min")
        fn2 = Client("29. Prepare room:\n• Equipment\n• Supplies\n• Safety check\n⏱️ 15 min")
        fn3 = Client("30. HANDOFF:\nReceive patient\n& SBAR report\n⚠️ HIGH RISK\n⏱️ 10 min")
        fn4 = Client("31. SAFETY CHECK:\n✓ Two identifiers\n✓ Allergy band\n✓ Fall risk\n⏱️ 5 min")
        fn5 = Client("32. Admission\nassessment:\n• Head-to-toe\n• Pain\n• Skin\n⏱️ 20 min")
        fn6 = Client("33. Review orders\nin EHR\n⏱️ 5 min")
        fn7 = Client("34. Patient & family\neducation\n⏱️ 10 min")
        fn8 = Client("35. SAFETY CHECK:\nMedication\nadministration\n✓ 5 Rights\n⏱️ 10 min")
        fn9 = Client("36. Document in EHR\n(complete admission)\n⏱️ 10 min")

    # ========================================================================
    # SWIM LANE 6: PHARMACIST (Medication Safety)
    # ========================================================================
    with Cluster("PHARMACIST\n(Medication Safety)", graph_attr={"bgcolor": pharmacist_color, "style": "rounded", "margin": "20"}):
        ph1 = Client("37. Receive medication\norders from EHR\n⏱️ 2 min")
        ph2 = Client("38. SAFETY CHECK:\n✓ Allergies\n✓ Interactions\n✓ Duplicates\n✓ Dosing\n⏱️ 10 min")
        ph3 = Client("39. Verify orders\nin EHR\n⏱️ 5 min")
        ph4 = Client("40. Prepare first\ndoses\n⏱️ 20 min")
        ph5 = Client("41. Deliver to\nnursing unit\n⏱️ 10 min")

    # ========================================================================
    # SWIM LANE 7: EHR SYSTEM (Documentation & Orders)
    # ========================================================================
    with Cluster("EHR SYSTEM\n(Documentation & Orders)", graph_attr={"bgcolor": ehr_color, "style": "rounded", "margin": "20"}):
        ehr1 = SQL("Patient\nRegistration")
        ehr2 = SQL("Triage\nDocumentation")
        ehr3 = SQL("Order Entry\nSystem (CPOE)")
        ehr4 = SQL("Results\nReporting")
        ehr5 = SQL("Admission\nOrders")
        ehr6 = SQL("Medication\nOrders")
        ehr7 = SQL("Nursing\nDocumentation")
        ehr8 = SQL("eMAR\n(Med Admin Record)")

    # ========================================================================
    # WORKFLOW CONNECTIONS - Patient-Centered Flow
    # ========================================================================

    # PHASE 1: ED ARRIVAL & TRIAGE
    p1 >> Edge(label="Arrives", color="blue") >> en1
    en1 >> Edge(label="Triages", color="purple") >> p2
    en1 >> Edge(label="Documents", color="purple") >> ehr2
    p2 >> Edge(label="History taken", color="blue") >> en2
    en2 >> Edge(label="Saves", color="purple") >> ehr2

    # PHASE 2: WAIT FOR ASSESSMENT (Non-Value-Added)
    p2 >> Edge(label="Waits", color="red", style="dashed") >> p3

    # PHASE 3: ED PHYSICIAN ASSESSMENT
    ehr2 >> Edge(label="Reviews", color="green") >> ed1
    ed1 >> Edge(label="Examines", color="green") >> p4
    p4 >> Edge(label="Examined by", color="blue") >> ed2
    ed2 >> Edge(label="Orders tests", color="green") >> ed3
    ed3 >> Edge(label="Orders", color="green") >> ehr3

    # PHASE 4: SAMPLE COLLECTION
    ehr3 >> Edge(label="Lab orders", color="purple") >> en3
    en3 >> Edge(label="Collects samples", color="purple") >> p4

    # PHASE 5: WAIT FOR RESULTS (Non-Value-Added)
    p4 >> Edge(label="Waits", color="red", style="dashed") >> p5
    en3 >> Edge(label="Monitors", color="purple") >> en4

    # PHASE 6: RESULTS & DIAGNOSIS
    ehr3 >> Edge(label="Results", color="green") >> ehr4
    ehr4 >> Edge(label="Reviews", color="green") >> ed4
    ed4 >> Edge(label="Diagnoses", color="green") >> ed5
    ed5 >> Edge(label="Documents", color="green") >> ehr4
    ed5 >> Edge(label="Explains", color="green") >> p6

    # PHASE 7: ADMISSION DECISION & HANDOFF
    ed6 >> Edge(label="⚠️ HANDOFF:\nConsult request", color="red", style="bold") >> h1
    h1 >> Edge(label="Reviews chart", color="orange") >> ehr4
    ehr4 >> Edge(label="Data", color="orange") >> h2
    h2 >> Edge(label="Accepts", color="orange") >> h3
    h3 >> Edge(label="Discusses", color="orange") >> p7

    # PHASE 8: ADMISSION ORDERS
    h4 >> Edge(label="Writes orders", color="orange") >> ehr5
    h5 >> Edge(label="Med orders", color="orange") >> ehr6
    h6 >> Edge(label="Room assigned", color="orange") >> ehr5

    # PHASE 9: WAIT FOR BED (Non-Value-Added)
    p7 >> Edge(label="Waits", color="red", style="dashed") >> p8

    # PHASE 10: FLOOR PREPARATION
    ehr5 >> Edge(label="Notification", color="pink") >> fn1
    fn1 >> Edge(label="Prepares", color="pink") >> fn2

    # PHASE 11: PHARMACY PROCESSING (Parallel)
    ehr6 >> Edge(label="New orders", color="lime") >> ph1
    ph1 >> Edge(label="⚠️ SAFETY CHECK", color="red", style="bold") >> ph2
    ph2 >> Edge(label="Verifies", color="lime") >> ph3
    ph3 >> Edge(label="Verified", color="lime") >> ehr6
    ph3 >> Edge(label="Prepares", color="lime") >> ph4

    # PHASE 12: PATIENT TRANSPORT
    en4 >> Edge(label="Prepares", color="purple") >> en5
    en5 >> Edge(label="Transports", color="purple") >> p9

    # PHASE 13: CRITICAL HANDOFF
    p9 >> Edge(label="Arrives", color="blue") >> fn3
    en5 >> Edge(label="⚠️ HANDOFF:\nSBAR Report", color="red", style="bold") >> en6
    en6 >> Edge(label="Report given", color="red", style="bold") >> fn3

    # PHASE 14: FLOOR ADMISSION & SAFETY CHECKS
    fn3 >> Edge(label="⚠️ SAFETY CHECK", color="red", style="bold") >> fn4
    fn4 >> Edge(label="Verified", color="pink") >> p10
    fn4 >> Edge(label="Assesses", color="pink") >> fn5
    fn5 >> Edge(label="Assessment", color="pink") >> p10
    fn5 >> Edge(label="Reviews orders", color="pink") >> fn6
    fn6 >> Edge(label="Checks", color="pink") >> ehr5
    fn6 >> Edge(label="Educates", color="pink") >> fn7
    fn7 >> Edge(label="Education", color="pink") >> p10

    # PHASE 15: MEDICATION ADMINISTRATION
    ph4 >> Edge(label="Delivers", color="lime") >> ph5
    ph5 >> Edge(label="Meds delivered", color="lime") >> fn8
    fn8 >> Edge(label="⚠️ SAFETY CHECK:\n5 Rights", color="red", style="bold") >> p11
    fn8 >> Edge(label="Documents", color="pink") >> fn9
    fn9 >> Edge(label="Records", color="pink") >> ehr8

print("✓ PNG and DOT files generated")

# Convert to Draw.io
try:
    subprocess.run([
        "graphviz2drawio",
        "diagrams/HospitalWorkflow/hospital_admission_workflow_v2.dot",
        "-o",
        "diagrams/HospitalWorkflow/hospital_admission_workflow_v2.drawio"
    ], check=True)
    print("✓ Draw.io file generated")
except:
    print("✗ graphviz2drawio not found (optional)")

print("\n" + "="*80)
print("HOSPITAL ADMISSION WORKFLOW - IHI QUALITY IMPROVEMENT APPROACH")
print("="*80)
print("\n🎯 AIM STATEMENT:")
print("   To safely and efficiently admit patients from the Emergency Department")
print("   to the hospital floor within 4 hours, with zero handoff-related errors.")
print("\n📊 KEY MEASURES:")
print("\n   OUTCOME MEASURES:")
print("   • Total ED to Floor time: Target <4 hours (Current: 4-8 hours)")
print("   • Handoff-related errors: Target 0 (High-risk points identified)")
print("   • Patient satisfaction: Target >90%")
print("\n   PROCESS MEASURES:")
print("   • Time to triage: Target <15 minutes")
print("   • Time to physician assessment: Target <30 minutes")
print("   • Time to admission decision: Target <3 hours")
print("   • Time to bed assignment: Target <30 minutes")
print("   • Pharmacy processing time: Target <30 minutes")
print("\n   BALANCING MEASURES:")
print("   • Staff satisfaction")
print("   • Medication errors")
print("   • Patient falls")
print("\n⏱️ TIME ANALYSIS:")
print("\n   VALUE-ADDED TIME (Direct patient care):")
print("   • Triage: 10 min")
print("   • Physical exam: 15 min")
print("   • Sample collection: 10 min")
print("   • Diagnosis discussion: 10 min")
print("   • Admission assessment: 20 min")
print("   • Patient education: 10 min")
print("   • Medication administration: 10 min")
print("   TOTAL VALUE-ADDED: ~85 minutes (29% of total time)")
print("\n   NON-VALUE-ADDED TIME (Waste):")
print("   • Wait for assessment: 15-30 min")
print("   • Wait for results: 60-120 min")
print("   • Wait for bed: 30-60 min")
print("   TOTAL WASTE: ~105-210 minutes (71% of total time)")
print("\n   OPPORTUNITY: Reduce non-value-added time by 50%")
print("\n⚠️ HIGH-RISK HANDOFF POINTS (3 Critical):")
print("\n   1. ED NURSE → ED PHYSICIAN")
print("      Risk: Incomplete triage information")
print("      Mitigation: Standardized triage template")
print("\n   2. ED PHYSICIAN → HOSPITALIST")
print("      Risk: Incomplete clinical picture")
print("      Mitigation: SBAR format, EHR review")
print("\n   3. ED NURSE → FLOOR NURSE")
print("      Risk: Lost information during transport")
print("      Mitigation: Structured handoff tool, bedside report")
print("\n✅ SAFETY CHECKPOINTS (4 Critical):")
print("\n   1. TRIAGE (ED Nurse)")
print("      • Vital signs documented")
print("      • Chief complaint recorded")
print("      • Pain assessed")
print("\n   2. MEDICATION REVIEW (Pharmacist)")
print("      • Allergy check")
print("      • Drug interaction screening")
print("      • Duplicate therapy check")
print("      • Appropriate dosing verified")
print("\n   3. PATIENT IDENTIFICATION (Floor Nurse)")
print("      • Two patient identifiers")
print("      • Allergy band verification")
print("      • Fall risk assessment")
print("\n   4. MEDICATION ADMINISTRATION (Floor Nurse)")
print("      • Right patient")
print("      • Right drug")
print("      • Right dose")
print("      • Right route")
print("      • Right time")
print("\n🔄 PDSA CYCLE OPPORTUNITIES:")
print("\n   PLAN: Test parallel processing of pharmacy orders")
print("   • Start pharmacy review during ED assessment")
print("   • Goal: Reduce pharmacy processing time by 50%")
print("\n   DO: Pilot on one unit for 2 weeks")
print("   • Pharmacist embedded in ED")
print("   • Real-time order review")
print("\n   STUDY: Measure results")
print("   • Pharmacy processing time")
print("   • Medication errors")
print("   • Staff satisfaction")
print("\n   ACT: Implement if successful")
print("   • Spread to all units")
print("   • Standardize process")
print("\n💡 IMPROVEMENT OPPORTUNITIES:")
print("\n   1. REDUCE WAIT TIMES:")
print("      • Implement bed management system")
print("      • Create discharge-by-noon protocol")
print("      • Use predictive analytics for bed needs")
print("\n   2. IMPROVE HANDOFFS:")
print("      • Standardize SBAR format")
print("      • Use electronic handoff tool")
print("      • Implement bedside handoff protocol")
print("\n   3. ENHANCE SAFETY:")
print("      • Barcode medication administration")
print("      • Electronic medication reconciliation")
print("      • Automated allergy checking")
print("\n   4. INCREASE EFFICIENCY:")
print("      • Parallel processing where possible")
print("      • Reduce duplicate documentation")
print("      • Streamline order entry")
print("\n📈 EXPECTED OUTCOMES:")
print("   • 50% reduction in total admission time")
print("   • Zero handoff-related errors")
print("   • 95% patient satisfaction")
print("   • Improved staff satisfaction")
print("   • Reduced medication errors")
print("\n🎓 IHI MODEL FOR IMPROVEMENT:")
print("   This workflow supports continuous quality improvement through:")
print("   • Clear aim statement")
print("   • Measurable outcomes")
print("   • Identified change opportunities")
print("   • PDSA cycle framework")
print("   • Focus on patient safety and experience")
print("="*80)

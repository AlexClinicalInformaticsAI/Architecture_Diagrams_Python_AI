"""
Hospital Admission Workflow - Swim Lane Diagram
Complete patient admission process from ED to hospital floor

This diagram shows the step-by-step workflow for admitting a patient
from the Emergency Department to a hospital floor, with all key participants
and their interactions with the EHR system.

Participants (Swim Lanes):
1. Patient
2. ED Nurse
3. ED Doctor
4. Hospitalist
5. Floor Nurse
6. Pharmacist
7. EHR System

Generates PNG, DOT, and Draw.io format diagrams
"""

import subprocess
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users, Client
from diagrams.generic.blank import Blank
from diagrams.generic.storage import Storage
from diagrams.generic.database import SQL
from diagrams.programming.framework import Fastapi
from diagrams.onprem.compute import Server
import os

# Graph attributes for swim lane layout
graph_attr = {
    "splines": "ortho",
    "nodesep": "1.0",
    "ranksep": "1.5",
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "rankdir": "TB"  # Top to bottom for swim lanes
}

# Swim lane colors
patient_color = "#E3F2FD"      # Light Blue
ed_nurse_color = "#F3E5F5"     # Light Purple
ed_doctor_color = "#E8F5E9"    # Light Green
hospitalist_color = "#FFF3E0"  # Light Orange
floor_nurse_color = "#FCE4EC"  # Light Pink
pharmacist_color = "#F1F8E9"   # Light Lime
ehr_color = "#E0F2F1"          # Light Teal

with Diagram(
    "Hospital Admission Workflow - ED to Floor",
    filename="diagrams/HospitalWorkflow/hospital_admission_workflow",
    outformat=["png", "dot"],
    show=False,
    direction="TB",
    graph_attr=graph_attr
):

    # SWIM LANE 1: PATIENT
    with Cluster("Patient", graph_attr={"bgcolor": patient_color, "style": "rounded"}):
        p1 = Users("Arrives at ED\nwith symptoms")
        p2 = Users("Provides\nmedical history")
        p3 = Users("Undergoes\nexamination")
        p4 = Users("Receives\ndiagnosis")
        p5 = Users("Consents to\nadmission")
        p6 = Users("Transported\nto floor")
        p7 = Users("Settled in\nroom")
        p8 = Users("Receives\nmedications")

    # SWIM LANE 2: ED NURSE
    with Cluster("ED Nurse", graph_attr={"bgcolor": ed_nurse_color, "style": "rounded"}):
        en1 = Client("Triages patient\n(vitals, chief complaint)")
        en2 = Client("Documents in EHR\n(initial assessment)")
        en3 = Client("Collects samples\n(labs ordered)")
        en4 = Client("Monitors patient\n(ongoing vitals)")
        en5 = Client("Prepares for\ntransport")
        en6 = Client("Gives report\nto floor nurse")

    # SWIM LANE 3: ED DOCTOR
    with Cluster("ED Doctor", graph_attr={"bgcolor": ed_doctor_color, "style": "rounded"}):
        ed1 = Client("Reviews triage\nnotes in EHR")
        ed2 = Client("Examines patient\n(physical exam)")
        ed3 = Client("Orders tests\n(labs, imaging)")
        ed4 = Client("Reviews results\nin EHR")
        ed5 = Client("Makes diagnosis\n(documents in EHR)")
        ed6 = Client("Decides admission\nneeded")
        ed7 = Client("Consults\nHospitalist")

    # SWIM LANE 4: HOSPITALIST
    with Cluster("Hospitalist", graph_attr={"bgcolor": hospitalist_color, "style": "rounded"}):
        h1 = Client("Receives consult\nrequest")
        h2 = Client("Reviews patient\ndata in EHR")
        h3 = Client("Accepts patient\nfor admission")
        h4 = Client("Writes admission\norders in EHR")
        h5 = Client("Orders medications\nin EHR")
        h6 = Client("Assigns to\nfloor/room")

    # SWIM LANE 5: FLOOR NURSE
    with Cluster("Floor Nurse", graph_attr={"bgcolor": floor_nurse_color, "style": "rounded"}):
        fn1 = Client("Receives admission\nnotification")
        fn2 = Client("Prepares room\n(equipment, supplies)")
        fn3 = Client("Receives patient\nfrom ED")
        fn4 = Client("Reviews orders\nin EHR")
        fn5 = Client("Performs admission\nassessment")
        fn6 = Client("Documents in EHR\n(nursing assessment)")
        fn7 = Client("Administers\nmedications")

    # SWIM LANE 6: PHARMACIST
    with Cluster("Pharmacist", graph_attr={"bgcolor": pharmacist_color, "style": "rounded"}):
        ph1 = Client("Receives medication\norders from EHR")
        ph2 = Client("Reviews for\ninteractions/allergies")
        ph3 = Client("Verifies orders\nin EHR")
        ph4 = Client("Prepares/dispenses\nmedications")
        ph5 = Client("Delivers to\nfloor")

    # SWIM LANE 7: EHR SYSTEM
    with Cluster("EHR System", graph_attr={"bgcolor": ehr_color, "style": "rounded"}):
        ehr1 = SQL("Patient\nRegistration")
        ehr2 = SQL("Triage\nDocumentation")
        ehr3 = SQL("Order Entry\nSystem")
        ehr4 = SQL("Lab/Imaging\nResults")
        ehr5 = SQL("Admission\nOrders")
        ehr6 = SQL("Medication\nOrders")
        ehr7 = SQL("Nursing\nDocumentation")
        ehr8 = SQL("Medication\nAdministration Record")

    # WORKFLOW CONNECTIONS - Following the admission process chronologically

    # Step 1: Patient arrives and triage
    p1 >> Edge(label="1. Arrives", color="blue") >> en1
    en1 >> Edge(label="2. Documents", color="purple") >> ehr2
    en1 >> Edge(label="3. Takes history", color="blue") >> p2

    # Step 2: ED Doctor assessment
    ehr2 >> Edge(label="4. Reviews", color="green") >> ed1
    ed1 >> Edge(label="5. Examines", color="green") >> p3
    ed2 >> Edge(label="6. Orders tests", color="green") >> ehr3

    # Step 3: ED Nurse collects samples
    ehr3 >> Edge(label="7. Lab orders", color="purple") >> en3
    en3 >> Edge(label="8. Monitors", color="purple") >> p3

    # Step 4: Results and diagnosis
    ehr3 >> Edge(label="9. Results ready", color="green") >> ehr4
    ehr4 >> Edge(label="10. Reviews", color="green") >> ed4
    ed5 >> Edge(label="11. Documents diagnosis", color="green") >> ehr4
    ed5 >> Edge(label="12. Explains", color="green") >> p4

    # Step 5: Admission decision
    ed6 >> Edge(label="13. Requests consult", color="green") >> h1
    h1 >> Edge(label="14. Reviews chart", color="orange") >> ehr4
    h2 >> Edge(label="15. Accepts", color="orange") >> ed7

    # Step 6: Patient consent
    ed7 >> Edge(label="16. Discusses admission", color="green") >> p5

    # Step 7: Admission orders
    h4 >> Edge(label="17. Writes orders", color="orange") >> ehr5
    h5 >> Edge(label="18. Medication orders", color="orange") >> ehr6
    h6 >> Edge(label="19. Assigns room", color="orange") >> ehr5

    # Step 8: Floor notification
    ehr5 >> Edge(label="20. Notification", color="pink") >> fn1
    fn1 >> Edge(label="21. Prepares", color="pink") >> fn2

    # Step 9: Pharmacy processing
    ehr6 >> Edge(label="22. New orders", color="lime") >> ph1
    ph2 >> Edge(label="23. Reviews", color="lime") >> ehr6
    ph3 >> Edge(label="24. Verifies", color="lime") >> ehr6
    ph4 >> Edge(label="25. Dispenses", color="lime") >> ph5

    # Step 10: Patient transport
    en5 >> Edge(label="26. Prepares transport", color="purple") >> p6
    p6 >> Edge(label="27. Arrives", color="blue") >> fn3

    # Step 11: Handoff
    en6 >> Edge(label="28. Report", color="purple") >> fn3

    # Step 12: Floor admission
    fn3 >> Edge(label="29. Reviews", color="pink") >> ehr5
    fn4 >> Edge(label="30. Checks orders", color="pink") >> ehr5
    fn5 >> Edge(label="31. Assesses", color="pink") >> p7
    fn6 >> Edge(label="32. Documents", color="pink") >> ehr7

    # Step 13: Medication administration
    ph5 >> Edge(label="33. Delivers meds", color="lime") >> fn7
    fn7 >> Edge(label="34. Administers", color="pink") >> p8
    fn7 >> Edge(label="35. Documents", color="pink") >> ehr8

print("✓ PNG and DOT files generated")

# Convert to Draw.io
try:
    subprocess.run([
        "graphviz2drawio",
        "diagrams/HospitalWorkflow/hospital_admission_workflow.dot",
        "-o",
        "diagrams/HospitalWorkflow/hospital_admission_workflow.drawio"
    ], check=True)
    print("✓ Draw.io file generated")
except:
    print("✗ graphviz2drawio not found (optional)")

print("\n" + "="*80)
print("HOSPITAL ADMISSION WORKFLOW SUMMARY")
print("="*80)
print("\nWorkflow: Emergency Department to Hospital Floor Admission")
print("\nParticipants (Swim Lanes):")
print("  1. Patient - The individual receiving care")
print("  2. ED Nurse - Emergency Department nursing staff")
print("  3. ED Doctor - Emergency Department physician")
print("  4. Hospitalist - Admitting physician")
print("  5. Floor Nurse - Inpatient unit nursing staff")
print("  6. Pharmacist - Medication management specialist")
print("  7. EHR System - Electronic Health Record system")
print("\nKey Process Steps (35 total):")
print("\n  PHASE 1: ED ARRIVAL & TRIAGE (Steps 1-3)")
print("    • Patient arrives with symptoms")
print("    • ED Nurse performs triage (vitals, chief complaint)")
print("    • Initial documentation in EHR")
print("    • Medical history collection")
print("\n  PHASE 2: ED ASSESSMENT (Steps 4-8)")
print("    • ED Doctor reviews triage notes")
print("    • Physical examination performed")
print("    • Diagnostic tests ordered (labs, imaging)")
print("    • ED Nurse collects samples")
print("    • Patient monitoring continues")
print("\n  PHASE 3: DIAGNOSIS (Steps 9-12)")
print("    • Lab/imaging results reviewed")
print("    • ED Doctor makes diagnosis")
print("    • Diagnosis documented in EHR")
print("    • Patient informed of findings")
print("\n  PHASE 4: ADMISSION DECISION (Steps 13-16)")
print("    • ED Doctor determines admission needed")
print("    • Hospitalist consult requested")
print("    • Hospitalist reviews patient data")
print("    • Hospitalist accepts patient")
print("    • Patient consents to admission")
print("\n  PHASE 5: ADMISSION ORDERS (Steps 17-19)")
print("    • Hospitalist writes admission orders")
print("    • Medication orders entered")
print("    • Room assignment made")
print("\n  PHASE 6: FLOOR PREPARATION (Steps 20-21)")
print("    • Floor Nurse receives notification")
print("    • Room prepared with equipment/supplies")
print("\n  PHASE 7: PHARMACY PROCESSING (Steps 22-25)")
print("    • Pharmacist receives medication orders")
print("    • Drug interaction/allergy review")
print("    • Orders verified in EHR")
print("    • Medications prepared and dispensed")
print("\n  PHASE 8: PATIENT TRANSPORT (Steps 26-28)")
print("    • ED Nurse prepares patient for transport")
print("    • Patient transported to floor")
print("    • Nursing handoff report given")
print("\n  PHASE 9: FLOOR ADMISSION (Steps 29-32)")
print("    • Floor Nurse receives patient")
print("    • Admission orders reviewed")
print("    • Nursing admission assessment performed")
print("    • Assessment documented in EHR")
print("\n  PHASE 10: MEDICATION ADMINISTRATION (Steps 33-35)")
print("    • Pharmacist delivers medications to floor")
print("    • Floor Nurse administers medications")
print("    • Administration documented in MAR")
print("\nEHR System Touchpoints:")
print("  • Patient Registration - Initial patient record")
print("  • Triage Documentation - Vital signs, chief complaint")
print("  • Order Entry System - Labs, imaging, medications")
print("  • Lab/Imaging Results - Diagnostic findings")
print("  • Admission Orders - Hospitalist orders")
print("  • Medication Orders - Prescriptions and dosing")
print("  • Nursing Documentation - Assessments and care")
print("  • Medication Administration Record - Med tracking")
print("\nCritical Handoffs:")
print("  1. ED Nurse → ED Doctor (triage to assessment)")
print("  2. ED Doctor → Hospitalist (admission consult)")
print("  3. Hospitalist → Floor Nurse (admission orders)")
print("  4. Pharmacist → Floor Nurse (medication delivery)")
print("  5. ED Nurse → Floor Nurse (patient handoff)")
print("\nQuality & Safety Checkpoints:")
print("  • Triage assessment (ED Nurse)")
print("  • Diagnostic workup (ED Doctor)")
print("  • Admission appropriateness (Hospitalist)")
print("  • Medication safety review (Pharmacist)")
print("  • Admission assessment (Floor Nurse)")
print("  • Medication administration verification (Floor Nurse)")
print("\nTypical Timeline:")
print("  • ED Triage to Assessment: 15-30 minutes")
print("  • Assessment to Diagnosis: 2-4 hours")
print("  • Admission Decision to Orders: 30-60 minutes")
print("  • Orders to Floor Notification: 15-30 minutes")
print("  • Pharmacy Processing: 30-60 minutes")
print("  • Transport to Floor: 15-30 minutes")
print("  • Floor Admission Process: 30-45 minutes")
print("  • Total ED to Floor Time: 4-8 hours (typical)")
print("\nKey Success Factors:")
print("  • Clear communication between all parties")
print("  • Accurate and timely EHR documentation")
print("  • Efficient order processing")
print("  • Proper medication reconciliation")
print("  • Thorough patient handoffs")
print("  • Coordinated care transitions")
print("="*80)

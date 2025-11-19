# Hospital Admission Workflow - ED to Floor

## Overview

This swim lane diagram illustrates the complete patient admission process from the Emergency Department (ED) to a hospital floor. It shows the interactions between all key participants and the Electronic Health Record (EHR) system throughout the admission journey.

## Participants (Swim Lanes)

### 1. **Patient**
The individual receiving medical care, progressing through the admission process.

### 2. **ED Nurse**
Emergency Department nursing staff responsible for:
- Initial triage and vital signs
- Sample collection for ordered tests
- Patient monitoring
- Documentation in EHR
- Patient transport preparation
- Handoff to floor nurse

### 3. **ED Doctor**
Emergency Department physician responsible for:
- Patient examination
- Diagnostic test ordering
- Result interpretation
- Diagnosis determination
- Admission decision
- Hospitalist consultation

### 4. **Hospitalist**
Admitting physician responsible for:
- Reviewing patient data
- Accepting patient for admission
- Writing admission orders
- Medication ordering
- Room assignment

### 5. **Floor Nurse**
Inpatient unit nursing staff responsible for:
- Room preparation
- Receiving patient from ED
- Admission assessment
- Order review and implementation
- Medication administration
- Documentation

### 6. **Pharmacist**
Medication management specialist responsible for:
- Reviewing medication orders
- Checking for drug interactions
- Verifying allergies
- Order verification in EHR
- Medication preparation and dispensing
- Delivery to nursing unit

### 7. **EHR System**
Electronic Health Record system providing:
- Patient registration
- Clinical documentation
- Order entry and management
- Results reporting
- Medication administration tracking
- Care coordination

---

## Workflow Phases

### Phase 1: ED Arrival & Triage (Steps 1-3)
**Duration**: 15-30 minutes

1. **Patient arrives** at Emergency Department with symptoms
2. **ED Nurse performs triage**:
   - Vital signs (blood pressure, heart rate, temperature, oxygen saturation)
   - Chief complaint documentation
   - Pain assessment
   - Initial acuity determination
3. **Documentation in EHR**: Triage notes entered
4. **Medical history collection**: Allergies, medications, past medical history

**Key Outputs**:
- Triage category assigned
- Initial vital signs recorded
- Chief complaint documented
- Patient registered in EHR

---

### Phase 2: ED Assessment (Steps 4-8)
**Duration**: 2-4 hours

5. **ED Doctor reviews** triage notes in EHR
6. **Physical examination** performed
7. **Diagnostic tests ordered**:
   - Laboratory tests (CBC, metabolic panel, cardiac markers, etc.)
   - Imaging studies (X-ray, CT, ultrasound, etc.)
   - EKG if indicated
8. **ED Nurse collects samples** for ordered tests
9. **Patient monitoring** continues with ongoing vital signs

**Key Outputs**:
- Physical exam findings documented
- Diagnostic orders placed
- Samples collected and sent to lab
- Continuous monitoring established

---

### Phase 3: Diagnosis (Steps 9-12)
**Duration**: 30-60 minutes after results available

10. **Lab/imaging results** become available in EHR
11. **ED Doctor reviews results**
12. **Diagnosis made** and documented
13. **Patient informed** of findings and treatment plan

**Key Outputs**:
- Diagnosis established
- Results reviewed and interpreted
- Patient education provided
- Treatment plan discussed

---

### Phase 4: Admission Decision (Steps 13-16)
**Duration**: 30-60 minutes

14. **ED Doctor determines** admission is necessary
15. **Hospitalist consult** requested through EHR
16. **Hospitalist reviews** patient data:
    - Triage notes
    - Physical exam findings
    - Lab and imaging results
    - Current vital signs
17. **Hospitalist accepts** patient for admission
18. **Patient consents** to admission after discussion

**Key Outputs**:
- Admission decision documented
- Hospitalist accepts patient
- Patient consent obtained
- Admission process initiated

---

### Phase 5: Admission Orders (Steps 17-19)
**Duration**: 15-30 minutes

19. **Hospitalist writes admission orders** in EHR:
    - Admitting diagnosis
    - Condition level (stable, fair, critical)
    - Diet orders
    - Activity level
    - Vital sign frequency
    - Nursing care orders
20. **Medication orders** entered:
    - Home medications to continue
    - New medications
    - PRN (as needed) medications
    - IV fluids if needed
21. **Room assignment** made based on:
    - Patient acuity
    - Isolation requirements
    - Bed availability
    - Unit specialization

**Key Outputs**:
- Complete admission orders in EHR
- Medication orders entered
- Room assigned
- Care plan established

---

### Phase 6: Floor Preparation (Steps 20-21)
**Duration**: 15-30 minutes

22. **Floor Nurse receives** admission notification from EHR
23. **Room prepared** with:
    - Clean linens
    - Medical equipment (IV pole, oxygen, monitors)
    - Supplies (gloves, gowns, etc.)
    - Patient belongings storage
    - Call bell tested

**Key Outputs**:
- Room ready for patient
- Equipment checked and functional
- Supplies stocked
- Floor nurse prepared for admission

---

### Phase 7: Pharmacy Processing (Steps 22-25)
**Duration**: 30-60 minutes

24. **Pharmacist receives** medication orders from EHR
25. **Drug interaction review**:
    - Check against patient allergies
    - Review for drug-drug interactions
    - Verify appropriate dosing
    - Check for duplicate therapy
26. **Orders verified** in EHR
27. **Medications prepared**:
    - First doses prepared
    - Unit dose packaging
    - IV admixtures if needed
28. **Medications delivered** to nursing unit

**Key Outputs**:
- Medications verified safe
- First doses prepared
- Medications delivered to floor
- Documentation in EHR

---

### Phase 8: Patient Transport (Steps 26-28)
**Duration**: 15-30 minutes

29. **ED Nurse prepares** patient for transport:
    - Ensures patient stable
    - Gathers belongings
    - Prints transport paperwork
    - Coordinates with transport team
30. **Patient transported** to floor via stretcher or wheelchair
31. **Nursing handoff** given:
    - SBAR format (Situation, Background, Assessment, Recommendation)
    - Current condition
    - Recent vital signs
    - Pending orders or concerns
    - Patient/family questions

**Key Outputs**:
- Patient safely transported
- Complete handoff communication
- Belongings transferred
- ED documentation complete

---

### Phase 9: Floor Admission (Steps 29-32)
**Duration**: 30-45 minutes

32. **Floor Nurse receives** patient
33. **Admission orders reviewed** in EHR
34. **Nursing admission assessment** performed:
    - Full vital signs
    - Head-to-toe physical assessment
    - Pain assessment
    - Fall risk assessment
    - Skin assessment
    - Psychosocial assessment
    - Patient/family education needs
35. **Assessment documented** in EHR

**Key Outputs**:
- Patient settled in room
- Complete nursing assessment
- Baseline established
- Care plan initiated

---

### Phase 10: Medication Administration (Steps 33-35)
**Duration**: 15-30 minutes

36. **Pharmacist delivers** medications to floor
37. **Floor Nurse administers** medications:
    - Verifies patient identity (two identifiers)
    - Reviews medication orders
    - Checks for allergies
    - Explains medications to patient
    - Administers medications
    - Monitors for adverse reactions
38. **Administration documented** in Medication Administration Record (MAR)

**Key Outputs**:
- Medications administered safely
- Patient educated about medications
- Documentation complete
- Monitoring plan established

---

## EHR System Components

### 1. **Patient Registration**
- Demographics
- Insurance information
- Emergency contacts
- Medical record number (MRN)

### 2. **Triage Documentation**
- Vital signs
- Chief complaint
- Triage category
- Initial assessment

### 3. **Order Entry System**
- Laboratory orders
- Imaging orders
- Medication orders
- Nursing orders
- Dietary orders

### 4. **Lab/Imaging Results**
- Laboratory values
- Radiology reports
- Pathology results
- Critical value alerts

### 5. **Admission Orders**
- Admitting diagnosis
- Condition level
- Care plan
- Activity orders
- Diet orders

### 6. **Medication Orders**
- Prescriptions
- Dosing schedules
- Route of administration
- Special instructions

### 7. **Nursing Documentation**
- Assessments
- Vital signs
- Intake/output
- Care interventions
- Patient education

### 8. **Medication Administration Record (MAR)**
- Scheduled medications
- PRN medications
- Administration times
- Nurse signatures

---

## Critical Handoffs

### 1. **ED Nurse → ED Doctor**
**When**: After triage completion  
**Information**: Vital signs, chief complaint, initial assessment, patient concerns

### 2. **ED Doctor → Hospitalist**
**When**: Admission decision made  
**Information**: Diagnosis, test results, treatment provided, admission rationale

### 3. **Hospitalist → Floor Nurse**
**When**: Admission orders written  
**Information**: Admission orders, care plan, special considerations

### 4. **Pharmacist → Floor Nurse**
**When**: Medications prepared  
**Information**: Medication details, special instructions, storage requirements

### 5. **ED Nurse → Floor Nurse**
**When**: Patient transport  
**Information**: SBAR report, current condition, pending issues, family concerns

---

## Quality & Safety Checkpoints

### Patient Identification
- Two patient identifiers used at every interaction
- Wristband verification
- Verbal confirmation when possible

### Medication Safety
- Five Rights: Right patient, drug, dose, route, time
- Allergy verification
- Drug interaction screening
- Double-check for high-risk medications

### Communication
- SBAR format for handoffs
- Read-back verification for verbal orders
- Closed-loop communication
- Family involvement when appropriate

### Documentation
- Real-time documentation in EHR
- Complete and accurate information
- Timely order entry
- Proper authentication

### Infection Control
- Hand hygiene before and after patient contact
- Appropriate PPE use
- Isolation precautions when indicated
- Environmental cleaning

---

## Typical Timeline

| Phase | Duration | Cumulative Time |
|-------|----------|-----------------|
| ED Arrival & Triage | 15-30 min | 0:15-0:30 |
| ED Assessment | 2-4 hours | 2:15-4:30 |
| Diagnosis | 30-60 min | 2:45-5:30 |
| Admission Decision | 30-60 min | 3:15-6:30 |
| Admission Orders | 15-30 min | 3:30-7:00 |
| Floor Preparation | 15-30 min | 3:45-7:30 |
| Pharmacy Processing | 30-60 min | 4:15-8:30 |
| Patient Transport | 15-30 min | 4:30-9:00 |
| Floor Admission | 30-45 min | 5:00-9:45 |
| Medication Administration | 15-30 min | 5:15-10:15 |

**Total Time**: 4-8 hours (typical)

*Note: Times vary based on patient acuity, ED volume, bed availability, and complexity of care needs.*

---

## Common Delays and Solutions

### Delay: Waiting for Lab Results
**Solution**: 
- Stat orders for urgent tests
- Point-of-care testing when available
- Parallel processing of multiple tests

### Delay: Bed Availability
**Solution**:
- Bed management system
- Discharge planning earlier in the day
- Boarding protocols in ED
- Surge capacity plans

### Delay: Hospitalist Availability
**Solution**:
- Dedicated admitting hospitalist
- Clear escalation pathways
- Telemedicine consultations
- Admission criteria protocols

### Delay: Pharmacy Processing
**Solution**:
- Pharmacist presence in ED
- Automated dispensing cabinets
- First-dose medications from ED
- Priority processing for admissions

### Delay: Transport Availability
**Solution**:
- Dedicated transport team
- Transport tracking system
- Nurse-assisted transport when appropriate
- Clear transport protocols

---

## Key Success Factors

### 1. **Communication**
- Clear, concise handoffs
- Standardized communication tools (SBAR)
- Real-time updates
- Team huddles

### 2. **Technology**
- Integrated EHR system
- Real-time order processing
- Electronic notifications
- Mobile access to patient information

### 3. **Coordination**
- Bed management system
- Care coordination team
- Admission navigator role
- Multidisciplinary rounds

### 4. **Efficiency**
- Streamlined processes
- Parallel workflows
- Reduced redundancy
- Continuous improvement

### 5. **Patient-Centered Care**
- Patient and family involvement
- Clear communication with patient
- Comfort and dignity maintained
- Cultural sensitivity

---

## Regulatory Considerations

### The Joint Commission Requirements
- National Patient Safety Goals
- Medication reconciliation
- Hand hygiene compliance
- Patient identification protocols

### CMS Requirements
- Two-midnight rule for admissions
- Observation vs. inpatient status
- Documentation requirements
- Quality measures

### HIPAA Compliance
- Privacy during handoffs
- Secure EHR access
- Minimum necessary information
- Patient consent

---

## Metrics and KPIs

### Efficiency Metrics
- ED length of stay
- Time to admission decision
- Time to bed assignment
- Time to first medication

### Quality Metrics
- Medication errors
- Patient falls
- Hospital-acquired infections
- Readmission rates

### Patient Experience
- Patient satisfaction scores
- Communication ratings
- Pain management effectiveness
- Discharge preparedness

---

## Diagram Generation

To generate the workflow diagram:

```bash
python hospital_admission_workflow.py
```

This creates:
- `hospital_admission_workflow.png` - Visual diagram
- `hospital_admission_workflow.dot` - GraphViz source
- `hospital_admission_workflow.drawio` - Editable Draw.io format

---

## Related Workflows

- **ED Discharge Process**
- **Surgical Admission Workflow**
- **ICU Transfer Workflow**
- **Hospital Discharge Planning**
- **Observation to Inpatient Conversion**

---

*This workflow represents a typical hospital admission process. Actual processes may vary by institution, patient acuity, and specific circumstances.*

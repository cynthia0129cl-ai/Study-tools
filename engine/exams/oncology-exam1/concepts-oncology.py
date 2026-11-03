# One concept card per concept, in teaching order. "points" are the facts shown on a Fix my misses card.
# They are also the Key ideas of the guide section with the same id, so card and guide always agree.
C = lambda id, unit, title, points, source: dict(id=id, unit=unit, title=title, points=points, source=source)
CONCEPTS = [
 # ---- Cancer risk factors
 C("c-risk-list", "risk", "The risk factor categories", [
  "The nine risk factor categories are carcinogens, environment, hormones, genetics, lifestyle, infectious disease, medications, immune status and nutrition.",
  "Carcinogen exposure is the most common risk factor, and risks are cumulative.",
  "Age and genetics cannot be changed; 5 to 10% of cancers come from known genetic syndromes such as BRCA1/2.",
  "Hereditary red flags are multiple primaries, bilateral tumors in paired organs, a younger-than-usual age, a tumor in the sex not usually affected, and two or more first-degree relatives with the same cancer.",
  "BRCA2 also raises the risk of pancreatic and prostate cancer and melanoma."], "study guide, Ch 13"),
 C("c-risk-table", "risk", "Risk factors by cancer (Table 13.2)", [
  "Cervical cancer: HPV, multiple partners, early sexual contact, tobacco use.",
  "Gastric cancer: H. pylori, alcohol, ulcers, smoking. Liver cancer: alcohol and hepatitis A, B or C.",
  "Testicular cancer: undescended testicle is the greatest risk. Lung cancer: tobacco, asbestos, coal, soot, tar, pollution, wood dust.",
  "Uterine cancer: estrogen therapy without progesterone, obesity, tamoxifen, PCOS, diabetes."], "study guide, Ch 13 Table 13.2"),
 C("c-risk-prev", "risk", "Levels of prevention", [
  "Primary prevention: risk factor modification, immunization (HPV, hepatitis), chemoprevention and avoiding carcinogens.",
  "Secondary prevention: screening for early detection (breast, cervical, colon, prostate).",
  "Tertiary prevention: reducing morbidity and mortality once disease is diagnosed."], "study guide, Ch 13 and class notes"),
 C("c-risk-caution", "risk", "CAUTION warning signs", [
  "C change in bowel or bladder habits; A a sore that does not heal; U unusual bleeding or discharge; T thickening or lump.",
  "I indigestion or difficulty swallowing; O obvious change in a wart or mole; N nagging cough or hoarseness.",
  "A sign lasting more than 2 weeks needs evaluation."], "study guide, Ch 13"),
 # ---- Staging
 C("c-stage-tnm", "stage", "TNM, stages and grade", [
  "T is the size of the tumor, N is the number of lymph nodes involved, and M is the presence of metastasis; M1 means the cancer is not local.",
  "Stage I is small with no obvious spread outside the organ, stage II invades deeper tissue or local nodes, stage III is large or locally advanced, and stage IV has metastasized.",
  "All hematologic malignancies are stage IV at diagnosis.",
  "Grade describes how differentiated the cells are; poorly differentiated cells are more aggressive."], "study guide, Ch 13 and class PLQ"),
 C("c-stage-sizes", "stage", "Size and stage tables", [
  "Breast sizes: 2 cm or less is stage I, 2 to 5 cm is stage II, over 5 cm is stage IIB or III; nodes 4 to 8 is IIIA, up to 9 is IIIB, 10 or more is IIIC.",
  "Prostate: T1 cannot be felt, T2 is confined to the prostate, T3 is locally extensive, T4 invades neighboring organs.",
  "Gleason is two grades of 1 to 5 added together, maximum 10; higher is worse.",
  "Ovarian FIGO: I ovaries, II pelvis, III peritoneum and/or nodes, IV distant."], "study guide, Ch 65 and Ch 66"),
 # ---- Biopsy
 C("c-bx-types", "biopsy", "Biopsy types and what they prove", [
  "A biopsy is the most specific test and is required for a definite diagnosis; labs and imaging are supportive; results take 3 to 10 days.",
  "Excisional biopsy removes the whole mass with a margin and is preferred; incisional (core) biopsy can track cells through normal tissue.",
  "Fine-needle aspiration is less traumatic but gives fewer cells; core needle gives a larger sample; vacuum-assisted uses a probe with no sutures.",
  "A negative sentinel node means no further nodes are removed; a positive one leads to an axillary dissection of 20 to 40 nodes.",
  "A liquid biopsy is a blood test for cancer cells or tumor DNA."], "study guide, Ch 13 and Ch 65"),
 C("c-bx-site", "biopsy", "Biopsy by site", [
  "Ovarian mass: biopsy is not recommended because it could spread cells; the diagnosis is surgical removal with pathology.",
  "Uterine: endometrial biopsy is 99% sensitive for high-grade cancer; a D&C is done if the biopsy is negative but bleeding continues.",
  "Cervical: colposcopy with biopsy after an abnormal Pap; the biopsy is diagnostic.",
  "Lung: bronchoscopy views and biopsies the airways; mediastinoscopy is an incision to biopsy the mediastinum."], "study guide, Ch 13, Ch 26 and Ch 65"),
 C("c-bx-marrow", "biopsy", "Bone marrow aspiration and biopsy", [
  "The most common site is the posterior iliac crest with the client prone or side-lying; the sternum or anterior iliac crest is done supine.",
  "Before: consent, allergies and bleeding risk. The client feels pressure and a brief pulling pain, and the procedure takes 5 to 10 minutes.",
  "After: direct pressure for 5 to 10 minutes, a sterile dressing, rest for several hours, dressing on at least 24 hours.",
  "Report bleeding that soaks the dressing or lasts more than 24 hours, and watch for infection."], "study guide, Ch 33"),
 # ---- Lung
 C("c-lung-types", "lung", "Small cell versus non-small cell", [
  "Small cell is about 15%, grows fast and spreads early, has a poor outlook (class: 6 months to 1 year), and surgery is not the main treatment.",
  "Non-small cell is about 85%, has three types (adenocarcinoma, squamous cell, large cell), is slower, and has a good 5-year survival if found early.",
  "More than 90% of lung cancer is caused by smoking; yearly low-dose CT is for high-risk clients (20 pack-years, current smoker or quit within 15 years)."], "study guide, Ch 26 and class notes"),
 C("c-lung-dx", "lung", "Lung cancer cues and diagnosis", [
  "Cues: new or changed cough, hemoptysis, shortness of breath, wheezing, hoarseness, chest pain, weight loss, frequent pneumonia.",
  "Headache and bone pain suggest metastasis to brain and bone; common sites are brain, bone, adrenal gland and the other lung.",
  "PET shows metabolic activity, not structure; sputum cytology, bronchoscopy and mediastinoscopy obtain cells or tissue."], "study guide, Ch 26"),
 C("c-lung-tx", "lung", "Lung cancer treatment", [
  "Lobectomy removes a lobe, pneumonectomy removes a lung, and a wedge resection removes a small section; surgery is preferred if there is no metastasis.",
  "Chemotherapy is the primary treatment for advanced disease; radiation is used when surgery is not an option or for palliation.",
  "WHO ladder: nonopioid, then moderate opioid plus nonopioid, then strong opioid plus nonopioid, given around the clock.",
  "Palliative care begins at diagnosis."], "study guide, Ch 26"),
 C("c-lung-nursing", "lung", "Lung cancer nursing care and chest tubes", [
  "Give oxygen to keep the SpO₂ at 90% or higher and position the client in semi-Fowler's.",
  "Small frequent meals with supplements; a large meal pushes on the diaphragm.",
  "Never clamp a chest tube; keep the system closed; continuous bubbling in the water-seal chamber is an air leak."], "study guide, Ch 26"),
 # ---- Labs
 C("c-labs-cbc", "labs", "CBC, WBC and ANC", [
  "A CBC uses a lavender (EDTA) tube; PT, INR and PTT use sodium citrate.",
  "A left shift is many immature neutrophils (bands) and means active infection.",
  "Neutropenia is an ANC below 1,500; 500 or below needs neutropenic precautions.",
  "Reticulocytes are immature RBCs: high means the marrow is responding, low means a hypoproliferative marrow.",
  "Low MCV is microcytic (iron deficiency); high MCV is macrocytic (B12 or folate)."], "study guide, Ch 33"),
 C("c-labs-plt", "labs", "Platelet thresholds", [
  "Normal platelets are 150,000 to 450,000/mm³.",
  "Bleeding precautions start below 100,000; spontaneous bleeding is possible below 50,000.",
  "Platelets are usually transfused below 20,000; below 5,000 a fatal CNS or GI bleed is possible."], "study guide, Ch 33 and Ch 34"),
 C("c-labs-iron", "labs", "Iron studies and the iron diet", [
  "In iron deficiency ferritin and transferrin saturation are low, TIBC is high, and the cells are microcytic and hypochromic.",
  "No iron supplements for 24 hours before a serum iron; draw it in the morning.",
  "Eat heme iron (red meat) and nonheme iron (spinach, beans) with vitamin C; dairy blocks absorption."], "study guide, Ch 33 and Ch 34"),
 C("c-labs-coag", "labs", "Clotting studies", [
  "The intrinsic pathway is monitored by PTT and heparin; the extrinsic pathway by PT/INR and warfarin.",
  "The INR goal on warfarin is 2 to 3.",
  "Bleeding time checks platelet function and is not done if platelets are under 75,000; platelet aggregation is impaired by aspirin, NSAIDs and von Willebrand disease."], "study guide, Ch 33"),
 # ---- Leukemia
 C("c-leuk-patho", "leuk", "What leukemia does", [
  "A stem cell mutates into immature blasts that never mature or die, producing leukocytosis.",
  "The crowded marrow cannot make enough RBCs and platelets, so anemia and thrombocytopenia occur.",
  "The blasts cannot fight infection, so neutropenia and infection occur.",
  "AML and ALL are acute and ALL is the most common childhood leukemia; CML and CLL are chronic and can turn acute."], "study guide, Ch 34"),
 C("c-leuk-risk", "leuk", "Leukemia risk factors", [
  "Risk factors are genetic anomalies, Down syndrome, radiation, benzene or chemical exposure, prior chemotherapy or radiation, and smoking.",
  "The Philadelphia chromosome (9;22) is found in more than 90% of CML.",
  "Oil refinery work means benzene exposure, the highest risk factor in the case."], "study guide, Ch 34"),
 C("c-leuk-tx", "leuk", "Leukemia treatment and medications", [
  "Chemotherapy is given in phases: induction (get remission), consolidation (treat hidden disease), maintenance (prevent relapse); remission is not a cure.",
  "AML induction example is daunorubicin plus cytarabine; imatinib targets Bcr-Abl in CML; ibrutinib is used in CLL.",
  "Prophylactic antibiotics, antivirals and antifungals are given during neutropenia.",
  "Radiation to the brain and spine treats CNS disease because chemotherapy cannot cross the blood–brain barrier.",
  "The textbook says G-CSF (filgrastim) is generally not indicated in leukemia."], "study guide, Ch 34"),
 C("c-leuk-nursing", "leuk", "Leukemia nursing priorities", [
  "After chemotherapy the first priority is infection; fever means broad-spectrum IV antibiotics immediately.",
  "Never take a rectal temperature in a neutropenic client.",
  "Teach to avoid dental cleanings when platelets are low, and go to the ED for fever of 102°F, chills or a nosebleed over 10 minutes.",
  "Offer sperm or egg banking before therapy."], "study guide, Ch 34"),
 # ---- Neutropenic precautions
 C("c-neut-def", "neut", "Neutropenia values and fever", [
  "Neutropenia is an ANC below 1,500; precautions start at 500 or below.",
  "A temperature of 100.4°F (38°C) or higher needs immediate care and IV antibiotics.",
  "Fever may be the first and only sign of infection."], "study guide, Ch 13 and Ch 34"),
 C("c-neut-prec", "neut", "Neutropenic precautions (Box 34.2)", [
  "Hand hygiene by everyone, a private room, avoid crowds, sick people, small children and pets.",
  "No live plants or cut flowers, no standing water or humidifiers.",
  "Wash raw fruits and vegetables well; avoid raspberries and blackberries.",
  "No rectal temperatures, suppositories or enemas, because rectal bacteria can enter the blood.",
  "Take prophylactic antimicrobials daily and finish the course; reverse isolation means staff wear PPE to protect the client."], "study guide, Ch 34 and class notes"),
 # ---- Hodgkin
 C("c-hodg-dx", "hodgkin", "Hodgkin lymphoma: signs and diagnosis", [
  "Reed–Sternberg cells define Hodgkin lymphoma; it has a better survival rate than non-Hodgkin lymphoma.",
  "Painless lymph node swelling; B symptoms are low-grade fever, drenching night sweats and weight loss.",
  "Itching is common in Hodgkin lymphoma; a dry cough worse lying flat suggests a mediastinal mass.",
  "A lymph node biopsy is definitive; uric acid and LDH are elevated."], "study guide, Ch 34"),
 C("c-hodg-comp", "hodgkin", "Lymphoma complications and nursing", [
  "Superior vena cava syndrome: facial and arm swelling, dyspnea, chest pain, dysphagia.",
  "Spinal cord compression: back pain, then sensory and motor change; an emergency.",
  "Hypercalcemia above 11 mg/dL: confusion, polyuria, heart block; IV fluids dilute calcium.",
  "Lymphoma staging: I one node, II two or more nodes on one side of the diaphragm, III both sides, IV organs plus nodes.",
  "Teach neutropenic and bleeding precautions before chemotherapy."], "study guide, Ch 34"),
 # ---- Multiple myeloma
 C("c-mm-patho", "mm", "Myeloma: patho and CRAB", [
  "A clone of plasma cells makes an M protein; lytic bone lesions release calcium.",
  "CRAB: hypercalcemia above 11.5, renal insufficiency (creatinine above 2), anemia (Hgb below 10), bone disease.",
  "Excess light chains (Bence Jones protein) are toxic to the kidneys.",
  "Myeloma is an incurable B-cell cancer of plasma cells."], "study guide, Ch 34"),
 C("c-mm-nursing", "mm", "Myeloma nursing interventions", [
  "Encourage fluids to dilute calcium and protect the kidneys; monitor serum and urine calcium, BUN and creatinine.",
  "Encourage ambulation as tolerated and position for comfort.",
  "Bisphosphonates such as ibandronate (Boniva) reduce bone breakdown, which lowers calcium and fractures.",
  "Sudden severe pain or new numbness may mean a fracture or cord compression: report at once.",
  "Thalidomide and lenalidomide are teratogenic."], "study guide, Ch 34 and class notes"),
 # ---- Breast
 C("c-breast-tx", "breast", "Breast cancer treatment", [
  "Lumpectomy is always followed by radiation; with chemotherapy the order is surgery, chemotherapy, then radiation.",
  "Neoadjuvant therapy is given before the primary treatment; adjuvant therapy is given after.",
  "DCIS is stage 0 and requires surgery; LCIS has no treatment and is followed with mammograms."], "study guide, Ch 65"),
 C("c-breast-meds", "breast", "Breast cancer medications (Table 65.3)", [
  "Tamoxifen blocks estrogen at its receptor for 5 to 10 years; avoid SSRIs and question oral contraceptives in estrogen-positive disease.",
  "Aromatase inhibitors (anastrozole, letrozole, exemestane) stop androgens becoming estrogen; they risk osteoporosis and fractures.",
  "Trastuzumab is for HER2-positive tumors and can cause cardiotoxicity; pembrolizumab is immunotherapy with rash, diarrhea and thyroid problems."], "study guide, Ch 65 and Davis Table 65.3"),
 C("c-breast-male", "breast", "Male breast cancer", [
  "It is about 100 times less common than in women, occurs at ages 60 to 70, and BRCA2 is the more common mutation.",
  "With little breast tissue it spreads early to the nipple, skin and muscle; mastectomy is usual.",
  "Hormone therapy is only for receptor-positive tumors, so question antiestrogen therapy in a receptor-negative client.",
  "Ultrasound is used under age 25; mammogram at 25 or older."], "study guide, Ch 66"),
 C("c-breast-nursing", "breast", "Breast cancer nursing care", [
  "Bloody drainage saturating the dressing is the most concerning wound finding; serosanguineous drainage is expected.",
  "Lymphedema follows axillary node removal; shoulder immobility is the most common long-term effect.",
  "Radiation effects: skin redness, itching, desquamation, breast swelling, and pneumonitis 6 weeks to 6 months later.",
  "Breast self-exam is not recommended; screening is by mammography."], "study guide, Ch 65"),
 # ---- Uterine
 C("c-ut-risk", "uterine", "Uterine cancer risk", [
  "The most common gynecologic cancer in the US, usually at ages 55 to 65.",
  "The number one risk factors are unopposed estrogen and obesity; tamoxifen, early menarche, late menopause, PCOS and diabetes add risk.",
  "About 80% are endometrioid adenocarcinoma; anyone on estrogen with a uterus needs progesterone."], "study guide, Ch 65 and Ch 13"),
 C("c-ut-dx", "uterine", "Uterine cancer diagnosis and treatment", [
  "Abnormal uterine or postmenopausal bleeding is the most common symptom and needs evaluation.",
  "Endometrial biopsy first; ultrasound shows a thickened endometrium; D&C if the biopsy is negative but bleeding continues.",
  "Treatment is removal of the uterus, tubes and ovaries; radiation is the usual adjuvant.",
  "Stomatitis: salt-water rinses and avoid hot or spicy food."], "study guide, Ch 65"),
 # ---- Cervical
 C("c-cerv-screen", "cervical", "Cervical screening guidelines", [
  "No screening before age 21; the first Pap is at 21 and is repeated every 3 years until 29.",
  "HPV testing is not a screen at 21 to 29, except as a reflex if atypical cells are found; primary HPV may start at 25 every 5 years.",
  "Ages 30 to 65: primary HPV or Pap plus HPV cotest every 5 years, or Pap alone every 3 years.",
  "Screening may stop after 65 with adequate negative results and no CIN 2 in 20 years."], "study guide, Ch 65 and class PLQ"),
 C("c-cerv-dx", "cervical", "Cervical cancer cause, signs and work-up", [
  "HPV is the cause; the HPV vaccine at age 11 to 12 (as early as 9) does not treat an existing infection.",
  "Dysplasia has no symptoms; vaginal bleeding, especially after intercourse, is the most common symptom of invasive cancer.",
  "An abnormal Pap with high-risk HPV leads to colposcopy with biopsy; nothing in the vagina for 24 hours before, and Lugol's is contraindicated with iodine or shellfish allergy.",
  "About 90% are squamous cell carcinomas in the transformation zone."], "study guide, Ch 65 and Ch 64"),
 C("c-cerv-tx", "cervical", "Cervical cancer treatment", [
  "Early disease: cone biopsy or radical trachelectomy if fertility is wanted; hysterectomy with node dissection if not.",
  "Higher stages: chemoradiation with brachytherapy.",
  "Pelvic exenteration can cure a recurrence confined to the pelvis."], "study guide, Ch 65"),
 # ---- Prostate
 C("c-pros-patho", "prostate", "Prostate cancer patho and screening", [
  "Tumors grow on the periphery of the gland, so urinary symptoms come late; spread is to lymph nodes, bone, rectum and bladder.",
  "PSA of 4 ng/mL or higher needs further assessment; PSA has high sensitivity but low specificity and cannot tell BPH from cancer.",
  "A needle biopsy confirms the diagnosis, followed by a Gleason score.",
  "African American men have a higher incidence and twice the mortality; BPH is not a precursor to prostate cancer."], "study guide, Ch 66"),
 C("c-pros-tx", "prostate", "Prostate cancer treatment and safety", [
  "Brachytherapy seeds are placed permanently through the perineum for cancer confined to the prostate; no sex for 2 weeks, then use a condom.",
  "The nurse minimizes contact and wears proper, thicker PPE with brachytherapy; an external beam client is not radioactive.",
  "Ablative hormone therapy suppresses testosterone; chemotherapy is for hormone-refractory disease."], "study guide, Ch 66 and class notes"),
 C("c-pros-postop", "prostate", "Post-op complications after prostatectomy", [
  "Impotence is the most expected; nerve-sparing surgery only tries to protect the erection nerves.",
  "Watch for urinary incontinence, infection (fever, pain, swelling, redness) and bleeding with clots.",
  "Manage bladder irrigation to clear clots and give stool softeners to avoid straining.",
  "A cancer client with fever, malaise and high WBC most likely has an infection."], "study guide, Ch 66 and class PLQ"),
 # ---- Testicular
 C("c-test-dx", "testis", "Testicular cancer risk, signs and markers", [
  "Cryptorchidism is the greatest risk factor; the average age is 33.",
  "The classic sign is a painless mass, sometimes with a firm or heavy feeling.",
  "AFP and hCG should fall after the tumor is removed; if not, look for more tumor.",
  "Cure rate is 90 to 100% if found early."], "study guide, Ch 66"),
 C("c-test-tx", "testis", "Testicular cancer treatment and teaching", [
  "All types start with removal of the affected testicle (orchiectomy).",
  "Seminoma is radiation sensitive; nonseminoma is not and gets node removal and chemotherapy.",
  "Bank sperm before treatment; follow up for at least 10 years; retroperitoneal node removal can damage ejaculation nerves.",
  "Bleomycin can damage the lungs and ifosfamide can cause hemorrhagic cystitis.",
  "After surgery, hypotension with tachycardia means volume loss and fever means infection."], "study guide, Ch 66"),
 # ---- End of life
 C("c-eol-diff", "eol", "Hospice versus palliative care", [
  "Palliative care is for any stage of serious illness, begins at diagnosis, and can continue with curative treatment.",
  "Hospice is for a prognosis of 6 months or less; curative treatment stops and the goal is comfort.",
  "All hospice is palliative, but not all palliative care is hospice."], "study guide, Ch 26 and Other Topics"),
 C("c-eol-nursing", "eol", "Nursing care at the end of life", [
  "Signs death is near: falling intake and urine output, mottled cool extremities, apnea periods, noisy secretions.",
  "Give opioids around the clock for pain and dyspnea, provide mouth care and repositioning, and honor advance directives.",
  "Hearing is often the last sense lost."], "study guide, Other Topics"),
]

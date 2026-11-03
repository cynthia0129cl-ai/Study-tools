# Lung cancer, Multiple myeloma, Prostate cancer, Cancer risk factors, Hodgkin lymphoma.
ITEMS = []
A = ITEMS.append

# ------------------------------------------------------------------ LUNG CANCER
A(mc("lung", "c-lung-types",
 "A 68-year-old client who has smoked two packs a day for decades is told the biopsy shows small cell (oat cell) lung cancer. Which statement by the nurse is accurate?",
 "“This type grows quickly and spreads to other organs early, so surgery is not the main treatment.”",
 {"“This is the most common type, making up about 85% of lung cancers.”": ("About 85% of lung cancers are non-small cell; small cell is about 15%.", "swaps the 85% and 15% figures"),
  "“If it is found early, the 5-year survival is good.”": ("Good early-stage survival describes non-small cell cancer; small cell has a poor outlook at any stage.", "gives small cell the non-small cell outlook"),
  "“It includes adenocarcinoma, squamous cell and large cell types.”": ("Those three cell types make up non-small cell cancer.", "mixes up the two types"),
  "“Surgery is used primarily for this type when it has not spread.”": ("Surgery is used primarily for non-small cell cancer without metastasis.", "mixes up the two types")},
 "Small cell lung cancer is about 15% of cases, grows fast and spreads early, and its outlook is poor at any stage: only 5 to 10% survive 5 years, and your class notes give a life expectancy of 6 months to 1 year. Non-small cell cancer is about 85%, has three cell types, grows more slowly, has a good 5-year survival if found early, and is the type for which surgery is used when there is no metastasis. (study guide, Ch 26 and class notes)", lp=True))

A(sata("lung", "c-lung-types",
 "The nurse reviews the features of non-small cell lung cancer with a nursing student.",
 ["It makes up about 85% of lung cancers", "Its cell types are adenocarcinoma, squamous cell carcinoma and large cell carcinoma", "Surgery is used primarily when there is no metastasis", "The 5-year survival is good when it is found at an early stage"],
 {"It grows quickly and spreads early to other organs": ("That describes small cell lung cancer.", "mixes up the two types"),
  "Life expectancy is typically 6 months to 1 year": ("That is the class figure for small cell lung cancer.", "mixes up the two types"),
  "It is also called oat cell cancer": ("Oat cell is another name for small cell lung cancer.", "mixes up the two types")},
 "Non-small cell lung cancer is the larger and slower group with three cell types, and early-stage disease has a good 5-year survival. Surgery is the preferred treatment when there is no metastasis. The wrong options all describe small cell, the faster and poorer-outlook type. (study guide, Ch 26 and class notes)", lp=True))

A(mc("lung", "c-lung-dx",
 "A 70-year-old client with known lung cancer reports a new headache and bone pain. Which finding does the nurse recognize as suggesting metastasis?",
 "Headache and bone pain",
 {"A new cough that does not go away": ("A new or changing cough is a presenting cue of lung cancer itself, not a sign of spread.", "treats a presenting cue as a sign of spread"),
  "Hoarseness": ("Hoarseness is a presenting symptom of lung cancer.", "treats a presenting cue as a sign of spread"),
  "Frequent pneumonia or bronchitis": ("This is a presenting cue from airway obstruction and infection.", "treats a presenting cue as a sign of spread"),
  "Hemoptysis": ("Hemoptysis comes from small vessels rupturing in the lung.", "treats a presenting cue as a sign of spread")},
 "Early lung cancer often has no symptoms. As it advances, cues include a new or changed cough, hemoptysis, shortness of breath, wheezing, hoarseness, chest pain, weight loss and frequent pneumonia. Headache and bone pain suggest metastasis to the brain and bone; common sites are brain, bone, adrenal gland and the other lung. Bone pain also prompts a calcium check. (study guide, Ch 26 and Ch 13)", lp=True))

A(mc("lung", "c-lung-dx",
 "A client with suspected lung cancer is scheduled for a PET scan. The client asks what the test shows. Which response by the nurse is best?",
 "“It shows areas of high metabolic activity, such as rapidly dividing cancer cells, rather than the structure of the lung.”",
 {"“It shows the structure of the airways so the provider can take a tissue sample.”": ("Airway structure and tissue sampling describe bronchoscopy.", "mixes up PET and bronchoscopy"),
  "“It is a small chest incision to look at the nodes in the middle of the chest.”": ("That describes mediastinoscopy.", "mixes up PET and mediastinoscopy"),
  "“It identifies the type of tumor cells in the mucus you cough up.”": ("That describes sputum cytology.", "mixes up PET and sputum cytology"),
  "“It looks only for fractures of the ribs.”": ("PET looks at metabolism; bone and abdominal scans look for metastasis.", None)},
 "A PET scan looks at metabolism, not structure, and lights up metabolically active tissue such as rapidly dividing cancer cells. Chest x-ray and CT find the lesion, sputum cytology may identify the tumor cells, bronchoscopy lets the provider see and biopsy the airways, and mediastinoscopy is a surgical incision to view and biopsy the mediastinum. (study guide, Ch 26)"))

A(match2("lung", "c-lung-tx",
 "The nurse reviews lung cancer surgery and testing with a client. Match each procedure with its description.",
 [("Lobectomy", "Removes one entire lobe when the cancer is localized to that lobe"),
  ("Pneumonectomy", "Removes the entire lung when cancer is spread diffusely through it"),
  ("Wedge resection", "Removes a small section of a lobe for cancer in one small area"),
  ("Mediastinoscopy", "A surgical incision to view and biopsy the mediastinum")],
 {"Removes one entire lobe when the cancer is localized to that lobe": "This is a lobectomy.",
  "Removes the entire lung when cancer is spread diffusely through it": "This is a pneumonectomy.",
  "Removes a small section of a lobe for cancer in one small area": "This is a wedge resection.",
  "A surgical incision to view and biopsy the mediastinum": "This is mediastinoscopy, a diagnostic test rather than a treatment."},
 "Surgery is preferred if there is no metastasis. The extent of cancer decides the operation: a small area gets a wedge resection, one lobe gets a lobectomy, and a diffusely spread cancer needs a pneumonectomy. Mediastinoscopy is used to biopsy the nodes. (study guide, Ch 26)"))

A(order("lung", "c-lung-tx",
 "The nurse explains the WHO pain ladder used for cancer pain. Place the steps in order from mild to severe pain.",
 ["Step 1: a nonopioid such as acetaminophen or an NSAID", "Step 2: a moderate opioid such as codeine, hydrocodone or oxycodone plus a nonopioid", "Step 3: a strong opioid such as morphine or fentanyl plus a nonopioid"],
 "The ladder moves up as pain gets worse, and a nonopioid is kept at every step. Doses are given around the clock rather than on demand so that pain peaks are avoided. (study guide, Ch 26 and Ch 11)", lp=True))

A(mc("lung", "c-lung-nursing",
 "A client with lung cancer has dyspnea and a SpO₂ of 87% on room air. Which action should the nurse take first?",
 "Raise the head of the bed to semi-Fowler's position and apply oxygen to keep the SpO₂ at 90% or higher",
 {"Lay the client flat to rest": ("Lying flat reduces lung expansion; semi-Fowler's allows full expansion and better oxygenation.", "positions flat for rest"),
  "Offer a large meal to improve strength": ("A large meal pushes on the diaphragm; small frequent meals with supplements are better.", "feeds a large meal"),
  "Encourage the client to walk the hall": ("Activity increases oxygen demand; the client has activity intolerance.", None),
  "Wait and recheck the SpO₂ in 1 hour": ("A SpO₂ below 90% is a significant oxygenation problem that needs action now.", None)},
 "A SpO₂ below 90% means poor gas exchange. Oxygen is given to keep the SpO₂ at 90% or higher, and semi-Fowler's allows full lung expansion and better oxygenation. Small frequent meals with supplements avoid pressure on the diaphragm, and pain, anti-anxiety and bronchodilator medications help the client relax and open the airway. (study guide, Ch 26)", lp=True))

A(mc("lung", "c-lung-nursing",
 "A nurse sees a coworker about to clamp the chest tube of a client who had a lobectomy, to move the client to a chair. Which action should the nurse take?",
 "Intervene, because the chest tube should never be clamped; air or fluid can build up and cause a tension pneumothorax",
 {"Allow it, because clamping prevents air from entering the pleural space": ("Clamping traps air and fluid in the pleural space and can cause a tension pneumothorax.", "believes clamping prevents air leaks"),
  "Allow it for a short time only": ("The rule is to never clamp the chest tube.", "believes a brief clamp is safe"),
  "Disconnect the tube from the drainage system to make moving easier": ("The system must stay closed to prevent air leaks.", "opens the closed system"),
  "Ask the client to hold the tube while standing": ("This does not address the unsafe clamping and the closed system must be maintained.", None)},
 "After lobectomy or pneumonectomy the nurse keeps the chest tube system closed, watches the water-seal chamber, and never clamps the tube. Persistent bubbling in the water-seal chamber means an air leak. Excess bloody drainage suggests a bleed and cloudy drainage suggests infection. (study guide, Ch 26)", lp=True))

A(mc("lung", "c-lung-nursing",
 "A client who had a lobectomy yesterday has continuous bubbling in the water-seal chamber of the chest tube drainage system. The nurse recognizes this as which finding?",
 "An air leak in the system",
 {"Normal re-expansion of the lung": ("Normal drainage does not cause persistent bubbling in the water-seal chamber.", None),
  "Excess bloody drainage": ("Bleeding is judged by the amount and color of drainage, not by bubbling.", None),
  "Infection of the pleural space": ("Cloudy drainage, not bubbling, suggests infection.", None),
  "Atelectasis": ("Atelectasis is suspected when breath sounds are diminished or absent.", None)},
 "Persistent bubbling in the water-seal chamber means there is an air leak in the system. The nurse also checks vital signs for hypotension or tachycardia from blood loss, breath sounds for atelectasis, and the suture line for infection. (study guide, Ch 26)"))

A(tf("lung", "c-lung-types",
 "A nurse tells a client with a 30 pack-year smoking history who quit 4 years ago that a yearly low-dose CT is recommended for all adults over age 65, regardless of smoking history. The nurse's statement is accurate.",
 False,
 "There is no general screening guideline for lung cancer. A yearly low-dose CT is for high-risk clients: current smokers or those who quit within 15 years, with at least a 20 pack-year history. The true version is that screening is for this high-risk group only. (study guide, Ch 13 and Ch 26)",
 "Marking True extends screening to everyone over 65; it is limited to high-risk clients.", lp=True))

A(tf("lung", "c-lung-tx",
 "A client newly diagnosed with lung cancer asks when palliative care can begin. The nurse answers that it begins at diagnosis to manage pain, dyspnea and nausea. The nurse's answer is accurate.",
 True,
 "Palliative care starts at diagnosis, not at the end of life. It manages pain, dyspnea and nausea and improves quality of life, and it is not the same as hospice. (study guide, Ch 26 Connection Check)",
 "Marking False delays palliative care to the end of life, which is the hospice timing.", lp=True))

# ------------------------------------------------------------------ MULTIPLE MYELOMA
A(sata("mm", "c-mm-patho",
 "The nurse reviews the CRAB criteria used to support a diagnosis of multiple myeloma.",
 ["Calcium above 11.5 mg/dL", "Creatinine above 2 mg/dL", "Hemoglobin below 10 g/dL", "Lytic bone lesions or pathologic fractures"],
 {"Platelets above 450,000/mm³": ("A high platelet count is not part of CRAB.", None),
  "Philadelphia chromosome present": ("The Philadelphia chromosome is linked to chronic myeloid leukemia.", "mixes up myeloma and leukemia"),
  "Reed–Sternberg cells on biopsy": ("Reed–Sternberg cells define Hodgkin lymphoma.", "mixes up myeloma and Hodgkin lymphoma")},
 "CRAB stands for hyperCalcemia (above 11.5 mg/dL), Renal insufficiency (creatinine above 2 mg/dL), Anemia (Hgb below 10 g/dL) and Bone disease (lytic lesions, osteopenia, pathologic fractures). Plasma cells of 10% or more in the marrow and an M protein in serum or urine complete the picture. (study guide, Ch 34)", lp=True))

A(mc("mm", "c-mm-patho",
 "A client with multiple myeloma has Bence Jones protein in the urine. Why does the nurse monitor BUN and creatinine closely?",
 "The excess light chains are toxic to the kidneys",
 {"The M protein lowers the blood pressure and starves the kidneys": ("The harm comes from light chains and calcium, not from low blood pressure.", None),
  "Bisphosphonates always cause kidney failure": ("The kidney damage in myeloma comes from light chains and hypercalcemia, not from treatment.", None),
  "The tumor grows directly inside the kidney": ("Myeloma is a plasma cell cancer of the marrow; the kidney is harmed by what the cells make.", None),
  "Low platelets cause bleeding into the kidneys": ("Bleeding is not the cause of the kidney damage here.", None)},
 "One clone of plasma cells overgrows the marrow and pumps out monoclonal immunoglobulin, the M protein. Excess light chains, called Bence Jones protein in the urine, are directly toxic to the kidney, and calcium released from lytic bone lesions adds stones and renal injury. The nurse watches BUN, creatinine, intake and output, and serum and urine calcium. (study guide, Ch 34)"))

A(mc("mm", "c-mm-nursing",
 "A client with multiple myeloma reports sudden severe back pain and new numbness in both legs. Which action should the nurse take first?",
 "Assess motor and sensory function in the legs and notify the provider immediately",
 {"Apply a heating pad to the back and reassess in the morning": ("Sudden severe pain with numbness may be a fracture or spinal cord compression, which cannot wait.", None),
  "Encourage the client to walk to loosen the back": ("Walking could worsen a vertebral fracture or cord compression.", None),
  "Give an extra dose of the calcium supplement": ("Hypercalcemia is a risk in myeloma, so extra calcium is harmful.", "forgets the client is at risk for hypercalcemia"),
  "Document the finding and continue routine care": ("These are emergency warning signs that must be reported.", None)},
 "Myeloma destroys bone, so sudden severe pain, or pain in a new spot, especially the back, may mean a pathologic fracture or vertebral collapse. Spinal cord compression causes numbness, tingling and motor changes. The nurse assesses and reports at once, and teaches the client to report sudden severe pain and any change in sensation or movement. (study guide, Ch 34)", lp=True))

A(sata("mm", "c-mm-nursing",
 "A client with multiple myeloma is admitted with hypercalcemia and bone pain. Which nursing interventions are appropriate?",
 ["Encourage fluids to dilute calcium and protect the kidneys", "Encourage ambulation as tolerated", "Position the client for comfort", "Monitor serum and urine calcium, BUN and creatinine"],
 {"Restrict fluids to lower urine output": ("Fluids are encouraged to dilute the calcium and prevent stones.", "restricts fluids in hypercalcemia"),
  "Maintain strict bed rest": ("Weight bearing builds bone and prevents DVT and deconditioning.", None),
  "Offer a calcium supplement for bone strength": ("The client already has too much calcium in the blood from bone breakdown.", "forgets the client has hypercalcemia")},
 "Fluids dilute calcium and protect the kidneys from stones and light chains. Walking as tolerated gives weight bearing that builds bone and helps prevent DVT. Positioning for comfort eases nerve compression, and monitoring calcium, BUN and creatinine tracks kidney damage. Bisphosphonates, chemotherapy and pain medication are given as ordered. (study guide, Ch 34 and class notes)", lp=True))

A(mc("mm", "c-mm-nursing",
 "A client with multiple myeloma is prescribed ibandronate (Boniva). Which purpose should the nurse include in teaching?",
 "It reduces bone breakdown, which lowers calcium and the risk of fractures",
 {"It replaces the clotting factors the client is missing": ("Replacing factors is the treatment for hemophilia.", None),
  "It kills the abnormal plasma cells directly": ("Chemotherapy such as thalidomide, lenalidomide or bortezomib attacks the cancer cells.", "mixes up bone drugs and chemotherapy"),
  "It raises the blood calcium to strengthen bone": ("The drug lowers calcium by slowing bone breakdown.", "reverses the effect on calcium"),
  "It lowers uric acid and prevents tumor lysis": ("Allopurinol and rasburicase are used for uric acid.", None)},
 "Bisphosphonates slow bone breakdown, so fewer fractures occur and calcium falls. Examples include ibandronate (Boniva), pamidronate and zoledronate. Long-term use with bisphosphonates or denosumab can cause osteonecrosis of the jaw. (study guide, Ch 34 and class notes)"))

A(mc("mm", "c-mm-nursing",
 "A nurse reviews the signs of hypercalcemia in a client with multiple myeloma. Which finding should the nurse expect?",
 "Constipation, muscle weakness and polyuria",
 {"Peaked T waves on the ECG": ("Peaked T waves are a sign of hyperkalemia, as in tumor lysis syndrome.", "mixes up calcium and potassium"),
  "Dilutional hyponatremia with seizures": ("That describes SIADH.", "mixes up calcium and sodium"),
  "Hypotension, tachycardia and hives": ("That picture fits anaphylaxis.", None),
  "Ribbon-like stools with vomiting": ("That suggests a bowel obstruction.", None)},
 "Hypercalcemia from bone breakdown causes confusion or lethargy, muscle weakness, polyuria and dehydration, constipation and nausea, bradycardia and heart block. Your class notes add tingling and burning sensation. Fluids dilute the calcium. (study guide, Ch 13, Ch 34 and class notes)"))

A(tf("mm", "c-mm-patho",
 "A nurse tells a client newly diagnosed with multiple myeloma that the disease is an incurable B-cell cancer of plasma cells. The nurse's statement is accurate.",
 True,
 "Multiple myeloma is an incurable cancer of plasma cells, which are mature B cells that make antibodies. Treatment controls the disease and its complications. (study guide, Ch 34)",
 "Marking False would tell the client the disease is curable; it is described as incurable.", lp=True))

A(tf("mm", "c-mm-nursing",
 "A nurse tells a woman of childbearing age who is starting thalidomide or lenalidomide for multiple myeloma that these drugs are safe to take during pregnancy. The nurse's statement is accurate.",
 False,
 "Thalidomide and lenalidomide are teratogenic. The true version is that these drugs can harm a fetus, so contraception is needed. (study guide, Ch 34)",
 "Marking True would expose a fetus to a teratogenic drug.", lp=True))

# ------------------------------------------------------------------ PROSTATE CANCER (post-op complications)
A(mc("prostate", "c-pros-patho",
 "A 71-year-old client with metastasis to the bone from prostate cancer says, “I never had any trouble urinating.” Which explanation by the nurse is correct?",
 "Prostate tumors usually grow at the edges of the gland, so they do not block urine flow early",
 {"The tumor grows inside the urethra but is too small to block it": ("Tumors grow on the periphery of the gland, away from the urethra.", "places the tumor at the urethra"),
  "The client's bladder muscle compensated for the blockage": ("There was no early blockage to compensate for.", None),
  "Prostate cancer never affects urination": ("Urinary symptoms appear when the cancer advances.", None),
  "The metastasis to the bone relieved the pressure on the urethra": ("Metastasis does not relieve urinary obstruction.", None)},
 "Prostate cancer is slow growing and asymptomatic until it is advanced. Because the tumors grow on the periphery of the gland, they do not obstruct urine flow early and go unnoticed until they cause pain. That is how a client can have late-stage disease with no urinary trouble. It spreads to lymph nodes, bone, rectum and bladder. (study guide, Ch 66 and class PLQ)", lp=True))

A(mc("prostate", "c-pros-patho",
 "A 56-year-old client has a PSA of 4.6 ng/mL and an enlarged prostate on digital rectal exam. Which statement by the nurse is accurate?",
 "“A PSA of 4 or higher needs further evaluation, and a biopsy confirms the diagnosis.”",
 {"“A PSA this high confirms that you have prostate cancer.”": ("PSA has high sensitivity but low specificity and cannot confirm cancer; biopsy does.", "treats PSA as diagnostic"),
  "“A PSA below 4 means cancer is not possible.”": ("No PSA value guarantees there is no cancer.", "treats a low PSA as a guarantee"),
  "“PSA rises only with cancer, not with infection or an enlarged prostate.”": ("Prostatitis and BPH also raise PSA, which is why it cannot tell BPH from cancer.", "thinks only cancer raises PSA"),
  "“The next step is a radical prostatectomy.”": ("Treatment decisions follow biopsy, Gleason score and staging.", None)},
 "PSA of 4 ng/mL or higher needs further assessment, and the diagnosis requires a needle biopsy, then a Gleason score and TNM staging. PSA has high sensitivity but low specificity, so infection and enlargement can raise it. A large palpable prostate plus a high PSA needs workup. (study guide, Ch 66 and Ch 13)", lp=True))

A(sata("prostate", "c-pros-postop",
 "A client has returned to the unit after a radical prostatectomy. Which complications should the nurse monitor for?",
 ["Erectile dysfunction", "Urinary incontinence", "Infection, such as fever, increasing pain, swelling or redness", "Bleeding with clots in the urine"],
 {"Hearing loss from ototoxicity": ("Ototoxicity is a chemotherapy effect of testicular cancer drugs such as cisplatin.", "borrows a complication from another cancer"),
  "Lymphedema of the arm": ("Arm lymphedema follows axillary node removal in breast cancer.", "borrows a complication from another cancer"),
  "Dry cough from pneumonitis": ("Pneumonitis follows chest radiation.", "borrows a complication from another cancer")},
 "Impotence is the most expected complication after radical prostatectomy and nerve-sparing surgery only tries to protect the erection nerves. Urinary incontinence, infection, and bleeding with clots are also watched for. The nurse manages bladder irrigation to clear clots, gives stool softeners to avoid straining, and uses aseptic wound care. (study guide, Ch 66; class notes)", lp=True))

A(mc("prostate", "c-pros-postop",
 "A client has continuous bladder irrigation after prostate surgery. The nurse explains that the irrigation is used to do what?",
 "Clear blood clots so the catheter stays open",
 {"Treat a urinary tract infection": ("Infection is treated with antibiotics; irrigation clears clots.", None),
  "Lower the PSA level": ("Irrigation does not change PSA.", None),
  "Dissolve bladder stones": ("Stones are not the purpose of irrigation after this surgery.", None),
  "Deliver chemotherapy to the bladder": ("Irrigation fluid is not chemotherapy.", None)},
 "After prostate surgery bleeding and clots can block urine flow. Bladder irrigation clears the clots and keeps the urine light pink. Stool softeners prevent straining, which could start bleeding. (study guide, Ch 66)"))

A(mc("prostate", "c-pros-postop",
 "After a prostatectomy a client is ordered a daily stool softener. The client asks why it is needed. Which response by the nurse is best?",
 "“It prevents straining, which could cause bleeding at the surgical site.”",
 {"“It lowers your PSA level.”": ("Stool softeners have no effect on PSA.", None),
  "“It treats the infection in your prostate.”": ("A stool softener does not treat infection.", None),
  "“It helps the radioactive seeds pass.”": ("Seeds are implanted in brachytherapy, not passed after prostatectomy.", None)},
 "Straining can raise pressure and cause bleeding after prostate surgery, so stool softeners are given with bladder irrigation and aseptic wound care. (study guide, Ch 66)"))

A(mc("prostate", "c-pros-tx",
 "A client is having permanent radioactive seeds placed through the perineum for early prostate cancer. Which statement by the client indicates understanding of safety teaching?",
 "“I will avoid sex for 2 weeks and then use a condom to protect my partner from radiation.”",
 {"“I can resume unprotected intercourse after one day.”": ("The teaching is no sex for 2 weeks, then a condom.", None),
  "“The seeds will be taken out after a week.”": ("Brachytherapy seeds for prostate cancer are placed permanently.", "thinks the seeds are temporary"),
  "“The seeds are placed through my abdomen under general anesthesia.”": ("They are placed through the perineum as an outpatient procedure.", None),
  "“The seeds are for cancer that has spread to my bones.”": ("Brachytherapy is for cancer that has not spread outside the prostate.", None)},
 "Brachytherapy places radioactive seeds permanently through the perineum, as an outpatient procedure, for cancer that has not spread outside the prostate. The client avoids sex for 2 weeks and then uses a condom. Radiation and brachytherapy can cause incontinence and impotence. (study guide, Ch 66)", lp=True))

A(mc("prostate", "c-pros-tx",
 "A nurse is caring for a client who has a radioactive implant for prostate cancer. Which action should the nurse take?",
 "Minimize contact time and wear proper, thicker PPE",
 {"Wear no protective equipment because the client is not radioactive": ("Not being radioactive is true for external beam therapy; with brachytherapy the nurse limits exposure.", "applies the external beam rule to brachytherapy"),
  "Wear only regular gloves": ("Proper, thicker PPE is needed to minimize radiation exposure.", None),
  "Spend as much time at the bedside as possible": ("Time near the source should be limited.", None),
  "Let the family handle all body-fluid care without teaching": ("Brachytherapy clients may eliminate radioactive material in body fluids, so the family is taught too.", None)},
 "With external beam radiation the client is not radioactive. With brachytherapy the nurse minimizes contact and uses proper, thicker PPE because body fluids may be radioactive, and the family is taught. (study guide, Ch 13, Ch 66 and class notes)", lp=True))

A(mc("prostate", "c-pros-postop",
 "A client with prostate cancer reports fever, malaise and a rising white blood cell count after treatment. Which principle should guide the nurse's care?",
 "Infection is the most likely cause",
 {"This is an expected response to the tumor": ("Fever with a high WBC in a cancer client points first to infection.", None),
  "This indicates hemorrhage": ("Hemorrhage shows with bleeding, low blood pressure and a rising heart rate.", None),
  "This indicates the cancer has become stage IV": ("Staging cannot be judged from a fever.", None),
  "This is an adverse effect of a stool softener": ("A stool softener does not cause fever.", None)},
 "In a cancer client, fever, malaise and an elevated WBC point to infection first. After prostate surgery infection shows as fever, increasing pain, swelling, redness, drainage and N/V. (study guide, Ch 66 and class PLQ)"))

A(mc("prostate", "c-pros-postop",
 "A client is scheduled for a nerve-sparing radical prostatectomy. Which statement by the client indicates understanding of the surgery?",
 "“The surgery tries to protect the nerves that control erection, but impotence is still likely.”",
 {"“The surgery guarantees I will keep normal erections.”": ("Radical prostatectomy almost always results in impotence; nerve-sparing only tries to protect the nerves.", "thinks nerve-sparing guarantees erections"),
  "“The surgery removes only the outer layer of the prostate.”": ("Radical prostatectomy removes the prostate and seminal vesicles, with or without pelvic nodes.", None),
  "“The surgery will prevent any problem with urine control.”": ("Urinary incontinence is a possible complication.", None),
  "“The surgery is done with radioactive seeds placed through the skin.”": ("That describes brachytherapy.", None)},
 "Radical prostatectomy removes the prostate and seminal vesicles, with or without pelvic nodes, and almost always results in impotence. The nerve-sparing approach attempts to keep intact the nerves that control erection. Incontinence, infection, bleeding and clots are other complications to watch for. (study guide, Ch 66)"))

A(tf("prostate", "c-pros-patho",
 "A nurse tells a client that African American men have a higher incidence of prostate cancer and about twice the mortality. The nurse's statement is accurate.",
 True,
 "African American men, and Caribbean men of African ancestry, have a higher incidence of prostate cancer and 2 times the mortality. Screening discussions start at age 45 for them. (study guide, Ch 66 and Ch 13)",
 "Marking False denies a documented disparity.", lp=True))

A(tf("prostate", "c-pros-patho",
 "A nurse teaches a client that benign prostatic hyperplasia is an early stage of prostate cancer. The nurse's statement is accurate.",
 False,
 "BPH is not cancer and is not a precursor to it, although a man can have BPH and prostate cancer at the same time. (study guide, Ch 66)",
 "Marking True treats BPH as a pre-cancer.", lp=True))

# ------------------------------------------------------------------ CANCER RISK FACTORS
A(mc("risk", "c-risk-list",
 "A nurse is reviewing risk factors with a 58-year-old client. Which finding is a nonmodifiable risk factor for cancer?",
 "A genetic predisposition such as a BRCA1 mutation",
 {"A sedentary lifestyle": ("A sedentary lifestyle is modifiable.", None),
  "A diet low in vegetables": ("Diet is modifiable.", None),
  "Smoking one pack a day": ("Smoking is modifiable.", None),
  "Heavy alcohol use": ("Alcohol use is modifiable.", None)},
 "Age and genetics cannot be changed, and 5 to 10% of cancers come from known genetic syndromes such as BRCA1/2, p53 and FAP. Lifestyle factors such as inactivity, poor diet, smoking and alcohol are modifiable. The nine risk factor categories are carcinogens, environment, hormones, genetics, lifestyle, infectious disease, medications, immune status and nutrition. Carcinogen exposure is the most common risk factor. (study guide, Ch 13)", lp=True))

A(mc("risk", "c-risk-table",
 "A 38-year-old client reports an HPV infection, multiple sexual partners, early sexual contact and tobacco use. For which cancer is the client at increased risk?",
 "Cervical cancer",
 {"Ovarian cancer": ("Ovarian risk is tied to BRCA1/2, nulliparity and not breastfeeding.", None),
  "Uterine cancer": ("Uterine risk is tied to estrogen, obesity, PCOS and tamoxifen.", None),
  "Breast cancer": ("Breast risk is tied to early menarche, late menopause, BRCA and obesity.", None),
  "Prostate cancer": ("Prostate cancer occurs in men and is tied to age, family history and pesticides.", None)},
 "Cervical cancer risk factors include HPV, multiple partners, early sexual contact, tobacco use and long-term oral contraceptive use. HPV is the cause: nearly all cervical cancers test positive. Each other option has its own typical risk set. (study guide, Ch 13 Table 13.2 and Ch 65)", lp=True))

A(match2("risk", "c-risk-table",
 "The nurse reviews risk factors from the cancer risk table. Match each cancer with a risk factor.",
 [("Gastric cancer", "H. pylori infection"),
  ("Liver cancer", "Hepatitis B or C"),
  ("Testicular cancer", "Undescended testicle"),
  ("Lung cancer", "Asbestos exposure")],
 {"H. pylori infection": "H. pylori is listed with gastric cancer.",
  "Hepatitis B or C": "Hepatitis A, B or C and alcohol are listed for liver cancer.",
  "Undescended testicle": "Cryptorchidism is the greatest risk for testicular cancer.",
  "Asbestos exposure": "Tobacco, asbestos, coal, soot, tar, pollution and wood dust are listed for lung cancer."},
 "Table 13.2 lists risk factors for each cancer. H. pylori, ulcers, alcohol and smoking go with gastric cancer; alcohol and hepatitis A, B or C with liver cancer; undescended testes, HIV and age 20 to 34 with testicular cancer; and tobacco, asbestos and pollution with lung cancer. (study guide, Ch 13 Table 13.2)", lp=True))

A(mc("risk", "c-risk-list",
 "A client with a BRCA2 mutation asks which cancers, besides breast and ovarian, are linked to this gene. Which response by the nurse is correct?",
 "Pancreatic cancer, prostate cancer and melanoma",
 {"Lung cancer and mesothelioma": ("Those are tied to tobacco and asbestos.", None),
  "Colon and rectal cancer": ("Colon cancer risk is tied to polyps, alcohol, obesity and inflammatory bowel disease in these materials.", None),
  "Bladder and kidney cancer": ("Those are tied to tobacco, pesticides and solvents.", None),
  "Cervical and vulvar cancer": ("Those are tied to HPV.", None)},
 "BRCA1 raises the risk of breast and ovarian cancer. BRCA2 also raises the risk of pancreatic and prostate cancer and melanoma, and it is the more common mutation in male breast cancer. (study guide, Ch 13 and Ch 66)"))

A(sata("risk", "c-risk-list",
 "A nurse reviews red flags for hereditary cancer.",
 ["Multiple primary tumors in the same client", "Bilateral tumors in paired organs", "Cancer at a younger age than usual", "A tumor in a sex not usually affected, such as male breast cancer", "Two or more first-degree relatives with the same cancer"],
 {"A single tumor found at the usual age in a client with no family history": ("This pattern does not suggest a hereditary syndrome.", None),
  "One distant relative with a different cancer": ("The flag is two or more first-degree relatives with the same cancer.", None)},
 "Red flags for hereditary cancer include multiple primaries, bilateral tumors in paired organs, a younger-than-usual age, a tumor in the sex not usually affected, and two or more first-degree relatives with the same cancer. (study guide, Ch 13)"))

A(match2("risk", "c-risk-prev",
 "The nurse is planning cancer prevention activities. Match each activity with its level of prevention.",
 [("Giving the HPV vaccine", "Primary prevention"),
  ("Arranging a colonoscopy at age 45", "Secondary prevention"),
  ("Managing side effects after a cancer diagnosis", "Tertiary prevention")],
 {"Primary prevention": "Primary prevention modifies risk: avoiding carcinogens, immunization and chemoprevention.",
  "Secondary prevention": "Secondary prevention is screening for early detection such as breast, cervical, colon and prostate screening.",
  "Tertiary prevention": "Tertiary prevention reduces morbidity and mortality once the disease is diagnosed."},
 "Primary prevention stops cancer before it starts: risk factor modification, immunization and chemoprevention. Secondary prevention finds it early by screening. Tertiary prevention limits harm after diagnosis. (study guide, Ch 13 and class notes)"))

A(blanks("risk", "c-risk-caution",
 "The nurse teaches the CAUTION warning signs. The A stands for a [1] that does not heal, the T stands for a [2] or lump, and a sign lasting more than [3] should be evaluated.",
 [("sore", {"rash": ("The A stands for a sore that does not heal.", None), "cough": ("A nagging cough is the N.", None)}),
  ("thickening", {"tenderness": ("The T stands for thickening or lump.", None), "tingling": ("Tingling is not part of CAUTION.", None)}),
  ("2 weeks", {"2 days": ("The guideline is more than 2 weeks.", None), "6 months": ("Waiting 6 months would delay evaluation.", None)})],
 "CAUTION stands for Change in bowel or bladder habits, A sore that does not heal, Unusual bleeding or discharge, Thickening or lump, Indigestion or difficulty swallowing, Obvious change in a wart or mole, and Nagging cough or hoarseness. A sign that lasts more than 2 weeks needs evaluation. (study guide, Ch 13)", lp=True))

A(tf("risk", "c-risk-list",
 "A nurse teaches a client that carcinogen exposure is the most common risk factor for cancer and that risks are cumulative. The nurse's teaching is accurate.",
 True,
 "A carcinogen damages DNA and is the most common risk factor, but exposure alone rarely causes cancer; multiple exposures plus genetic mutations that the immune system misses lead to cancer. (study guide, Ch 13)",
 "Marking False denies that carcinogen exposure is the most common risk.", lp=True))

A(tf("risk", "c-risk-list",
 "A nurse tells a client that most cancers come from known genetic syndromes such as BRCA1 and BRCA2. The nurse's statement is accurate.",
 False,
 "Known genetic syndromes account for only 5 to 10% of cancers. The true version is that most cancers are not from known inherited syndromes. (study guide, Ch 13)",
 "Marking True overstates the share of cancers caused by inherited syndromes.", lp=True))

# ------------------------------------------------------------------ HODGKIN LYMPHOMA
A(mc("hodgkin", "c-hodg-dx",
 "A 24-year-old client has painless neck swelling, drenching night sweats and generalized itching. A lymph node biopsy confirms Hodgkin lymphoma. Which finding on the biopsy defines this type?",
 "Reed–Sternberg cells",
 {"The Philadelphia chromosome": ("The Philadelphia chromosome is found in chronic myeloid leukemia.", "mixes up lymphoma and leukemia"),
  "Bence Jones protein": ("Bence Jones protein is a finding of multiple myeloma.", "mixes up lymphoma and myeloma"),
  "Heinz bodies": ("Heinz bodies are seen with G6PD deficiency.", None),
  "An M protein spike": ("The M protein is a finding of multiple myeloma.", "mixes up lymphoma and myeloma")},
 "Hodgkin lymphoma is defined by Reed–Sternberg cells, giant lymphocytes, and has a better survival rate than non-Hodgkin lymphoma. It peaks in young adulthood and again after 55 and is linked to Epstein–Barr virus. A lymph node biopsy is definitive. (study guide, Ch 34)", lp=True))

A(sata("hodgkin", "c-hodg-dx",
 "The nurse assesses a client with suspected Hodgkin lymphoma. Which findings are expected?",
 ["Painless swelling of cervical, axillary or inguinal lymph nodes", "Drenching night sweats", "Unexplained weight loss", "Generalized itching with scratch marks", "A dry cough that is worse when lying flat"],
 {"Tender, warm lymph nodes with a sore throat": ("Painful, tender nodes point to infection; lymphoma nodes are painless.", "expects painful nodes"),
  "A smooth red tongue and spoon-shaped nails": ("These are signs of iron deficiency anemia.", None),
  "Severe back pain with high calcium and high creatinine": ("That fits multiple myeloma.", "mixes up lymphoma and myeloma")},
 "Lymphoma causes painless lymph node swelling. B symptoms are low-grade fevers, drenching night sweats and unexplained weight loss. Itching is common in Hodgkin lymphoma, and a dry cough worse lying flat suggests a mediastinal mass that can compress the trachea. Fatigue is not a B symptom. (study guide, Ch 34 and Ch 13)", lp=True))

A(mc("hodgkin", "c-hodg-comp",
 "A client with Hodgkin lymphoma reports facial and arm swelling, shortness of breath, chest pain and trouble swallowing. Which complication does the nurse suspect?",
 "Superior vena cava syndrome",
 {"Tumor lysis syndrome": ("Tumor lysis causes hyperkalemia, hypocalcemia and renal failure after treatment.", "mixes up oncologic emergencies"),
  "Syndrome of inappropriate antidiuretic hormone": ("SIADH causes hyponatremia with confusion and seizures.", "mixes up oncologic emergencies"),
  "Bowel obstruction": ("Bowel obstruction causes vomiting, distention and ribbon-like stools.", "mixes up oncologic emergencies"),
  "Leukostasis": ("Leukostasis occurs in leukemia with a very high WBC.", "mixes up oncologic emergencies")},
 "Enlarged nodes or a mediastinal mass can squeeze the soft-walled superior vena cava so blood cannot return from the upper body. This is an emergency with dyspnea, edema of the face, neck and arms, and chest pain. Treatment includes chemotherapy or radiation and corticosteroids. (study guide, Ch 13 and Ch 34)", lp=True))

A(mc("hodgkin", "c-hodg-comp",
 "A client with lymphoma reports back pain followed by numbness and tingling in both legs. Which action should the nurse take first?",
 "Perform a neurologic assessment and notify the provider immediately",
 {"Offer a back massage and reassess later": ("Back pain with sensory change may be spinal cord compression, an emergency.", None),
  "Position the client for comfort and reassess in the morning": ("The delay could allow permanent paralysis.", None),
  "Document the findings and continue the plan of care": ("These are warning signs that need an urgent report.", None)},
 "Spinal cord compression is a lymphoma emergency. Back pain and sensory changes come before motor weakness, and bowel and bladder dysfunction is late. Radiation and corticosteroids give rapid relief. (study guide, Ch 13 and Ch 34)"))

A(mc("hodgkin", "c-hodg-comp",
 "A client with lymphoma has a serum calcium of 12 mg/dL, confusion and polyuria. Which intervention should the nurse anticipate?",
 "IV fluids to dilute the calcium",
 {"Restricting oral fluids": ("Fluids are encouraged to dilute the calcium.", None),
  "A calcium supplement": ("The calcium is already too high.", "forgets the client has hypercalcemia"),
  "A dose of heparin": ("Heparin treats clots, not hypercalcemia.", None)},
 "Hypercalcemia above 11 mg/dL is an emergency in lymphoma from bone involvement, causing dehydration, polyuria, confusion and heart block. IV fluids replace losses and dilute calcium. (study guide, Ch 34)"))

A(mc("hodgkin", "c-hodg-comp",
 "A client with lymphoma has involvement of two lymph node regions on the same side of the diaphragm. Which stage does the nurse document?",
 "Stage II",
 {"Stage I": ("Stage I is a single node.", None),
  "Stage III": ("Stage III means nodes on both sides of the diaphragm.", None),
  "Stage IV": ("Stage IV means organs plus nodes.", None)},
 "Lymphoma staging: I is one node, II is two or more nodes on the same side of the diaphragm, III is both sides, and IV is organs plus nodes. E marks extranodal disease and S the spleen. (study guide, Ch 34)"))

A(mc("hodgkin", "c-hodg-dx",
 "A client with painless lymph node enlargement has a CBC, chest x-ray and CT scan. Which test is definitive for diagnosing lymphoma?",
 "Lymph node biopsy",
 {"CBC": ("A CBC shows marrow involvement but does not diagnose lymphoma.", None),
  "Chest x-ray": ("Imaging shows extent, not the diagnosis.", None),
  "Serum uric acid and LDH": ("These are raised from high cell turnover but are not diagnostic.", None),
  "PET scan": ("A PET scan helps staging and does not confirm the diagnosis.", None)},
 "History, CBC, uric acid and LDH, viral testing and imaging support the diagnosis and stage the disease. A lymph node biopsy is definitive, and a bone marrow biopsy or lumbar puncture is added if marrow or CNS involvement is suspected. (study guide, Ch 34)"))

A(mc("hodgkin", "c-hodg-comp",
 "A client with lymphoma is about to start chemotherapy. Which information is most essential for the nurse to teach?",
 "Neutropenic and bleeding precautions",
 {"Preparing for surgery to remove the tumor": ("Surgery to remove the tumor is not typical; chemotherapy is the primary treatment.", None),
  "Preparing for a splenectomy": ("Splenectomy is now rare.", None),
  "How to avoid all fluids to reduce night sweats": ("Fluids replace losses from fever and sweats and dilute calcium.", None),
  "Limiting rest to speed recovery": ("The client should rest often and keep the treatment schedule.", None)},
 "Chemotherapy is the primary treatment for lymphoma, with radiation and immunotherapy. It lowers white cells and platelets, so neutropenic and bleeding precautions are the most essential teaching. The nurse also teaches the infection risk, frequent rest, nutrition, symptoms to report and fertility preservation. (study guide, Ch 34 and class PLQ)", lp=True))

A(tf("hodgkin", "c-hodg-dx",
 "A nurse tells a client with lymphoma that a dry cough that is worse lying flat may mean a mediastinal mass that can compress the airway. The nurse's statement is accurate.",
 True,
 "A mediastinal mass can compress the trachea, so a dry persistent cough worse lying flat is a warning sign and an airway risk. (study guide, Ch 34)",
 "Marking False ignores a warning sign of airway compression.", lp=True))

A(tf("hodgkin", "c-hodg-dx",
 "A nurse teaches that generalized itching with scratch marks is more common in non-Hodgkin lymphoma than in Hodgkin lymphoma. The nurse's teaching is accurate.",
 False,
 "Generalized pruritus with excoriation is common in Hodgkin lymphoma. The true version is that itching is more typical of Hodgkin lymphoma. (study guide, Ch 34)",
 "Marking True gives the symptom to the wrong lymphoma.", lp=True))

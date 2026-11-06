# Reserve questions: for every concept, one multiple choice and one select-all from a different angle.
# They are released two at a time when a question on that concept is missed.
ITEMS = []
A = ITEMS.append

# ---- risk factors
A(mc("risk", "c-risk-list", "A 36-year-old client with breast cancer reports that her mother and her sister also had breast cancer. Which feature most strongly suggests a hereditary cancer syndrome?",
 "A younger-than-usual age together with two first-degree relatives who had the same cancer",
 {"A single tumor found at age 78 with no family history": ("This pattern does not suggest a hereditary syndrome.", None),
  "A tumor in a client who has smoked for 40 years": ("Smoking is a carcinogen exposure, not an inherited pattern.", "mixes up exposure and inheritance"),
  "A cancer found during a routine screening": ("How a cancer was found says nothing about heredity.", None)},
 "Red flags for hereditary cancer include a younger-than-usual age and two or more first-degree relatives with the same cancer. Others are multiple primary tumors, bilateral tumors in paired organs and a tumor in the sex not usually affected. Known genetic syndromes account for 5 to 10% of cancers. (study guide, Ch 13)"))
A(sata("risk", "c-risk-list", "The nurse sorts a client's cancer risk factors into those that can be changed.",
 ["A sedentary lifestyle", "A poor diet", "Smoking", "Heavy alcohol use"],
 {"Age": ("Age cannot be changed.", "mixes up modifiable and nonmodifiable"), "A BRCA1 mutation": ("A genetic predisposition cannot be changed.", "mixes up modifiable and nonmodifiable")},
 "Modifiable risk factors include a sedentary lifestyle, poor diet, smoking and alcohol. Age and genetics are nonmodifiable, and 78% of cancers are diagnosed at age 55 or older. Disease-linked risks are modifiable only as far as the disease is managed. (study guide, Ch 13)"))
A(mc("risk", "c-risk-table", "A client has chronic hepatitis B infection. For which cancer is this client at increased risk?",
 "Liver cancer",
 {"Kidney cancer": ("Kidney cancer is tied to pesticides, solvents and tobacco.", None), "Thyroid cancer": ("Thyroid cancer is tied to ionizing radiation.", None), "Bladder cancer": ("Bladder cancer is tied to tobacco.", None)},
 "The risk table pairs each cancer with its exposures: hepatitis A, B or C and alcohol go with liver cancer. Signs include jaundice, easy bruising and nausea or vomiting. It spreads to the omentum, peritoneum and pleura. (study guide, Ch 13 Table 13.2)"))
A(sata("risk", "c-risk-table", "The nurse reviews risk factors listed for lung cancer.",
 ["Tobacco use", "Asbestos exposure", "Coal, soot or tar exposure", "Wood dust", "Air pollution"],
 {"H. pylori infection": ("H. pylori goes with gastric cancer.", "borrows another cancer's risk"), "Chronic hepatitis B": ("Hepatitis goes with liver cancer.", "borrows another cancer's risk"), "An undescended testicle": ("This is the greatest risk for testicular cancer.", "borrows another cancer's risk")},
 "Lung cancer risk factors in the table are tobacco, asbestos, coal, soot and tar, pollution and wood dust. Signs include chronic cough, hemoptysis, dyspnea and weight loss, and it spreads to brain, bone, adrenal and the other lung. The other options each belong to a different cancer. (study guide, Ch 13 Table 13.2)"))
A(mc("risk", "c-risk-prev", "A nurse counsels a client to quit tobacco and use sunscreen daily. Which level of prevention is this?",
 "Primary prevention",
 {"Secondary prevention": ("Secondary prevention is screening for early detection.", "mixes up prevention levels"), "Tertiary prevention": ("Tertiary prevention reduces harm after a diagnosis.", "mixes up prevention levels"), "Surveillance only": ("Counseling to avoid carcinogens is primary prevention.", None)},
 "Primary prevention stops cancer before it starts through risk factor modification, immunization, chemoprevention and avoiding carcinogens. Quitting tobacco for 10 years lowers lung cancer risk 30 to 50%. Sunscreen daily and a healthy weight are also primary prevention. (study guide, Ch 13)"))
A(sata("risk", "c-risk-prev", "Which activities are secondary prevention?",
 ["A screening mammogram", "A Pap smear", "A colon cancer screening test", "A discussion of PSA screening"],
 {"Giving the HPV vaccine": ("Immunization is primary prevention.", "mixes up prevention levels"), "Daily sunscreen": ("Avoiding carcinogens is primary prevention.", "mixes up prevention levels")},
 "Secondary prevention is screening for early detection: general check-up, breast, cervical, colon and prostate. A good screening test is sensitive, with few false negatives, and specific, with few false positives. Immunization and avoiding carcinogens are primary prevention. (study guide, Ch 13)"))
A(mc("risk", "c-risk-caution", "A client has had hoarseness and a nagging cough for 3 weeks. Which action should the nurse take?",
 "Refer the client for evaluation, because a CAUTION sign lasting more than 2 weeks needs evaluation",
 {"Reassure the client that it will probably clear up on its own": ("A sign lasting more than 2 weeks needs evaluation.", "waits too long"), "Advise waiting 3 more months": ("This delays evaluation.", "waits too long"), "Advise an over-the-counter cough suppressant only": ("This does not evaluate the cause.", None)},
 "The N in CAUTION is a nagging cough or hoarseness. Any CAUTION sign that lasts more than 2 weeks needs a provider's evaluation. Early detection is the point of secondary prevention. (study guide, Ch 13)"))
A(sata("risk", "c-risk-caution", "Which findings are among the seven CAUTION warning signs?",
 ["A change in bowel or bladder habits", "A sore that does not heal", "Unusual bleeding or discharge", "Indigestion or difficulty swallowing", "An obvious change in a wart or mole"],
 {"Night sweats": ("Night sweats are a constitutional sign, not one of the seven CAUTION letters.", "confuses constitutional signs with CAUTION"), "Unexplained weight loss": ("Weight loss is a constitutional sign, not one of the seven CAUTION letters.", "confuses constitutional signs with CAUTION")},
 "CAUTION lists seven changes: bowel or bladder habits, a sore that does not heal, unusual bleeding or discharge, thickening or lump, indigestion or difficulty swallowing, a change in a wart or mole, and a nagging cough or hoarseness. Constitutional signs are separate: fatigue, fever of unknown cause, unexplained weight loss and night sweats. (study guide, Ch 13)"))

# ---- staging
A(mc("stage", "c-stage-tnm", "A client's chart reads T2, N0, M0. Which interpretation by the nurse is correct?",
 "A tumor in size category 2 with no lymph node involvement and no metastasis",
 {"A tumor with spread to two lymph nodes": ("N0 means no lymph node involvement.", None), "A tumor that has metastasized": ("M0 means no metastasis.", "reads M0 as spread"), "A tumor with unknown size": ("T gives the tumor size.", None)},
 "T is the size of the tumor, N is the number of lymph nodes involved, and M is the presence of metastasis. A zero in N or M means none. M1 means the cancer has spread. (study guide, Ch 13)"))
A(sata("stage", "c-stage-tnm", "Which statements about cancer staging are correct?",
 ["Stage I is small with no obvious spread outside the organ", "Stage IV means the cancer has metastasized", "All hematologic malignancies are stage IV at diagnosis", "M1 means metastasis is present"],
 {"Grade shows how far the cancer has spread": ("Grade shows how differentiated the cells are; stage shows spread.", "mixes up grade and stage"), "Stage II means the cancer has spread to distant organs": ("Stage II invades deeper tissue or local nodes; distant spread is stage IV.", "mixes up the stage numbers")},
 "Staging shows size, nodes and metastasis. Stage II invades deeper tissue or local nodes, stage III is large or locally advanced, and stage IV has metastasized. Grading is separate and describes differentiation. (study guide, Ch 13)"))
A(mc("stage", "c-stage-sizes", "A client's breast cancer is 6 cm with no lymph node involvement and no metastasis. Which stage does the nurse expect?",
 "Stage IIB",
 {"Stage IIA": ("Stage IIA is 2 to 5 cm with no nodes, or under 2 cm with nodes.", "mixes up the breast cutoffs"), "Stage IIIA": ("Stage IIIA is over 5 cm with nodes, or any size with 4 to 8 nodes.", "mixes up the breast cutoffs"), "Stage IB": ("Stage IB is no tumor or under 2 cm with small node involvement.", "mixes up the breast cutoffs"), "Stage IV": ("Stage IV needs distant metastasis.", None)},
 "Breast sizes are 2 cm or less for stage I, 2 to 5 cm for stage II, and over 5 cm for IIB or III. A tumor over 5 cm with no nodes is stage IIB; with nodes it moves to IIIA. Nodes of 4 to 8 are IIIA, up to 9 is IIIB and 10 or more is IIIC. (study guide, Ch 65)"))
A(sata("stage", "c-stage-sizes", "Which staging facts are correct?",
 ["Prostate T1 cannot be felt", "Prostate T4 invades neighboring organs", "The maximum Gleason score is 10", "Ovarian stage II means spread into the pelvis"],
 {"Prostate T2 invades neighboring organs": ("T2 is confined to the prostate; T4 invades neighboring organs.", "mixes up the T numbers"), "A Gleason score of 2 is the worst": ("A higher Gleason score is worse.", "reverses the Gleason scale")},
 "Prostate staging runs T1 not felt, T2 confined, T3 locally extensive, T4 invading neighbors. Gleason adds two grades of 1 to 5 for a maximum of 10, and higher is worse. Ovarian FIGO staging is I ovaries, II pelvis, III peritoneum and/or nodes, IV distant. (study guide, Ch 65 and Ch 66)"))

# ---- biopsy
A(mc("biopsy", "c-bx-types", "Which biopsy is the least traumatic but yields fewer cells?",
 "Fine-needle aspiration",
 {"Excisional biopsy": ("Excisional removes the whole mass and a margin.", None), "Core needle biopsy": ("Core needle takes a larger sample with a wider needle.", None), "Surgical excision with wire localization": ("This removes a mass surgically after marking it.", None)},
 "FNA uses a needle to suction cells and is less traumatic, but gives fewer cells and limited molecular testing. Core needle and vacuum-assisted biopsies give larger samples. The excisional biopsy is preferred for diagnosis because it removes the whole mass. (study guide, Ch 13)"))
A(sata("biopsy", "c-bx-types", "Which statements about a sentinel node biopsy are correct?",
 ["It finds the first node the cancer drains to", "A radioactive tracer or blue dye is used", "It determines the stage", "If it is negative, no more nodes are removed"],
 {"If it is positive, no further surgery is needed": ("A positive sentinel node leads to an axillary dissection of 20 to 40 nodes.", "swaps negative and positive"), "It is used to diagnose lymphoma": ("Lymphoma is confirmed with a lymph node biopsy.", None)},
 "The sentinel node is the first node the cancer would reach. A negative result means the full axillary dissection can be skipped. A positive result leads to dissection of 20 to 40 nodes. (study guide, Ch 65)"))
A(mc("biopsy", "c-bx-site", "A client has an abnormal Pap smear and positive high-risk HPV. Which test is diagnostic for cervical cancer?",
 "A cervical biopsy taken at colposcopy",
 {"A repeat Pap smear": ("The Pap is a screening test.", "mixes up screening and diagnosis"), "An HPV test": ("The HPV test shows risk, not the diagnosis.", "mixes up screening and diagnosis"), "A pelvic MRI": ("MRI is used for staging.", None)},
 "After an abnormal result with high-risk HPV the cervix is examined at colposcopy and abnormal areas are biopsied. The biopsy is diagnostic. MRI, PET, CT and chest x-ray stage the cancer. (study guide, Ch 65)"))
A(sata("biopsy", "c-bx-site", "Which biopsy or diagnostic facts are correct for the site named?",
 ["An endometrial biopsy is 99% sensitive for high-grade cancer", "A D&C is done if the endometrial biopsy is negative but bleeding continues", "Bronchoscopy allows biopsy of the airways", "An ovarian mass is diagnosed by surgical removal and pathology"],
 {"A needle biopsy is the preferred test for an ovarian mass": ("Biopsy of an ovarian mass is not recommended.", "applies breast habits to the ovary"), "Mediastinoscopy is a blood test": ("It is a surgical incision to view and biopsy the mediastinum.", None)},
 "Each organ has its own sampling method. The ovary is removed and examined because a needle biopsy could spread cells. The endometrium is sampled with biopsy or D&C, the airways with bronchoscopy, and the mediastinum with mediastinoscopy. (study guide, Ch 13, Ch 26 and Ch 65)"))
A(mc("biopsy", "c-bx-marrow", "A client had a bone marrow biopsy 26 hours ago, and the dressing is soaked with blood. Which action should the nurse take?",
 "Report it to the provider, because bleeding that soaks the dressing or lasts more than 24 hours must be reported",
 {"Reinforce the dressing and recheck tomorrow": ("This bleeding must be reported.", "waits too long"), "Remove the dressing to inspect the site": ("The dressing stays on at least 24 hours and bleeding is reported.", None), "Document it as an expected finding": ("Expected care is pressure and a dry dressing; soaking is not expected.", None)},
 "After the biopsy the nurse applies direct pressure for 5 to 10 minutes and a sterile dressing, and the client rests for several hours. The dressing stays on at least 24 hours. Report bleeding that soaks the dressing or lasts more than 24 hours, and watch for infection. (study guide, Ch 33)"))
A(sata("biopsy", "c-bx-marrow", "Which actions are part of preparing a client for a bone marrow biopsy?",
 ["Obtain informed consent", "Ask about allergies", "Check platelets, coagulation studies and anticoagulants", "Explain that pressure and a brief pulling pain will be felt"],
 {"Tell the client that nothing will be felt": ("The client feels pressure on insertion and a brief pulling pain on aspiration.", None), "Position the client supine for the posterior iliac crest": ("The posterior iliac crest uses prone or side-lying; supine is for the sternum or anterior iliac crest.", "mixes up positions")},
 "Preparation covers consent, allergies and bleeding risk. The procedure takes 5 to 10 minutes and a mild sedative is allowed. The client may hear crunching. (study guide, Ch 33)"))

# ---- lung
A(mc("lung", "c-lung-types", "A client with small cell lung cancer asks about the outlook. Which response is accurate?",
 "“The outlook is poor at any stage; only 5 to 10% survive 5 years.”",
 {"“If it is found early, 5-year survival is good.”": ("That describes non-small cell cancer.", "gives small cell the non-small cell outlook"), "“Surgery usually cures it when there is no metastasis.”": ("Surgery is used primarily for non-small cell cancer.", "mixes up the two types"), "“It grows more slowly than other lung cancers.”": ("Small cell grows quickly and spreads early.", None)},
 "Small cell cancer is 15% of lung cancers, grows quickly and spreads to other organs. Its outlook is poor at any stage, and your class notes give 6 months to 1 year. Non-small cell cancer has a good 5-year survival when found early. (study guide, Ch 26 and class notes)"))
A(sata("lung", "c-lung-types", "Which statements are true of small cell (oat cell) lung cancer?",
 ["It makes up about 15% of lung cancers", "It grows quickly", "It spreads to other organs early", "Its outlook is poor at any stage"],
 {"It has three cell types: adenocarcinoma, squamous cell and large cell": ("Those are the three types of non-small cell cancer.", "mixes up the two types"), "Surgery is the primary treatment when there is no metastasis": ("That is used for non-small cell cancer.", "mixes up the two types")},
 "Small cell lung cancer is fast and spreads early, and outcomes are poor. Non-small cell cancer, about 85%, includes the three cell types and is the group where surgery is used when there is no metastasis. (study guide, Ch 26)"))
A(mc("lung", "c-lung-dx", "Which test allows the provider to see the airways and take a tissue sample?",
 "Bronchoscopy",
 {"PET scan": ("PET shows metabolic activity and does not take tissue.", None), "Chest x-ray": ("A chest x-ray finds the lesion.", None), "Bone scan": ("A bone scan looks for metastasis.", None)},
 "Bronchoscopy passes a scope through the mouth or nose to view the trachea and bronchi and biopsy. Sputum cytology may identify the tumor cells, and mediastinoscopy is a surgical incision to biopsy the mediastinum. A PET scan shows metabolism. (study guide, Ch 26)"))
A(sata("lung", "c-lung-dx", "Which findings are cues for lung cancer?",
 ["A new cough that does not go away", "Hemoptysis", "Hoarseness", "Chest pain", "Frequent pneumonia or bronchitis"],
 {"Perioral tingling with laryngospasm": ("That fits hypocalcemia.", None), "Ribbon-like stools": ("That suggests a bowel obstruction.", None)},
 "Lung cancer is often silent early. Cues include a new or changed cough, hemoptysis, shortness of breath, wheezing, hoarseness, chest pain, weight loss and frequent pneumonia. Headache and bone pain suggest metastasis. (study guide, Ch 26)"))
A(mc("lung", "c-lung-tx", "Cancer is found in one small area of one lobe of a client's lung with no metastasis. Which surgery does the nurse expect?",
 "Wedge resection",
 {"Pneumonectomy": ("This removes the entire lung for diffuse spread.", "mixes up the extent"), "Lobectomy": ("This removes an entire lobe for cancer localized to one lobe.", "mixes up the extent"), "Mediastinoscopy": ("This is a diagnostic incision, not a treatment.", None)},
 "A wedge resection removes a small section of a lobe. A lobectomy removes the whole lobe and a pneumonectomy removes the whole lung. Surgery is preferred if there is no metastasis. (study guide, Ch 26)"))
A(sata("lung", "c-lung-tx", "Which statements about lung cancer treatment are correct?",
 ["Radiation can be used for palliation of symptoms and pain", "Chemotherapy can be neoadjuvant or adjuvant", "Palliative care begins at diagnosis", "Cancer pain doses are given around the clock"],
 {"Surgery is preferred even when metastasis is present": ("Surgery is preferred when there is no metastasis.", None), "WHO step 1 uses a strong opioid": ("Step 1 is a nonopioid; strong opioids are step 3.", "mixes up the ladder steps")},
 "Treatment depends on the type, size, location and stage. Chemotherapy is primary for advanced disease or a client too ill for surgery. Pain is managed by the WHO ladder with around-the-clock dosing. (study guide, Ch 26)"))
A(mc("lung", "c-lung-nursing", "Which finding after a lobectomy suggests hemorrhage?",
 "Excess bloody chest tube drainage with hypotension and tachycardia",
 {"Cloudy chest tube drainage": ("Cloudy drainage suggests infection.", "mixes up bleeding and infection"), "Continuous bubbling in the water-seal chamber": ("This is an air leak.", None), "Diminished breath sounds": ("This suggests atelectasis.", None)},
 "After lobectomy the nurse watches vital signs, breath sounds, the suture line and the chest tube. Hypotension or tachycardia may mean excessive blood or fluid loss, and excess bloody drainage suggests a bleed. (study guide, Ch 26)"))
A(sata("lung", "c-lung-nursing", "Which are correct about chest tube care?",
 ["Keep the system closed", "Never clamp the chest tube", "Monitor the water-seal chamber", "Persistent bubbling means an air leak"],
 {"Clamp the tube briefly for transport": ("The tube is never clamped.", "believes a brief clamp is safe"), "Cloudy drainage is expected": ("Cloudy drainage suggests infection.", None)},
 "The closed system prevents air leaks. Clamping can trap air or fluid and cause a tension pneumothorax. The nurse watches drainage for bleeding or infection. (study guide, Ch 26)"))

# ---- labs
A(mc("labs", "c-labs-cbc", "A client with a bacterial infection has a WBC differential. Which cell type is expected to rise?",
 "Neutrophils",
 {"Eosinophils": ("Eosinophils rise with allergies and parasites.", None), "Lymphocytes": ("Lymphocytes rise with viral infections.", None), "Basophils": ("Basophils rise with allergy and inflammation.", None)},
 "Neutrophils are 50 to 70% of white cells, fight bacteria and fungi, and are the first to arrive. They rise with bacterial infection and fall with chemotherapy and radiation. A left shift means many immature neutrophils. (study guide, Ch 33)"))
A(sata("labs", "c-labs-cbc", "Which statements about neutrophils and the ANC are correct?",
 ["Neutrophils are the first white cells to arrive at an infection", "They remain in circulation about 6 hours", "Chemotherapy and radiation lower them", "An ANC below 1,500 is neutropenia"],
 {"The ANC measures platelets": ("The ANC counts neutrophils.", "mixes up neutropenia and thrombocytopenia"), "Mature neutrophils are called bands": ("Mature neutrophils are segs; immature ones are bands.", None)},
 "Neutrophils are phagocytic and first on the scene. Mature cells are segs and immature cells are bands. A low ANC means a high risk of infection. (study guide, Ch 33)"))
A(mc("labs", "c-labs-plt", "A client's platelet count is 18,000/mm³. Which expectation by the nurse is correct?",
 "Spontaneous bleeding is possible and platelets are usually transfused",
 {"No bleeding precautions are needed": ("Precautions start below 100,000.", None), "The count is a normal variation": ("Normal is 150,000 to 450,000.", None), "A fatal bleed is not possible at any count": ("A fatal CNS or GI bleed is possible below 5,000.", None)},
 "Below 20,000 spontaneous bleeding occurs and platelets are usually transfused. Bleeding precautions start below 100,000, and below 5,000 a fatal bleed is possible. (study guide, Ch 33 and Ch 34)"))
A(sata("labs", "c-labs-plt", "Which are bleeding precautions for a client with thrombocytopenia?",
 ["Use a soft-bristle toothbrush", "Use an electric razor", "Avoid IM injections", "Give a daily stool softener", "Teach the client not to blow the nose"],
 {"Take rectal temperatures": ("Rectal temperatures are avoided.", "uses a rectal route"), "Encourage vigorous flossing": ("Flossing is avoided.", None)},
 "Bleeding precautions reduce trauma: soft toothbrush, electric razor, shoes on, a clutter-free room, stool softener, no rectal thermometers, suppositories or enemas, and minimal BP cuff inflation. Direct pressure or ice for 5 minutes stops a cut. (study guide, Ch 34 Box 34.1)"))
A(mc("labs", "c-labs-iron", "Which instruction about oral iron is correct?",
 "Take it with orange juice and not with milk",
 {"Take it with milk to protect the stomach": ("Dairy blocks iron absorption.", "forgets that dairy blocks iron"), "Take it with an antacid": ("Antacids reduce iron absorption.", None), "Take it only when fatigue is severe": ("Iron is taken daily as prescribed.", None)},
 "Vitamin C increases absorption, and class notes add taking iron on an empty stomach. Oral iron can cause nausea, constipation, diarrhea and dark stools. IM iron uses Z-track. (study guide, Ch 34 and class notes)"))
A(sata("labs", "c-labs-iron", "Which statements about iron deficiency are correct?",
 ["Ferritin reflects iron stores", "Transferrin carries iron", "TIBC is high because there are empty binding spots", "Oral iron is first-line treatment"],
 {"Ferritin is high in iron deficiency": ("Ferritin is low in iron deficiency.", "reverses ferritin"), "Iron deficiency causes macrocytic cells": ("Iron deficiency causes microcytic cells.", "mixes up microcytic and macrocytic")},
 "Ferritin is stored iron, transferrin is the transport protein, and TIBC measures the iron transferrin could carry. In iron deficiency stores are empty, so ferritin and saturation are low and TIBC is high. (study guide, Ch 33)"))
A(mc("labs", "c-labs-coag", "A client is receiving a heparin infusion. Which laboratory test does the nurse use to monitor it?",
 "PTT",
 {"PT/INR": ("PT/INR monitors warfarin.", "mixes up heparin and warfarin"), "Bleeding time": ("Bleeding time tests platelet function.", None), "Ferritin": ("Ferritin is an iron store test.", None)},
 "The intrinsic pathway is monitored by PTT and the drug is heparin. The extrinsic pathway is monitored by PT/INR and the drug is warfarin. Your class notes list PT and PTT together; PTT is the safe answer for heparin. (study guide, Ch 33)"))
A(sata("labs", "c-labs-coag", "Which statements about clotting studies are correct?",
 ["PTT monitors heparin", "PT/INR monitors warfarin", "The warfarin INR goal is 2 to 3", "Platelet aggregation is impaired by aspirin"],
 {"PT monitors heparin": ("PT/INR monitors warfarin.", "mixes up heparin and warfarin"), "Bleeding time is done when platelets are 50,000": ("It is not done if platelets are under 75,000.", None)},
 "The two pathways each have a test and a drug. Platelet aggregation is impaired in von Willebrand disease and with aspirin or NSAIDs. (study guide, Ch 33)"))

# ---- leukemia
A(mc("leuk", "c-leuk-patho", "Which CBC pattern does the nurse expect in a client with newly diagnosed acute leukemia?",
 "Leukocytosis with anemia and thrombocytopenia",
 {"Leukopenia with polycythemia": ("Leukemia causes leukocytosis, and the red cells fall.", None), "Normal white cells with high platelets": ("Platelets fall because the marrow is crowded.", None), "High hemoglobin with high platelets": ("These rise in polycythemia vera.", "mixes up leukemia and polycythemia")},
 "Blasts crowd the marrow so RBCs and platelets fall while the white count may rise. Early on the count can look normal because only cells that escape into the blood show up. (study guide, Ch 34)"))
A(sata("leuk", "c-leuk-patho", "Which findings are expected in leukemia?",
 ["Swollen lymph glands", "Frequent infections and low-grade fevers", "Fatigue and pallor", "Bruising and petechiae", "Bone pain"],
 {"Bradycardia and weight gain": ("Leukemia causes weight loss from high metabolic demand.", None), "Ruddy facial flushing with itching after a bath": ("That fits polycythemia vera.", "mixes up leukemia and polycythemia")},
 "Blasts congest nodes and spleen, cause infections and anemia, and crowd out platelets. Bone pain comes from marrow swelling, and weight loss from high metabolism. (study guide, Ch 34)"))
A(mc("leuk", "c-leuk-risk", "A client has leukemia with the Philadelphia chromosome in more than 90% of cases. Which type does the nurse recognize?",
 "Chronic myeloid leukemia",
 {"Acute lymphoblastic leukemia": ("ALL is the common childhood type.", None), "Chronic lymphocytic leukemia": ("CLL is a chronic lymphoid type.", None), "Hodgkin lymphoma": ("Hodgkin lymphoma is a lymph node cancer.", None)},
 "The Philadelphia chromosome, a 9;22 swap, is found in more than 90% of CML. Imatinib targets the Bcr-Abl protein it produces. (study guide, Ch 34)"))
A(sata("leuk", "c-leuk-risk", "Which clients are at higher risk for leukemia?",
 ["A child with Down syndrome", "A worker with benzene exposure", "A client who received radiation", "A client who received prior chemotherapy"],
 {"A client with chronic H. pylori infection": ("H. pylori goes with gastric cancer.", "borrows another cancer's risk"), "A client with hepatitis B": ("Hepatitis goes with liver cancer.", "borrows another cancer's risk")},
 "Down syndrome raises the risk 10 to 30 times, and radiation, benzene and prior chemotherapy damage marrow cells. Smoking also adds risk. (study guide, Ch 34)"))
A(mc("leuk", "c-leuk-tx", "Which therapy uses the client's own T cells, engineered to kill leukemia cells?",
 "CAR-T therapy",
 {"Monoclonal antibody therapy": ("Monoclonal antibodies are made proteins, not engineered T cells.", None), "Induction chemotherapy": ("Chemotherapy is a drug treatment.", None), "Radiation to the brain and spine": ("This treats CNS disease.", None)},
 "CAR-T cells are the client's T cells engineered to kill leukemia cells, and the effect is permanent. Patients may live without B cells. (study guide, Ch 34)"))
A(sata("leuk", "c-leuk-tx", "Which statements about leukemia treatment are correct?",
 ["Chemotherapy is given in induction, consolidation and maintenance phases", "Brain and spine radiation treats CNS involvement", "Transplant is used for refractory or relapsed disease", "Prophylactic antimicrobials are given in neutropenia"],
 {"Remission means the client is cured": ("Remission is not a cure.", "treats remission as a cure"), "G-CSF is always indicated in leukemia": ("It is generally not indicated, since it may fuel the disease.", None)},
 "Therapy includes chemotherapy, targeted drugs, immunotherapy, transplant and supportive blood products. GVHD is a risk of transplant. (study guide, Ch 34)"))
A(mc("leuk", "c-leuk-nursing", "A 25-year-old client with leukemia will begin chemotherapy. Which teaching is a priority?",
 "Banking sperm or eggs before therapy because of the sterility risk",
 {"Chemotherapy has no effect on fertility": ("Sterility is a risk.", None), "Fertility can be restored by taking vitamins": ("This is not supported.", None), "Fertility is not discussed until after remission": ("Banking must happen before therapy.", None)},
 "Teaching covers neutropenic and bleeding precautions, signs of anemia and thrombocytopenia, the disease course, chemotherapy reactions and the sterility risk. Offering sperm or egg banking before therapy is a priority. (study guide, Ch 34)"))
A(sata("leuk", "c-leuk-nursing", "Which assessments does the nurse make for a client with leukemia?",
 ["Vital signs for fever", "Bruising and non-blanching petechiae", "CBC and WBC", "Signs of anemia such as pallor and dizziness"],
 {"Rectal temperature": ("Rectal temperatures are never taken in neutropenia.", "uses a rectal route"), "Deep palpation of the spleen": ("The spleen can rupture with deep palpation.", None)},
 "Assessments include fever, anemia signs, bruising and petechiae, and the CBC. Fever may be the first and only sign of infection. (study guide, Ch 34)"))

# ---- neutropenic precautions
A(mc("neut", "c-neut-def", "A client's ANC is 1,200/mm³. Which statement by the nurse is accurate?",
 "The client has neutropenia, and neutropenic precautions are formally started at 500 or below",
 {"The client has a normal ANC": ("An ANC below 1,500 is neutropenia.", None), "The client has thrombocytopenia": ("ANC counts neutrophils.", "mixes up neutropenia and thrombocytopenia"), "The client needs a platelet transfusion": ("Platelets are not shown.", None)},
 "Neutropenia is an ANC below 1,500, and neutropenic precautions start at 500 or below. A temperature of 100.4°F (38°C) or higher needs immediate care. (study guide, Ch 13 and Ch 34)"))
A(sata("neut", "c-neut-def", "Which statements about fever in a chemotherapy client are correct?",
 ["A temperature of 100.4°F (38°C) or higher is called in immediately", "Fever may be the first and only sign of infection", "IV broad-spectrum antibiotics are given immediately", "Fever with neutropenia can lead to sepsis"],
 {"Acetaminophen is given and the client waits to see if the fever settles": ("Waiting delays treatment.", "treats the fever at home"), "A low-grade fever is expected and can be ignored": ("It needs immediate care.", None)},
 "Myelosuppression plus fever is treated aggressively to prevent sepsis and shock. The client checks the temperature daily and calls for more than 100.4°F. (study guide, Ch 13 and Ch 34)"))
A(mc("neut", "c-neut-prec", "Which item should the nurse remove from the room of a client with neutropenia?",
 "A humidifier or a vase of fresh flowers",
 {"A hand sanitizer dispenser": ("Hand hygiene is a core precaution.", None), "A box of tissues": ("Tissues are not a hazard in the precautions.", None), "A call light": ("The call light is needed.", None)},
 "Live plants, cut flowers and standing water carry bacteria and mold, so they are removed. Reverse isolation means staff wear PPE to protect the client. (study guide, Ch 34 Box 34.2 and class notes)"))
A(sata("neut", "c-neut-prec", "Which actions are consistent with neutropenic precautions?",
 ["A private room", "Hand hygiene by everyone", "Washing raw fruits and vegetables well", "Restricting visitors with communicable diseases"],
 {"A humidifier at the bedside": ("No standing water or humidifiers.", None), "A potted plant on the windowsill": ("No live plants.", "forgets that plants carry mold")},
 "Precautions also include avoiding crowds, sick people, small children and pets, no rectal temperatures, suppositories or enemas, and taking prophylactic antimicrobials. (study guide, Ch 34 Box 34.2)"))

# ---- Hodgkin
A(mc("hodgkin", "c-hodg-dx", "Which finding helps the nurse distinguish a lymphoma node from an infected node?",
 "The lymphoma node is painless, while an infected node is usually more tender",
 {"The lymphoma node is hot and tender": ("Painful nodes suggest infection.", None), "The lymphoma node disappears within 48 hours": ("Lymphoma nodes persist.", None), "The lymphoma node causes high fever only": ("B symptoms accompany painless nodes.", None)},
 "Lymphoma causes painless lymph node swelling. Malignant nodes are usually less tender than infected ones. B symptoms are fever, drenching night sweats and weight loss. (study guide, Ch 34 and Ch 13)"))
A(sata("hodgkin", "c-hodg-dx", "Which tests are used for suspected lymphoma?",
 ["Lymph node biopsy", "Uric acid and LDH", "Chest x-ray, CT and PET", "Bone marrow biopsy if marrow involvement is suspected"],
 {"Bence Jones protein in the urine": ("That is a myeloma test.", "mixes up lymphoma and myeloma"), "JAK2 gene testing": ("JAK2 testing is for polycythemia vera.", None)},
 "History, CBC and imaging support the diagnosis, and a lymph node biopsy is definitive. A lumbar puncture is added if CNS involvement is suspected. (study guide, Ch 34)"))
A(mc("hodgkin", "c-hodg-comp", "A client with Hodgkin lymphoma has back pain followed by leg weakness. Which complication does the nurse suspect?",
 "Spinal cord compression",
 {"Superior vena cava syndrome": ("SVC syndrome causes facial and arm swelling and dyspnea.", None), "Hypercalcemia": ("Hypercalcemia causes polyuria and confusion.", None), "Venous thrombosis": ("DVT causes leg pain or swelling.", None)},
 "A mass can compress the spinal cord, causing back pain and sensory changes before motor weakness. It is an emergency treated with radiation and corticosteroids. (study guide, Ch 13 and Ch 34)"))
A(sata("hodgkin", "c-hodg-comp", "Which are complications of lymphoma?",
 ["Superior vena cava syndrome", "Spinal cord compression", "Hypercalcemia", "Myelodysplasia", "Venous thrombosis"],
 {"Leukostasis from a very high WBC in AML": ("Leukostasis occurs in AML with a very high WBC.", None), "SIADH from lung and brain cancer": ("SIADH is tied to brain and lung cancer.", None)},
 "Lymphoma complications include SVC syndrome, cord compression, hypercalcemia above 11, myelodysplasia, hepatic or renal failure, hyperviscosity and venous thrombosis. (study guide, Ch 34)"))

# ---- multiple myeloma
A(mc("mm", "c-mm-patho", "Which finding in a client with multiple myeloma shows kidney injury?",
 "A creatinine above 2 mg/dL with Bence Jones protein in the urine",
 {"A hemoglobin of 14 g/dL": ("This does not show kidney injury.", None), "A platelet count of 300,000": ("This is a normal platelet count.", None), "A serum calcium of 9 mg/dL": ("This is normal calcium.", None)},
 "Excess light chains are toxic to the kidney, and calcium adds stones and injury. Renal insufficiency, creatinine above 2 mg/dL, is the R in CRAB. (study guide, Ch 34)"))
A(sata("mm", "c-mm-patho", "Which facts describe multiple myeloma?",
 ["A clone of plasma cells makes an M protein", "Lytic bone lesions release calcium", "Excess light chains are toxic to the kidneys", "Plasma cells are 10% or more of the marrow"],
 {"Reed–Sternberg cells are the hallmark": ("That is Hodgkin lymphoma.", "mixes up myeloma and Hodgkin lymphoma"), "B symptoms are the classic presentation": ("Bone pain and CRAB are classic for myeloma.", None)},
 "Myeloma is an incurable plasma cell cancer, with an average age of 62, and is more common in people of African descent. It leads to bone pain, anemia, infection and hypercalcemia. (study guide, Ch 34)"))
A(mc("mm", "c-mm-nursing", "Which statement by a client with multiple myeloma shows understanding?",
 "“I will drink plenty of fluids to protect my kidneys.”",
 {"“I will limit fluids so I do not have to urinate at night.”": ("Fluids dilute calcium and protect the kidneys.", "restricts fluids in hypercalcemia"), "“I will take a calcium supplement for my bones.”": ("Calcium is already high.", "forgets the client has hypercalcemia"), "“I will stay in bed all day.”": ("Walking as tolerated prevents DVT and builds bone.", None)},
 "Fluids dilute calcium and protect the kidneys, and ambulation as tolerated builds bone and prevents DVT. Bisphosphonates reduce bone breakdown. (study guide, Ch 34 and class notes)"))
A(sata("mm", "c-mm-nursing", "Which findings should a client with multiple myeloma report immediately?",
 ["Sudden severe pain", "New numbness or tingling", "Confusion", "Fatigue, shortness of breath or dizziness"],
 {"Feeling comfortable after drinking fluids": ("This is expected.", None), "Taking short walks each day": ("Ambulation is encouraged.", None)},
 "Sudden severe pain or pain in a new spot may mean a fracture. New numbness or tingling may mean cord compression, and confusion may mean hypercalcemia. (study guide, Ch 34)"))

# ---- breast
A(mc("breast", "c-breast-tx", "A client is diagnosed with ductal carcinoma in situ. Which treatment does the nurse expect?",
 "Surgery",
 {"No treatment, only mammograms": ("That is the plan for lobular carcinoma in situ.", "mixes up DCIS and LCIS"), "Chemotherapy alone": ("DCIS requires surgery.", None), "Immunotherapy alone": ("Surgery is required.", None)},
 "DCIS is stage 0, confined to the lining of the milk ducts, and requires surgery. LCIS is no longer considered cancer and is followed with mammograms. (study guide, Ch 65)"))
A(sata("breast", "c-breast-tx", "Which statements about breast cancer treatment are correct?",
 ["Neoadjuvant chemotherapy is first line for intermediate and advanced operable cancer", "Radiation follows lumpectomy", "Radiation follows mastectomy if 4 or more nodes are positive", "Trastuzumab is used for HER2-positive tumors", "Endocrine therapy for receptor-positive tumors lasts 5 to 10 years"],
 {"Lumpectomy is not followed by radiation": ("It is always followed by radiation.", "skips radiation after lumpectomy"), "LCIS requires mastectomy": ("LCIS has no treatment.", "treats LCIS like invasive cancer")},
 "Treatment depends on stage: surgery, chemotherapy, radiation, targeted therapy, immunotherapy and endocrine therapy. Metastatic disease focuses on quality and quantity of life. (study guide, Ch 65)"))
A(mc("breast", "c-breast-meds", "A client on letrozole asks about long-term effects. Which risk should the nurse mention?",
 "Osteoporosis and fractures",
 {"Cardiotoxicity": ("Cardiotoxicity is linked to trastuzumab.", "mixes up drug effects"), "Endometrial cancer": ("That is a tamoxifen risk.", "mixes up drug effects"), "Hemorrhagic cystitis": ("That is a chemotherapy effect of ifosfamide.", None)},
 "Aromatase inhibitors block the conversion of androgens to estrogen and are taken for 5 to 10 years. Their main risk is osteoporosis and fractures. (study guide, Ch 65 and Davis Table 65.3)"))
A(sata("breast", "c-breast-meds", "Which effects are associated with tamoxifen?",
 ["Hot flashes", "Irregular bleeding or spotting", "Vaginal dryness or discharge", "DVT and PE", "Endometrial cancer"],
 {"Cardiotoxicity": ("This is linked to trastuzumab.", "mixes up drug effects"), "Hearing loss": ("This is not an effect of tamoxifen.", None)},
 "Tamoxifen is a SERM taken for 5 to 10 years. It also carries stroke, cataract and bone loss risk, and SSRIs reduce its metabolism. (study guide, Ch 65)"))
A(mc("breast", "c-breast-male", "Which statement about hormone therapy for male breast cancer is correct?",
 "It is used only when the tumor is receptor-positive",
 {"It is used for every male breast cancer": ("It works only on receptor-positive tumors.", None), "It is used instead of surgery": ("Mastectomy is usual.", None), "It is used to treat HER2-positive tumors": ("HER2-positive tumors get trastuzumab or pertuzumab.", "mixes up receptor and HER2 therapy")},
 "ER/PR testing tells whether hormone therapy will work, and HER2 testing tells whether monoclonal antibody therapy will work. Tamoxifen, aromatase inhibitors and fulvestrant are used only for receptor-positive tumors. (study guide, Ch 66)"))
A(sata("breast", "c-breast-male", "Which facts about male breast cancer are correct?",
 ["It is about 100 times less common than in women", "BRCA2 is the more common mutation", "It spreads early to the nipple, skin and muscle", "Mastectomy is the usual surgery"],
 {"Lumpectomy is the usual surgery": ("There is too little tissue for lumpectomy.", "assumes breast conservation applies"), "Radiation is the main treatment": ("Radiation is rarely used.", None)},
 "The usual age is 60 to 70. Targeted therapy with trastuzumab or pertuzumab for HER2-positive tumors can cause hypertension, bleeding, poor wound healing, clots and kidney damage. (study guide, Ch 66)"))
A(mc("breast", "c-breast-nursing", "Which is the most common long-term effect after axillary node removal?",
 "Immobility of the shoulder",
 {"Hypothermia": ("This is not a listed effect.", None), "Hemoptysis": ("This is a lung cancer cue.", None), "Gynecomastia": ("This is a sign of testicular cancer metastasis.", None)},
 "Long-term effects include pain, scarring, lymphedema (arm swelling from node removal) and shoulder immobility. Shoulder immobility is the most common. (study guide, Ch 65 and class notes)"))
A(sata("breast", "c-breast-nursing", "Which nursing actions apply after breast cancer surgery?",
 ["Assess vital signs for infection or bleeding", "Inspect the wound for redness, warmth or purulent drainage", "Measure daily weight", "Use a pain scale", "Watch mood and nonverbal cues for depression"],
 {"Apply rubefacients such as menthol rubs to radiated skin": ("Rubefacients are not used on radiated skin.", None), "Teach monthly breast self-exam as screening": ("Self-exam is not recommended.", None)},
 "The nurse also gives chemotherapy and antiemetics, cough and deep breathing prevent atelectasis, and encourages verbalization. (study guide, Ch 65)"))

# ---- uterine
A(mc("uterine", "c-ut-risk", "Which client is at highest risk for uterine cancer?",
 "A postmenopausal client with obesity who takes estrogen without progesterone and has a uterus",
 {"A premenopausal client who takes estrogen with progesterone": ("Progesterone with estrogen is protective.", "forgets that progesterone is protective"), "A client who exercises and keeps a healthy weight": ("This lowers risk.", None), "A client with HPV infection and no other risk": ("HPV is the cause of cervical cancer.", "borrows a cervical risk factor")},
 "Unopposed estrogen and obesity are the number one risk factors. The usual age is 55 to 65, and tamoxifen, PCOS and diabetes add risk. (study guide, Ch 65)"))
A(sata("uterine", "c-ut-risk", "Which are risk factors for uterine cancer?",
 ["Unopposed estrogen", "Obesity", "Tamoxifen use", "Polycystic ovary syndrome", "Diabetes"],
 {"Estrogen given with progesterone": ("It is protective.", None), "HPV infection": ("This is cervical cancer's cause.", "borrows a cervical risk factor")},
 "Estrogen without progesterone, anovulation, early menarche and late menopause increase risk. About 2 to 5% are hereditary. (study guide, Ch 65 and Ch 13)"))
A(mc("uterine", "c-ut-dx", "Which treatment is the usual adjuvant therapy after surgery for uterine cancer?",
 "Radiation",
 {"Lumpectomy": ("This is a breast surgery.", None), "Brachytherapy seeds in the prostate": ("This is prostate treatment.", None), "Trachelectomy": ("This is cervical surgery.", None)},
 "Treatment is surgical removal of the uterus, tubes and ovaries with washings and lymphadenectomy. Radiation is the usual adjuvant, and chemotherapy is for high-risk or higher-stage disease. (study guide, Ch 65)"))
A(sata("uterine", "c-ut-dx", "Which tests are used for suspected uterine cancer?",
 ["Endometrial biopsy", "Transvaginal ultrasound showing a thickened endometrium", "Dilation and curettage if the biopsy is negative but bleeding continues"],
 {"CA-125 screening": ("CA-125 is an ovarian marker and not a screening test.", "borrows an ovarian test"), "Colposcopy": ("Colposcopy is for the cervix.", None)},
 "Any postmenopausal bleeding needs evaluation, and the usual age is 55 to 65. (study guide, Ch 65)"))

# ---- cervical
A(mc("cervical", "c-cerv-screen", "A 35-year-old client had a normal Pap and HPV cotest today. When is her next screening?",
 "In 5 years",
 {"In 1 year": ("Ages 30 to 65 with a cotest are screened every 5 years.", None), "In 3 years": ("Every 3 years applies to Pap alone.", "mixes up the intervals"), "Never again": ("Screening continues to 65.", None)},
 "From age 30 to 65, primary HPV or a Pap and HPV cotest is repeated every 5 years, or Pap alone every 3 years. (study guide, Ch 65)"))
A(sata("cervical", "c-cerv-screen", "Which clients may need more frequent cervical screening?",
 ["A client with HIV", "An immunosuppressed client", "A client with DES exposure", "A client with prior dysplasia"],
 {"A client with a hysterectomy for a benign cause and no CIN 2": ("She may stop screening.", None), "A 67-year-old with adequate negative screening": ("She may stop.", None)},
 "HIV, immunosuppression, DES exposure or prior dysplasia may need more frequent screening. Transgender men still need breast, Pap and pelvic screening. (study guide, Ch 65)"))
A(mc("cervical", "c-cerv-dx", "During colposcopy the cervix is swabbed with Lugol's solution. Which finding indicates abnormal tissue?",
 "Areas that do not stain brown",
 {"Areas that stain brown": ("Normal tissue stains brown.", "reverses the stain"), "Areas that turn blue": ("This is not the described finding.", None), "No visible change": ("Abnormal areas do not stain.", None)},
 "Acetic acid and Lugol's iodine are applied and abnormal tissue does not stain brown; those areas are biopsied. Lugol's is contraindicated with iodine or shellfish allergy. (study guide, Ch 64)"))
A(sata("cervical", "c-cerv-dx", "Which are risk factors for HPV-related cervical cancer?",
 ["Early sexual activity", "Multiple partners", "Low socioeconomic status", "Immunosuppression"],
 {"HPV vaccination": ("The vaccine is preventive.", None), "Routine Pap screening": ("Screening is protective.", None)},
 "Contributors include HSV-2, smoking, douching, poor nutrition and long-term oral contraceptive use. (study guide, Ch 65)"))
A(mc("cervical", "c-cerv-tx", "Which statement about pelvic exenteration is correct?",
 "It removes all pelvic organs and can cure a pelvic recurrence, leaving a colostomy and urinary diversion",
 {"It is used for early cervical cancer in a client who wants fertility": ("A trachelectomy is used for fertility preservation.", "mixes up exenteration and trachelectomy"), "It removes only the cervix": ("That is a radical trachelectomy.", "mixes up exenteration and trachelectomy"), "It is a screening procedure": ("It is surgery.", None)},
 "Mortality is about 5% and morbidity about 70%. A client who has already been radiated can only receive chemotherapy. (study guide, Ch 65)"))
A(sata("cervical", "c-cerv-tx", "Which statements about cervical cancer treatment are correct?",
 ["Brachytherapy is internal radiation placed in or next to the tumor", "Chemotherapy makes the cells more sensitive to radiation", "A radical trachelectomy preserves fertility", "Five-year survival is 92% when localized"],
 {"Pelvic exenteration is used for early disease": ("It is for pelvic recurrence.", None), "Hysterectomy preserves fertility": ("A hysterectomy removes the uterus.", None)},
 "Higher stages use chemoradiation. Five-year survival is 92% localized, 58% regional and 17% distant. (study guide, Ch 65)"))

# ---- prostate
A(mc("prostate", "c-pros-patho", "To which sites does prostate cancer typically spread?",
 "Lymph nodes, bone, rectum and bladder",
 {"Brain and adrenal glands first": ("That is lung cancer's pattern.", "borrows another cancer's pattern"), "Peritoneum, omentum and pleura": ("That is ovarian cancer's pattern.", "borrows another cancer's pattern"), "Liver, lung and muscle": ("That is colon cancer's pattern.", "borrows another cancer's pattern")},
 "Prostate cancer spreads cell-to-cell to the rectum, pelvic floor, lower spine and hip. Bone pain suggests metastasis. (study guide, Ch 66 and Ch 13)"))
A(sata("prostate", "c-pros-patho", "Which are risk factors for prostate cancer?",
 ["Family history including BRCA mutations", "A diet high in red meat", "High calcium intake", "High body mass index", "Smoking"],
 {"A diet high in vegetables": ("Vegetables are protective.", None), "Selenium-rich foods": ("Selenium is protective.", None)},
 "More than 7 multivitamins a week, chemicals and STIs also add risk. Protective factors include vegetables, vitamin E, lycopene, selenium and antioxidants. (study guide, Ch 66)"))
A(mc("prostate", "c-pros-tx", "A client has prostate cancer that has spread to the bone. Which therapy suppresses testosterone, the hormone that feeds the tumor?",
 "Ablative hormone therapy",
 {"Brachytherapy": ("This places radioactive seeds.", None), "Cryotherapy": ("This freezes the prostate.", None), "TURP": ("This treats BPH by removing inner prostate tissue.", None)},
 "Ablative hormone therapy is used when cancer has spread to nodes or bone, and it is neoadjuvant when used to shrink the prostate before radiation. (study guide, Ch 66)"))
A(sata("prostate", "c-pros-tx", "Which statements about prostate cancer treatment are correct?",
 ["External beam radiation runs 5 times a week for 8 weeks", "Radical prostatectomy removes the prostate and seminal vesicles", "Chemotherapy is used once the cancer is hormone-refractory", "Brachytherapy seeds are placed permanently through the perineum"],
 {"Brachytherapy seeds are removed after one week": ("Prostate brachytherapy seeds are permanent.", "thinks the seeds are temporary"), "Cryotherapy has a high success rate": ("It has a low success rate and is often repeated.", None)},
 "CyberKnife takes 4 to 5 sessions. Cryotherapy can cause impotence, incontinence and rectal complications. (study guide, Ch 66)"))
A(mc("prostate", "c-pros-postop", "Which finding after prostate surgery should the client report?",
 "Fever, increasing pain and swelling at the site",
 {"Light pink urine on the first day": ("Light pink urine is expected with irrigation.", None), "A soft stool": ("Soft stool is the goal.", None), "Mild fatigue": ("Mild fatigue is not a warning sign.", None)},
 "Infection shows as fever, increasing pain, swelling, redness, drainage and nausea or vomiting. Clots and bleeding are also reported. (study guide, Ch 66)"))
A(sata("prostate", "c-pros-postop", "Which nursing actions apply after a radical prostatectomy?",
 ["Manage bladder irrigation", "Give stool softeners", "Use aseptic wound care", "Monitor for infection"],
 {"Encourage straining at stool": ("Straining can cause bleeding.", None), "Give a rectal enema": ("Straining and rectal procedures are avoided.", None)},
 "The outcomes are normal sexual function, normal urination and no incontinence. Teaching covers signs of infection and chemotherapy or radiation effects. (study guide, Ch 66)"))

# ---- testicular
A(mc("testis", "c-test-dx", "Which tumor markers does the nurse follow for testicular cancer?",
 "Alpha-fetoprotein and hCG",
 {"PSA and CA-125": ("PSA is prostate and CA-125 is ovarian.", "borrows other cancers' markers"), "Bence Jones protein": ("That is a myeloma marker.", None), "Reed–Sternberg cells": ("That is a Hodgkin finding.", None)},
 "AFP and hCG should fall after the tumor is removed; if they do not, look for more tumor. (study guide, Ch 66)"))
A(sata("testis", "c-test-dx", "Which findings fit testicular cancer?",
 ["A painless mass", "A firm or heavy feeling in the scrotum", "Swelling and redness", "A dull ache in the abdomen or scrotum"],
 {"Sudden severe pain with high fever": ("That suggests infection or torsion.", None), "Severe pain after a kick to the groin with a normal exam": ("That suggests trauma.", None)},
 "Metastasis may cause GI symptoms, low back pain, gynecomastia, dyspnea, cough, hemoptysis and a neck mass. Self-exam in a warm shower may find it first. (study guide, Ch 66)"))
A(mc("testis", "c-test-tx", "Which type of testicular cancer is radiation sensitive?",
 "Seminoma",
 {"Nonseminoma": ("Nonseminoma is not radiation responsive.", "swaps seminoma and nonseminoma"), "Embryonal carcinoma": ("It is a nonseminoma and is not radiation responsive.", None), "Teratoma": ("It is a nonseminoma and is not radiation responsive.", None)},
 "Seminoma is slow growing, occurs in men in their 30s to 40s, and gets radiation and/or chemotherapy after surgery. Nonseminoma gets node removal and chemotherapy. (study guide, Ch 66)"))
A(sata("testis", "c-test-tx", "Which adverse effects are linked to testicular cancer chemotherapy?",
 ["Hair loss and mouth sores", "Kidney damage", "Neuropathy and ototoxicity", "Lung damage with bleomycin", "Hemorrhagic cystitis with ifosfamide"],
 {"Hemorrhagic cystitis with bleomycin": ("Hemorrhagic cystitis is linked to ifosfamide.", "swaps the drugs"), "Lung damage with ifosfamide": ("Lung damage is linked to bleomycin.", "swaps the drugs")},
 "Chemotherapy can also cause infection, bleeding, nausea and diarrhea, lowered testosterone and cardiovascular risk. (study guide, Ch 66)"))

# ---- end of life
A(mc("eol", "c-eol-diff", "A hospice client's daughter asks whether her father can go back to curative treatment. Which response is correct?",
 "“Yes, a client can leave hospice to restart curative treatment.”",
 {"“No, once enrolled the client cannot leave hospice.”": ("Patients can leave hospice to restart curative treatment.", None), "“Only if the client has not yet been given morphine.”": ("Opioids do not bar a return to treatment.", None), "“Only after a 6-month wait.”": ("There is no required wait.", None)},
 "Hospice means the client stops curative treatment and chooses comfort care. The client can leave hospice to restart curative treatment. (study guide, Other Topics)"))
A(sata("eol", "c-eol-diff", "Which statements correctly relate hospice and palliative care?",
 ["All hospice is palliative", "Palliative care is broader than hospice", "Palliative care can run alongside curative treatment", "Palliative care is not the same as hospice"],
 {"All palliative care is hospice": ("Palliative care is broader.", "mixes up palliative and hospice"), "Hospice can start at diagnosis alongside chemotherapy": ("That is true of palliative care, not hospice.", "mixes up palliative and hospice")},
 "Hospice is for a prognosis of 6 months or less and replaces curative treatment with comfort. Palliative care can start at any stage. (study guide, Other Topics)"))
A(mc("eol", "c-eol-nursing", "Why does the nurse keep talking to a client who is unresponsive and dying?",
 "Hearing is often the last sense lost",
 {"Hearing is always the first sense lost": ("Hearing is often the last sense lost.", "reverses the order"), "Talking restores consciousness": ("This is not supported.", None), "The client's sight is unaffected": ("This is not stated.", None)},
 "Nursing care at the end of life includes emotional and spiritual support for the client and family. (study guide, Other Topics; standard content)"))
A(sata("eol", "c-eol-nursing", "Which nursing actions are appropriate for a dying client?",
 ["Give opioids on schedule for pain and dyspnea", "Provide mouth care", "Reposition the client", "Honor the advance directive and DNR order", "Provide emotional and spiritual support"],
 {"Withhold opioids until the respiratory rate rises": ("Opioids are given to keep the client comfortable.", "undertreats pain out of fear"), "Start curative chemotherapy": ("Curative treatment has stopped in hospice.", "mixes up palliative and hospice")},
 "The goal is comfort. Signs that death is near include falling intake and urine output, mottled extremities, apnea periods and noisy secretions. (study guide, Other Topics)"))

# ---- BPH
A(mc("prostate", "c-bph", "A man is prescribed finasteride (Proscar) for BPH. Which teaching is correct?",
 "A pregnant person should not handle crushed or broken tablets because the drug is teratogenic",
 {"Finasteride relaxes the smooth muscle of the bladder neck": ("That describes alpha-adrenergic blockers.", "mixes up the BPH drug classes"), "It works within 2 weeks": ("5-alpha reductase inhibitors take 3 to 6 months.", None), "It raises the PSA level": ("It lowers PSA.", None)},
 "5-alpha reductase inhibitors block testosterone from becoming DHT, so the prostate shrinks. Effects include decreased libido, ED and breast tenderness, and it can reduce male-pattern baldness. (study guide, Ch 66 and class notes)"))
A(sata("prostate", "c-bph", "Which are manifestations of benign prostatic hyperplasia?",
 ["Difficulty starting the urine stream", "A weak stream", "Dribbling after urination", "Nocturia", "Urgency and frequency"],
 {"It is an early stage of prostate cancer": ("BPH is not cancer and not a precursor.", None), "The PSA can tell BPH from cancer": ("PSA cannot separate them.", None)},
 "BPH affects 50% of men aged 51 to 60 and 90% over 80. Complications include retention, UTI, bladder stones and hydronephrosis. (study guide, Ch 66)"))

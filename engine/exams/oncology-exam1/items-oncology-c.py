# Cancer staging, Cervical guidelines, Testicular cancer, Biopsy procedures, Uterine cancer, Neutropenic precautions.
ITEMS = []
A = ITEMS.append

# ------------------------------------------------------------------ CANCER STAGING (TNM)
A(mc("stage", "c-stage-tnm",
 "A client with stage III breast cancer classified as T3, N2, M1 is being taught about the staging. Which statement by the client indicates a need for further teaching?",
 "“I am relieved that the cancer is still local.”",
 {"“The T tells me about the size of my tumor.”": ("This is correct; T is the size of the tumor.", None),
  "“The N tells me about the lymph nodes that are affected.”": ("This is correct; N is the number of lymph nodes involved.", None),
  "“The M1 tells me the cancer has spread to other parts of my body.”": ("This is correct; M1 means metastasis is present.", None)},
 "TNM stands for tumor size (T), number of lymph nodes involved (N) and presence of metastasis (M). M1 means metastasis is present, so the cancer is not local. A client who feels relieved that it is still local needs more teaching. (study guide, Ch 13 and class PLQ)", lp=True))

A(mc("stage", "c-stage-tnm",
 "A client has been told her breast cancer is stage III and asks what that means. Which description by the nurse is best?",
 "A large tumor or locally advanced cancer that may be in nearby lymph nodes",
 {"A small tumor with no obvious spread outside the organ": ("That describes stage I.", "mixes up the stage numbers"),
  "A tumor that has invaded deeper tissues or local lymph nodes": ("That describes stage II.", "mixes up the stage numbers"),
  "A cancer that has spread to other organs": ("Spread to other organs is stage IV.", "mixes up stage III and IV")},
 "Stage I is small with no obvious spread outside the organ, stage II invades deeper tissues or local nodes, stage III is large or locally advanced and possibly in local nodes, and stage IV has metastasized. Note: your class notes recorded a different answer for this case (spread to the lymph and blood systems); the textbook definition above is the one the case answer key supports, so confirm with your instructor. (study guide, Ch 13 and class PLQ)", lp=True))

A(match2("stage", "c-stage-tnm",
 "The nurse reviews cancer classification terms. Match each term with its meaning.",
 [("T", "Size of the primary tumor"),
  ("N", "Number of lymph nodes involved"),
  ("M", "Presence of distant spread, yes or no"),
  ("Grade", "How differentiated the cells look under the microscope")],
 {"Size of the primary tumor": "T is the tumor size.",
  "Number of lymph nodes involved": "N is the nodes involved.",
  "Presence of distant spread, yes or no": "M is metastasis.",
  "How differentiated the cells look under the microscope": "Grading describes differentiation; poorly differentiated cells are more aggressive."},
 "Staging describes how big the tumor is and how far it has spread. Grading is separate and describes how differentiated the cells look under the microscope, and poorly differentiated cells are harder to treat and more aggressive. (study guide, Ch 13)"))

A(mc("stage", "c-stage-sizes",
 "A client's breast cancer is 3.5 cm with no lymph node involvement and no metastasis. Which stage does the nurse expect on the chart?",
 "Stage IIA",
 {"Stage IA": ("Stage IA is a tumor up to 2 cm with no nodes.", "mixes up the breast size cutoffs"),
  "Stage IB": ("Stage IB is no tumor or under 2 cm with small node involvement.", "mixes up the breast size cutoffs"),
  "Stage IIB": ("Stage IIB is 2 to 5 cm with nodes, or over 5 cm with no nodes.", "mixes up the breast size cutoffs"),
  "Stage IIIA": ("Stage IIIA is over 5 cm with nodes, or any size with 4 to 8 nodes.", "mixes up the breast size cutoffs")},
 "Breast sizes to remember are 2 cm or less (stage I), 2 to 5 cm (stage II), and over 5 cm (stage IIB or III). A 2 to 5 cm tumor with no nodes is stage IIA. Nodes: 4 to 8 for IIIA, up to 9 for IIIB, 10 or more for IIIC. (study guide, Ch 65)", lp=True))

A(mc("stage", "c-stage-sizes",
 "A client's prostate cancer is described as T2. Which description does the nurse understand?",
 "The tumor is confined to the prostate",
 {"The tumor cannot be felt and is not seen on ultrasound": ("That describes T1.", "mixes up the T numbers"),
  "The tumor is locally extensive beyond the gland": ("That describes T3.", "mixes up the T numbers"),
  "The tumor has invaded neighboring organs": ("That describes T4.", "mixes up the T numbers")},
 "Prostate staging: T1 cannot be felt, T2 is confined to the prostate, T3 is locally extensive, and T4 invades neighboring organs. A Gleason grade is added: two sites are graded 1 to 5 and added for a maximum of 10, and a higher score means more poorly differentiated cells. (study guide, Ch 66)", lp=True))

A(mc("stage", "c-stage-sizes",
 "A client's pathology report lists a prostate Gleason score of 9. Which statement by the nurse is accurate?",
 "“A higher score means poorly differentiated cells and a worse prognosis, and 10 is the maximum.”",
 {"“A score of 9 means a 90% chance of cure.”": ("The score is a grade of the cells, not a cure percentage.", None),
  "“A score of 9 means the cancer is stage IX.”": ("Stages run I to IV; Gleason is a grade.", None),
  "“A lower score means more aggressive cancer.”": ("A higher score is worse.", "reverses the Gleason scale"),
  "“The score measures how large the tumor is.”": ("Size is the T in TNM; Gleason measures how differentiated the cells are.", None)},
 "The Gleason score adds the grades of two sites, each 1 to 5, for a maximum of 10. Grade 1 is well differentiated and has the best prognosis, and grade 5 is poorly differentiated. (study guide, Ch 66)"))

A(mc("stage", "c-stage-sizes",
 "A client's ovarian cancer has spread to the peritoneum and lymph nodes. Which FIGO stage does the nurse expect?",
 "Stage III",
 {"Stage I": ("Stage I is limited to the ovaries.", None),
  "Stage II": ("Stage II extends to the pelvis.", None),
  "Stage IV": ("Stage IV is distant spread.", None)},
 "FIGO staging for ovarian cancer is based on surgical findings: I ovaries, II pelvis, III peritoneum and/or nodes, and IV distant. (study guide, Ch 65)"))

A(mc("stage", "c-stage-tnm",
 "A pathology report describes a client's tumor cells as poorly differentiated. Which conclusion should the nurse draw?",
 "The cells look unlike the parent cell, and the cancer is more aggressive and harder to treat",
 {"The tumor is small and has not spread": ("Differentiation describes how cells look, not size or spread.", "mixes up grade and stage"),
  "The tumor has spread to lymph nodes": ("Node spread is the N in TNM.", "mixes up grade and stage"),
  "The cells look like the parent cell and respond well to treatment": ("That describes well differentiated cells.", "reverses the meaning")},
 "Altered differentiation means the cell no longer looks or acts like the parent cell. Well differentiated cells look like the parent cell, while poorly differentiated cells are more aggressive and harder to treat. This is the basis of grading, which is separate from staging. (study guide, Ch 13)"))

A(tf("stage", "c-stage-tnm",
 "A nurse tells a client with leukemia that all hematologic malignancies are considered stage IV at diagnosis because they involve the whole body from the start. The nurse's statement is accurate.",
 True,
 "Leukemia, lymphoma and multiple myeloma arise in blood-forming or lymph tissue and involve the whole body from the start, so they are stage IV at diagnosis. (study guide, Ch 13)",
 "Marking False would stage a leukemia like a small local solid tumor.", lp=True))

A(tf("stage", "c-stage-tnm",
 "A nurse teaches that the grade of a tumor describes how far the cancer has spread in the body. The nurse's teaching is accurate.",
 False,
 "Grade describes how differentiated the cells look; how far the cancer has spread is the stage. The true version is: staging shows size, nodes and metastasis, and grading shows differentiation. (study guide, Ch 13)",
 "Marking True mixes up grade and stage.", lp=True))

# ------------------------------------------------------------------ CERVICAL GUIDELINES
A(mc("cervical", "c-cerv-screen",
 "A 25-year-old client had her first Pap smear at age 21 with normal results. Primary HPV testing is not available at the clinic. Which services should the nurse expect at today's visit?",
 "A breast exam, a pelvic exam and a Pap smear without HPV cotesting",
 {"A Pap smear with an HPV cotest": ("HPV cotesting is not used before age 30.", "applies the 30 and older rule too early"),
  "An HPV test alone every year": ("HPV testing alone is primary screening every 5 years and is not available here.", None),
  "No screening until age 30": ("Pap smears are done every 3 years from age 21.", None),
  "An immediate colposcopy": ("Colposcopy is done after an abnormal result.", None)},
 "Cervical screening starts at 21 with a Pap every 3 years, and HPV testing is only a reflex test if atypical cells are found in ages 21 to 29. Primary HPV screening may start at 25 and repeat every 5 years. The Ch 13 table groups ages 25 to 65, while Ch 65 starts at 21; the Ch 65 schedule is used here. (study guide, Ch 65 and class PLQ)", lp=True))

A(mc("cervical", "c-cerv-screen",
 "A 19-year-old client who is sexually active asks when she needs her first Pap smear. Which response by the nurse is correct?",
 "“Your first Pap smear is at age 21.”",
 {"“You need one now, because you are sexually active.”": ("No screening is done before age 21.", "starts screening at first intercourse"),
  "“You should start at age 25 with an HPV test.”": ("Primary HPV screening may start at 25, but the Pap starts at 21.", None),
  "“You should start at age 30 with a cotest.”": ("Screening starts well before age 30.", None),
  "“You do not need screening if you receive the HPV vaccine.”": ("The vaccine does not replace screening.", None)},
 "No cervical screening is done before age 21. From 21 the Pap is repeated every 3 years. The HPV vaccine at age 11 to 12, and as early as 9, is prevention and does not treat an existing infection. (study guide, Ch 65)", lp=True))

A(sata("cervical", "c-cerv-screen",
 "A nurse reviews screening options for a healthy 40-year-old client.",
 ["Primary HPV testing every 5 years", "A Pap and HPV cotest every 5 years", "A Pap test alone every 3 years"],
 {"A Pap test alone every year": ("Pap alone is repeated every 3 years.", None),
  "A Pap test alone every 5 years": ("Pap alone is every 3 years; the 5-year interval applies to HPV testing.", None)},
 "From age 30 to 65, screening is primary HPV or a Pap and HPV cotest every 5 years, or Pap alone every 3 years. HIV, immunosuppression, DES exposure or prior dysplasia may need more frequent screening. (study guide, Ch 65)", lp=True))

A(mc("cervical", "c-cerv-screen",
 "A 67-year-old client has had adequate negative cervical screenings and no history of CIN 2 in the last 20 years. What should the nurse expect about further screening?",
 "She may stop screening",
 {"She needs a Pap every year for life": ("Screening may stop after 65 with adequate negative results.", None),
  "She needs a colposcopy every 3 years": ("Colposcopy follows an abnormal result.", None),
  "She needs a hysterectomy": ("There is no indication for surgery.", None)},
 "Screening may stop after 65 if prior screening was adequate and negative with no CIN 2 in 20 years. A hysterectomy for a benign cause with no CIN 2 history also ends screening. (study guide, Ch 65)"))

A(mc("cervical", "c-cerv-dx",
 "A client has an abnormal Pap smear and a positive high-risk HPV test. Which procedure does the nurse expect next?",
 "Colposcopy with biopsy",
 {"A repeat Pap smear in 3 years": ("An abnormal result with high-risk HPV is followed up now.", None),
  "A hysterectomy": ("Treatment is decided after the biopsy.", None),
  "A CA-125 blood test": ("CA-125 is an ovarian marker and is not a screening test.", "borrows an ovarian test"),
  "A mammogram": ("A mammogram screens the breast.", None)},
 "An abnormal Pap with high-risk HPV leads to colposcopy: the cervix is swabbed with acetic acid or Lugol's, and abnormal areas are biopsied. The biopsy is diagnostic. MRI, PET, CT and chest x-ray stage the cancer. (study guide, Ch 65 and Ch 64)", lp=True))

A(mc("cervical", "c-cerv-dx",
 "A 40-year-old client with invasive cervical cancer reports bleeding after intercourse. Which statement about the clinical manifestations is accurate?",
 "Vaginal bleeding, especially after intercourse, is the most common symptom of invasive cancer, while dysplasia has no symptoms",
 {"Early dysplasia causes heavy bleeding and pain": ("Dysplasia has no symptoms and usually cannot be seen.", None),
  "Bloating and early satiety are the typical first signs": ("That is the pattern of ovarian cancer.", "borrows ovarian symptoms"),
  "A hard painless breast lump is typical": ("That describes breast cancer.", None)},
 "Cervical dysplasia has no symptoms. Vaginal bleeding, especially postcoital bleeding, is the most common symptom of invasive cancer, and malodorous discharge and pain with intercourse may be present. The nursing focus is prevention through Pap screening and the HPV vaccine. (study guide, Ch 65)", lp=True))

A(mc("cervical", "c-cerv-dx",
 "A client is scheduled for a colposcopy. Which statement by the client indicates understanding of the preparation?",
 "“I will not put anything in my vagina for 24 hours before the test.”",
 {"“I need a full bladder for this test.”": ("The client empties the bladder first; a full bladder is for pelvic ultrasound.", "mixes up colposcopy and ultrasound prep"),
  "“It is fine to use Lugol's solution even though I am allergic to shellfish.”": ("Lugol's is contraindicated with iodine or shellfish allergy.", None),
  "“I should schedule it for the heaviest day of my period.”": ("The test is rescheduled if menstruating heavily.", None)},
 "Before a colposcopy the client empties the bladder, has nothing in the vagina for 24 hours, and the test is rescheduled during heavy menstruation. A pregnancy test and consent are done, and Lugol's is contraindicated with iodine or shellfish allergy. (study guide, Ch 64)"))

A(mc("cervical", "c-cerv-tx",
 "A 29-year-old client with early-stage cervical cancer wants to keep her fertility. Which surgery does the nurse expect to be offered?",
 "Radical trachelectomy",
 {"Radical hysterectomy with lymph node dissection": ("This is for a client who does not desire fertility.", None),
  "Pelvic exenteration": ("Exenteration is for recurrence confined to the pelvis and removes all pelvic organs.", None),
  "Chemoradiation with brachytherapy": ("This is used for higher stages and is not a fertility-preserving surgery.", None)},
 "Early disease may be treated with cone biopsy or a radical trachelectomy, which removes the cervix only, for a client who wants to keep fertility. Without a fertility wish, simple or radical hysterectomy with node dissection is done. Higher stages use chemoradiation, and pelvic exenteration can cure a pelvic recurrence. (study guide, Ch 65)"))

A(tf("cervical", "c-cerv-dx",
 "A nurse tells a student that most cervical cancers are squamous cell carcinomas that arise in the transformation zone where the endocervix meets the ectocervix. The nurse's statement is accurate.",
 True,
 "About 90% of cervical cancers are squamous cell carcinomas arising in the transformation zone. Most of the rest are adenocarcinomas of the glandular cells of the endocervix. The Pap samples this junction. (study guide, Ch 65 and Ch 64)",
 "Marking False denies the main cell type of cervical cancer.", lp=True))

A(tf("cervical", "c-cerv-dx",
 "A nurse tells a client that HPV vaccination treats an existing HPV infection and makes cervical screening unnecessary. The nurse's statement is accurate.",
 False,
 "The vaccine is given at age 11 to 12 (it can start at 9) and does not treat an existing infection. Routine screening is still needed. The true version is that vaccination is prevention and screening continues. (study guide, Ch 65)",
 "Marking True would tell the client to skip screening.", lp=True))

# ------------------------------------------------------------------ TESTICULAR CANCER
A(mc("testis", "c-test-dx",
 "A 31-year-old client reports a firm, painless lump in his scrotum with a heavy feeling. Which part of his history is the greatest risk factor for testicular cancer?",
 "An undescended testicle in childhood",
 {"Klinefelter's syndrome": ("Klinefelter's is a listed risk but not the greatest.", "ranks a minor risk above cryptorchidism"),
  "HIV infection": ("HIV is a listed risk but not the greatest.", "ranks a minor risk above cryptorchidism"),
  "Cigarette smoking": ("Smoking is listed among others but is not the greatest.", "ranks a minor risk above cryptorchidism"),
  "Down syndrome": ("Down syndrome is listed among other risks but is not the greatest.", "ranks a minor risk above cryptorchidism")},
 "Cryptorchidism, one or both testes failing to descend from the abdomen into the scrotum, is the greatest risk factor. Others include Down syndrome, Klinefelter's, HIV, family history, cancer in the other testicle and smoking. The average age is 33, and the cure rate is 90 to 100% if it is found early. (study guide, Ch 66)", lp=True))

A(mc("testis", "c-test-dx",
 "A 29-year-old client has a mass in one testicle. Which description of the classic presentation does the nurse expect?",
 "A painless mass, sometimes with a firm or heavy feeling in the scrotum",
 {"Sudden severe scrotal pain with fever after a kick to the groin": ("Sudden pain after trauma suggests testicular injury, not the classic cancer mass.", "confuses trauma with cancer"),
  "A tender, red, hot scrotum with painful urination": ("Painful, red and hot suggests infection such as epididymitis.", None),
  "Bright red blood in the semen with urgency": ("That points toward the prostate, not the testis.", None)},
 "The classic sign of testicular cancer is a painless mass. Some men have a dull abdominal ache or a dull scrotal ache, a firm or heavy feeling, swelling and redness. Metastasis may cause GI symptoms, low back pain, gynecomastia, cough or hemoptysis. (study guide, Ch 66)", lp=True))

A(mc("testis", "c-test-tx",
 "A client with testicular cancer asks the nurse about the best treatment. Which response is correct?",
 "“Treatment for all types starts with removal of the affected testicle.”",
 {"“Radiation alone is the best first treatment.”": ("Radiation is added after surgery for seminoma only.", None),
  "“Chemotherapy alone is used first for every type.”": ("Surgery comes first; chemotherapy follows.", None),
  "“Hormone therapy is the first treatment.”": ("Hormone therapy is not the treatment for testicular cancer.", None),
  "“Observation with ultrasound is enough for all types.”": ("Removal of the testicle and its blood supply is the starting treatment.", None)},
 "All types start with orchiectomy through an abdominal incision. Seminoma then gets radiation and/or chemotherapy; nonseminoma gets lymph node removal and chemotherapy, not radiation. Chemotherapy drugs include cisplatin, etoposide, bleomycin, ifosfamide, paclitaxel and vinblastine. (study guide, Ch 66 and class PLQ)", lp=True))

A(mc("testis", "c-test-dx",
 "A client's AFP and hCG levels stayed elevated after orchiectomy. What does the nurse understand this to mean?",
 "More tumor may remain, so further workup is needed",
 {"The surgery cured the cancer": ("These markers should fall after the tumor is removed.", None),
  "The client has developed hypercalcemia": ("The markers are not calcium results.", None),
  "The client has a benign condition": ("Persistent elevation points to remaining tumor.", None)},
 "Alpha-fetoprotein and hCG are tumor markers for testicular cancer, and staging is TNM plus S for serum tumor markers. They should fall after removal of the tumor, and if they do not, more tumor should be looked for. (study guide, Ch 66)"))

A(sata("testis", "c-test-tx",
 "The nurse is teaching a client who will start treatment for testicular cancer.",
 ["Bank sperm before treatment to preserve fertility", "Follow up for at least 10 years", "Retroperitoneal lymph node removal can damage nerves that control ejaculation", "Report signs of infection after surgery"],
 {"Fertility is not affected by treatment": ("Treatment can affect fertility, which is why sperm banking is offered first.", None),
  "Follow-up can stop after 1 year": ("Follow-up lasts at least 10 years, the usual window for recurrence.", None),
  "Chemotherapy has no effect on the kidneys or hearing": ("Chemotherapy can cause kidney damage and ototoxicity.", None)},
 "Bank sperm before treatment, follow up for at least 10 years, and know that retroperitoneal lymph node resection may damage the ejaculation nerves. Report infection signs. Chemotherapy can cause hair loss, mouth sores, nausea, infection, bleeding, kidney damage, neuropathy, ototoxicity, lung damage with bleomycin and hemorrhagic cystitis with ifosfamide. (study guide, Ch 66)", lp=True))

A(match2("testis", "c-test-tx",
 "The nurse reviews testicular cancer facts. Match each item with its description.",
 [("Seminoma", "Slow-growing and very sensitive to radiation"),
  ("Nonseminoma", "Grows and spreads faster and is not responsive to radiation"),
  ("Bleomycin", "Can cause lung damage"),
  ("Ifosfamide", "Can cause hemorrhagic cystitis")],
 {"Slow-growing and very sensitive to radiation": "Seminoma occurs in men in their 30s to 40s.",
  "Grows and spreads faster and is not responsive to radiation": "Nonseminoma includes embryonal and teratoma types, from teens to 40s.",
  "Can cause lung damage": "Bleomycin is the chemotherapy listed for lung damage.",
  "Can cause hemorrhagic cystitis": "Ifosfamide is listed for hemorrhagic cystitis."},
 "Seminoma is slow growing and radiation sensitive, so it is treated with surgery then radiation and/or chemotherapy. Nonseminoma grows faster and is not radiation responsive, so it gets surgery, node removal and chemotherapy. (study guide, Ch 66)"))

A(mc("testis", "c-test-tx",
 "A client returns from an orchiectomy with a blood pressure of 88/50 mm Hg and a heart rate of 124 beats per minute. What does the nurse suspect?",
 "Volume loss",
 {"Infection": ("Fever, not hypotension with tachycardia, points to infection.", None),
  "Pain only": ("Pain can raise the heart rate but does not lower the blood pressure.", None),
  "Normal recovery": ("These vital signs are abnormal.", None)},
 "After testicular surgery hypotension and tachycardia mean volume loss, while fever means infection. The nurse gives aseptic wound care and watches for infection. (study guide, Ch 66)"))

A(tf("testis", "c-test-tx",
 "A nurse explains to a client that alpha-fetoprotein and hCG levels should fall after the tumor is removed. The nurse's statement is accurate.",
 True,
 "AFP and hCG are tumor markers that should fall after removal of the tumor; failure to fall suggests more tumor. (study guide, Ch 66)",
 "Marking False would make a persistent rise sound normal.", lp=True))

A(tf("testis", "c-test-tx",
 "A nurse teaches a client with a nonseminoma that radiation is the main treatment because this type is very sensitive to radiation. The nurse's teaching is accurate.",
 False,
 "Nonseminoma grows and spreads faster and is not responsive to radiation. It is treated with surgery plus lymph node removal, then chemotherapy. Seminoma is the radiation-sensitive type. (study guide, Ch 66)",
 "Marking True gives nonseminoma the seminoma's radiation sensitivity.", lp=True))

# ------------------------------------------------------------------ BIOPSY PROCEDURES
A(mc("biopsy", "c-bx-types",
 "A client asks why the provider wants a biopsy when a CT scan already shows a mass. Which response by the nurse is best?",
 "“A biopsy is the most specific test and is required for a definite diagnosis of cancer.”",
 {"“A CT scan can identify the exact cell type of the tumor.”": ("CT shows the location and organ or vessel involvement, not the cell type.", "thinks imaging can diagnose cancer"),
  "“A PET scan is the most specific test for cancer.”": ("A PET scan shows metabolic hot spots and supports the diagnosis.", "thinks imaging can diagnose cancer"),
  "“A tumor marker blood test is enough to confirm cancer.”": ("Markers support the diagnosis and track treatment but do not confirm it.", "thinks labs can diagnose cancer"),
  "“A biopsy is done only after treatment has started.”": ("Tissue is needed to diagnose, stage and grade before treatment.", None)},
 "Labs and imaging are supportive. A biopsy is the most specific way to diagnose cancer and gives tissue for stage and grade. Results take 3 to 10 days. CT shows the mass location, PET shows active areas, and MRI is best for brain, joint and breast. (study guide, Ch 13 and class PLQ)", lp=True))

A(mc("biopsy", "c-bx-types",
 "A client with a breast mass is scheduled for an excisional biopsy rather than an incisional biopsy. The client asks why. Which response by the nurse is correct?",
 "“An excisional biopsy removes the whole mass with a margin, while an incisional biopsy can track cancer cells through normal tissue.”",
 {"“An incisional biopsy removes the whole mass, so it is preferred.”": ("The excisional biopsy removes the whole mass; incisional cuts into the mass.", "swaps excisional and incisional"),
  "“An excisional biopsy only suctions a few cells with a needle.”": ("That describes fine-needle aspiration.", None),
  "“An excisional biopsy tests the blood for tumor DNA.”": ("That describes a liquid biopsy.", None),
  "“Both types carry the same risk of spreading cells.”": ("The incisional type can track cells through normal tissue.", None)},
 "Excisional biopsy removes the whole mass plus a margin and is preferred. Incisional (core) biopsy cuts into the mass and risks tracking cancer cells through normal tissue. Fine-needle aspiration is less traumatic but yields fewer cells. (study guide, Ch 13)", lp=True))

A(match2("biopsy", "c-bx-types",
 "The nurse reviews biopsy procedures. Match each with its description.",
 [("Fine-needle aspiration", "A needle suctions cells from near the skin; less traumatic but fewer cells"),
  ("Core needle biopsy", "A wider needle with a cutter removes a larger sample"),
  ("Vacuum-assisted biopsy", "An imaging-guided probe with a vacuum and rotating cutter, with no sutures"),
  ("Sentinel node biopsy", "Finds the first node the cancer drains to and determines the stage")],
 {"A needle suctions cells from near the skin; less traumatic but fewer cells": "This is FNA, such as for a breast mass.",
  "A wider needle with a cutter removes a larger sample": "This is a core needle biopsy.",
  "An imaging-guided probe with a vacuum and rotating cutter, with no sutures": "This is vacuum-assisted biopsy, done with local anesthesia.",
  "Finds the first node the cancer drains to and determines the stage": "This is a sentinel node biopsy, using a radioactive tracer or blue dye."},
 "FNA, core needle and vacuum-assisted biopsies are different needle methods with different sample sizes. A surgical excision removes a mass under 2.5 cm entirely, and a nonpalpable mass is marked with a hooked wire first. A sentinel node biopsy finds the first node the cancer drains to. (study guide, Ch 13 and Ch 65)"))

A(mc("biopsy", "c-bx-types",
 "A client's sentinel lymph node biopsy is negative for cancer. What does the nurse understand this to mean?",
 "No further nodes need to be removed",
 {"A full axillary dissection of 20 to 40 nodes is still required": ("Axillary dissection is done when the sentinel node is positive.", "swaps negative and positive"),
  "The cancer has metastasized to bone": ("The sentinel node does not show bone spread.", None),
  "The tumor is stage IV": ("A negative sentinel node does not make a stage IV tumor.", None)},
 "The sentinel node is the first node the cancer would reach, found with a radioactive tracer or blue dye, and it determines the stage. If it is negative, the full axillary dissection can be skipped. If it is positive, an axillary dissection of 20 to 40 nodes follows. (study guide, Ch 65)", lp=True))

A(mc("biopsy", "c-bx-site",
 "A client has a pelvic mass thought to be ovarian cancer. The client asks why the provider is not doing a needle biopsy of the mass. Which response is correct?",
 "“A biopsy could spread the cancer cells; the diagnosis is made by removing the mass surgically and examining it.”",
 {"“A needle biopsy is always done first for ovarian masses.”": ("Biopsy of an ovarian mass is not recommended.", "applies breast biopsy habits to the ovary"),
  "“A CA-125 blood test is enough to diagnose ovarian cancer.”": ("CA-125 is normal in 50% of early cases and also rises with other conditions.", None),
  "“A Pap smear will confirm the diagnosis.”": ("A Pap samples the cervix.", None)},
 "A biopsy of an ovarian mass is not recommended because it could spread the cancer. The definitive diagnosis is surgical removal of the mass plus pathology. In uterine cancer the endometrial biopsy is 99% sensitive for high-grade cancer, and D&C is done if the biopsy is negative but bleeding continues. (study guide, Ch 65)", lp=True))

A(mc("biopsy", "c-bx-marrow",
 "A client is scheduled for a bone marrow aspiration and biopsy. Which statement by the client indicates a need for further teaching?",
 "“Odds are I will die from this procedure.”",
 {"“I will feel pressure when the needle goes in.”": ("This is correct teaching.", None),
  "“I may feel a brief pulling pain when the marrow is drawn out.”": ("This is correct teaching.", None),
  "“I will keep the dressing on for at least 24 hours.”": ("This is correct teaching.", None)},
 "The procedure takes 5 to 10 minutes and a mild sedative is allowed. The client feels pressure on insertion and a brief pulling pain on aspiration, and may hear crunching. A statement that the client will die from it shows fear and misinformation and needs correction. (study guide, Ch 33 and class PLQ)", lp=True))

A(mc("biopsy", "c-bx-marrow",
 "The nurse prepares a client for a bone marrow biopsy at the most common site. Which position does the nurse use?",
 "Prone or side-lying, for the posterior iliac crest",
 {"Supine, because the most common site is the sternum": ("The most common site is the posterior iliac crest; the sternum and anterior iliac crest use supine.", "swaps the common site and position"),
  "Sitting upright with the arms crossed": ("This does not expose the posterior iliac crest.", None),
  "Trendelenburg": ("This position is not used for this procedure.", None)},
 "The most common site is the posterior iliac crest, with the client prone or side-lying. The sternum or anterior iliac crest is done supine. Before the procedure: consent, allergies and bleeding risk (platelets, coagulation studies, anticoagulants). (study guide, Ch 33)"))

A(sata("biopsy", "c-bx-marrow",
 "The nurse provides care after a bone marrow biopsy.",
 ["Hold direct pressure for 5 to 10 minutes and apply a sterile dressing", "Have the client rest for several hours", "Leave the dressing on for at least 24 hours", "Report bleeding that soaks the dressing or lasts more than 24 hours"],
 {"Remove the dressing after 1 hour to inspect the site": ("The dressing stays on at least 24 hours.", None),
  "Encourage vigorous exercise right away": ("The client rests for several hours.", None)},
 "After the procedure the nurse applies direct pressure for 5 to 10 minutes and a sterile dressing, and the client rests for several hours. The dressing stays on at least 24 hours. Bleeding that soaks the dressing or lasts more than 24 hours is reported, and the nurse watches for infection and gives analgesia. (study guide, Ch 33)"))

A(mc("biopsy", "c-bx-types",
 "A client asks what a liquid biopsy is. Which description by the nurse is accurate?",
 "A blood test that looks for cancer cells or tumor DNA",
 {"Removal of the whole mass with a margin": ("That describes an excisional biopsy.", None),
  "A needle that suctions cells from a mass": ("That describes fine-needle aspiration.", None),
  "A scope that looks inside the airways": ("That describes bronchoscopy.", None)},
 "A liquid biopsy is a blood test for cancer cells or tumor DNA, used for example in non-small cell lung, breast, colorectal, GI and ovarian cancers. (study guide, Ch 13)"))

A(tf("biopsy", "c-bx-types",
 "A nurse tells a client that the results of a tissue biopsy usually take 3 to 10 days. The nurse's statement is accurate.",
 True,
 "Biopsy results take 3 to 10 days. The nurse explains the purpose, preparation, aftercare and when results are expected. (study guide, Ch 13)",
 "Marking False gives the client an unrealistic expectation about when results arrive.", lp=True))

A(tf("biopsy", "c-bx-types",
 "A nurse tells a client that blood tests and imaging can give a definitive diagnosis of cancer without a biopsy. The nurse's statement is accurate.",
 False,
 "Labs and imaging are supportive. A biopsy is required for a definitive cytopathologic diagnosis. The true version is that tissue confirmation is needed. (study guide, Ch 13)",
 "Marking True treats supportive tests as diagnostic.", lp=True))

# ------------------------------------------------------------------ UTERINE CANCER
A(mc("uterine", "c-ut-dx",
 "A 60-year-old postmenopausal client calls the clinic. Which statement requires the nurse's immediate follow-up?",
 "“I have had some vaginal bleeding.”",
 {"“I feel a little tired in the afternoons.”": ("Mild afternoon fatigue is not the red flag for uterine cancer.", None),
  "“I have mild joint stiffness in the mornings.”": ("This is not the key warning sign for a gynecologic cancer.", None),
  "“I had trouble falling asleep last night.”": ("This is not the key warning sign for a gynecologic cancer.", None),
  "“I had heartburn after a spicy dinner.”": ("This is not the key warning sign for a gynecologic cancer.", None)},
 "Abnormal uterine or vaginal bleeding is the most common symptom of uterine cancer, and any postmenopausal bleeding needs evaluation. The typical age is 55 to 65, and the median is 60. (study guide, Ch 65 and class PLQ)", lp=True))

A(sata("uterine", "c-ut-risk",
 "The nurse reviews risk factors for uterine (endometrial) cancer.",
 ["Unopposed estrogen exposure", "Obesity", "Tamoxifen use", "Early menarche and late menopause", "Polycystic ovary syndrome"],
 {"Estrogen given together with progesterone": ("Progesterone with estrogen is protective; the risk is estrogen without progesterone.", "forgets that progesterone is protective"),
  "Maintaining a healthy weight and exercising": ("These help prevent uterine cancer.", None),
  "HPV infection": ("HPV is the cause of cervical cancer.", "borrows a cervical risk factor")},
 "The number one risk factors are unopposed estrogen (estrogen therapy without progesterone, tamoxifen, anovulation) and obesity, since fat makes estrogen. Chapter 13 adds early menarche, late menopause, PCOS and diabetes. (study guide, Ch 65 and Ch 13)", lp=True))

A(mc("uterine", "c-ut-risk",
 "A nurse is describing the most common type of uterine cancer to a client. Which description is correct?",
 "Endometrioid adenocarcinoma, which is estrogen-driven and usually found early",
 {"Serous or clear cell carcinoma, which is the most common type": ("Type II serous or clear cell cancers are aggressive and occur in older clients, but they are not the most common.", None),
  "Uterine sarcoma, which is the most common type": ("Sarcoma makes up only 3 to 5%.", None),
  "Squamous cell carcinoma of the cervix": ("That is the main type of cervical cancer.", "borrows a cervical cancer type")},
 "About 80% of uterine cancers are endometrioid adenocarcinoma, type I, estrogen-driven and usually early with about 88% survival. Type II is aggressive and has a poor prognosis, and sarcoma of the muscle is 3 to 5%. (study guide, Ch 65)"))

A(mc("uterine", "c-ut-dx",
 "A postmenopausal client has vaginal bleeding. Which diagnostic test does the nurse expect to be done first for uterine cancer?",
 "Endometrial biopsy",
 {"CA-125 blood test": ("CA-125 is an ovarian marker.", "borrows an ovarian test"),
  "Colposcopy": ("Colposcopy is for the cervix after an abnormal Pap.", None),
  "Mammogram": ("A mammogram screens the breast.", None)},
 "The endometrial biopsy is 99% sensitive for high-grade cancer, and a pelvic transvaginal ultrasound shows a thickened endometrium. A D&C scrapes the lining if the biopsy is negative but bleeding continues. (study guide, Ch 65)", lp=True))

A(mc("uterine", "c-ut-dx",
 "A client's endometrial biopsy is negative but she continues to have postmenopausal bleeding. Which procedure does the nurse expect?",
 "Dilation and curettage",
 {"No further testing is needed": ("Continued bleeding needs evaluation.", None),
  "Repeat screening in 3 years": ("The bleeding needs follow-up now.", None),
  "A bone marrow biopsy": ("This is for blood and marrow disorders.", None)},
 "A D&C scrapes the uterine lining for tissue when the biopsy is negative but bleeding continues. It is done with NPO status and consent, and normal postoperative bleeding is expected. (study guide, Ch 65 and Ch 64)"))

A(mc("uterine", "c-ut-dx",
 "A client has stage I uterine cancer. Which treatment does the nurse expect?",
 "Surgery to remove the uterus, fallopian tubes and ovaries",
 {"Chemotherapy alone": ("Chemotherapy is for higher-risk disease and gives only a modest response.", None),
  "Observation only": ("Early stage I is often cured by surgery.", None),
  "Pelvic exenteration": ("Exenteration is for a pelvic recurrence of cervical cancer.", "borrows a cervical cancer treatment"),
  "Radical trachelectomy": ("This surgery is for early cervical cancer.", "borrows a cervical cancer treatment")},
 "Surgery removes the uterus, tubes and ovaries plus washings and lymphadenectomy, and early stage I is often cured by surgery alone. Progestin therapy is used for stage I if surgery is not possible. Radiation is the usual adjuvant. (study guide, Ch 65)", lp=True))

A(mc("uterine", "c-ut-risk",
 "A 52-year-old client with a uterus is prescribed estrogen for menopausal symptoms. Which statement should the nurse include in teaching to lower the risk of uterine cancer?",
 "“Estrogen is taken with progesterone because estrogen alone can cause the lining of the uterus to overgrow.”",
 {"“Estrogen is safe alone because it protects the uterus.”": ("Estrogen alone is unopposed and raises uterine cancer risk.", "forgets that estrogen alone is a risk"),
  "“Estrogen should be stopped if you gain weight.”": ("Weight management helps, but the key point is progesterone.", None),
  "“Only women who have had a hysterectomy need progesterone.”": ("The women who need it are those with a uterus.", None)},
 "Anyone on estrogen who has a uterus needs progesterone too. Tamoxifen users need monitoring for endometrial hyperplasia. Prevention also includes a healthy weight and exercise. (study guide, Ch 65)", lp=True))

A(mc("uterine", "c-ut-dx",
 "A client receiving chemotherapy for uterine cancer has stomatitis. Which instruction by the nurse is correct?",
 "Avoid hot or spicy food and use salt-water rinses",
 {"Eat hot soups to soothe the mouth": ("Hot food irritates stomatitis.", None),
  "Use a hard toothbrush to keep the mouth clean": ("A soft toothbrush is used.", None),
  "Avoid fluids to keep the mouth dry": ("Fluids help; dryness worsens mouth sores.", None)},
 "Comfort measures for chemotherapy include antiemetics and salt-water rinses for stomatitis, and avoiding hot or spicy food. (study guide, Ch 65)"))

A(tf("uterine", "c-ut-risk",
 "A nurse teaches a client that anyone who takes estrogen therapy and has a uterus also needs progesterone. The nurse's teaching is accurate.",
 True,
 "Estrogen without progesterone is unopposed and raises the risk of uterine cancer, so a client with a uterus takes progesterone too. (study guide, Ch 65)",
 "Marking False would leave estrogen unopposed.", lp=True))

A(tf("uterine", "c-ut-risk",
 "A nurse tells a client that ovarian cancer is the most common gynecologic cancer in the United States. The nurse's statement is accurate.",
 False,
 "Uterine (endometrial) cancer is the most common gynecologic cancer in the US; ovarian cancer is the deadliest because 70 to 75% are found at stage III or IV. (study guide, Ch 65)",
 "Marking True swaps the most common gynecologic cancer with the deadliest one.", lp=True))

# ------------------------------------------------------------------ NEUTROPENIC PRECAUTIONS
A(mc("neut", "c-neut-def",
 "A client receiving chemotherapy has an absolute neutrophil count of 480/mm³. Which nursing action is the priority?",
 "Implement neutropenic precautions, including a private room and hand hygiene by everyone",
 {"Implement bleeding precautions": ("Bleeding precautions are for a low platelet count.", "mixes up neutropenia and thrombocytopenia"),
  "Encourage visitors and fresh flowers to lift the client's mood": ("Crowds and live plants are avoided in neutropenia.", None),
  "Take the client's temperature rectally": ("Rectal temperatures are never used in neutropenia.", None),
  "Offer iron-rich foods": ("Iron foods are for iron deficiency anemia.", None)},
 "Neutropenia is an ANC below 1,500, and neutropenic precautions start at 500 or below. A fever of 100.4°F (38°C) or higher means broad-spectrum IV antibiotics immediately. The nurse uses hand hygiene, a private room and restricts visitors with communicable diseases. (study guide, Ch 13 and Ch 34)", lp=True))

A(sata("neut", "c-neut-prec",
 "The nurse is teaching a client with neutropenia about precautions at home.",
 ["Wash hands often and ask visitors to do the same", "Avoid crowds and people who are sick", "Avoid live plants and cut flowers", "Avoid standing water, such as in a humidifier"],
 {"Keep fresh cut flowers in the bedroom": ("Live plants and cut flowers carry bacteria and mold.", "forgets that plants and flowers carry mold"),
  "Take the temperature rectally when ill": ("No rectal temperatures, suppositories or enemas; rectal bacteria can enter the blood.", None),
  "Eat raspberries and blackberries as a healthy snack": ("Raspberries and blackberries are bumpy and hard to wash, so they are avoided.", None)},
 "Neutropenic precautions include hand hygiene by everyone, avoiding crowds, sick people, small children and pets, washing raw fruits and vegetables well, no raspberries or blackberries, no live plants or cut flowers, no standing water, a private room in the hospital, and no rectal temperatures, suppositories or enemas. Your class notes add reverse isolation, where staff wear PPE to protect the client. (study guide, Ch 34 Box 34.2 and class notes)", lp=True))

A(mc("neut", "c-neut-prec",
 "A client with neutropenia is being discharged. Which statement by the client indicates a need for further teaching?",
 "“I will put fresh cut flowers on my bedside table to cheer me up.”",
 {"“I will wash raw fruits and vegetables well.”": ("This is correct teaching.", None),
  "“I will check my temperature every day and call if it is above 100.4°F.”": ("This is correct teaching.", None),
  "“I will take my antibiotics every day and finish the whole course.”": ("This is correct teaching; prophylactic antimicrobials are taken daily.", None)},
 "Live plants and cut flowers carry bacteria and mold, so they are avoided at home and in the hospital. Correct teaching includes washing produce, daily temperature checks with a call for more than 100.4°F (38°C), and taking prophylactic antimicrobials daily. (study guide, Ch 34 Box 34.2)", lp=True))

A(mc("neut", "c-neut-def",
 "A client at home who is receiving chemotherapy has a temperature of 100.6°F (38.1°C). Which instruction by the nurse is correct?",
 "“Seek care or call your provider right away, because IV antibiotics can prevent sepsis.”",
 {"“Take acetaminophen and call tomorrow if it persists.”": ("Waiting delays treatment; fever may be the only sign of infection.", "treats the fever at home"),
  "“Drink extra fluids and recheck in 12 hours.”": ("This delays treatment.", "treats the fever at home"),
  "“A low-grade fever is expected and can be ignored.”": ("A temperature of 100.4°F or higher requires immediate care.", None)},
 "Fever in a chemotherapy client is a medical emergency because infection can lead to sepsis. The client checks a temperature daily and calls for more than 100.4°F (38°C), fever, rigors or illness. (study guide, Ch 13 and Ch 34)"))

A(mc("neut", "c-neut-prec",
 "The nurse reviews the orders of a client with an ANC of 450/mm³. Which order should the nurse question?",
 "Bisacodyl rectal suppository as needed for constipation",
 {"Prophylactic levofloxacin daily": ("Prophylactic antibiotics are used in neutropenia.", None),
  "Oral temperature every 4 hours": ("Oral temperatures are appropriate.", None),
  "Private room with strict hand hygiene": ("This is part of neutropenic precautions.", None)},
 "Suppositories, enemas and rectal temperatures are avoided because rectal bacteria can enter the blood and cause infection. Prophylactic antibiotics, antivirals and antifungals are used, along with a private room. (study guide, Ch 34 Box 34.2)", lp=True))

A(mc("neut", "c-neut-prec",
 "A client with leukemia is neutropenic. Which visitor should the nurse restrict?",
 "A sibling who has a cold and a cough",
 {"A well adult friend who has washed her hands": ("A healthy visitor using hand hygiene is allowed.", None),
  "The client's spouse who is well and wears a mask as requested": ("A well visitor is allowed.", None),
  "An asymptomatic adult relative who sanitizes his hands": ("A well adult with hand hygiene is allowed.", None)},
 "The plan includes restricting visitors with communicable diseases, avoiding sick people, crowds, small children and pets, and hand hygiene by everyone. (study guide, Ch 34 and class PLQ)"))

A(match2("neut", "c-neut-def",
 "The nurse reviews neutropenia values with a new graduate. Match each value with its meaning.",
 [("ANC below 1,500", "Neutropenia and an infection risk"),
  ("ANC 500 or below", "Neutropenic precautions begin"),
  ("Temperature of 100.4°F (38°C) or higher", "Call the provider immediately")],
 {"Neutropenia and an infection risk": "An ANC below 1,500 is neutropenia.",
  "Neutropenic precautions begin": "At an ANC of 500 or below the client is on neutropenic precautions, and IV antibiotics are given for fever.",
  "Call the provider immediately": "A fever of 100.4°F (38°C) or higher in a chemotherapy client is called in right away."},
 "Neutropenia is an ANC below 1,500. At 500 or below neutropenic precautions are started, and a fever of 100.4°F (38°C) or higher calls for immediate care and broad-spectrum antibiotics. (study guide, Ch 13 and Ch 34)"))

A(tf("neut", "c-neut-prec",
 "A nurse explains that in reverse isolation for a neutropenic client the nurse wears protective equipment to protect the client from infection. The nurse's explanation is accurate.",
 True,
 "Reverse isolation protects the client: staff and visitors wear PPE when required and exposures are limited. (class notes and study guide, Ch 34)",
 "Marking False would turn it into isolation that protects others instead.", lp=True))

A(tf("neut", "c-neut-prec",
 "A nurse tells a neutropenic client that raspberries and blackberries are safe to eat because they are easy to wash. The nurse's statement is accurate.",
 False,
 "Raspberries and blackberries are bumpy and hard to wash, so they are avoided. Other raw fruits and vegetables are washed well. (study guide, Ch 34 Box 34.2)",
 "Marking True would let the client eat fruit that is hard to clean.", lp=True))

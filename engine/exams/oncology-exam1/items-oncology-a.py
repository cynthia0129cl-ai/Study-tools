# Leukemia, End of life, Breast cancer, Labs.  Source tags: (study guide) = your NUR 291 Exam 1 study guides,
# (class notes) = your purple NUR 291 notes inside them, (slides) = your lecture slides inside them.
ITEMS = []
A = ITEMS.append

# ------------------------------------------------------------------ LEUKEMIA
A(mc("leuk", "c-leuk-risk",
 "A 62-year-old client reports fatigue, shortness of breath on stairs, and bleeding gums. The client has worked in an oil refinery since age 18 and has smoked for more than 40 years. Hgb is 9.4 g/dL and platelets are 97,000/mm³. Which part of the history places this client at the highest risk for leukemia?",
 "Long-term benzene exposure from refinery work",
 {"Smoking for more than 40 years": ("Smoking is a listed leukemia risk factor, but it is not the highest risk in this history; the case names benzene as the highest.", "ranks smoking above benzene"),
  "Fatigue with shortness of breath on exertion": ("This is a manifestation of anemia from a crowded marrow, not something that causes leukemia.", "mixes up a symptom with a risk factor"),
  "Bleeding gums": ("Bleeding gums are a sign of thrombocytopenia, not a cause of leukemia.", "mixes up a symptom with a risk factor"),
  "A hemoglobin of 9.4 g/dL": ("A low hemoglobin is a result of marrow crowding by blasts, not a risk factor.", "mixes up a symptom with a risk factor")},
 "Leukemia risk factors include genetic anomalies, Down syndrome, radiation, benzene or other chemical exposure, prior chemotherapy or radiation, and smoking. In this case the oil refinery is the benzene exposure and is identified as the highest risk factor. The low hemoglobin, low platelets, fatigue and bleeding gums are the effects of blasts crowding the marrow. They are findings the nurse assesses, not causes. (study guide, Ch 34 case)", lp=True))

A(sata("leuk", "c-leuk-risk",
 "The nurse is reviewing risk factors for leukemia with a client's family.",
 ["Down syndrome", "Prior chemotherapy or radiation", "Benzene exposure", "Presence of the Philadelphia chromosome in chronic myeloid leukemia"],
 {"A diet high in red meat": ("A diet high in red meat is a prostate cancer risk factor, not a leukemia risk factor.", "borrows a risk factor from another cancer"),
  "Undescended testicle": ("Cryptorchidism is the greatest risk factor for testicular cancer.", "borrows a risk factor from another cancer"),
  "Unopposed estrogen exposure": ("Unopposed estrogen is a main risk factor for uterine cancer.", "borrows a risk factor from another cancer")},
 "Down syndrome raises leukemia risk about 10 to 30 times. Radiation, benzene and prior chemotherapy damage marrow stem cells. The Philadelphia chromosome, a 9;22 swap, is found in more than 90% of chronic myeloid leukemia. Each wrong option is the signature risk of a different cancer. (study guide, Ch 34)", lp=True))

A(mc("leuk", "c-leuk-patho",
 "A 7-year-old child is admitted with fever, bone pain, and bruising. Testing confirms the most common childhood leukemia. Which type should the nurse expect the chart to list?",
 "Acute lymphoblastic leukemia",
 {"Acute myeloid leukemia": ("AML is acute but is tied to benzene, radiation and prior chemotherapy in adults; ALL is the most common childhood type.", "mixes up AML and ALL"),
  "Chronic myeloid leukemia": ("CML is chronic and marked by the Philadelphia chromosome, not the typical childhood form.", "mixes up acute and chronic types"),
  "Chronic lymphocytic leukemia": ("CLL is chronic and can be present for years before it is found; it is not the common childhood leukemia.", "mixes up acute and chronic types"),
  "Multiple myeloma": ("Multiple myeloma is a plasma cell cancer of older adults, not a leukemia.", "confuses myeloma with leukemia")},
 "Leukemias are named by the stem cell line and the speed of onset. AML and ALL have a sudden, acute onset, and ALL is the most common childhood leukemia. CML and CLL can be present for years before turning acute. Multiple myeloma is a separate plasma cell cancer. (study guide, Ch 34)", lp=True))

A(mc("leuk", "c-leuk-patho",
 "A client newly diagnosed with leukemia asks, “My white count is high, so why am I getting infections and bruising so easily?” Which response by the nurse is best?",
 "“The extra white cells are immature blasts that cannot fight infection, and they crowd out the cells that make platelets and red cells.”",
 {"“Your body is making too many healthy neutrophils, and they are destroying your platelets.”": ("The high count is from immature blasts, not healthy neutrophils, and they do not destroy platelets.", "thinks the extra cells are healthy"),
  "“The high count means your immune system is working extra hard to fight an infection.”": ("A high count in leukemia does not mean a stronger defense; the blasts are immature and useless.", "thinks a high WBC means strong defense"),
  "“Your chemotherapy has lowered your platelets and made you prone to infection.”": ("The client has just been diagnosed; the problem comes from the leukemia itself, not from treatment.", "blames chemotherapy before treatment starts"),
  "“Your spleen is destroying your blood cells faster than they can be made.”": ("Splenomegaly can occur, but the main cause is marrow crowding by blasts.", "blames the spleen")},
 "An unknown stimulus mutates a stem cell, which clones immature blasts that never mature and never die. The marrow, spleen and lymph tissue fill with blasts. The crowded marrow cannot make enough RBCs and platelets, so anemia and thrombocytopenia follow. The blasts cannot fight infection, so neutropenia and infections follow even when the count is high. (study guide, Ch 34)"))

A(order("leuk", "c-leuk-tx",
 "The nurse is explaining the phases of chemotherapy for leukemia to a client. Place the phases in the order they are given.",
 ["Induction to bring the leukemia into remission", "Consolidation to treat hidden disease", "Maintenance to prevent relapse"],
 "Induction aims to get remission. Consolidation treats leukemia cells that cannot be seen. Maintenance helps prevent relapse. Remission is not a cure, which is why therapy continues in phases. (study guide, Ch 34)"))

A(match2("leuk", "c-leuk-tx",
 "The nurse reviews medications used for leukemia. Match each drug with its role.",
 [("Imatinib", "Blocks the Bcr-Abl protein in CML"),
  ("Ibrutinib", "Targeted therapy used in CLL"),
  ("Daunorubicin with cytarabine", "Induction chemotherapy for AML"),
  ("Filgrastim", "Growth factor that raises neutrophils")],
 {"Blocks the Bcr-Abl protein in CML": "Imatinib is a Bcr-Abl inhibitor given for CML; it does not treat CLL.",
  "Targeted therapy used in CLL": "Ibrutinib is the targeted agent listed for CLL.",
  "Induction chemotherapy for AML": "Daunorubicin plus cytarabine (Ara-C) is the AML example regimen.",
  "Growth factor that raises neutrophils": "Filgrastim is G-CSF, which raises neutrophils and can cause bone pain."},
 "Imatinib targets the Bcr-Abl abnormality of CML and ibrutinib is used in CLL. Daunorubicin plus cytarabine is the AML chemotherapy example. Filgrastim (G-CSF) raises neutrophils; the textbook says growth factors are generally not indicated in leukemia because they could fuel the disease, although the case patient received it, so ask your instructor how it will be tested. (study guide, Ch 34)", lp=True))

A(mc("leuk", "c-leuk-tx",
 "A client with acute leukemia is receiving chemotherapy and has an absolute neutrophil count of 0.6 ×10³/mm³. Which medication group does the nurse expect to be ordered to lower the risk of infection?",
 "Prophylactic antibiotics, antivirals and antifungals",
 {"Aspirin": ("Aspirin inhibits platelets and raises bleeding risk; it does not prevent infection and is unsafe with thrombocytopenia.", "reaches for a bleeding drug"),
  "Megestrol": ("Megestrol is used for anorexia, not infection prevention.", "picks a drug for a different problem"),
  "Mesna": ("Mesna protects the bladder from hemorrhagic cystitis.", "picks a drug for a different problem"),
  "Allopurinol": ("Allopurinol prevents high uric acid in tumor lysis; it does not prevent infection.", "picks a drug for a different problem")},
 "Chemotherapy causes myelosuppression, and severe neutropenia lets infection spread quickly. The case patient received prophylactic antibiotics, antivirals and antifungals along with blood products. Examples listed are levofloxacin or moxifloxacin, acyclovir and fluconazole. Each wrong option protects against a different chemotherapy problem. (study guide, Ch 34)", lp=True))

A(tf("leuk", "c-leuk-tx",
 "A client whose leukemia is in remission after induction chemotherapy tells the nurse, “I am relieved because this means I am cured.” The nurse recognizes that this statement is accurate.",
 False,
 "Remission means no detectable leukemia cells, but hidden disease can remain. That is why consolidation and maintenance follow induction. The true version is: remission is not the same as a cure, and treatment continues to prevent relapse. (study guide, Ch 34)",
 "Marking True treats remission as a cure; the teaching need is that remission does not mean cure.", lp=True))

A(tf("leuk", "c-leuk-tx",
 "A client with leukemia involving the brain asks why radiation to the brain and spine is planned along with chemotherapy. The nurse says it is because chemotherapy cannot cross the blood–brain barrier. The nurse's statement is accurate.",
 True,
 "Chemotherapy given by vein does not reach the central nervous system well. Radiation to the brain and spine treats leukemia cells that hide there. Some chemotherapy is also given intrathecally. (study guide, Ch 34)",
 "Marking False denies that the blood–brain barrier blocks chemotherapy; this is the reason radiation is added.", lp=True))

A(mc("leuk", "c-leuk-nursing",
 "A client receiving chemotherapy for acute leukemia has a temperature of 101.8°F (38.8°C) and an ANC of 0.6 ×10³/mm³. Which action should the nurse take first?",
 "Notify the provider immediately so broad-spectrum IV antibiotics can be started",
 {"Give acetaminophen and recheck the temperature in 1 hour": ("Waiting delays treatment; fever may be the only sign of infection and needs antibiotics immediately.", "treats the fever, not the infection"),
  "Take a rectal temperature to confirm the reading": ("Rectal temperatures are never done in neutropenia because rectal bacteria can enter the blood.", "uses a rectal route"),
  "Encourage oral fluids and bed rest": ("Fluids and rest are supportive but do not treat a possible infection, which is an emergency.", "treats the fever, not the infection"),
  "Apply a cooling blanket": ("Cooling lowers the temperature but does not treat the infection behind it.", "treats the fever, not the infection")},
 "In a chemotherapy client, fever is often the first and only sign of infection, and infection is the most common cause of death besides the disease itself. Myelosuppression with fever is treated aggressively with broad-spectrum antibiotics to prevent sepsis. A fever of 100.4°F (38°C) or higher is the trigger to call. Rectal temperatures and suppositories are avoided because rectal bacteria can enter the blood. (study guide, Ch 13 and Ch 34)", lp=True))

A(mc("leuk", "c-leuk-nursing",
 "A client with leukemia has a platelet count of 19,000/mm³ after chemotherapy. Which statement by the client indicates a need for further teaching?",
 "“I have an appointment to get my teeth cleaned this week.”",
 {"“I will go to the emergency department if I have a nosebleed that lasts more than 10 minutes.”": ("This is correct teaching; a nosebleed lasting more than 10 minutes needs emergency care.", None),
  "“I will go to the emergency department if my temperature reaches 102°F.”": ("This is correct teaching; fever with neutropenia needs prompt treatment.", None),
  "“I will use an electric razor instead of a blade.”": ("This is correct teaching; an electric razor lowers the risk of cuts and bleeding.", None)},
 "With platelets this low, dental cleaning can cause bleeding and bacteria can enter the blood, so it should be avoided. The other statements show correct bleeding and infection teaching: report a prolonged nosebleed and fever, and use an electric razor. After chemotherapy the first priority is infection, and platelets below 20,000 can bleed spontaneously. (study guide, Ch 34 case; class notes)", lp=True))

# ------------------------------------------------------------------ END OF LIFE
A(mc("eol", "c-eol-diff",
 "A client with newly diagnosed stage III lung cancer will start chemotherapy next week. The client asks the nurse when pain, shortness of breath and nausea can be managed by a specialty team. Which response is best?",
 "“Palliative care can start now, at diagnosis, and it can continue along with chemotherapy.”",
 {"“Palliative care begins only after the cancer stops responding to treatment.”": ("Palliative care is not limited to the end of life; it starts at diagnosis.", "thinks palliative means end of life only"),
  "“You must stop chemotherapy before palliative care can begin.”": ("Palliative care can continue alongside chemotherapy, radiation and surgery; stopping curative treatment is a hospice requirement.", "mixes up palliative and hospice"),
  "“Palliative care is available only when a doctor estimates less than 6 months to live.”": ("The 6-month prognosis is the hospice rule, not the palliative rule.", "mixes up palliative and hospice")},
 "Palliative care relieves symptoms such as pain, dyspnea and nausea and improves quality of life for the client and family at any stage of a serious illness. It starts on the day of diagnosis and can go on while the client receives chemotherapy, radiation or surgery. Hospice is different: it is for the end of life and curative treatment stops. (study guide, Ch 26 and Other Topics)", lp=True))

A(sata("eol", "c-eol-diff",
 "The nurse is teaching a family about hospice care for a client with end-stage cancer.",
 ["The client has a prognosis of 6 months or less if the disease runs its usual course", "Curative treatment is stopped and the focus is on comfort", "Family support continues after the death, including bereavement", "The client can leave hospice to restart curative treatment"],
 {"Hospice can begin the day any serious illness is diagnosed": ("Starting at diagnosis describes palliative care; hospice is for the end of life.", "mixes up palliative and hospice"),
  "Chemotherapy and radiation are continued to cure the disease": ("Hospice means the client stops curative treatment and chooses comfort care.", "mixes up palliative and hospice")},
 "Hospice is for a client whose prognosis is 6 months or less. The client stops curative treatment and chooses comfort, dignity and a peaceful death, and the family receives support including bereavement. Hospice is usually provided at home but can be in a facility or nursing home, and a client can leave to restart curative care. All hospice is palliative, but not all palliative care is hospice. (study guide, Other Topics; standard content as labeled in the guide)", lp=True))

A(mc("eol", "c-eol-diff",
 "A client with heart failure and several hospitalizations wants help with symptoms but still wants to try every treatment that might extend life. Which type of care fits this client's goals?",
 "Palliative care",
 {"Hospice care": ("Hospice requires stopping curative treatment and a prognosis of 6 months or less; this client wants to keep treating.", "mixes up palliative and hospice"),
  "Hospice care with continued curative treatment": ("Hospice means the client stops curative treatment.", "mixes up palliative and hospice"),
  "Care only after the client is declared terminal": ("Palliative care is open to anyone with a serious illness at any stage.", "thinks palliative means end of life only"),
  "Bereavement care only": ("Bereavement support is a feature of hospice for the family after a death, not the client's present goal.", "mixes up palliative and hospice")},
 "Palliative care is for anyone with a serious illness at any age or stage, and curative treatment can continue with it. Hospice is limited to the last months of life and replaces curative treatment with comfort care. The client's wish to keep treating points to palliative care. (study guide, Other Topics; standard content as labeled in the guide)"))

A(tf("eol", "c-eol-diff",
 "A nurse tells the daughter of a client with advanced cancer, “All hospice care is palliative, but not all palliative care is hospice.” The statement is accurate.",
 True,
 "Hospice focuses on comfort at the end of life, so it is a form of palliative care. Palliative care is broader and can start at diagnosis alongside curative treatment, so it is not always hospice. (study guide, Other Topics; Ch 26)",
 "Marking False would mean hospice is not palliative or that palliative care is always hospice; neither is true.", lp=True))

A(tf("eol", "c-eol-diff",
 "A nurse explains to a client with a new cancer diagnosis that palliative care and hospice are the same thing. The nurse's statement is accurate.",
 False,
 "Palliative care can begin at diagnosis and continue alongside curative treatment. Hospice is for the end of life and curative treatment stops. The true version is: palliative care is not the same as hospice. (study guide, Ch 26 and Other Topics)",
 "Marking True treats the two as the same; palliative care is broader than hospice.", lp=True))

A(sata("eol", "c-eol-nursing",
 "A hospice nurse is assessing a client who is actively dying. Which findings suggest that death is near?",
 ["Decreased oral intake and urine output", "Mottled, cool extremities", "Periods of apnea with Cheyne-Stokes breathing", "Noisy secretions"],
 {"A sudden increase in appetite and energy with a rising urine output": ("Intake and urine output fall as death nears; they do not rise.", None),
  "Warm, pink, well-perfused extremities": ("Mottled, cool extremities are the sign of approaching death.", None)},
 "As death nears, intake and urine output fall, the extremities become mottled and cool, and breathing becomes irregular with apnea and Cheyne-Stokes patterns. Noisy secretions, the “death rattle,” and a falling level of consciousness are also expected. Hearing is often the last sense lost, so the nurse keeps talking to the client. (study guide, Other Topics; standard content)"))

A(mc("eol", "c-eol-nursing",
 "A client in hospice care has dyspnea and pain at the end of life. Which action by the nurse is most consistent with comfort care?",
 "Give the opioid as ordered on a regular schedule and provide mouth care and repositioning",
 {"Withhold opioids until the client's respiratory rate rises": ("Opioids, including morphine for dyspnea, are given to keep the client comfortable.", "undertreats pain out of fear"),
  "Start curative chemotherapy to reduce the symptoms": ("Hospice means curative treatment has stopped.", "mixes up palliative and hospice"),
  "Ignore the advance directive until the family arrives": ("Advance directives and DNR orders are honored in end-of-life care.", None),
  "Limit visitors to protect the client from emotional strain": ("Emotional and spiritual support for the client and family is part of nursing care.", None)},
 "Nursing care at the end of life manages pain around the clock, uses opioids such as morphine for dyspnea, and provides mouth care, repositioning, and emotional and spiritual support. The nurse honors advance directives and a DNR order. (study guide, Other Topics; standard content)"))

# ------------------------------------------------------------------ BREAST (female and male) AND MEDICATIONS
A(mc("breast", "c-breast-meds",
 "A 52-year-old client with estrogen receptor–positive breast cancer is starting tamoxifen. Which medication on the client's list should the nurse question?",
 "A combined oral contraceptive",
 {"Acetaminophen as needed": ("Acetaminophen has no interaction with tamoxifen in these materials.", None),
  "A multivitamin": ("A multivitamin is not a hormone and does not feed an estrogen-positive tumor.", None),
  "Calcium with vitamin D": ("Calcium and vitamin D are not hormones and do not fuel the tumor.", None),
  "A stool softener": ("A stool softener has no hormonal effect on the tumor.", None)},
 "Estrogen-positive tumors are fed by estrogen, so oral contraceptives are questioned. Combined oral contraceptives also raise the risk of clots. Tamoxifen blocks estrogen at its receptor and is taken for 5 to 10 years. The other medications have no hormone effect. (study guide, Ch 65; Davis Table 65.3)", lp=True))

A(mc("breast", "c-breast-meds",
 "A client with breast cancer who takes tamoxifen reports depression and a new prescription for an SSRI. Which concern should the nurse raise with the provider?",
 "SSRIs reduce how tamoxifen is metabolized",
 {"SSRIs increase the blood level of tamoxifen to a toxic range": ("The interaction lowers the tamoxifen's effect by reducing its metabolism; it does not cause toxicity.", "reverses the direction of the interaction"),
  "SSRIs cause cardiotoxicity when combined with tamoxifen": ("Cardiotoxicity is linked to trastuzumab, not to this combination.", "mixes up drug effects"),
  "SSRIs raise the risk of endometrial cancer with tamoxifen": ("Endometrial cancer risk comes from tamoxifen itself, not from SSRIs.", "mixes up drug effects"),
  "SSRIs cause bone loss when combined with tamoxifen": ("Bone loss is tied to aromatase inhibitors, and to tamoxifen in premenopausal clients, not to this SSRI interaction.", "mixes up drug effects")},
 "Tamoxifen is a selective estrogen receptor modulator that works only if the body converts it normally. SSRIs reduce tamoxifen metabolism, so the nurse tells the provider before the SSRI is started. Tamoxifen's own risks include DVT, PE, stroke, cataracts and endometrial cancer. (study guide, Ch 65; Davis Table 65.3)", lp=True))

A(match2("breast", "c-breast-meds",
 "The nurse reviews medications for breast cancer. Match each drug with its key nursing consideration.",
 [("Tamoxifen", "Blocks estrogen at its receptor; avoid SSRIs"),
  ("Anastrozole", "Blocks conversion of androgens to estrogen; risk of osteoporosis and fractures"),
  ("Trastuzumab", "For HER2-positive tumors; watch for cardiotoxicity"),
  ("Pembrolizumab", "Immunotherapy given with chemotherapy before surgery; rash, diarrhea, thyroid problems")],
 {"Blocks estrogen at its receptor; avoid SSRIs": "Tamoxifen is a SERM taken for 5 to 10 years.",
  "Blocks conversion of androgens to estrogen; risk of osteoporosis and fractures": "Aromatase inhibitors such as anastrozole, letrozole and exemestane work this way.",
  "For HER2-positive tumors; watch for cardiotoxicity": "Trastuzumab (Herceptin) is a targeted antibody; it also causes fatigue, joint pain, diarrhea and fever.",
  "Immunotherapy given with chemotherapy before surgery; rash, diarrhea, thyroid problems": "Pembrolizumab (Keytruda) is immunotherapy used with chemotherapy for high-risk triple-negative cancer."},
 "Tamoxifen blocks estrogen at the receptor, while aromatase inhibitors stop androgens from becoming estrogen, so only the aromatase inhibitor carries the osteoporosis warning of this pair. Trastuzumab targets HER2 and can harm the heart. Pembrolizumab is immunotherapy. (study guide, Ch 65; Davis Table 65.3)", lp=True))

A(mc("breast", "c-breast-male",
 "A 64-year-old male client has had a mastectomy for breast cancer. His tumor is estrogen receptor–negative and HER2-negative. Which order should the nurse question?",
 "Antiestrogen therapy",
 {"Pain medication as needed": ("Pain medication helps with coughing, deep breathing and walking after surgery.", None),
  "Dressing change using aseptic technique": ("This is routine post-operative wound care.", None),
  "Emptying and recording the surgical drain": ("Drain care and recording color and amount is expected after mastectomy.", None),
  "Teaching about suture care": ("Suture care and signs of infection are part of expected teaching.", None)},
 "Hormone therapy, such as tamoxifen, aromatase inhibitors or fulvestrant, works only on receptor-positive tumors. This tumor is receptor-negative, so antiestrogen therapy would not help and the order should be questioned. Trastuzumab and pertuzumab are for HER2-positive tumors. The other orders are routine post-operative care. (study guide, Ch 66; Davis table notes)", lp=True))

A(mc("breast", "c-breast-male",
 "A 66-year-old male client with a BRCA2 mutation finds a lump behind his nipple. Which statement about breast cancer in men is accurate for the nurse to include in teaching?",
 "It is far less common than in women, and the small amount of breast tissue means it spreads easily to the nipple, skin and muscle",
 {"It is as common as breast cancer in women": ("It is about 100 times less common than in women.", "overstates how common it is"),
  "Lumpectomy is the usual treatment because the tissue is small": ("Mastectomy is the usual treatment because there is so little tissue.", "assumes breast conservation applies"),
  "Radiation is the main treatment": ("Radiation is rarely used.", "assumes breast conservation applies"),
  "BRCA1 is far more common than BRCA2 in men": ("BRCA2 is the more common mutation in male breast cancer.", "mixes up BRCA1 and BRCA2")},
 "Male breast cancer is about 100 times less common than in women and occurs mainly between ages 60 and 70. BRCA2 is the more common mutation. With so little tissue behind the nipple, the tumor is easier to feel but spreads to the nipple, skin and muscle early. Mastectomy is usual, with chemotherapy and hormone therapy only for receptor-positive tumors. (study guide, Ch 66)"))

A(mc("breast", "c-breast-male",
 "A 22-year-old male client has a palpable lump behind the nipple and a strong family history of breast cancer. Which imaging does the nurse expect the provider to order first?",
 "Ultrasound",
 {"Mammogram": ("A mammogram is the choice for men age 25 and older; this client is under 25.", "ignores the age cutoff"),
  "Bone scan": ("A bone scan looks for metastasis after the cancer is confirmed.", None),
  "PET scan": ("PET scanning is used later to look for metastasis.", None),
  "Chest x-ray": ("A chest x-ray is a staging test for spread, not the first imaging of a breast lump.", None)},
 "In men the workup includes a clinical breast exam, then ultrasound if the client is under 25 years old or mammogram if 25 or older, and MRI. ER/PR and HER2 receptor tests then guide therapy. Bone scan, PET and chest x-ray look for metastasis. (study guide, Ch 66)"))

A(mc("breast", "c-breast-tx",
 "A 45-year-old client is scheduled for a lumpectomy for early-stage breast cancer. The client asks what treatment will follow surgery. Which response by the nurse is correct?",
 "“Breast conservation surgery is always followed by radiation, with chemotherapy first if it is indicated.”",
 {"“Radiation is not needed if the lumpectomy removed the whole tumor.”": ("Lumpectomy is always followed by radiation.", "skips radiation after lumpectomy"),
  "“Radiation is given first to shrink the tumor, then surgery.”": ("Chemotherapy, not radiation, is the usual neoadjuvant treatment to shrink a tumor before surgery.", "mixes up neoadjuvant therapies"),
  "“A mastectomy will be needed after the lumpectomy.”": ("Lumpectomy and mastectomy are equivalent for early disease; the patient chooses one.", None),
  "“Only hormone pills are given after a lumpectomy.”": ("Hormone therapy is added for receptor-positive tumors but does not replace radiation.", None)},
 "Lumpectomy removes only the tumor plus a margin, and it is always followed by radiation. When chemotherapy is indicated the order is surgery, then chemotherapy, then radiation. For early disease lumpectomy and mastectomy are equivalent, so the client chooses. Endocrine therapy for 5 to 10 years is added for receptor-positive tumors. (study guide, Ch 65)", lp=True))

A(mc("breast", "c-breast-tx",
 "A client has a 2 cm breast mass and the plan is chemotherapy before surgery, then mastectomy, then oral hormonal therapy. How should the nurse describe the oral hormonal therapy?",
 "Adjuvant therapy given after the primary treatment",
 {"Neoadjuvant therapy given before the primary treatment": ("Neoadjuvant therapy is given before the definitive treatment; the chemotherapy in this plan is the neoadjuvant part.", "mixes up neoadjuvant and adjuvant"),
  "Palliative therapy to relieve symptoms": ("The hormonal therapy is given to lower the risk from leftover cells, not to relieve symptoms.", None),
  "Primary therapy": ("The primary therapy is the definitive treatment, here the surgery.", None),
  "Debulking therapy": ("Debulking is partial removal of a tumor by surgery.", None)},
 "Neoadjuvant treatment is given before definitive treatment to shrink the tumor, and adjuvant treatment is given after to treat leftover microscopic cells. In this plan chemotherapy first is neoadjuvant and radiation plus oral hormonal therapy after surgery are adjuvant. (study guide, Ch 13 case and class PLQ)", lp=True))

A(sata("breast", "c-breast-tx",
 "A nurse reviews facts about breast cancer in situ lesions.",
 ["Ductal carcinoma in situ is stage 0 and requires surgery", "Lobular carcinoma in situ has no treatment and is followed with mammograms", "Both lesions raise the risk of later invasive cancer"],
 {"Lobular carcinoma in situ requires a mastectomy": ("LCIS is no longer considered cancer and has no treatment; the focus is surveillance and risk reduction.", "treats LCIS like invasive cancer"),
  "Ductal carcinoma in situ needs no treatment": ("DCIS requires surgery.", "mixes up DCIS and LCIS")},
 "DCIS is confined to the lining of the milk ducts, is stage 0, and requires surgery. LCIS is in the milk-producing lobules and is no longer considered cancer, so it has no treatment and the client is followed with mammograms and risk reduction. Both increase the chance of later invasive cancer. (study guide, Ch 65)"))

A(mc("breast", "c-breast-nursing",
 "A client returns to the unit after a mastectomy and axillary node removal. Which finding is the most concerning?",
 "Bloody drainage saturating the dressing",
 {"Serosanguineous drainage in the surgical drain": ("Serosanguineous drainage is expected after surgery.", None),
  "Mild incisional pain rated 3 out of 10": ("Mild pain is expected and is treated, which also helps coughing and ambulation.", None),
  "A temperature of 99.0°F (37.2°C)": ("This is not a fever and is not the most concerning finding.", None)},
 "Bloody drainage that saturates the dressing suggests bleeding and is the most concerning wound finding. Serosanguineous drainage is expected. Immediate post-operative complications include infection, wound dehiscence, pulmonary embolism and pneumonia. (study guide, Ch 65)", lp=True))

A(sata("breast", "c-breast-nursing",
 "A client had radiation after a lumpectomy for left breast cancer. Which findings should the nurse monitor for as radiation effects?",
 ["Redness and itching of the skin", "Patchy desquamation", "Breast swelling", "A dry cough 6 weeks to 6 months later"],
 {"Hot flashes and vaginal dryness": ("These are effects of endocrine therapy, not radiation.", "mixes up radiation and hormone effects"),
  "Skin rashes and flu-like symptoms": ("These are effects of immunotherapy.", "mixes up radiation and immunotherapy effects")},
 "Radiation irritates the skin, so the nurse monitors for redness, itching and patchy desquamation. The breast can swell for 6 to 18 months, and radiation pneumonitis causes a nonproductive cough 6 weeks to 6 months later. Late cardiac risk also exists. (study guide, Ch 65)"))

A(tf("breast", "c-breast-nursing",
 "A nurse teaches a client with breast cancer that monthly breast self-examination is the recommended screening method. The nurse's teaching is accurate.",
 False,
 "Breast self-exam is not recommended according to Chapter 65 and the slides. Screening is by mammography: annual from 45 to 54, then annual or every 2 years from age 55 while healthy. The true version is: breast self-exam is not recommended as screening. (study guide, Ch 65)",
 "Marking True repeats the old teaching; the materials say breast self-exam is not recommended.", lp=True))

A(tf("breast", "c-breast-nursing",
 "A nurse tells a client after axillary node removal that the most common long-term effect is shoulder immobility and that arm swelling is called lymphedema. The nurse's statement is accurate.",
 True,
 "Removal of axillary nodes can cause lymphedema, arm swelling. Shoulder immobility, or frozen shoulder, is the most common long-term effect. Pain and scarring also occur. (study guide, Ch 65; class notes)",
 "Marking False denies a long-term effect that is listed as the most common one.", lp=True))

# ------------------------------------------------------------------ LABS: CBC, WBC, platelets
A(mc("labs", "c-labs-cbc",
 "A client with leukemia has a platelet count of 45,000/mm³. Which action by the nurse is the priority?",
 "Initiate bleeding precautions",
 {"Initiate neutropenic precautions": ("Neutropenic precautions are triggered by a low ANC, not by a low platelet count.", "mixes up neutropenia and thrombocytopenia"),
  "Increase iron-rich foods in the diet": ("Iron foods address iron deficiency anemia, not platelets.", None),
  "Give a vitamin K injection": ("Vitamin K helps clotting factors, not a low platelet count.", None),
  "Encourage vigorous exercise": ("Activity that risks falls and bumps raises the bleeding risk.", None)},
 "Normal platelets are 150,000 to 450,000/mm³. Precautions start below 100,000, spontaneous bleeding is possible below 50,000 and especially below 20,000, and below 5,000 a fatal CNS or GI bleed can occur. A count of 45,000 calls for bleeding precautions such as a soft toothbrush, electric razor and no IM injections. (study guide, Ch 33 and cheat sheet)", lp=True))

A(order("labs", "c-labs-plt",
 "Place these platelet counts in order from the highest to the lowest as the nurse considers bleeding risk.",
 ["150,000/mm³: lower limit of normal", "100,000/mm³: start bleeding precautions", "50,000/mm³: spontaneous bleeding possible", "20,000/mm³: platelets usually transfused", "5,000/mm³: fatal CNS or GI bleed possible"],
 "Below 150,000 is thrombocytopenia. Bleeding precautions begin below 100,000, spontaneous bleeding becomes possible below 50,000, platelets are usually transfused below 20,000, and below 5,000 a fatal CNS or GI bleed is possible. (study guide, Ch 33, Ch 34 and cheat sheet)", lp=True))

A(mc("labs", "c-labs-cbc",
 "A client receiving chemotherapy has a WBC differential showing an ANC of 400/mm³. Which conclusion should the nurse draw?",
 "The client has severe neutropenia and a high risk of infection",
 {"The client has thrombocytopenia and a high risk of bleeding": ("ANC measures neutrophils, not platelets.", "mixes up neutropenia and thrombocytopenia"),
  "The client has anemia and needs iron": ("ANC measures neutrophils, not red cells or iron.", None),
  "The client has a normal infection-fighting ability": ("An ANC below 1,500 is neutropenia and 500 or below is severe.", None),
  "The client has polycythemia": ("Polycythemia is too many red cells.", None)},
 "A WBC differential shows the proportion of each type of white cell, and neutrophils are the first cells to arrive at an infection. Neutropenia is an ANC below 1,500, and 500 or below is severe and calls for neutropenic precautions. A fever of 100.4°F (38°C) or higher with neutropenia is treated aggressively. (study guide, Ch 13, Ch 33, Ch 34)", lp=True))

A(mc("labs", "c-labs-cbc",
 "A client has a WBC differential showing many immature neutrophils, or bands. What does the nurse understand this left shift to mean?",
 "The marrow is releasing immature cells to fight an active infection",
 {"The client has a chronic viral infection": ("Left shift points to active bacterial-type infection or inflammation, not to a chronic viral illness.", None),
  "The client has too many red blood cells": ("Left shift concerns white cells.", None),
  "The client has normal marrow with stable cell counts": ("Many bands means the marrow is being pushed to release cells early.", None),
  "The client has low platelets": ("A left shift is a white-cell finding, not a platelet finding.", None)},
 "In a left shift, immature neutrophils (bands) outnumber the normal amount, usually 3 to 5%. The marrow is pumping cells out early to fight infection or inflammation. Bands are not very effective at fighting infection. Bacterial infection raises neutrophils, while chemotherapy and radiation lower them. (study guide, Ch 33)"))

A(mc("labs", "c-labs-cbc",
 "A client's report lists reticulocytes of 4% of RBCs after a hemorrhage. What does the nurse understand this to mean?",
 "The marrow is responding to blood loss by making more red cells",
 {"The marrow is not producing red cells": ("A low reticulocyte count shows a marrow that is not producing, such as in aplastic or pernicious anemia.", "reverses the meaning"),
  "The client has leukemia": ("Reticulocytes are immature red cells and do not point to leukemia.", None),
  "The client is dehydrated": ("Dehydration raises the hematocrit but does not explain reticulocytes.", None),
  "The client has thrombocytopenia": ("Reticulocytes are red cells, not platelets.", None)},
 "Reticulocytes are immature red cells, normally 0.5 to 2.5% of RBCs. They rise when the marrow responds to hemolysis or blood loss, and they fall when the marrow is hypoproliferative. (study guide, Ch 33)"))

A(blanks("labs", "c-labs-iron",
 "A client with iron deficiency anemia has a serum iron test scheduled. The nurse explains that iron supplements must be held for at least [1] before the test, that the sample is best drawn in the [2], and that the total iron-binding capacity will be [3].",
 [("24 hours", {"4 hours": ("Iron supplements are held at least 24 hours.", None), "2 weeks": ("Two weeks is far longer than needed.", None)}),
  ("morning", {"evening": ("Iron levels drop in the evening, so the sample is drawn in the morning.", None), "afternoon": ("The morning draw is recommended.", None)}),
  ("high", {"low": ("TIBC is high in iron deficiency because there are many empty binding spots.", "reverses TIBC in IDA"), "normal": ("TIBC is not normal in iron deficiency; it rises.", None)})],
 "Iron supplements are avoided for at least 24 hours and an overnight fast is recommended. Serum iron is drawn in the morning because levels are lower in the evening. In iron deficiency TIBC is high because transferrin has many empty seats, while ferritin and transferrin saturation are low. (study guide, Ch 33 and class notes)", lp=True))

A(mc("labs", "c-labs-iron",
 "A 25-year-old client with fatigue, pale nailbeds, a smooth red tongue and low ferritin has iron deficiency anemia. Which lunch choice shows the client understood diet teaching?",
 "Roast beef, steamed spinach, tomato soup and orange juice",
 {"Cheese pizza with a glass of milk": ("Dairy blocks iron absorption and this lunch has little iron.", "forgets that dairy blocks iron"),
  "Cereal with milk and a banana": ("Milk blocks iron absorption.", "forgets that dairy blocks iron"),
  "Plain pasta with butter and a vanilla milkshake": ("This meal has little iron and the dairy blocks absorption.", "forgets that dairy blocks iron"),
  "Toast with margarine and tea": ("This meal has no heme iron, no vitamin C source, and no iron-rich vegetables.", None)},
 "Heme iron from red meat is paired with nonheme iron from spinach and vitamin C from tomatoes and orange juice, which increases absorption. Dairy and antacids reduce iron absorption. The class notes add that iron is taken with vitamin C on an empty stomach, not with milk. (study guide, Ch 34 and class notes)", lp=True))

A(sata("labs", "c-labs-iron",
 "A client has iron deficiency anemia. Which laboratory findings should the nurse expect?",
 ["Decreased serum ferritin", "Increased total iron-binding capacity", "Decreased transferrin saturation", "Decreased MCV"],
 {"Increased serum ferritin": ("Ferritin reflects iron stores and is low in iron deficiency.", None),
  "Increased MCV": ("An increased MCV is macrocytic, as in B12 or folate deficiency; iron deficiency is microcytic.", "mixes up microcytic and macrocytic"),
  "Increased transferrin saturation": ("Transferrin saturation is always low in iron deficiency.", None)},
 "In iron deficiency the stores (ferritin) are empty, iron and transferrin saturation are low, TIBC is high because transferrin has empty binding spots, and cells are small and pale (low MCV and MCHC). The class slide gives ferritin below 100 for IDA and the textbook gives below 10; ask your instructor which number will be tested. (study guide, Ch 33 and Ch 34)"))

A(match2("labs", "c-labs-coag",
 "The nurse reviews coagulation studies. Match each test with what it monitors.",
 [("PTT", "Heparin, through the intrinsic pathway"),
  ("PT/INR", "Warfarin, through the extrinsic pathway"),
  ("Bleeding time", "Platelet function"),
  ("Platelet aggregation", "Abnormal platelet function from aspirin or von Willebrand disease")],
 {"Heparin, through the intrinsic pathway": "PTT or aPTT monitors heparin.",
  "Warfarin, through the extrinsic pathway": "PT and INR monitor warfarin; the INR goal is 2 to 3.",
  "Platelet function": "Bleeding time checks overall platelet function and is not done if platelets are under 75,000.",
  "Abnormal platelet function from aspirin or von Willebrand disease": "Platelet aggregation is impaired in von Willebrand disease and with aspirin or NSAIDs."},
 "The intrinsic pathway is monitored by PTT and the drug is heparin. The extrinsic pathway is monitored by PT and INR and the drug is warfarin. Your class notes list PT and PTT together for the intrinsic pathway, but the book and slide picture pair heparin with PTT, so PTT is the safe answer for heparin. (study guide, Ch 33 and class notes)", lp=True))

A(mc("labs", "c-labs-cbc",
 "A nurse is preparing to collect blood for a CBC. Which tube should the nurse use?",
 "Lavender (EDTA) tube",
 {"Light blue (sodium citrate) tube": ("Sodium citrate tubes are used for PT, INR and PTT.", "mixes up the CBC and coagulation tubes"),
  "Red top with no additive": ("The CBC is drawn in an EDTA tube.", None),
  "Green (heparin) tube": ("A heparin tube is not the tube listed for the CBC.", None)},
 "A CBC uses a lavender (EDTA) tube, and PT, INR and PTT use sodium citrate filled completely. The tourniquet comes off as soon as blood flows, because a tourniquet left on for more than a minute falsely raises RBC, Hgb and Hct. (study guide, Ch 33)"))

A(tf("labs", "c-labs-cbc",
 "A nurse teaches a student that a client with iron deficiency anemia will typically show microcytic and hypochromic red cells. The nurse's statement is accurate.",
 True,
 "A low MCV means small (microcytic) cells and a low MCHC means pale (hypochromic) cells. Both are classic in iron deficiency and lead poisoning. (study guide, Ch 33)",
 "Marking False would label iron deficiency as macrocytic; macrocytic cells point to B12 or folate deficiency.", lp=True))

A(tf("labs", "c-labs-cbc",
 "A nurse tells a student that a platelet count of 100,000/mm³ is the level at which spontaneous bleeding becomes possible. The nurse's statement is accurate.",
 False,
 "At 100,000 bleeding precautions start. Spontaneous bleeding becomes possible below 50,000, and especially below 20,000. The true version is: precautions start at 100,000, and spontaneous bleeding is possible below 50,000. (study guide, Ch 33 and cheat sheet)",
 "Marking True moves the spontaneous-bleeding threshold up to 100,000.", lp=True))

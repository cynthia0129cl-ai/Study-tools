# New questions from the instructor slide decks and PLQ files you sent after the first build (Ch 11, 13, 26, 33, 34, 65, 66 and PLQs).
# Only facts in those files are used. Where a PLQ has no answer key, the note says what was kept and why.
ITEMS = []
A = ITEMS.append
S66 = "(Ch 66 slides)"
S65 = "(Ch 65 slides)"
S34 = "(Ch 34 slides)"
S33 = "(Ch 33 slides)"
S11 = "(Ch 11 slides)"

# ---------------- Ch 66 PLQs ----------------
A(note(mc("prostate", "c-pros-patho", "A client with advanced prostate cancer reports new bone pain, fatigue and unintended weight loss. What should the nurse prioritize in the assessment and care plan?",
 "Assess for bone metastasis-related complications and plan interventions to manage pain and prevent fractures.",
 {"Focus mainly on urinary retention as the cause of the fatigue and weight loss.": ("Prostate cancer spreads to lymph nodes, bone, rectum and bladder, so new bone pain points to metastasis rather than urinary retention.", "treats a symptom of spread as a urinary problem"),
  "Evaluate erectile dysfunction first because it is the most urgent symptom.": ("Bone pain with weight loss signals spread of the disease; sexual function is not the priority here.", "picks a quality-of-life issue over the new danger"),
  "Advise the client to drink more fluid to reduce the fatigue and weight loss.": ("Fluids do not explain or treat bone pain, fatigue and weight loss from advanced disease.", "offers a simple fix for a serious sign")},
 "Prostate cancer is slow growing and silent until advanced, and it metastasizes to lymph nodes, bone, rectum and bladder. New bone pain, fatigue and weight loss in an advanced case should therefore be assessed as bone metastasis, with pain control and fracture prevention in the plan. " + S66, lp=True),
 "From your Chapter 66 PLQ file. The file did not mark the answer; the first choice is the one your slides support.", src="plq"))

A(note(sata("prostate", "c-pros-patho", "A client with prostate cancer is being assessed for manifestations of the disease and its spread. Which findings does the nurse recognize as associated with prostate cancer?",
 ["Increased urinary frequency and a weak urine stream", "Bone pain", "Blood in the urine or semen"],
 {"Night sweats": ("Drenching night sweats belong to lymphoma, not prostate cancer.", "mixes up lymphoma and prostate cancer"),
  "Shortness of breath": ("Shortness of breath is not a listed prostate cancer manifestation; it goes with anemia, polycythemia and lung disease in your notes.", None),
  "Skin rash and itching": ("A rash with itching is not a listed prostate cancer manifestation.", None),
  "Weight gain": ("Unintended weight loss, not gain, goes with advanced cancer.", "reverses the weight change")},
 "Prostate cancer is silent until advanced, then causes trouble urinating with a weak stream, and the mass and its spread cause pain, including bone pain. Blood in the urine or semen is also a prostate finding in your quiz. " + S66, lp=True),
 "From your Chapter 66 PLQ file, which has no answer key. I kept only the options your slides or quiz support and left out the ambiguous ones (erectile dysfunction, fatigue and bruising, abdominal masses). Ask your instructor if those are keyed.", src="plq"))

# ---------------- Ch 66 slides: BPH, prostate, testicular ----------------
A(mc("prostate", "c-bph", "A nurse is caring for a client with BPH who has trouble starting urination and reports dribbling afterward. Which assessment best checks for urinary retention?",
 "Bladder scan to check the post-void residual (PVR)",
 {"Digital rectal exam alone": ("The DRE feels the size of the prostate; it does not measure how much urine stays in the bladder.", "confuses prostate size with bladder emptying"),
  "Serum PSA level": ("PSA is a diagnostic blood test, not a check of bladder emptying.", None),
  "Temperature check": ("Temperature helps find infection, which is a risk with BPH, but it does not measure retention.", None)},
 "BPH symptoms come from obstruction of urine flow by the enlarged prostate. The nurse's BPH assessments include urinary symptoms, temperature, a focused abdominal exam, bladder scan and urinalysis, and the nurse checks the PVR and may catheterize. " + S66))

A(mc("prostate", "c-bph", "About what proportion of men over age 80 have benign prostatic hyperplasia?",
 "90%",
 {"50%": ("About 50% is the figure for men aged 51 to 60.", "uses the younger age group's number"), "10%": ("This is far too low; BPH becomes nearly universal in very old men.", None), "25%": ("This does not match the figures in your slides.", None)},
 "BPH is an enlargement of the prostate, about the size of a walnut, affecting 50% of men aged 51 to 60 and 90% of men over 80. " + S66))

A(mc("prostate", "c-pros-tx", "A client's prostate cancer has stopped responding to hormone therapy. Which treatment does the nurse expect to be used next?",
 "Chemotherapy",
 {"Watchful waiting": ("Watchful waiting is used for BPH with few symptoms, not for cancer that has stopped responding to hormones.", "applies the BPH plan to cancer"),
  "Transurethral resection of the prostate (TURP)": ("TURP is a surgical treatment for BPH.", "mixes up BPH and cancer treatment"),
  "A 5-alpha reductase inhibitor": ("5-alpha reductase inhibitors limit DHT and are a BPH medication.", "mixes up BPH and cancer treatment")},
 "Ablative hormone therapy suppresses the testosterone that promotes the tumor and is used in men whose cancer has spread to lymph nodes. Chemotherapy is used when the cancer is hormone refractory. " + S66, lp=True))

A(mc("testis", "c-test-dx", "A nurse teaches a group about testicular injury. Which statement is correct?",
 "Most testicular trauma is blunt, for example from sports injuries, a kick to the groin, a motor vehicle crash or straddling an object.",
 {"Most testicular trauma is penetrating.": ("Only about 15% is penetrating; about 85% is blunt.", "reverses the proportions"),
  "Testicular trauma occurs mainly in men over age 65.": ("Your slides place it mostly at ages 25 to 40.", None),
  "Testicular trauma is repaired by removing both testicles.": ("The surgical repair in your slides is primary closure using the remaining scrotal skin.", None)},
 "About 85% of testicular trauma is blunt (sports injuries, a kick to the groin, motor vehicle crashes, straddling an object or falls) and about 15% is penetrating. It is most common at ages 25 to 40 and is repaired by primary closure with the remaining scrotal skin. " + S66))

# ---------------- Ch 65 slides: breast, ovarian ----------------
A(mc("breast", "c-breast-tx", "A client chooses breast conservation therapy for stage I breast cancer with a tumor larger than 2 cm. What does the nurse tell the client to expect after surgery?",
 "Chemotherapy first, followed by radiation therapy",
 {"Radiation first, followed by chemotherapy": ("In this case the chemotherapy came after surgery and radiation was given once the chemotherapy was complete.", "reverses the order"),
  "Chemotherapy and physical therapy": ("Radiation, not physical therapy, follows chemotherapy after breast conservation.", None),
  "Follow-up surgery 6 months later": ("No second surgery is planned; chemotherapy runs 3 to 6 months after surgery.", None)},
 "In the case study the client with a tumor over 2 cm needed 3 to 6 months of chemotherapy after surgery, then radiation, which is recommended for all breast conservation patients. If the tumor is estrogen positive she takes tamoxifen for 5 years and has lifelong follow-up with mammograms. " + S65))

A(mc("breast", "c-breast-nursing", "A client is receiving radiation treatments after breast surgery. Which side effect should the nurse monitor for?",
 "Redness, itching and irritation of the radiated skin",
 {"Swelling of the affected arm": ("Arm swelling (lymphedema) comes from removal of axillary lymph nodes, not from radiation.", "mixes up surgery and radiation effects"),
  "Opening of the surgical wound": ("Wound dehiscence is an immediate post-op complication.", None),
  "Infection of the surgical site": ("Infection is an immediate post-op complication, not the expected radiation effect.", None)},
 "Radiation causes skin irritation, redness, itching and burning at the treated site. Lymphedema from removal of axillary nodes and shoulder immobility are surgical complications. " + S65))

A(mc("uterine", "c-ovarian", "Which statement about ovarian cancer screening and diagnosis is correct?",
 "There is no recommended screening test; a CA 125 blood test is used when it is suspected, but it can be normal in about half of early cases.",
 {"An annual CA 125 level is the recommended screening test.": ("There is no recommended screening test for ovarian cancer.", "treats the marker as a screening test"),
  "A needle biopsy of the ovary is the preferred first test.": ("Biopsy is not recommended at this time; pelvic ultrasound visualizes the ovaries.", None),
  "A normal CA 125 rules out ovarian cancer.": ("About 50% of early cases have a normal CA 125.", "trusts a normal marker")},
 "If ovarian cancer is suspected the work-up includes CA 125, pelvic ultrasound and CT, and surgical removal of the mass with biopsy gives the definitive diagnosis. Because about half of early cases have a normal CA 125 and no screening test is recommended, 70 to 75% are found in late stages III and IV. " + S65, lp=True))

A(sata("uterine", "c-ovarian", "Which findings does the nurse recognize as early signs of ovarian cancer?",
 ["Bloating", "Pelvic or abdominal pain", "Early satiety or problems eating", "Urinary urgency or frequency"],
 {"Ascites": ("Ascites, excess fluid in the abdomen, is a later-stage finding.", "calls a late sign an early one"),
  "Postcoital bleeding": ("Postcoital bleeding goes with cervical cancer.", "mixes up cervical and ovarian cancer")},
 "Early ovarian cancer causes vague symptoms: bloating, pelvic or abdominal pain, early satiety and urinary urgency or frequency. Ascites appears later, and the nurse tracks abdominal girth and weight. " + S65, lp=True))

A(mc("uterine", "c-ovarian", "Which history lowers a client's risk of ovarian cancer?",
 "Breastfeeding",
 {"Long-term use of estrogen and progesterone replacement": ("Long-term hormone replacement raises the risk.", "reverses the effect"),
  "A BRCA1 or BRCA2 mutation": ("These gene mutations raise the risk.", None),
  "Hereditary nonpolyposis colorectal cancer in the family": ("This hereditary syndrome is a risk factor.", None)},
 "Breastfeeding, pregnancy and oral contraceptives are protective. Long-term hormone replacement, advanced age (mostly the 70s), BRCA1 or BRCA2 mutations and hereditary nonpolyposis colorectal cancer raise the risk. " + S65))

A(mc("breast", "c-risk-list", "A nurse reviews breast cancer risk. Which statement is accurate?",
 "Carriers of a BRCA1 or BRCA2 mutation have a 50 to 80% lifetime risk of breast cancer.",
 {"BRCA mutations cause most breast cancers.": ("Known genetic mutations account for only 5 to 10% of breast cancers.", "overstates the genetic share"),
  "Early menopause raises the risk by 30 to 50%.": ("Early menarche and late menopause raise the risk by 30 to 50%.", "reverses menopause timing"),
  "Having a live birth doubles the risk.": ("Lack of pregnancy and live childbirth doubles the risk.", "reverses the effect")},
 "More ovulatory cycles over a lifetime raise the risk, which is why early menarche and late menopause add 30 to 50% and never having a pregnancy and live birth doubles it. Genetic mutations account for 5 to 10% of cases, but carriers have a 50 to 80% lifetime risk. " + S65))

# ---------------- Ch 34 slides: thrombocytopenia, PV, lymphoma, leukemia ----------------
A(sata("labs", "c-thrombo", "A client has thrombocytopenia. Which nursing actions are part of bleeding precautions?",
 ["Avoid intramuscular injections", "Avoid rectal temperatures", "Use minimal inflation when taking the blood pressure", "Minimize blood draws"],
 {"Give medications by intramuscular injection when the oral route is hard": ("Intramuscular injections are avoided because they can cause bleeding.", "forgets IM injections are avoided"),
  "Take rectal temperatures for accuracy": ("Rectal temperatures are avoided with low platelets.", None)},
 "With thrombocytopenia the nurse implements bleeding precautions: avoid intramuscular injections and rectal temperatures, use minimal blood pressure cuff inflation, minimize blood draws and provide a safe environment. The client is also taught to avoid sexual intercourse when the platelet count is below 50,000. " + S34, lp=True))

A(mc("labs", "c-thrombo", "A client with thrombocytopenia asks when sexual intercourse should be avoided. What does the nurse answer?",
 "When the platelet count is below 50,000",
 {"When the platelet count is below 150,000": ("The teaching threshold in your slides is 50,000.", "uses the lower limit of normal"),
  "Only when the white blood cell count is low": ("The concern with intercourse is bleeding from a low platelet count.", "mixes up platelets and white cells"),
  "Intercourse never needs to be restricted": ("Your slides list avoiding intercourse below 50,000 as teaching.", None)},
 "Teaching for thrombocytopenia includes bleeding precautions, the need for frequent laboratory tests and avoiding sexual intercourse when the platelet count is below 50,000. " + S34))

A(mc("labs", "c-thrombo", "A client receiving heparin develops a falling platelet count. Which condition does the nurse suspect, and what is the treatment?",
 "Heparin-induced thrombocytopenia, an immune response to heparin; the heparin is discontinued.",
 {"Idiopathic thrombocytopenic purpura after a viral infection; the platelet count is simply watched.": ("ITP follows a viral infection or immunization in children and is not caused by a drug.", None),
  "Hemophilia; clotting factors are replaced.": ("Hemophilia is a genetic deficiency of Factor VIII or IX and does not begin with heparin use.", "mixes up two bleeding disorders"),
  "Polycythemia vera; fluids are increased.": ("Polycythemia vera is too many red blood cells, not a low platelet count.", None)},
 "Heparin-induced thrombocytopenia is an immune response to heparin, and treatment includes discontinuing the heparin. Risk factors for low platelets also include malignancy, infection, sulfa medications, autoimmune conditions such as SLE and DIC. " + S34, lp=True))

A(mc("labs", "c-thrombo", "Which statement about hemophilia is correct?",
 "It is a genetic disorder caused by a deficiency of Factor VIII or Factor IX.",
 {"It is caused by an immune response to heparin.": ("That describes heparin-induced thrombocytopenia.", "mixes up two bleeding disorders"),
  "It follows a viral infection or immunization in children.": ("That describes idiopathic thrombocytopenic purpura.", None),
  "It is an overproduction of red blood cells.": ("That describes polycythemia vera.", None)},
 "Hemophilia is a genetic deficiency of Factor VIII or Factor IX, and treatment includes replacement of clotting factors. " + S34))

A(sata("pv", "c-pv", "A client with polycythemia vera is being taught how to prevent complications. Which instructions are correct?",
 ["Drink plenty of fluids because hydration lowers the risk of clotting", "Avoid tight, restrictive clothing", "Avoid extreme temperatures", "Observe bleeding precautions"],
 {"Limit fluids to reduce blood volume": ("Aggressive hydration is the teaching because the blood is too thick.", "reverses the fluid advice"),
  "Stay on bedrest to protect the circulation": ("Routine moderate exercise is encouraged.", None)},
 "Polycythemia vera makes the blood thick (hyperviscosity) and risks thrombosis and hemorrhage. The nurse teaches aggressive hydration, avoiding tight clothing and extreme temperatures, bleeding precautions, routine moderate exercise and small frequent meals. " + S34, lp=True))

A(mc("hodgkin", "c-hodg-comp", "Which complication of malignant lymphoma should the nurse monitor for when a client reports new back pain and numbness in the legs?",
 "Spinal cord compression",
 {"Hyperviscosity of the blood from too many red cells": ("Hyperviscosity is a listed lymphoma complication, but it causes thick blood, not leg numbness with back pain.", None),
  "Splenectomy complications": ("A splenectomy is a surgical option, not a complication.", None),
  "Iron-deficiency anemia": ("This is a different blood disorder.", None)},
 "Complications of malignant lymphoma include superior vena cava syndrome, spinal cord compression, hypercalcemia, myelodysplasia, hepatic or renal dysfunction, hyperviscosity and venous thrombotic events. The nurse assesses neurological status, the lower extremities and spinal cord and nerve root compression. " + S34, lp=True))

A(mc("leuk", "c-leuk-risk", "Which factor in a client's history is listed in your slides as a genetic risk for leukemia?",
 "Down syndrome",
 {"Iron-deficiency anemia": ("Anemia is a blood disorder, not a genetic risk factor for leukemia.", None),
  "Hemophilia": ("Hemophilia is a clotting factor disorder.", "mixes up genetic blood disorders"),
  "Polycythemia vera": ("Polycythemia vera is a separate blood disorder.", None)},
 "Genetic anomalies, including Down syndrome, are risk factors for leukemia. An unknown stimulus mutates a myeloid or lymphoid stem cell, the leukemic cells multiply without apoptosis, and the marrow, spleen and lymph nodes fill with blasts. " + S34))

A(mc("mm", "c-mm-nursing", "Which laboratory values does the nurse monitor in a client with multiple myeloma?",
 "Serum and urine calcium and serum BUN",
 {"Serum potassium and sodium only": ("Your slides list serum and urine calcium and BUN for myeloma, because of hypercalcemia and the risk to kidney function.", None),
  "Reticulocyte count and TIBC": ("These are used to look at iron and red cell production.", "mixes up iron studies and myeloma monitoring"),
  "Alpha-fetoprotein and hCG": ("These are tumor markers for testicular cancer.", "mixes up tumor markers")},
 "Myeloma nursing assessments include vital signs, fatigue, pain, paresthesias, intake and output, and serum and urine calcium and BUN. Actions include fluids as tolerated, bisphosphonates, pain medication and ambulation as tolerated, with the aim of controlled pain and optimal renal function. " + S34, lp=True))

# ---------------- Ch 33 slides: hematology assessment ----------------
A(mc("labs", "c-labs-iron", "A client is scheduled for a serum iron level. Which instruction should the nurse give?",
 "Do not take iron supplements for at least 24 hours before the test.",
 {"Continue the iron supplements as usual.": ("Iron supplements are held for at least 24 hours before the test.", "assumes supplements do not matter"),
  "Fast for 12 hours before the test.": ("Your slides do not list fasting; they list holding iron supplements.", None),
  "Three samples will be drawn at hourly intervals.": ("Your slides describe a venipuncture sample, not timed samples.", None)},
 "Instruct the client to avoid taking an iron supplement for at least 24 hours before iron studies. Serum ferritin shows the ability to store iron, transferrin its transport capacity, and total iron-binding capacity the iron in the plasma. " + S33, lp=True))

A(mc("labs", "c-labs-cbc", "Which test does the nurse expect to be ordered to help diagnose thalassemia?",
 "Hemoglobin electrophoresis",
 {"Coombs test": ("The Coombs test looks for immunoglobulins on red cells and is used to diagnose hemolytic disease of the newborn.", "mixes up two tests"),
  "Leukocyte alkaline phosphatase": ("This enzyme level rises with infection, stress, inflammation, pregnancy, steroid use and leukemia.", None),
  "Prothrombin time": ("This is a clotting study.", None)},
 "Hemoglobin electrophoresis separates and measures normal and abnormal hemoglobin and helps diagnose thalassemias, in which alpha or beta hemoglobin is absent or reduced. " + S33))

A(mc("labs", "c-labs-cbc", "The spleen has which role in blood function?",
 "It acts as a filter, removing abnormal white blood cells and platelets.",
 {"It is the primary site of blood cell formation.": ("The bone marrow is the primary site of blood formation (hematopoiesis).", "mixes up spleen and marrow"),
  "It produces plasma proteins that clot blood.": ("Clotting is carried out by platelets and the coagulation cascade; the spleen is not described as producing clots.", None),
  "It stores oxygen for the red cells.": ("Hemoglobin carries oxygen.", None)},
 "The bone marrow is the primary site of hematopoiesis and makes stem cells that become myeloid cells (RBCs, WBCs, platelets) or lymphoid cells (T or B lymphocytes). The spleen filters out abnormal WBCs and platelets. " + S33))

# ---------------- Ch 13 slides ----------------
A(sata("risk", "c-risk-caution", "Which findings are listed among oncologic emergencies?",
 ["Neutropenic fever", "Hypercalcemia", "Spinal cord compression", "Deep vein thrombosis"],
 {"Mild dysplasia": ("Mild dysplasia is an early cell change, not an acute emergency.", None),
  "A benign tumor": ("Benign tumors are not cancerous and are not listed as emergencies.", None)},
 "Oncologic emergencies are acute complications that need urgent treatment because of tumor growth. They are structural, metabolic or hematological, and common examples are neutropenic fever, arrhythmia, DVT, hypercalcemia and spinal cord compression. " + S66.replace("66", "13")))

# ---------------- Ch 11 slides: pain ----------------
A(mc("pain", "c-pain", "Which finding does the nurse correlate with neuropathic pain?",
 "Direct damage to nerve fibers",
 {"Recent tissue trauma": ("Recent trauma goes with acute nociceptive pain.", None),
  "Rapidly dividing cells": ("This describes cancer growth, not the cause of neuropathic pain.", None),
  "Pain that resolves within weeks": ("That fits acute pain.", None)},
 "Nociceptive pain includes cutaneous, somatic and visceral pain, while neuropathic pain comes from damage to nerve fibers. Chronic pain lasts months to years, is unpredictable and responds inconsistently to common and adjuvant treatments. " + S11))

A(mc("pain", "c-pain", "Which description fits acute pain?",
 "Short duration, sudden onset, predictable course and improving intensity",
 {"Lasts months to years and disrupts normal activities": ("That describes chronic pain.", "swaps acute and chronic"),
  "Unpredictable course that responds inconsistently to treatment": ("That describes chronic pain.", None),
  "Persistent pain with no known cause": ("This is a chronic pain pattern.", None)},
 "Acute pain lasts hours to weeks, starts suddenly, alerts the person and prompts withdrawal, and improves in a predictable way. Chronic pain lasts months to years, is sustained or spontaneous, and its intensity is unpredictable. " + S11))

A(mc("pain", "c-pain", "In the OPQRST-AAA pain assessment, what does the S stand for?",
 "Severity of pain",
 {"Source of pain": ("Your slides list the letters as onset, quality, region and radiation, severity, time and duration, then aggravating and alleviating factors and associated manifestations.", None),
  "Sleep pattern": ("Sleep is assessed separately as an effect of pain, not as the S.", None),
  "Site of injury": ("The R covers region and radiation.", "mixes up region and severity")},
 "Onset, Quality, Region and radiation, Severity, Time and duration, plus Aggravating and alleviating factors and Associated manifestations make up the focused pain assessment. Intensity is measured with numeric, verbal or visual analog scales. " + S11))

A(mc("pain", "c-pain", "A nurse explains why cox-1 inhibition by NSAIDs can cause harm. Which statement is correct?",
 "COX-1 protects the lining of the gastrointestinal tract, so inhibiting it is harmful to the GI tract.",
 {"COX-1 inhibition raises platelet aggregation.": ("NSAIDs inhibit platelet aggregation.", "reverses the platelet effect"),
  "COX-1 inhibition causes respiratory depression.": ("Respiratory depression is an opioid risk.", "mixes up NSAID and opioid risks"),
  "COX-1 inhibition raises prostaglandin production.": ("NSAIDs block prostaglandin synthesis.", None)},
 "NSAIDs block prostaglandin synthesis (COX 1 and 2). COX-1 inhibition disrupts the protective lining of the GI tract, and NSAIDs inhibit platelet aggregation, so low platelets raise the risk. " + S11, lp=True))

A(mc("pain", "c-pain", "Which principle from the World Health Organization guidelines does the nurse apply when managing pain?",
 "Give analgesics at regular intervals according to the pain intensity, with individualized dosing.",
 {"Give analgesics only when the client asks for them": ("The WHO principle is regular intervals.", "waits for the client to ask"),
  "Use the same dose for every client": ("Dosing is individualized, with attention to dose and response.", None),
  "Treat pain only after the cause is found": ("The goal is to improve functional quality of life while the cause is addressed.", None)},
 "WHO principles: give analgesics at regular intervals, according to pain intensity, with individualized dosing, attention to dose and response and evaluation of the response. The goal is improved functional quality of life. " + S11, lp=True))

A(mc("pain", "c-pain", "An older adult with dementia cannot rate pain on a scale. What should the nurse use?",
 "Observations of behavior and changes in routine behavior, along with self-report when possible",
 {"Assume the client has no pain": ("Older adults' pain is already underdiagnosed and undertreated.", "assumes no pain"),
  "Ask only the family and skip the client": ("Self-report is used when possible, with cognitive testing and behavior observation.", None),
  "Wait until the client asks for medication": ("Clients with cognitive or communication impairment may not ask.", None)},
 "In adults with cognitive or communication impairment, use self-report, tests of cognition and observations of behavior, including changes in routine behavior. Pain in older adults is underdiagnosed and undertreated and can lead to depression, falls, sleep disturbance and malnutrition. " + S11))

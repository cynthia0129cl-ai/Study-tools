# New base questions for chapters that were thin: Ch 26 lung (+14), Ch 33 labs (+10), Ch 66 BPH (+3), End of life (+5).
ITEMS = []
A = ITEMS.append

# ------------------------------------------------------------------ CH 26 LUNG (+14)
A(mc("lung", "c-lung-types",
 "A 45-year-old client with a 20-year smoking history asks what causes lung cancer. Which statement by the nurse is accurate?",
 "“Smoking causes more than 90% of lung cancers, and the risk rises with the number of cigarettes and the years smoked.”",
 {"“Only current smokers are at risk; second-hand smoke and radon do not raise the risk.”": ("Second-hand smoke and radon are both listed risk factors.", "thinks only active smoking counts"),
  "“Smoking causes about half of lung cancers, and the rest come from asbestos.”": ("More than 90% of lung cancer is caused by smoking.", "understates smoking"),
  "“The risk is the same no matter how much a person has smoked.”": ("Risk rises with the number of cigarettes and the years smoked.", "thinks dose does not matter"),
  "“Exposure to asbestos at work does not add to the risk.”": ("Occupational pollutants and asbestos are listed risk factors.", "ignores occupational causes")},
 "Smoking is the most preventable cause of lung cancer and accounts for more than 90% of cases. Carcinogens in smoke damage the lining of the lung, and the damage adds up with each cigarette and each year. Second-hand smoke, radon, occupational pollutants and asbestos add risk. (study guide, Ch 26)"))

A(mc("lung", "c-lung-dx",
 "A client newly diagnosed with lung cancer asks why the provider keeps stressing that it is usually found late. Which response by the nurse is best?",
 "“Early disease often has no symptoms, and survival depends on the stage at diagnosis: about 49% for stage IA but about 1% for stage IV.”",
 {"“Survival is about the same no matter when the cancer is found.”": ("Survival depends strongly on the stage at diagnosis.", "thinks stage does not change survival"),
  "“Lung cancer causes severe pain right away, so it is almost always found early.”": ("Lung cancer is often silent until a late stage.", "expects early symptoms"),
  "“Only small cell cancer has a worse outlook when found late.”": ("Stage matters for lung cancer overall; small cell is poor at any stage.", None),
  "“Stage IV has the best survival because it is the most treated.”": ("Stage IV survival is about 1%.", None)},
 "Lung cancer is often silent until a late stage and is most common after age 65. Stage IA survival is about 49%, while stage IV survival is about 1%. This is why high-risk clients are screened with a yearly low-dose CT. (study guide, Ch 26)"))

A(mc("lung", "c-lung-types",
 "A nursing student asks how cigarette smoke produces lung cancer. Which explanation by the nurse is correct?",
 "Smoke causes dysplasia of the lung lining; repeated exposure leads to mutations that switch oncogenes on, switch tumor suppressors off, let cells avoid apoptosis, and stop DNA repair",
 {"One exposure changes a normal cell directly into a metastatic cell": ("Cancer develops through repeated exposure and accumulating mutations, not one exposure.", "thinks one exposure causes cancer"),
  "Smoke makes the lung produce extra immune cells that attack healthy lung tissue": ("This is not the described mechanism; the mechanism is mutation and loss of growth control.", None),
  "Smoke blocks oxygen so cells shrink and stop dividing": ("Cancer is uncontrolled growth, not shrinkage.", None)},
 "Carcinogens such as cigarette smoke cause dysplasia of the lung epithelium. With repeated exposure mutations accumulate: oncogenes turn on, tumor suppressors turn off, cells evade apoptosis and DNA repair fails. The result is uncontrolled growth of abnormal cells, which is carcinogenesis. (study guide, Ch 26)"))

A(sata("lung", "c-lung-nursing",
 "A client with lung cancer is admitted with dyspnea. Which findings does the nurse interpret correctly?",
 ["A SpO₂ below 90% means a significant gas exchange problem", "Wheezes suggest airway obstruction", "Rhonchi suggest secretions in the upper airways", "Hemoptysis means small vessels are rupturing", "Pain increases the respiratory rate and lowers quality of life"],
 {"A fever means the tumor is shrinking": ("A fever means infection.", "reads fever as tumor response"),
  "Weight loss is caused by chemotherapy only, and the work of breathing does not matter": ("Both chemotherapy side effects and the work of breathing cause weight loss.", "ignores the work of breathing")},
 "Oxygen saturation shows how well the lungs exchange gas, and below 90% is significant. Wheezes mean narrowed airways, rhonchi mean secretions in the larger airways, and hemoptysis comes from ruptured small vessels. Pain raises the respiratory rate, and both chemotherapy and the work of breathing cause weight loss. (study guide, Ch 26)"))

A(mc("lung", "c-lung-nursing",
 "A client with lung cancer is taught pursed-lip breathing. Which explanation of its purpose should the nurse give?",
 "It helps clear sputum, reduces breathlessness and removes trapped air",
 {"It sedates the client so the respiratory rate drops": ("It is a breathing technique, not a sedative.", None),
  "It replaces the need for oxygen therapy": ("Oxygen is still given to keep the SpO₂ at 90% or higher.", None),
  "It prevents the cancer from spreading to the brain": ("A breathing technique does not affect metastasis.", None)},
 "Breathing techniques such as pursed-lip breathing help the client clear sputum, reduce breathlessness and remove trapped air. They are taught with pacing of activities, small frequent meals, and correct inhaler use. Oxygen and medications are still given as needed. (study guide, Ch 26)"))

A(mc("lung", "c-lung-nursing",
 "A client with lung cancer tires easily and becomes short of breath when washing and dressing. Which teaching should the nurse give?",
 "“Pace your activities with rests, because that conserves energy and lowers the work of breathing.”",
 {"“Do everything at once so you only have to rest one time.”": ("Grouping everything at once increases the work of breathing and fatigue.", None),
  "“Avoid all activity until your treatment is finished.”": ("The client should pace activity, not stop it.", None),
  "“Breathe faster during activity to bring in more oxygen.”": ("Controlled breathing, such as pursed-lip breathing, is taught instead.", None)},
 "Activity intolerance from fatigue and dyspnea is a nursing diagnosis in lung cancer. Pacing activities conserves energy and lowers the work of breathing. The nurse also teaches breathing techniques, small frequent meals and smoking cessation. (study guide, Ch 26)"))

A(mc("lung", "c-lung-tx",
 "A client with lung cancer asks why pain medicine is ordered at set times instead of only when needed. Which response is best?",
 "“Giving it around the clock keeps a steady level of control instead of peaks of pain.”",
 {"“It prevents you from becoming addicted.”": ("Giving the medicine on a schedule is for steady relief, not for addiction prevention.", None),
  "“It lets you use less pain medicine overall.”": ("The reason is steady control, not a smaller total dose.", None),
  "“It treats the cancer cells directly.”": ("Pain medicine relieves pain and does not treat the tumor.", None)},
 "Cancer pain is managed with the WHO ladder, and doses are given around the clock rather than on demand. A steady level of medicine avoids the peaks of pain that come when doses are delayed. Pain control also lets the lungs expand better. (study guide, Ch 26)"))

A(mc("lung", "c-lung-nursing",
 "A client who had a lobectomy has a red, warm incision with thick yellow drainage on the suture line. Which complication does the nurse suspect?",
 "Infection of the suture line",
 {"Normal healing": ("Redness and warmth with thick yellow drainage is not normal healing.", None),
  "Atelectasis": ("Atelectasis is suspected when breath sounds are diminished or absent.", None),
  "A bleed": ("A bleed shows as excess bloody drainage, hypotension or tachycardia.", None)},
 "After lobectomy or pneumonectomy the nurse monitors vital signs, breath sounds, the suture line and the chest tube. A red, warm suture line with thick yellow drainage means infection, and cloudy chest tube drainage also suggests infection. Excess bloody drainage suggests a bleed. (study guide, Ch 26)"))

A(sata("lung", "c-lung-nursing",
 "The nurse teaches a client with lung cancer who is going home.",
 ["Quitting smoking can change the course of the disease", "Pace activities to conserve energy", "Eat small, frequent meals with supplements", "Take pain medicine around the clock", "Use the inhaler correctly as part of the medication regimen"],
 {"Take pain medicine only when the pain becomes severe": ("Pain medicine is given around the clock to avoid peaks of pain.", "waits for severe pain"),
  "Wait until chemotherapy is finished before trying to quit smoking": ("Smoking cessation can change the course of the disease, so it should not wait.", "delays quitting"),
  "Eat one large meal a day to save energy": ("A large meal pushes on the diaphragm; small frequent meals are better.", "gives a large meal")},
 "Teaching covers breathing techniques, pacing activities, smoking cessation, nutrition, the medication regimen and pain control. Expected outcomes are controlled pain, enough appetite and weight, and adequate oxygenation, and the client is referred for pulmonary rehabilitation and palliative care. (study guide, Ch 26)"))

A(mc("lung", "c-lung-nursing",
 "A 39-year-old client with asthma is in the tripod position using pursed-lip breathing and cannot finish a sentence. Heart rate is 150, respirations 40, SpO₂ 88%, and there are bilateral wheezes. Which is the nurse's priority?",
 "Airway management, including oxygen",
 {"Teaching the client to stop smoking": ("Smoking cessation is a long-term part of the plan, not the priority in an acute attack.", "teaches before treating the airway"),
  "Reviewing the asthma action plan": ("Education is the most important part of long-term management, but the airway comes first now.", "teaches before treating the airway"),
  "Obtaining a peak flow reading before any treatment": ("The client is in distress with a SpO₂ of 88%; the airway and oxygen come first.", None),
  "Giving a large meal for energy": ("This does nothing for the airway and increases pressure on the diaphragm.", None)},
 "The client is showing signs of severe obstruction and low oxygen: tripod position, pursed-lip breathing, tachycardia, tachypnea and a SpO₂ of 88%. When a partially obstructed airway is suspected, airway management is the priority. Oxygen, albuterol nebulizers and a corticosteroid follow. (study guide, Ch 26 asthma case and class PLQ)", lp=True))

A(mc("lung", "c-lung-nursing",
 "A client with an asthma attack was wheezing, but now no wheezes are heard and the breath sounds are diminished. What does the nurse conclude?",
 "The client is not moving air, which is an emergency",
 {"The attack is resolving and the airway is open": ("Wheezing that stops along with diminished breath sounds means little air is moving.", "reads silence as improvement"),
  "The client has developed a pleural effusion": ("The finding is a partially obstructed airway.", None),
  "The client no longer needs oxygen": ("This is a sign of worsening obstruction or exhaustion and needs urgent treatment.", None)},
 "In asthma, wheezes need air moving through narrowed airways. If wheezing goes away while breath sounds are diminished, the client is not moving air because of worsening obstruction or exhaustion. This is an emergency, with a risk of respiratory failure, and a rising PaCO₂ signals impending failure. (study guide, Ch 26 and class PLQ)", lp=True))

A(mc("lung", "c-lung-nursing",
 "A client with asthma is being discharged. Which statement shows a need for further teaching?",
 "“I can stop all my medicines once my asthma is under control.”",
 {"“I will rinse my mouth after using my inhaled steroid.”": ("This is correct; rinsing prevents oral candidiasis.", None),
  "“I will blow into the peak flow meter three times and write down the highest reading.”": ("This is correct peak flow technique.", None),
  "“I will not stop my prednisone suddenly and will take it as the taper directs.”": ("This is correct; prednisone is tapered.", None)},
 "Asthma medicines are not stopped when asthma is controlled; the controller medicine keeps it controlled. The most important part of management is education using an asthma action plan built on peak flow readings. Prednisone is tapered, never stopped suddenly. (study guide, Ch 26 and class PLQ)", lp=True))

A(mc("lung", "c-lung-nursing",
 "A client with asthma has a rescue inhaler and a controller inhaled corticosteroid. Which instruction should the nurse give?",
 "Use the short-acting beta agonist (albuterol) for rescue, and rinse the mouth after the inhaled corticosteroid",
 {"Use the inhaled corticosteroid as the rescue medicine during an attack": ("The inhaled corticosteroid is the controller; albuterol is the rescue medicine.", "mixes up rescue and controller"),
  "Skip rinsing the mouth so the medicine stays in the lungs": ("Rinsing prevents oral candidiasis.", None),
  "Stop the controller when there are no symptoms": ("Controllers are continued even when the client feels well.", None)},
 "The rescue medicine is a short-acting beta₂ agonist such as albuterol. The controller is an inhaled corticosteroid, and the client rinses the mouth afterward to prevent oral candidiasis. Peak flow is measured by blowing three times and recording the highest reading. (study guide, Ch 26)"))

A(mc("lung", "c-lung-tx",
 "A client with advanced lung cancer is too ill for surgery. Which treatment is the primary option?",
 "Chemotherapy",
 {"Wedge resection": ("Surgery is preferred only when there is no metastasis and the client can have it.", None),
  "Lobectomy": ("Surgery is not an option for this client.", None),
  "Observation only": ("Chemotherapy is the primary treatment for advanced cancer or a client too ill for surgery.", None)},
 "Chemotherapy is the primary treatment for advanced lung cancer or a client too ill for surgery, and it can be neoadjuvant or adjuvant. Radiation is used when surgery is not an option, before or after surgery, or for palliation of symptoms and pain. (study guide, Ch 26)"))

# ------------------------------------------------------------------ CH 33 LABS AND ASSESSMENT (+10)
A(mc("labs", "c-labs-cbc",
 "The nurse is assessing the abdomen of a client with an enlarged spleen. Which action is correct?",
 "Palpate the left upper quadrant lightly",
 {"Palpate deeply to measure the size of the spleen": ("An enlarged spleen is tender and can rupture with deep palpation.", "palpates deeply"),
  "Palpate firmly in all four quadrants": ("The spleen is assessed in the LUQ with light palpation.", None),
  "Avoid inspecting the abdomen": ("Inspection for masses and distention is part of the exam.", None),
  "Percuss only the right lower quadrant": ("The spleen is in the left upper quadrant.", None)},
 "The spleen sits in the left upper quadrant and filters old red cells and abnormal white cells and platelets. When it is enlarged it is tender and can rupture, so the nurse palpates the LUQ lightly with the client supine. Your class notes add standing on the opposite (right) side of the client. (study guide, Ch 33 and class notes)"))

A(sata("labs", "c-labs-iron",
 "A 25-year-old client has fatigue, shortness of breath, a heart rate of 118, a respiratory rate of 26, a blood pressure of 90/72, a hemoglobin of 9 and a low ferritin. Which findings does the nurse expect or recognize?",
 ["Pale skin and nail beds", "A red, swollen tongue", "Tachycardia as compensation for hypoxemia", "Tachypnea as compensation for hypoxemia", "A low ferritin showing depleted iron stores"],
 {"A high blood pressure because the blood is thick": ("In anemia the systolic blood pressure is lower; thick blood and high pressure go with too many red cells.", "reverses the blood pressure change"),
  "A decreased respiratory rate": ("The respiratory rate rises as the lungs work harder to deliver oxygen.", None)},
 "In iron deficiency anemia there is not enough hemoglobin to carry oxygen. The heart rate and respiratory rate rise to compensate, the blood pressure is lower, and the skin and nail beds are pale. Glossitis, a red, swollen tongue, goes with iron deficiency and pernicious anemia. (study guide, Ch 33 case and class notes)"))

A(mc("labs", "c-labs-plt",
 "A client who takes aspirin daily is scheduled for surgery. The client asks how long aspirin affects clotting. Which response is correct?",
 "“Aspirin irreversibly blocks platelets for their whole life span, which is 4 to 7 days.”",
 {"“Aspirin affects clotting for only a few hours.”": ("Aspirin blocks platelets for their life span of 4 to 7 days.", "thinks the effect is brief"),
  "“Aspirin lowers the number of platelets but they work normally.”": ("Aspirin blocks platelet function; it does not simply lower the count.", None),
  "“Aspirin affects only the clotting factors made by the liver.”": ("Aspirin acts on platelets.", None)},
 "Aspirin and other salicylates block platelets irreversibly, and platelets live 4 to 7 days. Other drugs that predispose to bleeding include NSAIDs, heparin, warfarin, DOACs, clopidogrel and antineoplastics. The nurse also asks about herbs and supplements. (study guide, Ch 33)"))

A(mc("labs", "c-labs-plt",
 "During a hematologic history the client mentions taking ginger and garlic supplements. Which concern should the nurse have?",
 "They promote bleeding",
 {"They raise the platelet count": ("Ginger and garlic promote bleeding; they do not raise the platelet count.", None),
  "They raise the hemoglobin": ("They are not iron supplements and do not raise hemoglobin.", None),
  "They prevent infection in neutropenia": ("They are not a protection against infection.", None)},
 "Ginger and garlic promote bleeding, so the nurse asks about herbs and supplements in the medication history. Goldenseal and green tea can reduce the effect of anticoagulants. (class notes and study guide, Ch 33)"))

A(mc("labs", "c-labs-coag",
 "A client has a mechanical heart valve and takes warfarin. Which INR goal does the nurse expect?",
 "2.5 to 3.5",
 {"0.9 to 1.1": ("This is the normal INR for a client who is not on an anticoagulant.", "gives the non-anticoagulated range"),
  "2 to 3": ("This is the usual warfarin goal; a mechanical valve has a higher goal.", "gives the usual warfarin goal"),
  "5 to 6": ("This is too high and risks bleeding.", None)},
 "The normal INR is 0.9 to 1.1 without an anticoagulant. The warfarin goal is 2 to 3, and a client with a mechanical valve has a goal of 2.5 to 3.5. INR rises with DIC, cirrhosis and vitamin K deficiency. (study guide, Ch 33)"))

A(mc("labs", "c-labs-cbc",
 "A newborn's laboratory report shows a positive Coombs test. What does the nurse understand this to mean?",
 "Antibodies are present on the red cells, as in hemolytic disease of the newborn",
 {"The infant has too many red blood cells": ("Polycythemia is too many red cells; Coombs detects antibodies.", None),
  "The infant has a platelet disorder": ("Coombs tests antibodies on red cells, not platelets.", None),
  "The infant has a clotting factor deficiency": ("Clotting factors are tested with PT and PTT.", None)},
 "The Coombs test detects immunoglobulins (antibodies) on red cells. A positive result is seen with hemolytic disease of the newborn, a transfusion reaction and autoimmune hemolytic anemia. (study guide, Ch 33)"))

A(mc("labs", "c-labs-cbc",
 "A client has a high neutrophil count but the leukocyte alkaline phosphatase (LAP) is not elevated. Which condition does the nurse suspect?",
 "Chronic myeloid leukemia",
 {"A bacterial infection": ("LAP rises with infection, stress, inflammation, pregnancy and steroids.", "forgets that infection raises LAP"),
  "Pregnancy": ("LAP rises in pregnancy.", None),
  "Corticosteroid use": ("LAP rises with steroid use.", None),
  "Iron deficiency anemia": ("This does not explain a high neutrophil count.", None)},
 "LAP is an enzyme made by mature neutrophils and is elevated with infection, stress, inflammation, pregnancy, steroids and leukemia. High neutrophils without a high LAP suggest chronic myeloid leukemia. (study guide, Ch 33)"))

A(mc("labs", "c-labs-plt",
 "A client's platelet count is 60,000/mm³ and a bleeding time is ordered. Which action should the nurse take?",
 "Hold the test and notify the provider",
 {"Perform the test as ordered": ("Bleeding time is not done if platelets are under 75,000.", "does not check the platelet count first"),
  "Continue the test for 30 minutes": ("The test is stopped if bleeding lasts more than 15 minutes.", None),
  "Give vitamin K first": ("Vitamin K does not raise platelets.", None)},
 "Bleeding time, normally 3 to 8 minutes, tests platelet function and is not done when platelets are under 75,000. If it is done, it is stopped when bleeding lasts more than 15 minutes. (study guide, Ch 33)"))

A(mc("labs", "c-labs-cbc",
 "The nurse is teaching about the life cycle of red blood cells. Where are old red cells broken down, and what becomes of the heme?",
 "In the spleen; heme becomes iron that is recycled and bilirubin that is excreted in bile",
 {"In the bone marrow; heme becomes platelets": ("The marrow makes red cells; the spleen breaks old ones down.", None),
  "In the kidneys; heme becomes erythropoietin": ("EPO is released by the kidneys to stimulate RBC production; it is not made from heme.", None),
  "In the liver; heme becomes albumin": ("Albumin is a plasma protein made by the liver; heme becomes iron and bilirubin.", None)},
 "Red cells live about 120 days and the marrow makes new ones, which need iron, B₁₂ and folic acid. The spleen breaks down old cells: globin becomes amino acids and heme becomes iron, which is recycled, plus bilirubin, which is excreted in bile. (study guide, Ch 33)"))

A(mc("labs", "c-labs-cbc",
 "A 58-year-old man has a hematocrit of 58%, an RBC count of 6.4 million and a headache with blurred vision. Which condition does the nurse suspect?",
 "Polycythemia",
 {"Iron deficiency anemia": ("In iron deficiency the hemoglobin and hematocrit are low.", "reverses the direction of the values"),
  "Aplastic anemia": ("Aplastic anemia lowers all three cell lines.", None),
  "Thrombocytopenia": ("A low platelet count is not shown.", None)},
 "Too many red cells make the blood thick, which increases viscosity and decreases oxygen transport. A hematocrit above 52% in men and an RBC above 6 million fit polycythemia, with headache, dizziness and blurred vision. (study guide, Ch 33 and Ch 34)"))

# ------------------------------------------------------------------ CH 66 BPH (+3)
A(mc("prostate", "c-bph",
 "A 65-year-old man has nocturia three or four times a night, urgency and occasional incontinence. His PSA is below 2 ng/mL, the digital rectal exam and urinalysis are unremarkable. Which approach does the nurse expect?",
 "Watchful waiting with follow-up",
 {"Immediate TURP": ("Surgery is for retention, kidney damage, overflow incontinence, stones, recurrent UTI or severe hematuria.", "jumps to surgery"),
  "An indwelling catheter": ("A catheter is used if medications fail and he cannot have surgery.", None),
  "Chemotherapy": ("BPH is not cancer.", None),
  "Radical prostatectomy": ("That is cancer surgery; BPH is not cancer.", "treats BPH as cancer")},
 "With minimal symptoms and minimal enlargement the first approach is watchful waiting or active surveillance with a yearly exam. If the symptoms worsen, a 5-alpha reductase inhibitor or an alpha-adrenergic blocker may be prescribed. The nurse teaches recognition of worsening symptoms and the need for follow-up. (study guide, Ch 66 and slides)"))

A(mc("prostate", "c-bph",
 "A client with benign prostatic hyperplasia says, “I'm glad I can still take my decongestants for my cold.” What does the nurse conclude?",
 "The client needs more teaching because decongestants and tranquilizers worsen obstruction",
 {"The client understands the teaching": ("Decongestants and tranquilizers are avoided because they constrict and increase urinary retention.", "thinks decongestants are safe"),
  "The client may take decongestants only at night": ("They are avoided at any time.", None),
  "The client should also take a tranquilizer to sleep": ("Tranquilizers also worsen retention.", None)},
 "In BPH the enlarged prostate narrows the urethra. Tranquilizers and decongestants cause constriction and increase urinary retention, so they are avoided. The client should also limit fluids in the evening to reduce nocturia. (study guide, Ch 66 and class notes)"))

A(mc("prostate", "c-bph",
 "A client is prescribed tamsulosin (Flomax) for BPH. Which explanation of its action should the nurse give?",
 "It relaxes the smooth muscle of the prostate and bladder neck so urine flows more easily",
 {"It shrinks the prostate by blocking the change of testosterone to DHT": ("That describes 5-alpha reductase inhibitors such as finasteride.", "mixes up the two BPH drug classes"),
  "It lowers the PSA level": ("5-alpha reductase inhibitors lower PSA; alpha blockers do not.", None),
  "It kills prostate cancer cells": ("BPH is not cancer.", None)},
 "Alpha-adrenergic blockers relax smooth muscle of the prostate and bladder neck, so the urethra is squeezed less. They work in 2 weeks to 4 months, and the nurse teaches rising slowly because of orthostatic hypotension. Your class notes say Flomax “dilates the urethra,” but the textbook says it does not; choose “relaxes the prostate muscle” if it is offered. (study guide, Ch 66 and class notes)"))

# ------------------------------------------------------------------ END OF LIFE (+5)
A(mc("eol", "c-eol-diff",
 "The family of a client with end-stage cancer wants the client to be cared for at home. Which statement by the nurse about hospice is accurate?",
 "“Hospice is usually provided at home, but it can also be given in a hospice facility or a nursing home.”",
 {"“Hospice can only be provided in a hospital.”": ("Hospice is usually at home but also in facilities and nursing homes.", None),
  "“Hospice requires the client to continue chemotherapy.”": ("Hospice means curative treatment stops.", "mixes up palliative and hospice"),
  "“Hospice ends when the client dies, with no support for the family.”": ("Family support continues after death, including bereavement.", None)},
 "Hospice care aims at comfort, dignity and a peaceful death. It is usually given at home but can be in a hospice facility or nursing home. Family support continues after death with bereavement care. (study guide, Other Topics; standard content)"))

A(mc("eol", "c-eol-diff",
 "Which client qualifies for hospice care?",
 "A client with a terminal illness certified by physicians with a prognosis of 6 months or less",
 {"Any client with a newly diagnosed serious illness": ("That describes who may receive palliative care.", "mixes up palliative and hospice"),
  "A client who wants every curative treatment to continue": ("Hospice means curative treatment stops.", "mixes up palliative and hospice"),
  "Only a client who is admitted to a hospital": ("Hospice is usually provided at home.", None)},
 "Hospice is for a terminal illness certified by physicians, with a prognosis of 6 months or less if the disease runs its usual course. Palliative care is open to anyone with a serious illness at any age or stage. (study guide, Other Topics; standard content)"))

A(mc("eol", "c-eol-diff",
 "A client with newly diagnosed pancreatic cancer reports pain, dyspnea and nausea and asks what a palliative care team will do. Which response is best?",
 "“The team relieves your symptoms and improves quality of life for you and your family while you continue treatment.”",
 {"“The team will take over once all treatment has stopped.”": ("Palliative care can continue alongside treatment from diagnosis.", "thinks palliative means end of life only"),
  "“The team can only help if you have 6 months or less to live.”": ("The 6-month rule is for hospice.", "mixes up palliative and hospice"),
  "“The team replaces your oncology team.”": ("Palliative care works together with curative treatment.", None)},
 "Palliative care relieves symptoms such as pain, dyspnea and nausea and improves quality of life for the patient and family. It can start at diagnosis and continues with chemotherapy, radiation or surgery. (study guide, Ch 26 and Other Topics)"))

A(mc("eol", "c-eol-nursing",
 "A client in hospice care has just died. Which statement about hospice support for the family is accurate?",
 "Hospice offers bereavement support to the family after the death",
 {"Hospice care ends the moment the client dies, with no further contact": ("Family support includes bereavement after death.", None),
  "Hospice offers only physical care for the client": ("Hospice includes emotional and spiritual support for the family.", None),
  "Hospice support is offered only if the client was in a hospital": ("Hospice is usually at home.", None)},
 "Hospice goals are comfort, dignity and a peaceful death, and the family receives support including bereavement after the death. Nursing care includes pain control, mouth care, repositioning, and emotional and spiritual support. (study guide, Other Topics; standard content)"))

A(sata("eol", "c-eol-diff",
 "A nurse is describing palliative care to a client with a new cancer diagnosis.",
 ["It can begin at diagnosis", "It can continue along with chemotherapy, radiation or surgery", "It relieves symptoms such as pain, dyspnea and nausea", "It improves quality of life for the client and the family", "It is available at any stage of a serious illness"],
 {"It requires a prognosis of 6 months or less": ("That requirement belongs to hospice.", "mixes up palliative and hospice"),
  "It requires the client to stop curative treatment": ("That is the rule for hospice, not for palliative care.", "mixes up palliative and hospice")},
 "Palliative care is for anyone with a serious illness at any age or stage. It starts at diagnosis, can run with curative treatment, and focuses on symptom relief and quality of life for client and family. Hospice is the form of palliative care at the end of life with a 6-month prognosis and no curative treatment. (study guide, Ch 26 and Other Topics)"))

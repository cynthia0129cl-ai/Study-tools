# Reserve questions for the concepts added with the practice quiz: polycythemia vera, pain ladder, medication math.
ITEMS = []
A = ITEMS.append
A(mc("pv", "c-pv", "A client with polycythemia vera has a hematocrit of 56%. Which treatment does the nurse expect?",
 "Therapeutic phlebotomy of 350 to 500 mL weekly until the hematocrit is below 45%",
 {"Iron supplements to raise the hemoglobin": ("The problem is too many red cells.", None), "Erythropoietin injections": ("Erythropoietin stimulates red cell production; it is low in polycythemia vera.", "reverses the aim of treatment"), "A transfusion of red blood cells": ("This would worsen the hyperviscosity.", None)},
 "Too many red cells make the blood thick, slowing circulation and lowering oxygen delivery. Phlebotomy removes red cells until the hematocrit is below 45%, and hydroxyurea or interferon suppress the marrow when white cells and platelets are high. Low-dose aspirin or anagrelide reduce thrombosis. (study guide, Ch 34)"))
A(sata("pv", "c-pv", "Which findings are expected in polycythemia vera?",
 ["Generalized itching, especially after a warm bath", "Facial flushing", "Splenomegaly with fullness in the left upper abdomen", "Headache and blurred vision", "Orthopnea"],
 {"Pallor and spoon-shaped nails": ("Those suggest iron deficiency anemia.", "mixes up anemia and polycythemia"), "A low hematocrit": ("The hematocrit is high, above 52% in men.", "reverses the direction of the values")},
 "Hyperviscosity, hypervolemia and engorged capillaries cause the symptoms. Thrombosis such as MI, stroke, PE and DVT is the main danger, so sudden chest pain, headache or shortness of breath is reported immediately. (study guide, Ch 34)"))
A(mc("pain", "c-pain", "Which type of medication is kept at every step of the WHO pain ladder?",
 "A nonopioid",
 {"A strong opioid": ("Strong opioids are used only at step 3.", None), "A benzodiazepine": ("It is not part of the ladder.", None), "A corticosteroid alone": ("Corticosteroids are adjuvants.", None)},
 "A nonopioid is kept at every step to add relief and lower the opioid dose. It has no respiratory depression or addiction, but limits include GI bleeding and kidney injury for NSAIDs and liver injury for acetaminophen. (study guide, Ch 11)"))
A(sata("pain", "c-pain", "Which are adverse effects of opioids?",
 ["Respiratory depression", "Constipation", "Nausea and vomiting", "Urinary retention", "Confusion and delirium in older adults"],
 {"Hemorrhage from COX-1 inhibition": ("That is an NSAID effect.", "mixes up NSAID and opioid effects"), "Liver failure at 3,000 mg a day": ("That is acetaminophen toxicity.", "mixes up acetaminophen and opioid effects")},
 "Opioid effects come from mu receptors. Tolerance and addiction are different: fewer than 5% of cancer patients become addicted. (study guide, Ch 11)"))
A(num("dose", "c-dose", "A provider orders 300 mg. The vial contains 100 mg per mL. How many milliliters does the nurse draw up?", 3, "mL",
 "(Desired ÷ Have) × Quantity = (300 mg ÷ 100 mg) × 1 mL = 3 mL",
 "The ordered dose is three times the dose in each milliliter, so three milliliters are needed. (study guide, Other Topics: medication math, standard content)",
 near={"0.33": "0.33 divides 100 by 300, which inverts the ratio.", "30": "30 uses a misplaced decimal.", "300": "300 is the ordered milligrams, not milliliters."}))
A(sata("dose", "c-dose", "Which conversion facts are correct?",
 ["1 kg equals 2.2 lb", "1 g equals 1,000 mg", "1 mg equals 1,000 mcg", "1 tsp equals 5 mL"],
 {"1 oz equals 15 mL": ("1 oz equals 30 mL; 15 mL is 1 tbsp.", "mixes up oz and tbsp"), "1 tbsp equals 5 mL": ("1 tbsp equals 15 mL; 5 mL is 1 tsp.", "mixes up tsp and tbsp")},
 "Also 1 oz equals 30 mL and 1 tbsp equals 15 mL. Check units before you calculate and round per your program's rules. (study guide, Other Topics: medication math, standard content)"))

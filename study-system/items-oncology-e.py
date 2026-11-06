# Pain ladder (Ch 11) and medication math, from the study guide.
ITEMS = []
A = ITEMS.append

A(mc("pain", "c-pain", "A client with severe cancer pain is not relieved by a moderate opioid plus a nonopioid. According to the WHO ladder, which medication group does the nurse expect next?",
 "A strong opioid such as morphine or fentanyl plus a nonopioid",
 {"Acetaminophen alone": ("Step 1 is a nonopioid alone for mild pain.", "mixes up ladder steps"), "A weaker opioid such as codeine plus a nonopioid": ("That is step 2, which has not worked.", "mixes up ladder steps"), "An NSAID alone": ("A nonopioid alone is step 1 for mild pain.", "mixes up ladder steps")},
 "The WHO ladder has three steps: nonopioid for mild pain, a moderate opioid plus a nonopioid for moderate pain, and a strong opioid plus a nonopioid for severe pain. A nonopioid stays at every step, with or without an adjuvant. Doses are given around the clock for cancer pain. (study guide, Ch 26 and Ch 11)"))
A(mc("pain", "c-pain", "A client takes Percocet for pain and also acetaminophen for a headache. Which teaching is most important?",
 "Acetaminophen is limited to 1,000 mg per dose and 3,000 mg in 24 hours, and combination products contain acetaminophen",
 {"Acetaminophen has no daily limit when taken with an opioid": ("The limit is 3,000 mg in 24 hours.", None), "Acetaminophen is safe in any amount for the liver": ("It can cause liver damage at higher doses.", None), "Acetaminophen is an anti-inflammatory and should replace the NSAID": ("It has few anti-inflammatory effects.", None)},
 "Acetaminophen causes liver damage in excess. Hidden acetaminophen is in Percocet, Vicodin and cold medicines, so the nurse teaches reading labels. Alcohol and barbiturates increase hepatotoxicity. (study guide, Ch 11)"))
A(mc("pain", "c-pain", "A client receiving morphine has slowed respirations and has not had a bowel movement in 4 days. Which receptor explains both effects?",
 "Mu receptors",
 {"Beta receptors": ("Beta receptors are not the opioid effect described.", None), "COX-1 receptors": ("COX-1 inhibition by NSAIDs causes GI ulcers and bleeding.", "mixes up NSAID and opioid effects"), "NMDA receptors": ("NMDA blockers such as ketamine are adjuvants for resistant pain.", None)},
 "Opioid binding at mu receptors causes respiratory depression, constipation (decreased GI motility), sedation, miosis and euphoria. Respiratory depression is the most critical adverse effect, and stool softeners and laxatives are almost always needed. (study guide, Ch 11)"))

A(num("dose", "c-dose", "The provider orders 500 mg of a drug by mouth. The pharmacy supplies a liquid labeled 250 mg per 5 mL. How many milliliters does the nurse give?", 10, "mL",
 "(Desired ÷ Have) × Quantity = (500 mg ÷ 250 mg) × 5 mL = 10 mL",
 "The basic formula is desired over have times quantity. Here the dose needed is twice the dose in each 5 mL, so the volume is 2 × 5 = 10 mL. (study guide, Other Topics: medication math, standard content)",
 near={"2": "2 is the number of 250 mg doses; it was not multiplied by the 5 mL quantity.", "5": "5 is the quantity per dose on the label, not the volume for 500 mg.", "2.5": "2.5 divides 5 by 2, which inverts the ratio.", "25": "25 multiplies 500 by 5 and does not divide by the 250 mg on hand."}))
A(num("dose", "c-dose", "A child who weighs 44 lb is ordered 15 mg/kg of a medication. How many milligrams does the nurse give?", 300, "mg",
 "44 lb ÷ 2.2 = 20 kg; 15 mg/kg × 20 kg = 300 mg",
 "Weight-based dosing needs the weight in kilograms first: pounds divided by 2.2. Then multiply the dose per kilogram by the weight. (study guide, Other Topics: medication math, standard content)",
 near={"660": "660 multiplies 15 by 44 pounds; pounds must be converted to kilograms first.", "33": "33 divides the dose by 2.2 instead of the weight.", "150": "150 does not follow from the setup."}))
A(num("dose", "c-dose", "A provider orders 1,000 mL of IV fluid to infuse over 8 hours by pump. At what rate in mL/hr should the nurse set the pump?", 125, "mL/hr",
 "Total mL ÷ hours = 1,000 mL ÷ 8 hr = 125 mL/hr",
 "A pump rate is volume divided by time in hours. No drop factor is needed for a pump. (study guide, Other Topics: medication math, standard content)",
 near={"8": "8 is the number of hours; divide the volume by the hours.", "31": "31 is the gravity drip rate in gtt/min for a 15 gtt/mL set, not the pump rate.", "480": "480 is the number of minutes in 8 hours."}))
A(num("dose", "c-dose", "The nurse hangs 1,000 mL to infuse over 8 hours by gravity. The tubing drop factor is 15 gtt/mL. What is the rate in drops per minute? Round to a whole number.", 31, "gtt/min",
 "(1,000 mL × 15 gtt/mL) ÷ 480 min = 31.25, round to 31 gtt/min",
 "Gravity drip rate is volume times the drop factor, divided by the minutes. Eight hours is 480 minutes. Round per your program's rules, usually a whole number for drops. (study guide, Other Topics: medication math, standard content)",
 near={"125": "125 is the pump rate in mL/hr; the drop factor and minutes were not used.", "15": "15 is only the drop factor.", "62": "62 divides by 240 minutes instead of 480."}))
A(num("dose", "c-dose", "A 500 mL bag is infusing at 100 mL/hr. How many hours will the bag take to infuse?", 5, "hours",
 "Total mL ÷ mL/hr = 500 ÷ 100 = 5 hours",
 "Infusion time is the total volume divided by the hourly rate. (study guide, Other Topics: medication math, standard content)",
 near={"50": "50 multiplies the volume by 0.1 or misplaces a decimal.", "0.2": "0.2 divides the rate by the volume (inverted)."}))
A(num("dose", "c-dose", "A heparin infusion contains 25,000 units in 250 mL (100 units/mL). The order is 1,000 units/hr. At what rate in mL/hr should the pump run?", 10, "mL/hr",
 "Ordered units/hr ÷ units/mL = 1,000 ÷ 100 = 10 mL/hr",
 "First find the concentration of the bag, 100 units per mL, then divide the hourly order by it. (study guide, Other Topics: medication math, standard content)",
 near={"100": "100 is the concentration in units/mL, not the pump rate.", "25": "25 does not follow from the setup.", "1000": "1,000 is the ordered units, not mL."}))

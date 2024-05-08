def ask_symptoms():
    symptoms = []

    print("Welcome to the Auto Maintenance Expert System!")
    print("Please answer the following questions about your car's symptoms:")

    print("1. Is the engine making strange noises? (yes/no)")
    answer = input().lower()
    if answer == "yes":
        symptoms.append("Strange engine noises")
        print("   - Is it a knocking sound or a squealing sound? (knocking/squealing)")
        engine_noise_type = input().lower()
        if engine_noise_type == "knocking":
            symptoms.append("Knocking engine noise")
        elif engine_noise_type == "squealing":
            symptoms.append("Squealing engine noise")

    print("2. Is the car experiencing rough idling? (yes/no)")
    answer = input().lower()
    if answer == "yes":
        symptoms.append("Rough idling")
        print("   - Is the idle RPM too high or too low? (high/low)")
        idling_issue = input().lower()
        if idling_issue == "high":
            symptoms.append("High idle RPM")
        elif idling_issue == "low":
            symptoms.append("Low idle RPM")

    print("3. Are you experiencing any issues with acceleration? (yes/no)")
    answer = input().lower()
    if answer == "yes":
        symptoms.append("Acceleration issues")
        print("   - Is the acceleration sluggish or jerky? (sluggish/jerky)")
        acceleration_issue = input().lower()
        if acceleration_issue == "sluggish":
            symptoms.append("Sluggish acceleration")
        elif acceleration_issue == "jerky":
            symptoms.append("Jerky acceleration")

    print("4. Is the car pulling to one side while driving? (yes/no)")
    answer = input().lower()
    if answer == "yes":
        symptoms.append("Pulling to one side")
        print("   - Is it pulling to the left or to the right? (left/right)")
        pulling_side = input().lower()
        if pulling_side == "left":
            symptoms.append("Pulling to the left")
        elif pulling_side == "right":
            symptoms.append("Pulling to the right")

    print("5. Is there smoke coming from the exhaust? (yes/no)")
    answer = input().lower()
    if answer == "yes":
        symptoms.append("Smoke from exhaust")
        print("   - What color is the smoke? (white/black/blue)")
        smoke_color = input().lower()
        if smoke_color == "white":
            symptoms.append("White smoke from exhaust")
        elif smoke_color == "black":
            symptoms.append("Black smoke from exhaust")
        elif smoke_color == "blue":
            symptoms.append("Blue smoke from exhaust")

    print("6. Are there any dashboard warning lights illuminated? (yes/no)")
    answer = input().lower()
    if answer == "yes":
        symptoms.append("Dashboard warning lights")
        print("   - Which warning lights are illuminated? (ABS/Check Engine/Others)")
        warning_lights = input().lower()
        if "abs" in warning_lights:
            symptoms.append("ABS warning light")
        if "check engine" in warning_lights:
            symptoms.append("Check engine warning light")

    return symptoms

def diagnose_issues(symptoms):
    issues = []

    if "Strange engine noises" in symptoms:
        if "Knocking engine noise" in symptoms:
            issues.append("Possible engine knock, may need engine inspection.")
        if "Squealing engine noise" in symptoms:
            issues.append("Possible issues with belts or pulleys, check belt tension and condition.")

    if "Rough idling" in symptoms:
        if "High idle RPM" in symptoms:
            issues.append("Possible vacuum leak or throttle issue, check idle control valve.")
        if "Low idle RPM" in symptoms:
            issues.append("Possible issues with fuel delivery or spark plugs, check fuel pressure and ignition system.")

    if "Acceleration issues" in symptoms:
        if "Sluggish acceleration" in symptoms:
            issues.append("Possible issues with fuel system, check fuel filter and injectors.")
        if "Jerky acceleration" in symptoms:
            issues.append("Possible transmission issues, check transmission fluid and components.")

    if "Pulling to one side" in symptoms:
        if "Pulling to the left" in symptoms or "Pulling to the right" in symptoms:
            issues.append("Possible alignment or tire issues, check tire pressure and alignment.")

    if "Smoke from exhaust" in symptoms:
        if "White smoke from exhaust" in symptoms:
            issues.append("Possible coolant leak, check coolant level and radiator for leaks.")
        if "Black smoke from exhaust" in symptoms:
            issues.append("Possible issues with fuel mixture, check air filter and fuel injectors.")
        if "Blue smoke from exhaust" in symptoms:
            issues.append("Possible oil burning, check for oil leaks and engine condition.")

    if "Dashboard warning lights" in symptoms:
        if "ABS warning light" in symptoms:
            issues.append("Possible issues with ABS system, check ABS sensors and module.")
        if "Check engine warning light" in symptoms:
            issues.append("Possible engine issues, perform diagnostic scan for fault codes.")

    if len(issues) == 0:
        issues.append("No specific issues detected based on provided symptoms. Further inspection may be needed.")

    return issues
symptoms = ask_symptoms()
issues = diagnose_issues(symptoms)
print("\nPossible car issues based on symptoms:")
for issue in issues:
    print("-", issue)

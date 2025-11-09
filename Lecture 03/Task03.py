gender = input("Please enter your biological gender (male/female): ")
hemoglobin = float(input("Please enter your hemoglobin level (g/L): "))

if gender.lower() == "female":
    if hemoglobin < 117:
        print("Your hemoglobin level is low.")
    elif hemoglobin <= 155:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")

elif gender.lower() == "male":
    if hemoglobin < 134:
        print("Your hemoglobin level is low.")
    elif hemoglobin <= 167:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
else:
        print("Invalid information.")
# project
# create the initial variables below
print("\nExercise 1:")
age = 28
sex = 0  # 0 for female, 1 for male
bmi = 26.2
num_of_children = 3
smoker = 0  # 0 for non-smoker, 1 for smoker

# Add insurance estimate formula below
print("\nExercise 2:")
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print("\nExercise 3:")
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# Age Factor
print("\nExercise 4:")
age += 4

print("\nExercise 5:")
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's new insurance cost is " + str(new_insurance_cost) + " dollars.")

print("\nExercise 6-7:")
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

# BMI Factor
print("\nExercise 8-9:")
age = 28
bmi  += 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")

# Male vs. Female Factor
print("\nExercise 10-11:")
bmi = 26.2
sex = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")


# Extra Practice
print("\nExercise 13:")
smoker = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being a smoker instead of a non-smoker is " + str(change_in_insurance_cost) + " dollars.")

# Changing number of children
smoker = 0  # Reset smoker status
num_of_children += 2  # Increasing number of children by 2

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for having 2 more children is " + str(change_in_insurance_cost) + " dollars.")

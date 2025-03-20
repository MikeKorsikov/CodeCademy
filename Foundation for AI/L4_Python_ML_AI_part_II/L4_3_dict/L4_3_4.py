# project 2
# Add your code here
# Step 1: Create an empty dictionary
medical_costs = {}

# Step 2: Add patients and their insurance costs
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0

# Step 3: Add multiple patients in one line
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})

# Step 4: Print the dictionary
print("Medical Costs:", medical_costs)

# Step 5: Update Vinay's insurance cost
medical_costs["Vinay"] = 3325.0

# Print updated dictionary
print("Updated Medical Costs:", medical_costs)

# Step 6: Calculate total cost
total_cost = sum(medical_costs.values())

# Step 7: Calculate average cost
average_cost = total_cost / len(medical_costs)

# Print average insurance cost
print(f"Average Insurance Cost: {average_cost}")

# Step 8: Create names and ages lists
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

# Step 9: Zip lists together
zipped_ages = zip(names, ages)

# Step 10: Create names_to_ages dictionary using list comprehension
names_to_ages = {name: age for name, age in zipped_ages}

# Print names_to_ages
print("Names to Ages:", names_to_ages)

# Step 11: Get Marina's age
marina_age = names_to_ages.get("Marina", None)
print(f"Marina's age is {marina_age}")

# Step 12: Create an empty medical_records dictionary
medical_records = {}

# Step 13-14: Add patients and their detailed records
medical_records["Marina"] = {
    "Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0
}
medical_records["Vinay"] = {
    "Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0
}
medical_records["Connie"] = {
    "Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0
}
medical_records["Isaac"] = {
    "Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0
}
medical_records["Valentina"] = {
    "Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0
}

# Step 15: Print medical_records
print("Medical Records:", medical_records)

# Step 16: Print Connie's insurance cost
print(f"Connie's insurance cost is {medical_records['Connie']['Insurance_cost']} dollars.")

# Step 17: Remove Vinay from medical records
medical_records.pop("Vinay", None)

# Step 18: Iterate through records and print details
for name, data in medical_records.items():
    print(f"{name} is a {data['Age']} year old {data['Sex']} {data['Smoker']} "
          f"with a BMI of {data['BMI']} and insurance cost of {data['Insurance_cost']}.")

# Step 19 (Extra): Function to update medical records
def update_medical_records(name, age, sex, bmi, children, smoker, insurance_cost):
    medical_records[name] = {
        "Age": age, "Sex": sex, "BMI": bmi, "Children": children,
        "Smoker": smoker, "Insurance_cost": insurance_cost
    }
    print(f"{name}'s record has been updated.")

# Example update
update_medical_records("Alex", 30, "Male", 22.5, 1, "Non-smoker", 5000.0)

# Print final medical records
print("Final Medical Records:", medical_records)

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = (250 * age - 128 * sex + 370 * bmi + 
                      425 * num_of_children + 24000 * smoker - 12500)
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    return estimated_cost

# Estimate insurance costs
maria_insurance_cost = estimate_insurance_cost("Maria", 31, 0, 23.1, 1, 0)
rohan_insurance_cost = estimate_insurance_cost("Rohan", 25, 1, 28.5, 3, 0)
valentina_insurance_cost = estimate_insurance_cost("Valentina", 53, 0, 31.4, 0, 1)

# Create a list of names
names = ["Maria", "Rohan", "Valentina"]

# Create a list of actual insurance costs
insurance_costs = [4150.0, 5320.0, 35210.0]

# Combine names and actual insurance costs
insurance_data = list(zip(names, insurance_costs))
print("Here is the actual insurance cost data:", insurance_data)

# Create a list for estimated insurance costs
estimated_insurance_data = []

# Append estimated insurance data
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))

# Print estimated insurance data
print("Here is the estimated insurance cost data:", estimated_insurance_data)

# Calculate differences between actual and estimated costs
insurance_cost_difference = [(name, actual - estimated) for (name, actual), (_, estimated) in zip(insurance_data, estimated_insurance_data)]
print("Difference between actual and estimated insurance costs:", insurance_cost_difference)

# Estimate insurance cost for Akira
akira_insurance_cost = estimate_insurance_cost("Akira", 19, 1, 27.1, 0, 0)
names.append("Akira")
insurance_costs.append(2930.0)
estimated_insurance_data.append(("Akira", akira_insurance_cost))

# Print updated lists
insurance_data = list(zip(names, insurance_costs))
print("Updated actual insurance cost data:", insurance_data)
print("Updated estimated insurance cost data:", estimated_insurance_data)

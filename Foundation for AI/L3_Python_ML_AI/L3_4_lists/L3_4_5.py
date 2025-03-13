names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here

#1
names.insert(len(names)+1, "Priscilla")
insurance_costs.insert(len(names)+1, 8320.0)
print(names)
print(insurance_costs)

#2-3
medical_records = list(zip(names, insurance_costs))
print(medical_records)

#4-5
num_medical_records = len(medical_records)
print(f"There are {num_medical_records} medical records.")

#6-7
first_medical_record = medical_records[0]
print(f"Here is the first medical record: {first_medical_record}")

#8
medical_records.sort()
print(f"Here are the medical records sorted by insurance cost: {medical_records}")

#9-10
insurance_costs.sort()
cheapest_three = insurance_costs[0:3]
print(f"Here are the three cheapest insurance costs in our medical records: {cheapest_three}")

#11-12
priciest_three = insurance_costs[-3:]
print(f"Here are the three most expensive insurance costs in our medical records: {priciest_three}")

#13
occurrences_paul = names.count("Paul")
print(f"There are {occurrences_paul} individuals with the name Paul in our medical records.")

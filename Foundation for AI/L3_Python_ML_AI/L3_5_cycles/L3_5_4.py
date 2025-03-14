names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here

#1
total_cost = 0

#2
for cost in actual_insurance_costs:
  total_cost += cost

#3
average_cost = total_cost / len(actual_insurance_costs)

#4
print(f"Average Insurance Cost: {average_cost} dollars.")

#5-9
for i in range(0, len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print(f"The insurance cost for {name} is {insurance_cost} dollars.")
  if insurance_cost > average_cost:
    print(f"The insurance cost for {name} is above average.")
  elif insurance_cost < average_cost:
    print(f"The insurance cost for {name} is below average.")
  else:
    print(f"The insurance cost for {name} is equal to the average.")

#10
updated_estimated_costs = [cost * (11/10) for cost in estimated_insurance_costs]

#11
print(updated_estimated_costs)



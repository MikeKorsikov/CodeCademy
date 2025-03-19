# project

medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
#1
print(medical_data)

#2
updated_medical_data = medical_data.replace("#", "$")
print(updated_medical_data)

#3
num_records  = 0

#4
for i in updated_medical_data:
  if i == "$":
    num_records += 1

#5
print(f"There are {num_records} medical records in the data.")

#6
medical_data_split = updated_medical_data.split(";")
print(medical_data_split)

#7
medical_records = []

#8
for i in medical_data_split:
  medical_records.append(i.split(','))

print(medical_records)

#9
medical_records_clean = []

#10-12
for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)

#13
print(medical_records_clean)

#14-15
for record in medical_records_clean:
  record[0] = record[0].upper()
  print(record[0])

#16
names = []
ages = []
bmis = []
insurance_costs = []

#17
for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

#18
print("Names: " + str(names))
print("Ages: " + str(ages))
print("BMI: "  + str(bmis))
print("Insurance Costs: " + str(insurance_costs))

#19
total_bmi = 0

#20
for bmi in bmis:
  total_bmi += float(bmi)
print(total_bmi)

#21
average_bmi = total_bmi / len(bmis)
print(f"Average BMI: {average_bmi}")


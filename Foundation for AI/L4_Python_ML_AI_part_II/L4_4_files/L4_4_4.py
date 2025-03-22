# project
import os
print("Current Working Directory:", os.getcwd())

# Task 1: 
# Import the CSV module
import csv

# Task 2:
# Create a list to store compromised users
compromised_users = []

# Task 3:
# Open the 'passwords.csv' file
with open('passwords.csv', 'r') as password_file:
  # Task 4:
  # Parse the CSV file
  password_csv = csv.DictReader(password_file)
  # Task 5:
  # Iterate through each row in the CSV
  for password_row in password_csv:
    # Task 6
    #print(password_row['Username'])
    # Task 7:
    compromised_users.append(password_row['Username'])

# Task 8
# Open a new file 'compromised_users.txt' in write mode
with open('compromised_users.txt', 'w') as compromised_user_file:
  # Task 9
  # Write each compromised user to the file
  for user in compromised_users:
    # Task 10
    compromised_user_file.write(user + '\n')

# Task 12:
import json

# Task 13:
# Open a new JSON file 'boss_message.json' in write mode
with open('boss_message.json', 'w') as boss_message:
  # Task 14:
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
    }

  # Task 15:
  # Write the dictionary to the JSON file
  json.dump(boss_message_dict, boss_message)

# Task 16:
# Open a new file 'new_passwords.csv' in write mode
with open('new_passwords.csv', 'w') as new_passwords_obj:
  # Task 17:
  # Define Slash Null's signature
  slash_null_sig = """
U
GOT
HACKED"""
  # Task 18:
  # Write the signature to the new file
  new_passwords_obj.write(slash_null_sig)


#Task 19:
import os
# Remove the original 'passwords.csv' file
os.remove('passwords.csv')


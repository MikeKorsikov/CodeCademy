# Import datetime library
from datetime import datetime  

# Print current date and time
print(datetime.now())

# Define the Block class
class Block:
    # Default constructor for the Block class
    def __init__(self, transactions, previous_hash, nonce=0):
        self.timestamp = datetime.now()  # Store the current timestamp
        self.transactions = transactions  # Store transactions
        self.previous_hash = previous_hash  # Store the previous block's hash
        self.nonce = nonce  # Initialize nonce with a default value of 0
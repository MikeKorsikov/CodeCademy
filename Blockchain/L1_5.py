from blockchain import Blockchain

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# example 1
my_blockchain = Blockchain()

my_blockchain.add_block(new_transactions)
my_blockchain.print_blocks()
my_blockchain.chain[1].transactions = 'fake_transactions'
my_blockchain.validate_chain()


# example 2
# import sha256
from hashlib import sha256

# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 2
nonce = 0

# creating the proof 
proof = sha256((str(nonce)+str(new_transactions)).encode()).hexdigest()

# printing proof
print(proof)
  
# finding a proof that has 2 leading zeros
while (proof[:2] != '0' * difficulty):
  nonce += 1
  proof = sha256((str(nonce) + str(new_transactions)).encode()).hexdigest()
final_proof = proof

# printing final proof that was found
print(final_proof)

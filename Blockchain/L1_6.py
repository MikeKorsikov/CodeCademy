from blockchain import Blockchain

block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

print("\nEmpty chain:")
local_blockchain = Blockchain()
local_blockchain.print_blocks()

# add 1
print("\nAdded 1st block:")
local_blockchain.add_block(block_one_transactions)
local_blockchain.print_blocks()

# add 2
print("\nAdded 2nd block:")
local_blockchain.add_block(block_two_transactions)
local_blockchain.print_blocks()

# add 3
print("\nAdded 3rd block:")
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()

#amend content of transaction (fake) 
local_blockchain.chain[2].transactions = fake_transactions

#validate blockchain
print("\nValidate blockchain:")
local_blockchain.validate_chain()

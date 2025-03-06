#imports the Block class from block.py
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()
    
    def genesis_block(self):
        genesis_block = Block([], "0")
        self.chain.append(genesis_block)
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Creates a new block and adds it to the chain
        pass

    def new_transactions(self):
        # Adds a new transaction to the list of transactions
        pass

    @staticmethod
    def hash(block):
        # Hashes a block
        pass

    @staticmethod
    def last_block(self):
        # Returns last block in the chain
        pass
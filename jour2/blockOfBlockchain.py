class Block: 
    def __init__(self, index, previousHash, data, timestamp, blockHash, nonce):
        self.index = index
        self.previousHash = previousHash
        self.data = data
        self.timestamp = timestamp
        self.blockHash = blockHash
        self.nonce = nonce
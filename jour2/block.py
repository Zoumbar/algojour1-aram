from hashlib import sha256
from datetime import datetime


def calculateHash(self):
    bloc = (
        str(self.index)
        + str(self.previousHash)
        + str(self.timestamp)
        + str(self.data)
        + str(self.nonce)
    )
    return sha256(bloc.encode("utf-8")).hexdigest()


class Block:
    def __init__(self, index, previousHash, data, timestamp, hash, nonce):
        self.index = index
        self.previousHash = previousHash
        self.data = data
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = calculateHash(self)

    def check(self):
        while self.hash[0:3] != "000":
            self.nonce = self.nonce + 1
            newHash = calculateHash(self)
            self.hash = newHash


class Blockchain:
    def __init__(self):
        self.blocks = []
        firstBlock = Block(0, "none", "First Block", datetime.now(), "", 0)
        firstBlock.check()
        self.blocks.append(firstBlock)

    def AddBlock(self, nbBlock):
        x = 0
        while x < nbBlock:
            Index = self.blocks[x].index + 1
            PreviousHash = self.blocks[x].hash
            NewBlock = Block(Index, PreviousHash, "Données du block", datetime.now(), "", 0)
            NewBlock.check()
            self.blocks.append(NewBlock)
            x += 1


blockchain = Blockchain()
blockchain.AddBlock(2)

for block in blockchain.blocks:
    print (
    str("Block index : " + str(block.index) + 
    "\n    Previous hash : " + str(block.previousHash) +
    "\n    Timestamp : " + str(block.timestamp) +
    "\n    Data : " + str(block.data) +
    "\n    Hash : " + str(block.hash) +
    "\n    Nonce : " + str(block.nonce) +
    "\n"
    ))
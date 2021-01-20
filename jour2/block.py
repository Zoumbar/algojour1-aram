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
        while self.hash[0:2] != "00":
            self.nonce = self.nonce + 1
            newHash = calculateHash(self)
            self.hash = newHash


class Blockchain:
    def __init__(self):
        self.blocks = []

        firstBlock = Block(0, "none", "First Block", datetime.now(), "", 0)
        firstBlock.check()
        self.blocks.append(firstBlock)


    def AddBlock(self, blockToAdd):
        x = 0
        while x < blockToAdd:
            Index = self.blocks[x].index + 1
            PreviousHash = self.blocks[x].hash
            NewBlock = Block(Index, PreviousHash, "Block", datetime.now(), "", 0  )
            NewBlock.check()
            self.blocks.append(NewBlock)
            x = x + 1


blockchain = Blockchain()
blockchain.AddBlock(2)

for block in blockchain.blocks:
    print (
    str("Block index : " + str(block.index) + 
    "\nPrevious hash : " + str(block.previousHash) +
    "\nTimestamp : " + str(block.timestamp) +
    "\nData : " + str(block.data) +
    "\nHash : " + str(block.hash) +
    "\nNonce : " + str(block.nonce) +
    "\n"
    ))
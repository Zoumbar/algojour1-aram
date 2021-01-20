from hashlib import sha256
from datetime import datetime

def calculateHash(block):
        bloc = str(block.index) + str(block.previousHash) + str(block.timestamp) + str(block.data) + str(block.nonce)
        return(sha256(bloc.encode('utf-8')).hexdigest())

class Block:

    def __init__(self, index, previousHash, data, timestamp, hash, nonce):
        self.index = index
        self.previousHash = previousHash
        self.data = data
        self.timestamp = timestamp
        self.nonce = 0
        self.hash = calculateHash(self)

    def check(self):
         while self.hash[0:2] != "00":
            self.nonce += 1
            self.hash = calculateHash(self)
            

class Blockchain:

    def __init__(self):
        self.blockchain = []
        first = Block(0, "none", "First Block", datetime.now(), "", 0)
        first.check()
        self.blockchain.append(first)



print(first.hash)
print("nonce: ", first.nonce)


#if str[0,3] == "000"

#bchain = Blockchain(3)
#
#    blockn1 = bchain.newBlock("Second Block")
#    bchain.addBlock(blockn1)
#
#    blockn2 = bchain.newBlock("Third Block")
#    bchain.addBlock(blockn2)
#
#    blockn3 = bchain.newBlock("Fourth Block")
#    bchain.addBlock(blockn3)
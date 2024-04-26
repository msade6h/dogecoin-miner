import hashlib
import time

class Miner:
    def __init__(self, wallet_address, difficulty=5):
        self.wallet_address = wallet_address
        self.difficulty = difficulty
        self.nonce = 0  

    def hash_with_nonce(self, data, nonce):
        data_with_nonce = data + str(nonce)
        return hashlib.sha256(data_with_nonce.encode()).hexdigest()

    def mine_block(self, data):
        nonce = self.nonce  
        while True:
            hash_result = self.hash_with_nonce(data, nonce)
            if hash_result.startswith('0' * self.difficulty):
                print("Block successfully mined!")
                self.nonce = nonce + 1  
                return nonce, hash_result
            nonce += 1


wallet_address = "Addres Wallet"
data = "Data for the new block"

miner = Miner(wallet_address)

while True:  
    nonce, hash_result = miner.mine_block(data)
    print(f"Nonce found: {nonce}")
    print(f"Hash: {hash_result}")

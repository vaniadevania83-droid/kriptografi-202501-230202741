import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Menghitung hash SHA-256 dari konten blok.
        """
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Melakukan Proof of Work dengan mencari hash yang diawali dengan jumlah '0' 
        sesuai difficulty.
        """
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"[+] Block mined: {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Tingkat kesulitan (jumlah nol di awal hash)

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        # Proses mining terjadi di sini
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# --- Main Program Execution ---
if __name__ == "__main__":
    print("=== TinyChain Proof of Work Demo ===")
    my_chain = Blockchain()
    
    print("\nSedang menambang (mining) blok 1...")
    start_time = time.time()
    my_chain.add_block(Block(1, "", "Transaksi A -> B: 10 Coin"))
    print(f"Waktu mining: {time.time() - start_time:.4f} detik")

    print("\nSedang menambang (mining) blok 2...")
    start_time = time.time()
    my_chain.add_block(Block(2, "", "Transaksi B -> C: 5 Coin"))
    print(f"Waktu mining: {time.time() - start_time:.4f} detik")
    
    print("\n=== Blockchain Valid ===")
    for block in my_chain.chain:
        print(f"Index: {block.index}, Hash: {block.hash}, Data: {block.data}")
# --- Parameter Publik (Disepakati) ---
P = 23 # Bilangan prima
G = 5  # Generator

# --- Pihak Alice ---
def alice_turn():
    # Kunci Rahasia Alice (a)
    a_private = 6
    print(f"Alice memilih kunci rahasia (a): {a_private}")
    
    # Hitung Kunci Publik Alice (A)
    # A = G^a mod P
    A_public = pow(G, a_private, P)
    print(f"Kunci Publik Alice (A): {G}^{a_private} mod {P} = {A_public}")
    return a_private, A_public

# --- Pihak Bob ---
def bob_turn():
    # Kunci Rahasia Bob (b)
    b_private = 15
    print(f"Bob memilih kunci rahasia (b): {b_private}")

    # Hitung Kunci Publik Bob (B)
    # B = G^b mod P
    B_public = pow(G, b_private, P)
    print(f"Kunci Publik Bob (B): {G}^{b_private} mod {P} = {B_public}")
    return b_private, B_public

# --- Pertukaran Kunci dan Hasil Akhir ---
def exchange_and_calculate(A, B, a, b):
    print("\n--- Pertukaran Kunci Publik (A dan B) ---")
    
    # Alice menghitung kunci rahasia bersama (K_A)
    # K_A = B^a mod P
    K_A = pow(B, a, P)
    print(f"Alice menghitung Kunci Bersama (K_A): {B}^{a} mod {P} = {K_A}")

    # Bob menghitung kunci rahasia bersama (K_B)
    # K_B = A^b mod P
    K_B = pow(A, b, P)
    print(f"Bob menghitung Kunci Bersama (K_B): {A}^{b} mod {P} = {K_B}")

    print("\n--- Verifikasi ---")
    if K_A == K_B:
        print(f"Kedua kunci bersama sama! Kunci Rahasia Bersama: {K_A}")
    else:
        print("Gagal! Kedua kunci tidak sama.")

# --- Eksekusi Program Utama ---
if __name__ == "__main__":
    print(f"Parameter Publik: P={P}, G={G}")
    
    a_private, A_public = alice_turn()
    b_private, B_public = bob_turn()
    
    exchange_and_calculate(A_public, B_public, a_private, b_private)
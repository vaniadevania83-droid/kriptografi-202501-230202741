# --- Aritmetika Modular ---
def A(a,b,n):return (a+b)%n               # Penjumlahan
def B(a,b,n):return ((a-b)%n+n)%n        # Pengurangan (aman)
def C(a,b,n):return (a*b)%n               # Perkalian
def D(b,e,n):return pow(b,e,n)            # Eksponensiasi

# --- GCD & Extended Euclidean ---
def G(a,b): # GCD rekursif
    if b==0:return a
    return G(b,a%b)

def E(a,b): # EGCD iteratif
    x0,x1,y0,y1=1,0,0,1
    while b!=0:
        q=a//b
        a,b=b,a%b
        x0,x1=x1,x0-q*x1
        y0,y1=y1,y0-q*y1
    return a,x0,y0

def I(a,n): # Invers Modular
    g,x,_=E(a,n)
    if g!=1:return None
    return ((x%n)+n)%n

# --- Logaritma Diskrit ---
def L(a,b,n):
    for x in range(n):
        if D(a,x,n)==b:return x
    return None

# PENGUJIAN SATU BARIS (Output Bersatu)

# Aritmetika Modular
print(f"7 + 5 mod 12 = {A(7, 5, 12)}")
print(f"5 - 7 mod 12 = {B(5, 7, 12)}")
print(f"7 * 5 mod 12 = {C(7, 5, 12)}")
print(f"7^128 mod 13 = {D(7, 128, 13)}")

# GCD
print(f"gcd(270, 192) = {G(270, 192)}")

# Invers Modular
print(f"Invers 10 mod 17 = {I(10, 17)}")

# Logaritma Diskrit
print(f"3^x ≡ 4 (mod 7), x = {L(3, 4, 7)}")

print("\n=== EKSEKUSI SELESAI ===")
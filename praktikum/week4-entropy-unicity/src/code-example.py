import math

def calculate_entropy(keyspace_size):
    return math.log2(keyspace_size)

def calculate_unicity_distance(HK, R=0.95, A=26):
    return HK / (R * math.log2(A))

def analyze_brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600 * 24)
    return days

# --- EKSEKUSI ---
# Kunci yang diuji
KEYS_16 = 2**16
KEYS_64 = 2**64

print("===Analisis Kekuatan Kunci===")
print(f"Entropi Ruang Kunci 2^16:{calculate_entropy(KEYS_16):.3f}bit") 
print(f"Entropi Ruang Kunci 2^64:{calculate_entropy(KEYS_64):.3f}bit") 

# Menghitung Unicity Distance langsung dengan fungsi di dalam print
print(f"Jarak Unicity Kunci 16-bit:{calculate_unicity_distance(calculate_entropy(KEYS_16)):.3f}") 

print(f"Estimasi Waktu  Brute Force(10^6attempts/sec):")
print(f"Kunci 16-bit:{analyze_brute_force_time(KEYS_16):.6f}hari") 
print(f"Kunci 64-bit:{analyze_brute_force_time(KEYS_64):.2f}hari") 
print("===EKSEKUSISELESAI===")

# ==========================================
# PROGRAM 2: PERPANGKATAN (REKURSIF)
# ==========================================

def pangkat(basis, eksponen):
    """
    RUNTUNAN ALGORITMA:
    1. KASUS DASAR (Base Case): Jika eksponen adalah 0, hasil adalah 1 (Aturan x^0 = 1)[span_17](start_span)[span_17](end_span)[span_18](start_span)[span_18](end_span).
    2. KASUS DASAR 2: Jika eksponen adalah 1, hasil adalah basis itu sendiri[span_19](start_span)[span_19](end_span)[span_20](start_span)[span_20](end_span).
    3. LANGKAH REKURSI:
       - Kalikan basis dengan hasil pemanggilan fungsi (basis, eksponen - 1)[span_21](start_span)[span_21](end_span)[span_22](start_span)[span_22](end_span).
    """
    # Fungsi Rekursi
    if eksponen == 0:
        return 1  # Base Case 1[span_23](start_span)[span_23](end_span)[span_24](start_span)[span_24](end_span)
    elif eksponen == 1:
        return basis  # Base Case 2[span_25](start_span)[span_25](end_span)[span_26](start_span)[span_26](end_span)
    else:
        # Rekursi: Basis * (basis^(eksponen-1))[span_27](start_span)[span_27](end_span)[span_28](start_span)[span_28](end_span)
        return basis * pangkat(basis, eksponen - 1)

# Uji Coba Program
b, e = 6, 3
print(f"Basis: {b}, Pangkat: {e}")
print(f"Proses Rekursi: 6 * 6 * 6")
print(f"Hasil Akhir: {pangkat(b, e)}") # Output: 216

# Penjelasan
# Rekursi Untuk Pangkat
"""
Pemanggilan Pertama (6^3):
​Basis = 6, Pangkat = 3.  
​Pangkat belum nol, maka simpan angka 6 dan panggil fungsi kembali dengan pangkat dikurangi satu (3 - 1 = 2).  
​Status: 6 \times \text{pangkat}(6, 2).  
​Pemanggilan Kedua (6^2):
​Pangkat belum nol, simpan angka 6 lagi dan panggil fungsi dengan pangkat dikurangi satu (2 - 1 = 1).  
​Status: 6 \times (6 \times \text{pangkat}(6, 1)).  
​Pemanggilan Ketiga (6^1):
​Pangkat belum nol, simpan angka 6 terakhir dan panggil fungsi dengan pangkat dikurangi satu (1 - 1 = 0).  
Pemanggilan Keempat (Base Case - 6^0):
​Pangkat sudah mencapai 0.  
​Sesuai aturan matematika, bilangan pangkat 0 adalah 1, maka fungsi mengembalikan nilai 1.  
​Hasil Akhir (Proses Kalkulasi)
​Setelah mencapai base case, program akan mulai mengalikan semua nilai yang telah dikumpulkan di memori secara berurutan:
​6 \times 6 \times 6 \times 1.  
​Hasil: 216.
"""

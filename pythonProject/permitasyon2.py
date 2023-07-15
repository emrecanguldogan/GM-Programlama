"""
  While döngüsü ile yapılmış bir permütasyon hesaplayan program
"""

def faktoriyelHesapla(i):
    toplam = i
    while i > 1:
        toplam = toplam * (i-1)
        i -= 1
    return toplam

def permutasyonHesapla(j, k):
    permutasyon = faktoriyelHesapla(j)/faktoriyelHesapla((j-k))
    return permutasyon


print("Permütasyon hesabı için lütfen sayıları giriniz.")

sayi1 = int(input("1. Sayı Giriniz: "))

sayi2 = int(input("2. Sayı Giriniz: "))

print("\nSonuç:", permutasyonHesapla(sayi1, sayi2))
"""
  Kendini çağıran fonksiyonlar ile yapılmış bir permütasyon hesaplayan program
"""

def faktoriyelHesapla(i):
    if i == 1:
        return 1

    else:
        return i * faktoriyelHesapla(i - 1)


def permutasyonHesapla(j, k):
    l = 0

    if k > j:
        l = l

    else:
        l = faktoriyelHesapla(j) / faktoriyelHesapla(j - k)
        return l


print("Permütasyon hesabı için lütfen sayıları giriniz.")

sayi1 = int(input("1. Sayı Giriniz: "))

sayi2 = int(input("2. Sayı Giriniz: "))

print("\nSonuç:", permutasyonHesapla(sayi1, sayi2))
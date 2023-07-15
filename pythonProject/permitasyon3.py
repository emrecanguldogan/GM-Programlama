def faktoriyelHesapla(i):
    toplam = 1
    for a in range(1, i+1):
        toplam *= a
    return toplam

def permutasyonHesapla(j, k):
    permutasyon = faktoriyelHesapla(j)/faktoriyelHesapla((j-k))
    return permutasyon


print("Permütasyon hesabı için lütfen sayıları giriniz.")

sayi1 = int(input("1. Sayı Giriniz: "))

sayi2 = int(input("2. Sayı Giriniz: "))

print("\nSonuç:", permutasyonHesapla(sayi1, sayi2))
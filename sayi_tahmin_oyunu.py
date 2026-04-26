import random

cevap = random.randint(0, 100)


hak = 5

while hak > 0:
    tahmin = int(input("0 İle 100 arasında bir sayı tahmin edin: "))

    hak -= 1
    
    if tahmin == cevap:
        print("Cevabınız Doğru :)")
        break
    else:
        if tahmin < cevap:
            print("Lütfen daha büyük bir sayı girin")
        else:
            print("Lütfen daha küçük bir sayı girin ")
    print(f"Şu kadar hakkın kaldı: {hak}")


if hak > 0:
    print(f"Oyun Bitti Sayı:{cevap}")

input("Çıkmak İçin Enter'a basın...")            
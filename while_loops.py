
# verilen cevaba göre sonsuz döngüde sürekli olarak dört işlem yapan, basit hesap makinesi 

while True:    
    sayi1 = int(input("1. Sayı: "))
    sayi2 = int(input("2. Sayı: "))
    islem = input("İşlem Seçiniz (+, -, *, /):")
    
    if islem == "+":
        print("Toplama işleminin sonucu:", (sayi1 + sayi2))
    elif islem == "-":
        print("Toplama işleminin sonucu:", (sayi1 - sayi2))
    elif islem == "*":
        print("Toplama işleminin sonucu:", (sayi1 * sayi2))
    elif islem == "/":
        print("Toplama işleminin sonucu:", (sayi1 / sayi2))
    else:
        print("Geçersiz İşlem")
    
    cevap = input("İşlem yapmaya devam etmek ister misiniz? (evet için 'e', hayır için 'h')")
    if cevap == "e":
        continue
    elif cevap == "h":
        break
    else:
        print("Cevabınızı 'e' veya 'h' olarak belirtmelisiniz")
    


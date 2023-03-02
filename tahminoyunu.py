import random
rand = int(random.uniform(1,100))
sayac = 0
while True:
    sayac += 1
    number = int(input("Sayı giriniz:"))
    if rand < number:
        print("Daha küçük bir sayı giriniz")
    elif rand > number:
        print("Daha büyük bir sayı giriniz")
    elif rand == number:
        print("Tebrikler. Sayıyı tahmin ettiniz!")
        print("Seçilen Sayı: {0}".format(rand))
        print("Tahmin sayınız: {0}".format(sayac))
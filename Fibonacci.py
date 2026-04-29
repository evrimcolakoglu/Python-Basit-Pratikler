"""
Kullanıcıdan 2'den büyük bir sayı alan ve bu sayıya kadar (bu sayı dahil) Fibonacci serisini ekrana yazdıran bir Python fonksiyonu yazınız.

Kurallar:

Kullanıcının girdiği sayı en az 3 olmalıdır. Eğer kullanıcı 2 veya daha küçük bir sayı girerse, ekrana "Lütfen 2'den büyük bir sayı girin." şeklinde bir uyarı vermelidir.

Fibonacci serisi şu şekilde tanımlanır:
İlk iki terim: 0 ve 1
Sonraki her terim, kendisinden önceki iki terimin toplamıdır.

Fibonacci serisini liste olarak ekrana yazdırınız.

Örnek Çalıştırma:

Bir sayı girin: 10
Fibonacci Serisi: [0, 1, 1, 2, 3, 5, 8]
"""


def fibonacci():
    sayi1 = int(input("Sayı giriniz: "))
    if sayi1 <= 2:
        print("Lütfen 2'den büyük bir sayı girin.")
        return
    
    fib_serisi = []
    a = 0
    b = 1

    while a <= sayi1:
        fib_serisi.append(a)
        
        temp = a + b
        a = b
        b = temp

    print("Fibonacci Serisi: ", fib_serisi)

fibonacci()



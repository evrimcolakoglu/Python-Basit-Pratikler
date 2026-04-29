"""
Sayı Tahmin Oyunu - Python Projesi

Bu projede, Python kullanarak bir "Sayı Tahmin Oyunu" yapmanız beklenmektedir. 
Program rastgele bir sayı seçecek ve oyuncu bu sayıyı tahmin etmeye çalışacaktır.
Oyuncunun 7 tahmin hakkı olacak ve her tahminde kaç hakkı kaldığı ekrana yazdırılacaktır.

Kurallar ve Gereksinimler
-   Rastgele Sayı Üretimi: Program, 1 ile 100 arasında rastgele bir sayı seçmelidir.
-   Tahmin Girişi: Kullanıcıdan bir tahmin almalıdır.
-   Hata Kontrolü: Kullanıcının sadece sayı girdiğinden emin olunmalıdır (ipucu isdigit() kullanılabilir).

-   Geri Bildirim: Kullanıcının tahmini:
        Doğruysa: "Tebrikler! Doğru tahmin ettiniz!" mesajı gösterilmelidir.
        Küçükse: "Daha büyük bir sayı girin." mesajı gösterilmelidir.
        Büyükse: "Daha küçük bir sayı girin." mesajı gösterilmelidir.

-   Tahmin Hakkı: Her yanlış tahminde kalan tahmin hakkı azaltılmalıdır.
-   Hakkı Biten Oyuncu: Oyuncu sayıyı bilemezse, "Bilemediniz! Doğru sayı ... idi." mesajı gösterilmelidir.
-   Tekrar Oynama Seçeneği: Oyun sonunda oyuncuya tekrar oynamak isteyip istemediği sorulmalıdır.
        "E" derse oyun tekrar başlamalıdır.
        "H" derse oyun sonlandırılmalıdır.

Örnek Çıktı:
- - - - - - -
1 ile 100 arasında bir sayı tahmin edin. 7 hakkınız var!
Kalan hakkınız: 7 - Tahmininiz: 50
Daha büyük bir sayı girin.
Kalan hakkınız: 6 - Tahmininiz: 75
Daha küçük bir sayı girin.
Kalan hakkınız: 5 - Tahmininiz: 65
Daha büyük bir sayı girin.
Kalan hakkınız: 4 - Tahmininiz: 69
Tebrikler! Doğru tahmin ettiniz! 
Tekrar oynamak ister misiniz? (E/H): 
"""

import random

def sayitahminoyunu():

        while True:

                hak = 7
                sayi = random.randint(1,100)
                t_sayi = 0

                print("1 ile 100 arasında bir sayı tahmin edin. 7 hakkınız var!")

                while hak > 0:
                        t_sayi = input(f"Kalan hakkınız: {hak} - Tahmininiz: {t_sayi} \nf")

                        if t_sayi.isdigit():
                                t_sayi = int(t_sayi)

                                if t_sayi == sayi:
                                        print("Tebrikler! Doğru tahmin ettiniz!")
                                        break

                                elif t_sayi < sayi:
                                        print("Daha büyük bir sayı girin.")
                                
                                else:
                                        print("Daha küçük bir sayı girin.")
                                
                                hak -= 1

                        else:

                                print("Lütfen geçerli bir sayı giriniz!")

                if t_sayi != sayi:
                        print(f"Bilemediniz, doğru sayı: {sayi} idi.")

                tekrar = input("Tekrar oynamak ister misiniz? (E/H)").strip().lower()

                if tekrar != "e":
                        print("Oynadığınız için teşekkürler!")
                        break

sayitahminoyunu()

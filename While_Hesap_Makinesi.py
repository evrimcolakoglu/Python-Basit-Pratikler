""" 
PYTHON PROJE #5
- - - - - - - -
Kullanıcının iki sayı girerek toplama, çıkarma, çarpma ve bölme işlemlerini yapabileceği bir
hesap makinesi programı yazın. Program şu özelliklere sahip olmalıdır:

Kullanıcıya yapmak istediği işlemi seçmesi için bir menü sunulmalıdır:

1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
5. Çıkış
Kullanıcı geçerli bir işlem seçtikten sonra iki sayı girmesi istenmelidir.

İşlem sonucu ekrana yazdırılmalıdır.

Kullanıcı 5 girerek çıkış yapmadıkça program sürekli çalışmalıdır.

Bölme işleminde sıfıra bölme durumu kontrol edilmelidir.
"""

while True:
    print(
    """
    While Hesap Makinesi

    1- Toplama
    2- Çıkarma
    3- Bölme
    4- Çarpma
    5- Üs Alma
    6- Çıkış

    """
    )

    secim = input("(1-6) arasında bir sayı giriniz: ")

    if secim == "6":
        "Programdan başarıyla çıkıldı."
        break

    if secim in ["1","2","3","4","5"]:
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("İkinci sayıyı giriniz: "))

        if secim == "1":
            print(sayi1+sayi2)
            break
        if secim == "2":
            print(sayi1-sayi2)
            break
        if secim == "3":
            print(sayi1/sayi2)
            break
        if secim == "4":
            print(sayi1*sayi2)
            break
        if secim == "5":
            print(sayi1**sayi2)
            break    

    else:
        print("Geçersiz seçim, lütfen 1-6 arasında bir değer giriniz: ")
    


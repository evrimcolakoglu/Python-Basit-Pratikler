while True: # Programın devamlı çalışır olmasını sağlar.
    
    #Metin Bölümü

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

    secim = input("(1-6) arasında bir sayı giriniz: ") #Kullanıcının belirleyeceği 1-6 arasındaki sayı için bir 'secim' değişkeni.

    #If-Else Döngüsü

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
    


"""
PYTHON KODLAMA PROJESİ

agirlikli_ortalama_hesapla(mt1, mt2, f) isimli bir Python fonksiyonu yazınız.

Bu fonksiyon üç sınav sonucunu alır (100 üzerinde notlar girilecek) ve ağırlıklı ortalamayı hesaplar.

Sınavların ağırlıkları sırasıyla %20, %35 ve %45 olarak verilmiştir.

Ortalamayı ekrana yazdırın

Ayrıca eğer ortalama notu 50'den küçükse veya final notu 20'den küçükse
(midterm notları ne olursa olsun) bütünlemeye kaldınız yazsın, aksi takdirde geçtiniz yazsın.
"""

def agirlikli_ortalama_hesapla(mt1, mt2, f):

    ortalama = 0.2*mt1 + 0.35*mt2 + 0.45*f

    if ortalama<50 or f<20:
        print("Bütünlemeye kaldınız.")
    else:
        print(0.2*mt1 + 0.35*mt2 + 0.45*f) 
    
agirlikli_ortalama_hesapla(85,95,10)
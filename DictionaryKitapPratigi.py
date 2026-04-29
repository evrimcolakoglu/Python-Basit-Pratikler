kitaplar = [
    ("Şeker Portakali", 180),
    ("Simyacı", 184),
    ("1984", 352),
    ("Hayvan Çiftliği", 152)
]

fazla_sayfali_kitaplar = []

toplam_sayfa = 0

for kitap_adi, sayfa_sayisi in kitaplar:
    if sayfa_sayisi > 170:
        fazla_sayfali_kitaplar.append(kitap_adi)
        toplam_sayfa += sayfa_sayisi
        
print("170'den fazla sayfası olan kitaplar: ")
print(fazla_sayfali_kitaplar)

print("Toplam sayfa sayıları: ")
print(toplam_sayfa)

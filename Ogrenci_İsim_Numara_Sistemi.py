isimler = ["Ali", "Ece", "Kaan", "Mete", "Batu", "Veli", "Ayşe"]
numaralar = [145, 178, 164, 175, 185, 180, 134]


#Döngü Kullanarak

#a için çözüm

sayi_max = 0

for i in range(len(numaralar)):
    if numaralar[i] > sayi_max:
        sayi_max = numaralar[i]
        numara_sahibi_max = isimler[i]
            
print(sayi_max, numara_sahibi_max)
    
#b için çözüm

sayi_min = sayi_max

for i in range(len(numaralar)):
    if numaralar[i] < sayi_min:
        sayi_min = numaralar[i]
        numara_sahibi_min = isimler[i]
            
print(sayi_min, numara_sahibi_min)    

#Python Fonksiyonu Kullanarak

#a için çözüm

maxsayi = max(numaralar)
maxogrenci = isimler[numaralar.index(maxsayi)]

#b için çözüm

minsayi = min(numaralar)
minogrenci = isimler[numaralar.index(minsayi)]

print(f"Max öğrenci ve numarası: {maxogrenci}-{maxsayi}, Min öğrenci ve numarası: {minogrenci}-{minsayi}")
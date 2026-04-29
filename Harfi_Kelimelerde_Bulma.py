cumle = input("Lütfen bir cümle giriniz: ")
harf = input("Lütfen bir harf giriniz: ")

harf = harf.lower()

kelimeler = cumle.split()

sayac = 0

for kelime in kelimeler:
    if harf in kelime.lower():
        sayac += 1

print(f"{harf} harfini içeren kelime sayısı {sayac}")
def kelimeSayaci(metin):
    kelime=metin.split()
    return len(kelime)
metin=input("metni giriniz: ")
kelimesayisi=kelimeSayaci(metin)

print(f"girilen metinde kelime sayısı: {kelimesayisi}")

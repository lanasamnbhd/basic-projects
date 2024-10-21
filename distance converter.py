def mesafeDonusturucu(mesafe, birim):
    if birim=="km":
        mil=mesafe*0.621371
        metre=mesafe*1000
        return mil, metre
    elif birim=="mil":
        km=mesafe/0.621371
        metre=km*1000
        return km, metre
    elif birim=="metre":
        km=mesafe/1000
        mil=km*0.621371
        return km, mil
    else:
        return None

mesafe=float(input("dönüştürmek istediğiniz mesafeyi girin: "))
birim=input("lütfen birimi giriniz(km, mil, metre): ").lower()
sonuc=mesafeDonusturucu(mesafe,birim)

if sonuc:
    if birim=="km":
        print(f"{mesafe} km={sonuc[0]} mil={sonuc[1]} metre")
    elif birim=="mil":
        print(f"{mesafe} mil={sonuc[0]} km={sonuc[1]} metre")
    elif birim=="metre":
        print(f"{mesafe} metre={sonuc[0]} km={sonuc[1]} mil")
    else:
        print("bir hata oluştu. lütfen tekrar deneyin.")

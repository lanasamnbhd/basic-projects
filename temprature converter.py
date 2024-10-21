def sicaklikDonusturucu(sicaklik, birim):
    if birim=="celcius":
        kelvin=sicaklik+273.15
        fahrenheit=sicaklik*(9/5)+32
        return kelvin, fahrenheit
    elif birim=="kelvin":
        celcius=sicaklik-273.15
        fahrenheit=celcius*(9/5)+32
        return celcius, fahrenheit
    elif birim=="fahrenheit":
        celcius=(sicaklik-32)(5/9)
        kelvin=celcius-273.15
        return celcius, kelvin
    else:
        return None

sicaklik=float(input("dönüştürmek istediğiniz sıcaklığı girin: "))
birim=input("lütfen birimi giriniz(celcius, fahrenheit, kelvin): ").lower()
sonuc=sicaklikDonusturucu(sicaklik,birim)

if sonuc:
    if birim=="celcius":
        print(f"{sicaklik} celcius={sonuc[0]} kelvin={sonuc[1]} fahrenheit")
    elif birim=="kelvin":
        print(f"{sicaklik} kelvin={sonuc[0]} celcius={sonuc[1]} fahrenheit")
    elif birim=="fahrenheit":
        print(f"{sicaklik} fahrenheit={sonuc[0]} celcius={sonuc[1]} kelvin")
    else:
        print("bir hata oluştu. lütfen tekrar deneyin.")

def kutleDonusturucu(kutle, birim):
    if birim=="kg":
        lb=kutle/0.45
        gr=kutle*1000
        return lb, gr
    elif birim=="lb":
        kg=kutle*0.45
        gr=kg*1000
        return kg, gr
    elif birim=="gr":
        kg=kutle/1000
        lb=kg*0.45
        return kg, lb
    else:
        return None

kutle=float(input("dönüştürmek istediğiniz kütleyi girin: "))
birim=input("lütfen birimi giriniz(kg, lb, gr): ").lower()
sonuc=kutleDonusturucu(kutle,birim)

if sonuc:
    if birim=="kg":
        print(f"{kutle} kg={sonuc[0]} lb={sonuc[1]} gr")
    elif birim=="lb":
        print(f"{kutle} lb={sonuc[0]} kg={sonuc[1]} gr")
    elif birim=="gr":
        print(f"{kutle} gr={sonuc[0]} kg={sonuc[1]} lb")
    else:
        print("bir hata oluştu. lütfen tekrar deneyin.")

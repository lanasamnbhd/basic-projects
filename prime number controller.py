def asm(sayi):
    if sayi<2:
        return False
    for i in range(2,int(sayi**0.5)+1):
        if sayi%i==0:
            return False
    return True

sayi=int(input("sayiyi girin: "))
if asm(sayi): print("sayı asaldır")
else: print("sayı asal değildir")

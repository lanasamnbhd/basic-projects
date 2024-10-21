import random
import string

def parolaOlusturucu(uzunluk):
    karakterSeti=string.ascii_letters + string.digits+string.punctuation

    parola=''.join(random.choice(karakterSeti) for i in range(uzunluk))
    return parola

uzunluk=int(input("oluşturulacak parolanın uzunluğunu giriniz:"))
parola=parolaOlusturucu(uzunluk)
print(f"parola={parola}")

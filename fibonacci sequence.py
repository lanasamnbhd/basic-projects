def fibo(n):
    fibserie=[0,1]

    for i in range(2,n):
        newN=fibserie[i-1]+fibserie[i-2]
        fibserie.append(newN)
    return fibserie

terimSayisi=int(input("kaç terimlik bir seri istiyorsunuz? "))

if terimSayisi<=0:
    print("lütfen pozitif bir değer girin")
elif terimSayisi==1:
    print([0])
else:
    sonuc=fibo(terimSayisi)
    print(f"fibonacci serisi:({terimSayisi} terim):{sonuc}")

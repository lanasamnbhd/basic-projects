import datetime

zaman=datetime.datetime.now()
tarih=zaman.strftime("%d/%m/%Y")
saat=zaman.strftime("%H:%M:%S")

print(f"bugünün tarihi:{tarih}")
print(f"şuanki saat:{saat}")

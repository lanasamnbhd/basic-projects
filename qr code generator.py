import pyqrcode
from pyqrcode import QRCode

s="https://youtu.be/RHe3gk8CnfE?si=2P4HBn8uXUyvswhy" #paste your link here
url=pyqrcode.create(s)

print(url.terminal(quiet_zone=1))

import pyqrcode
data="{hussainint }"
qr=pyqrcode.create(data)
qr.png("qrcode.png", scale=8)

# requires pyqrcode and pypng module
# pip3 install pyqrcode
# pip3 install pypng
# generate QR code from string data

import pyqrcode
from pyqrcode import QRCode
import png

#string to be represented
s="Muhammad Izham bin Ismail 791030075091"

#generate the code
url = pyqrcode.create(s)

#create and save png file
url.svg("testQR.svg",scale=16)

testpng = pyqrcode.create(s, error='L', version=27, mode='binary')
testpng.png("testQR.png",scale=2)


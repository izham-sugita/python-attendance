# combine column Name and Matrix into one string
# generate sha256 for Name+Matrix
# the generated sha256 will be embedded into QR code

import hashlib

import sys

import pandas as pd 

df = pd.read_csv("./namelist-0.csv")

print(df)
print()

list0 = df["Name"].tolist()
list1 = df["Matrix"].tolist()


#create security feature by hashing
hashlist = []
total_element = len(list0)

for el in range(total_element):
	st = list0[el]+" "+str(list1[el])
	hashlist.append(st)


list3 =[]
for el in range(len(hashlist)):
	hash_object = hashlib.sha256(hashlist[el].encode())
	hex_dig = hash_object.hexdigest()
	print(hex_dig)
	list3.append(hex_dig)

df["sha256"]=list3

print(df)

'''
import pyqrcode
from pyqrcode import QRCode
import png

#string to be represented
# s="Muhammad Izham bin Ismail 791030075091"
s = list3[0]

#generate the code
url = pyqrcode.create(s)

#create and save png file
testpng = pyqrcode.create(s, error='L', version=27, mode='binary')
testpng.png("testQR.png",scale=2)
'''

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
from random import choices,randint
from string import ascii_letters

flag=os.environ.get('FLAG', 'FLAG{REDIRECT}')

def encrypt(plain,key):
    Ckey=bytearray([key]*16)
    cipher=AES.new(Ckey,AES.MODE_ECB)
    return cipher.encrypt(plain)

secret="".join(choices(ascii_letters,k=32))



Padded_secret=pad(secret.encode(),16)
keys=[randint(0,256) for i in range(4)]
for i in keys:
    Padded_secret=encrypt(Padded_secret,i)
print("Here is our encrypted secret :"+Padded_secret.hex())
guess=input("try to guess it :")
if guess==secret:
    print("Wow u Got it "+flag)
else:
    print("Not today !")

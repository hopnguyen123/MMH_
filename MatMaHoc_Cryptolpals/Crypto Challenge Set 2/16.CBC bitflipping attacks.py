import random
import string
from Crypto.Cipher import AES
import os

#Random KEY 16 BYTES
Random_ASCII=''.join(random.choices(string.ascii_uppercase+string.digits,k=16))
KEY=""
for i in Random_ASCII:
    x=hex(ord(i))[2:]
    KEY+=x
KEY=bytes.fromhex(KEY)
print(KEY)

iv=os.urandom(16)
def Encrypt_AES_CBC(data):
    BLOCK_SIZE=16
    FAD = "["
    du=len(data)%BLOCK_SIZE
    if du!=0:
        data_padding = data + (BLOCK_SIZE - len(data) % BLOCK_SIZE) * FAD
    else:
        data_padding = data
    cipher = AES.new(KEY, AES.MODE_CBC,iv)
    ct = cipher.encrypt(data_padding.encode('utf-8'))
    return ct

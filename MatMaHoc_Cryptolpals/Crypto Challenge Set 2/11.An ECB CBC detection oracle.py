#Xong
import string
import random
from Crypto.Cipher import AES
import os

#Random KEY 16 BYTES
Random_ASCII=''.join(random.choices(string.ascii_uppercase+string.digits,k=16))
KEY=""
for i in Random_ASCII:
    x=hex(ord(i))[2:]
    KEY+=x
KEY=bytes.fromhex(KEY)

#Append 5->10 bytes PLAINTEXT
def Append_PlainText(data):
    Number_left=random.randint(5,10)
    Random_Append1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=Number_left))
    Number_right = random.randint(5, 10)
    Random_Append2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=Number_right))
    data=Random_Append1+data+Random_Append2
    return data

def Encrypt_AES_ECB(data):
    BLOCK_SIZE=16
    FAD="["
    data_padding=data+(BLOCK_SIZE-len(data)%BLOCK_SIZE)*FAD
    cipher=AES.new(KEY,AES.MODE_ECB)
    ct=cipher.encrypt(data_padding.encode('utf-8'))
    return ct

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

def encryption_oracle(pt):
    padded_pt = Append_PlainText(pt)
    if random.randint(0, 1) == 0:
        return Encrypt_AES_ECB(padded_pt)
    else:
        return Encrypt_AES_CBC(padded_pt)

def detect_encryption_oracle():
    pt = 'BLUE VIETCOMBANK' * 3
    ct = encryption_oracle(pt)
    return ct[16:32] == ct[32:48]

if __name__=='__main__':
    print(detect_encryption_oracle())
#Xong
import base64
from Crypto.Cipher import AES

def GiaiMa(key,data,iv):                    #Key,data,iv (type = bytes)
    pt=AES.new(key,AES.MODE_CBC,iv)
    plaintext=pt.decrypt(data).decode()
    return plaintext


key = b'YELLOW SUBMARINE'                   #Convert KEY(type = bytes)
iv = b'\x00' * AES.block_size               #   iv (type = bytes)

data=open("bai10.txt")                      #Mở Data
DATA=data.read()
ciphertext = base64.b64decode(DATA)         #Convert:   BASE64 -> CipherTEXT (bytes)

plaintext=GiaiMa(key,ciphertext,iv)         #Giải mã CipherTEXT -> PlainTEXT
print(plaintext)

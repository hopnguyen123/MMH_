# xong
import base64
from Crypto.Cipher import AES

def GiaiMa(ciphertext,key):
    MatMa=AES.new(key,AES.MODE_ECB)            #Thiết lập mode_ECB của AES, khi biết key
    plaintext=MatMa.decrypt(ciphertext)
    print(plaintext)

key = b'YELLOW SUBMARINE'       #Chuyển string -> bytes

data=open('data07.txt')             #Đọc File
data=data.read()

ciphertext=base64.b64decode(data)   #Chuyển base64 -> ciphertext (bytes)f

GiaiMa(ciphertext,key)

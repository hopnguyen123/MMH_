#Hàm random 1 trong 10 dãy input
#Hàm tạo khoá AES  (block 16bbytes) -> mã hoá chuỗi đã được chọn ở trên
#Hàm iv random
#Giải mã CiherTEXT
# ktra phần đệm -> true or false : dựa vào phần đệm
#Nếu mà Plaintext (k đệm ) -> False
#Nếu plaintext (có đệm ) -> đệm hợp lý : True

#Xong
import random as rd
import string
import os
from Crypto.Cipher import AES


#Chọn 1 trong 10 chuỗi
def Choose_String():
    data = open("bai17.txt")
    data=data.read().split("\n")
    index=rd.randint(0,9)
    input=data[index]
    return input

#Tạo key - AES
def Create_KEY():
    KEY = ''.join(rd.choices(string.ascii_uppercase+string.digits,k=16))        #Tạo KEY: gồm chữ cái và số (16 kí tự) , type = string
    return KEY
#Chuyển KEY từ type = string -> type = hex
def Convert_KEY_to_HEX(data):
    x = ""
    for i in data:
        y = hex(ord(i))[2:]
        x += y
    KEY = bytes.fromhex(x)
    return KEY

#Tạo iv
iv=os.urandom(16)   #type = bytes

#AES _ CBC
def Encypt_AES_CBC(data,key,iv):
    data=pading(data)                               #Mở rộng chuỗi ban đầu
    cipher=AES.new(key,AES.MODE_CBC,iv)
    ct=cipher.encrypt(data.encode('utf-8'))
    return ct
def Decrypt_AES_CBC(data,key,iv):
    decipher=AES.new(key,AES.MODE_CBC,iv)
    pt=decipher.decrypt(data).decode()
    return pt

#Check padding
def Check_padding_oracle(data):
    last=ord(data[-1])                              #Kiểm tra padding
    if last ==0 or last >15:
        return False
    if len(set(map(ord,data[-last:]))) == 1:        #N kí tự đầu tiên có giá trị = N, vd: 4 kí tự cuối cùng đều = 4
        return True
    else:
        return False                                #Nếu k padding -> False

List_pad=["\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0A","\x0B","\x0C","\x0D","\x0E","\x0F"]
def pading(data):
    n=len(data)
    SoLuongDem=16-n%16
    if SoLuongDem>0 and SoLuongDem!=16:             #padding theo BLOCK_SIZE = 16
        data = data + List_pad[SoLuongDem-1]*SoLuongDem
    return data



key__=Create_KEY()                  #B1: Tạo key
print("KEY ASCII: ",key__)

KEY=Convert_KEY_to_HEX(key__)       #B2: Chuyển KEY -> bytes
print("KEY bytes: ",KEY)

print("iv: ",iv)                    #B3: Tạo iv

data=Choose_String()                #B4: Chọn chuỗi
print("DATA: ",data)
print("len(DATA): ",len(data))

data=Encypt_AES_CBC(data,KEY,iv)    #B5: Mã hoá + padidng (nếu cần)
print("Encrypt: ",data)

data=Decrypt_AES_CBC(data,KEY,iv)   #B6: Giải mã
print("Decrypt: ",data)

check=Check_padding_oracle(data)    #B7: Kiểm tra padding (nhờ giải mã ciphertext)
print(check)

# MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg== : Trường hợp '\x08' là phím backspace ==> nên các kí tự bị xoá
#MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=
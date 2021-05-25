#Viết 1 hàm chuyển string -> dictionary (xong)
#Viết 1 hàm chuyển từ dictionayr -> string (xong)
#Viết 1 hàm profile_for(...) -> "foo@bar.com" --> {email: 'foo@bar.com", uid:10,role: 'user'} (xong)
#   Viết 1 hàm từ ouput phía trên --> email=foo@bar.com&uid=10&role=user (xong)
#   không được phép đặt địa chỉ email "foo@bar.com&role=admin" (xong)

#Tạo Khoá AES ngẫu nhiên
#   A. Mã hoá hồ sơ người dùng (user profile) theo khoá "provide" ??
#   B. ???
#NoTE: chỉ sử dụng thông tin người dùng nhập vào profile_for() vào tạo ra hồ sơ role=admin

import random
import string
from Crypto.Cipher import AES

#Hàm chuyển String -> Dictionary
def Convert_Str_to_Dic(input):
    data=input.split('&')
    dic={}
    for i in data:
        i=i.split('=')
        dic[i[0]]=i[1]
    return dic

# x="foo=bar&baz=qux&zap=zazzle"
# y=x.split('&')
# dic={}
# for i in y:
#     z=i.split('=')
#     dic[z[0]]=z[1]
# y=Convert_Str_to_Dic(x)
# print(y)


#Hàm Chuyển Dictionary --> String
def Convert_Dic_to_Str(input):
    list=[]
    for i in input.items():
        str=i[0]+'='+i[1]
        list.append(str)
    str='&'.join(list)
    return str
#
# x={'foo': 'bar', 'baz': 'qux', 'zap': 'zazzle'}
# str=Convert_Dic_to_Str(x)
# print(str)

#Hàm profile_for()
def profile_for(input):
    dic={'email':input.replace('&','').replace('=',''),
         'uid':'10',
         'role':'user'
        }
    str=Convert_Dic_to_Str(dic)
    return str
#
# x=profile_for("foo@bar.com&role=admin")
# print(x)

#Hàm Random_Key
def Random_Key():
    key=random.choices(string.ascii_uppercase+string.digits,k=16)
    List=[]
    for i in key:
        x=hex(ord(i))[2:]
        List.append(x)
    List=''.join(List)
    KEY=bytes.fromhex(List)
    return KEY

KEY=Random_Key()

List_pad=["\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0A","\x0B","\x0C","\x0D","\x0E","\x0F"]
def pading(data):
    n=len(data)
    SoLuongDem=16-n%16
    if SoLuongDem>0 and SoLuongDem!=16:             #padding theo BLOCK_SIZE = 16
        data = data + List_pad[SoLuongDem-1]*SoLuongDem
    return data

def Check_padding_oracle(data):
    last=ord(data[-1])                              #Kiểm tra padding
    if last ==0 or last >15:
        return -1
    if len(set(map(ord,data[-last:]))) == 1:        #N kí tự đầu tiên có giá trị = N, vd: 4 kí tự cuối cùng đều = 4
        return -last
    else:
        return -1                                #Nếu k padding -> False

def Encryt_AES_ECB(input):
    n_=len(input)
    input=pading(input)
    cipher=AES.new(KEY,AES.MODE_ECB)
    ct=cipher.encrypt(input.encode('utf-8'))
    return ct
def Decrypt_AES_ECB(input):
    decipher=AES.new(KEY,AES.MODE_ECB)
    pt=decipher.decrypt(input).decode()
    index_padding=Check_padding_oracle(pt)
    plaintext=pt[:index_padding]
    return plaintext

def encrypt_profile(input):
    str1=profile_for(input)
    str2=Encryt_AES_ECB(str1)
    return str2

def decrypt_profile(input):
    str1=Decrypt_AES_ECB(input)
    dic1=Convert_Str_to_Dic(str1)
    return dic1

# x="foo@bar.com"
# x=encrypt_profile(x)
# print(x)
# x=decrypt_profile(x)
# print(x)

'''
#input: HHHHHHHHHHadmin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b (26bytes)
#Sau khi encrypt_profile()
   b1_1: profile_for() .... input --> email=HHHHHHHHHHadmin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b .....
                                   '   đoạn này đủ 32 bytes                                          '
                                   các đoạn sau không quan trọng
    b2_1: Encryt_AES_ECB()    --> 1 chuỗi mã
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#input:  bad@email.com
Sau khi encrypt_profile()
    b1_2: profile_for() .. input --> 'email=bad@email.com&uid=10&role='
                                    ' đoạn này đủ 32 bytes          ' -> cái phía sau là 16bytes (user....)
    b2_2: Encryt_AES_ECB()    --> 1 chuỗi mã

Sau các bước trên: ta lấy b2_2[:-16] --> để sau đó giải mã ra được 'email=bad@email.com&uid=10&role='
                       lấy b2_1[16:32]="admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b" 
                                        --> để sau đó giải mã ra được 'admin'
                    GHÉP b2_2 + b2_1 --> giải mã --> ra kết quả

    
                                    

'''
string_1 = encrypt_profile('H' * 10 + 'admin' + '\x0b' * 11)
string_2 = encrypt_profile('Hop@email.com')
result = string_2[:-16] + string_1[16:32]
print(decrypt_profile(result))




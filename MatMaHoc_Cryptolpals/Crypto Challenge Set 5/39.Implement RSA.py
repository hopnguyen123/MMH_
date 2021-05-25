#Xong
import random
from Crypto.Util.number import isPrime

#B1: Tạo Số nguyên tố
def SinhSoNguyenTo():
    List_primes=[]          #Tạo danh sách các số nguyên tố từ 2 -> 9999
    for i in range(2,999):
        if isPrime(i):
            List_primes.append(i)

    result = random.choice(List_primes)  #Chọn 1 trong các số nguyên tố trên
    return result

#Tìm ước chung lớn nhât
def GCD(a,b):
    if(b==0):
        return a
    else:
        return GCD(b,a%b)

#Tìm e
def Tim_e(phi_n):
    for e in range(2,phi_n):
        if GCD(phi_n,e)==1:
            return e

def Tim_d(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e         #Phần nguyên
        temp2 = temp_phi - temp1 * e#Phần dư
        temp_phi = e                #Gán lại e cho temp_phi
        e = temp2                   # e = phần dư

        x = x2 - temp1 * x1         #
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d+phi

#Mã hoá, giải mã RSA - 1 kí tự
def encrypt_1character(data,e,n):
    c=data**e%n
    return c
def decrypt_1character(data,d,n):
    m=data**d%n
    return m

#Mã hoá, Giải mã RSA chuỗi
def encrypt_RSA(pt):
    l=[]
    for i in pt:
        i = ord(i)
        i = encrypt_1character(i,e,n)
        l.append(i)
    return l
def decrypt_RSA(ct):
    pt=""
    for i in ct:
        i = decrypt_1character(i,d,n)
        i=chr(i)
        pt+=i
    return pt

p=SinhSoNguyenTo()
q=SinhSoNguyenTo()
print("p: ",p)
print("q: ",q)

n=p*q
phi_n=(p-1)*(q-1)

e=Tim_e(phi_n)
d=Tim_d(e,phi_n)
print("e: ",e)
print("d: ",d)

print("PUBLIC KEY: ",e," , ",n)
print("PRIVATE KEY: ",d," , ",n)

plaintext=input("Nhap input: ")
ct=encrypt_RSA(plaintext)
pt=decrypt_RSA(ct)
print("CT: ",ct)
print("PT: ",pt)

# p=7
# q=17
# e=5
# M=32
#
# n=p*q
# phi_n=(p-1)*(q-1)
# d=Tim_d(e,phi_n)
# c=encrypt_1character(M,e,n)
# m=decrypt_1character(c,d,n)
#
# print("p: ",p)
# print("q: ",q)
# print("e: ",e)
# print("M: ",M)
# print("n: ",n)
# print("phi_n: ",phi_n)
# print("PUBLIC KEY: ",e," , ",n)
# print("PRIVATE KEY: ",d," , ",n)
# print("c: ",c)
# print("d: ",d)


#Câu a: p=11,q=3,e=3,M=4,d=27,c=31
#Câu b: p=7,q=17,e=5, M=32, d=77,c=2
#Câu c: p=23,q=41,e=7,M=35, d=503,c=545
#câu d:
# m=decrypt_1character(c,d,n)
# print("m: ",m)






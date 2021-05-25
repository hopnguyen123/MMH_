import random
from Crypto.Util.number import isPrime

#Tạo danh sách các số nguyên tố từ 2 -> 9999
List_primes=[]
for i in range(2,999):
    if isPrime(i):
        List_primes.append(i)

p = random.choice(List_primes)
q=random.choice(List_primes)
print("p: ",p)
print("q: ",q)

n=p*q
phi_n=(p-1)*(q-1)
print("n: ",n)
print("phi_n: ",phi_n)


def GCD(a,b):
    if(b==0):
        return a
    else:
        return GCD(b,a%b)

def Tim_e(phi_n):
    for e in range(2,phi_n):
        if GCD(phi_n,e)==1:
            return e

#Tìm d
def Tim_d(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

#public key: e,n
#private key: d,n
e=Tim_e(phi_n)
d=Tim_d(e,phi_n)
print("e: ",e)
print("d: ",d)
print("PUBLIC KEY: ",e," , ",n)
print("PRIVATE KEY: ",d," , ",n)

def encrypt_1character(data,e,n):
    c=data**e%n
    return c
def decrypt_1character(data,d,n):
    m=data**d%n
    return m

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

plaintext=input("Nhap input: ")
ct=encrypt_RSA(plaintext)
pt=decrypt_RSA(ct)
print("CT: ",ct)
print("PT: ",pt)







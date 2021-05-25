from Crypto.Cipher import AES
import os
from Crypto.Util import Counter

# key=os.urandom(32)
# counter=Counter.new(64)
# print(counter)
# for i in counter.items():
#     print(i[1])
#     print(type(i[1]))
# aes = AES.new(key, AES.MODE_CTR, counter=Counter.new(128))
# encrypted = aes.encrypt("NguyenNgocHop".encode('utf-8'))
# print(encrypted)
# decipher=AES.new(key,AES.MODE_CTR, counter=Counter.new(128))
# pt=decipher.decrypt(encrypted).decode()
# print(pt)

KEY=b'YELLOW SUBMARINE'
nonce='\x00'*16
print(nonce)
aes = AES.new(KEY, AES.MODE_CTR,counter=Counter.)
encrypted = aes.encrypt("NguyenNgocHop".encode('utf-8'))
print(encrypted)
decipher=AES.new(KEY,AES.MODE_CTR, nonce)
pt=decipher.decrypt(encrypted).decode()
print(pt)




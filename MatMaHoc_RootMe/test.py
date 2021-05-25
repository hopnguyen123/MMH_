from hashlib import sha3_512 as sh3
import sys
import hashlib

if sys.version_info < (3, 6):
    import sha3

str = "GeeksforGeeks"
s=str.encode()  #Chuyển từ str -> bytes     ("hasaki" -> b'hasaki') mỗi kí tự là ascii
# create a sha3 hash object
hash_sha3_512 = hashlib.new("sha3_512", str.encode())

print("\nSHA3-512 Hash: ", hash_sha3_512.hexdigest())

#0d6e577505f50cac9885e31a70da8bb47c59dd771e7d722e13949d692e607b98e36fb2b921761ca37f94fbc2fa2840bbfedd825e4f65b5187d0d883420352be3
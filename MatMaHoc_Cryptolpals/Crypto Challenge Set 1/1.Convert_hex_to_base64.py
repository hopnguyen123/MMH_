#HOÀN THÀNH
from base64 import b64encode, b64decode

# hex -> base64
str1 = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
str2=bytes.fromhex(str1)                #Chuyển str1 (string) -> str1(hex) ==> Sau đó chuyển về bytes
b64 = b64encode(str2).decode()          #Giải mã -> base64
print('base64:', b64)

# base64 -> hex
s2 = b64decode(b64.encode()).hex()
print('hex is:', s2)


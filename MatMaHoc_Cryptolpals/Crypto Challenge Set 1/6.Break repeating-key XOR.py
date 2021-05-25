from base64 import b64decode,b64encode
data = open("data06.txt")
Data = data.read().split('\n')  #Data có kiểu List, len(Data) = 64 tương ứng 64 dòng

List_cipher=[]
for i in Data:
    i=b64decode(i).decode()     #Chuyen base64 -> chuoi string
    List_cipher.append(i)

# print(List_cipher)
String_cipher=''.join(List_cipher)
print(len(String_cipher))

def Convert_String_to_bit(input):       #Chuyển string -> bit (type = string)
    x1=""
    for i in input:
        x2=bin(ord(i))[2:]
        them_=8-len(x2)
        x2=them_*"0"+x2
        x1+=x2
    return x1
def Distance_Hamminng(input1,input2):   #Khoảng cách giữa 2 chuỗi
    dem=0
    input1=Convert_String_to_bit(input1)
    input2=Convert_String_to_bit(input2)
    for i1,i2 in zip(input1,input2):
        if i1 != i2:
            dem+=1
    return dem

key_sizes = []
# For each key size
for KEYSIZE in range(2, 41):
    running_sum = []
    for i in range(0, int(len(String_cipher) / KEYSIZE) - 1):
        running_sum.append(Distance_Hamminng(String_cipher[i * KEYSIZE:(i + 1) * KEYSIZE],String_cipher[(i + 1) * KEYSIZE:(i + 2) * KEYSIZE]) / KEYSIZE)
    key_sizes.append((sum(running_sum)/ len(running_sum), KEYSIZE))
key_sizes.sort(key=lambda a: a[0])
print(key_sizes)
print(key_sizes[0][1])

x1="Terminator X: Bring the noise"
x2=String_cipher[0:29]
for i1,i2 in zip(x1,x2):
    x=chr(ord(i1)^ord(i2))
    print(x,end='')


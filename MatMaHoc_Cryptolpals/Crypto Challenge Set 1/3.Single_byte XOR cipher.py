#XONG
import binascii

encoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
input_string = binascii.unhexlify(encoded)          #type(string) -> hex string (2ki tu) -> ascii

List_kq=[]
for so in range(256):           #Xét từng kí tự 0 -> 255 (bảng ascii)
    l=[]
    for kitu in input_string:   #Xét từng kí tự ascii (2 kí tự hex) trong input
        kq=chr(so^kitu)
        l.append(kq)
    l=''.join(l)
    List_kq.append(l)

def DemKiTu(s):
    dem=0
    for i in s:
        if (i>='a' and i<='z') or (i>='A' and i<='Z') or (i==' '):
            dem+=1
    return dem

#Xét từng chuỗi sau khi XOR -> chuỗi nào có kí tự a->z,A->Z nhiều nhất (Là KẾT QUẢ)
max=0
index=0
for i in range(len(List_kq)):
    soluong=DemKiTu(List_kq[i])
    if soluong>max:
        max=soluong
        index=i

print(List_kq[index])

# "Cooking MC's like a pound of bacon"
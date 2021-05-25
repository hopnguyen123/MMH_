#   XONG

import binascii

data = open("data04.txt")                   #Đọc File
List_input = data.read().split('\n')
# print(len(List_input))    #327 dòng

#Chuyen 327 dòng -> binascii (từ hex)
List_nums=[]                                #Chuyển các dòng -> ascii
for i in List_input:
    string_input = binascii.unhexlify(i)
    List_nums.append(string_input)

OUTPUT=[] #327 dòng X 256 kí tự = ...
for i in List_nums:
    for key in range(256):
        l=[]
        for kitu in i:
            x = chr(kitu^key)
            l.append(x)
        s = ''.join(l)
        OUTPUT.append(s)
    OUTPUT.append(s)

def DemKiTu(s):
    dem=0
    for i in s:
        if ((i>='a' and i<='z') or (i>='A' and i<='Z')) or (i==' '):
            dem+=1
    return dem

max=0
index_out=0
n_ = len(OUTPUT)
index_output=[]
for i in range(n_):
    sokitu = DemKiTu(OUTPUT[i])
    if sokitu >max:
        max = sokitu
        index_out=i

print(OUTPUT[index_out])

text = open('ch7.bin','rb').read()
print(text)
l=[]
l1=[]
def dem(string):
    dem=0
    for i in string:
        if (i>='a'and i<='z') or (i>='A'and i<='Z') or (i==' '):
            dem+=1
    return dem


for i in range(0,256):
    s=""
    for c in text:
        if c+i>255:
            continue
        else:
            s+=chr(c+i)
    l.append(s)
    l1.append(dem(s))
for i in l:
    print(i)
# max=0
# index=0
# for i in range(len(l1)):
#     if l1[i]>max:
#         max=l1[i]
#         index=i
#
# print(l[index])


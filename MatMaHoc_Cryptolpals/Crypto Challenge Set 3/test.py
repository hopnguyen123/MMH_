List_pad=["\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0A","\x0B","\x0C","\x0D","\x0E","\x0F"]
data="MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg=="
n=len(data)
print("n: ",n)
SoLuongDem=16-n%16
if SoLuongDem>0 and SoLuongDem!=16:
    print("ll_1: ",data)
    data = data + List_pad[SoLuongDem-1]*8
    print("ll: ",data)
    print("padding: ",List_pad[SoLuongDem-1]*8)
    x=List_pad[SoLuongDem-1]
    print("x: ",x)
    print(type(x))

print("list_pad")
for i in range(len(List_pad)):
    print(List_pad[i])
    print(ord(List_pad[i]))
    print(type(List_pad[i]))
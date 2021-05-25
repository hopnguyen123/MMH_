#Xong
def valid_pkcs7_padding(s):
    last = ord(s[-1])                       #Chuyển kí tự cuối cùng của chuỗi -> int
    # print(x)
    if len(set(map(ord, s[-last:]))) == 1:  #Số lượng kí tự sau cùng (nếu giống nhau) -> set{...}==1
        return True
    else:
        return False

x1="ICE ICE BABY\x04\x04\x04\x04"
x2="ICE ICE BABY\x07\x07\x07\x07\x07\x07"
x3="ICE ICE BABY\x01\x02\x03\x04"
k1=valid_pkcs7_padding(x1)      #vd: 4 kí tự cuối cùng giống nhau --> True
print(k1)
k1=valid_pkcs7_padding(x2)      #vd: 7 kí tự cuối cùng khác nhau --> False
print(k1)
k1=valid_pkcs7_padding(x3)
print(k1)


# for KEYSIZE in range(2,41):
#     print(KEYSIZE)

def Convert_String_to_bit(input):       #Chuyển string -> bit (type = string)
    x1=""
    for i in input:
        x2=bin(ord(i))[2:]
        them_=8-len(x2)
        x2=them_*"0"+x2
        x1+=x2
    return x1
# x="this is a test"
# k=Convert_String_to_bit(x)
# print(k)

def Distance_Hamminng(input1,input2):   #Khoảng cách giữa 2 chuỗi
    dem=0
    input1=Convert_String_to_bit(input1)
    input2=Convert_String_to_bit(input2)
    for i1,i2 in zip(input1,input2):
        if i1 != i2:
            dem+=1
    return dem
x1="wokka wokka!!!"
x2="this is a test"
x=Distance_Hamminng(x1,x2)
print(x)


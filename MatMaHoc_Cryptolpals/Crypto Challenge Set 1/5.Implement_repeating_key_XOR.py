#HOÀN THÀNH

input_1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
n_ = len(input_1)

key ="ICE"
KEY_out = ""

dem=1
dem_key = 0
while dem <= n_:
    KEY_out+=key[dem_key]
    dem_key+=1
    if dem_key==3:
        dem_key=0
    dem+=1

z = zip(input_1,KEY_out)        #Lấy từng cặp kí tự của input_1 và input_2
output = [ord(i1)^ord(i2) for i1,i2 in z]   #Xor từng cặp kí tự

l=""                            #
for i in output:
    l+=hex(i)[2:]
print(l)



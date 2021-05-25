#xong

#Chuyen file .txt -> list -> string
data = open("data08.txt")
Data = data.read().split("\n")
input=''.join(Data)

#Index -> cat chuoi
index_l=[]
n_=len(input)
for i in range(0,n_,32):
    index_l.append(i)

#Cat chuoi 32kitu hex (128bit)
input_l=[]
for i in index_l:
    l_=input[i:i+32]
    input_l.append(l_)

#Tim chuoi bi lap lai (repeat) do mode ECB
n_=len(input_l)
max=0
k=0
for i in range(n_):
    dem=0
    j=i+1
    while j<n_:
        if input_l[i]==input_l[j]:
            dem+=1
        j+=1
    if dem>max:
        max=dem
        print(dem)
        print(i)
        k=i

print(max)
print(input_l[k])

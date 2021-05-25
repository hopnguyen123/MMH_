#xong
data = open("data06.txt")
Data=data.read()
list_row=Data.split("\n")

result=""
for i in list_row:
    i=i.split("+")
    for j in i:
        result+=j[0]*int(j[2:])
    result+="\n"

result=result.replace("0"," ")
result=result.replace("1","█")
print(result)
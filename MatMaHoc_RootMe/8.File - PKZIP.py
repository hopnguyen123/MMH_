#xong
import zipfile as zf
import itertools

def GiaiNen(file_):
    for i in itertools.product(range(10), repeat=5):   #tạo số từ 00000 -> 99999 (100.000 số )
        password = ''.join(map(str, i))                  #Chuyển từ tuple (1,2,3,4,5) -> string 12345
        PASS=bytes(password,'utf-8')                               #Chuyển từ string 12345 -> bytes b'12345'
        try:
            file_.extractall(pwd=PASS)
            return password
        except:
            pass


file = zf.ZipFile('ch5.zip')       #Để đọc và ghi file Zip
Password = GiaiNen(file)           #Giai nen file

if Password:
    print(Password)
else:
    print("Dont Crack")




#https://docs.python.org/3/library/zipfile.html
#https://stackoverflow.com/questions/33577116/zipfile-method-doesnt-works/43750441
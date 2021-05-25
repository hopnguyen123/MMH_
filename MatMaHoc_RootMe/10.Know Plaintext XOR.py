#xong
key = 'fallen'
keyLen = len(key)

fr = open('ch3.bmp','rb+')       #Mở file và đọc theo từng bytes
string = fr.read()
fr.close()

newstring = ""

for i in range(len(string)):     #Xor từng byte với key[index] tương ứng
 newstring += chr(string[i] ^ ord(key[i%keyLen]))

fw = open('ch3_out.png','wb+')   #Mở vào ghi theo từng bytes -> 1 picture
fw.write(newstring.encode(encoding="latin1"))
fw.close()
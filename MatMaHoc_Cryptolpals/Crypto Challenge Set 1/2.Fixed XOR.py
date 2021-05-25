#HOÀN THÀNH

#Chuyển string từ hex -> bytes
#Chuyển từng cụm 2 kí tự (string) -> hệ hex. VD '1c' type(string) -> 'ox1c' type(hex)
byte_string_1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
byte_string_2=bytes.fromhex('686974207468652062756c6c277320657965')

for b1, b2 in zip(byte_string_1, byte_string_2):  # Lấy từng cặp tương ứng xor với nhau
    x = b1 ^ b2
    print(hex(x)[2:], end='')  # Chuyển qua hex


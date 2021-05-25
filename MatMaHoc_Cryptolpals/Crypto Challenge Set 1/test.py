#bai 06
# l_base64_char=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
#                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
#                 '0','1','2','3','4','5','6','7','8','9','+','-']
#
# def Convert_base64_to_int(input_string):
#     chuoi = ""
#     n_ = len(l_base64_char)
#     for i in input_string:
#         for j in range(n_):
#             if (i == l_base64_char[j]):
#                 x = bin(j)[2:]
#                 n_x = len(x)
#                 them = 6 - n_x
#                 for i in range(them):
#                     x = "0" + x
#         chuoi += x
#     return chuoi
#
# def SoSanhChuoi(input_string1,input_string2):
#     n_=len(input_string1)
#     dem=0
#     for i in range(n_):
#         if(input_string1[i]!=input_string2[i]):
#             dem+=1
#     return dem

#Bài 6

x="BgBHVBwNRU0HBAxTEjwMHghJGgkRTxRMIRpHKwAFHUdZEQQJAGQmB1MANxYG"
print(len(x))

k="8a10247f90d0a05538888ad6205882196f5f6d05c21ec8dca0cb0be02c3f8b09e382963f443aa514daa501257b09a36bf8c4c392d8ca1bf4395f0d5f2542148c7e5ff22237969874bf66cb85357ef99956accf13ba1af36ca7a91a50533c4d89b7353f908c5a166774293b0bf6247391df69c87dacc4125a99ec417221b58170e633381e3847c6b1c28dda2913c011e13fc4406f8fe73bbf78e803e1d995ce4d"
print(len(k))
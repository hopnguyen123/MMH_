#xong
plaintext="YELLOW SUBMARINE"
dem=len(plaintext)
n_=20
so_bype_them=n_-dem

p1="\x04"
print(p1)
print(type(p1))
for i in range(so_bype_them):
    plaintext+=p1
print(plaintext)
#Thuật toán sinh d
#Câu a: p=11,q=3,e=3,M=4,d=27,c=31
# p=11
# q=3
# n=p*q
# e=3
# phi_n=(p-1)*(q-1)
# M=4
e=550
phi_n=1759
def Tim_d(e,phi_n):
    x1=0
    x2=1
    while(True):
        qi=phi_n//e
        ri=phi_n-e*qi
        if ri==0:
            return xi
        xi = x1 - (x2 * qi)
        phi_n=e
        e=ri
        x1=x2
        x2=xi


d=Tim_d(e,phi_n)
print("d: ",d)

x = input().split(" ")
a, b, c, d = x
A = int(x[0])
B = int(x[1])
C = int(x[2])
D = int(x[3])

if A % 2 == 0:
    P = True
if B > C and D > A and (C + D) > (A + B) and C >= 0 and D >= 0 and P == True:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

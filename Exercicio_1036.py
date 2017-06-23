import math

f = input().split(" ")
a, b, c = f
A = float(f[0])
B = float(f[1])
C = float(f[2])

delta = (B)**2 - (4*A*C)

while True:
    if A <= 0 or delta < 0:
        print("Impossivel calcular")
        break
    else:
        x1 = (-(B) + math.sqrt(delta))/(2*(A))
        x2 = (-(B) - math.sqrt(delta))/(2*(A))
        print("R1 = %.5f"%x1)
        print("R2 = %.5f"%x2)
        break

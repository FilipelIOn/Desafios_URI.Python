limit_overflow = int(input())
equ = input().split()

p, fun, q = int(equ[0]), equ[1], int(equ[2])

if fun == "+":
    result = p + q
else:
    result = p * q

if result <= limit_overflow:
    print("OK")
else:
    print("OVERFLOW")

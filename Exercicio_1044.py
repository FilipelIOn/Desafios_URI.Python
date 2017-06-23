num = input().split(" ")
a, b = num

a = int(a)
b = int(b)

if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

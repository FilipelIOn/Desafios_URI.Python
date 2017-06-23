num = input().split(" ")
a, b, c = num

a = int(a)
b = int(b)
c = int(c)
n = [a, b, c]

n.sort()
for numeros in n:
    print(numeros)
print("")
for numeros in num:
    print(numeros)

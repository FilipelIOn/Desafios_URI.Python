tri = input().split(" ")
a, b, c = tri

a = float(a)
b = float(b)
c = float(c)

y = [a, b, c]
y.sort(reverse = True)

a = y[0]
b = y[1]
c = y[2]

x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0

if a > 0 and b > 0 and c > 0:
    for i in range(2):
        if a >= (b + c) and (x1 == 0):
            print("NAO FORMA TRIANGULO")
            break
        elif (a)**2 == ((b)**2 + (c)**2) and (x2 == 0):
            print("TRIANGULO RETANGULO")
            x2 += 1
        elif (((a)**2) > ((b)**2 + (c)**2)) and (x3 == 0):
            print("TRIANGULO OBTUSANGULO")
            x3 += 1
        elif (((a)**2) < ((b)**2 + (c)**2)) and (x4 == 0):
            print("TRIANGULO ACUTANGULO")
            x4 += 1
        elif a == b == c and (x5 == 0):
            print("TRIANGULO EQUILATERO")
            x5 += 1
        elif (a == b or a == c or b == c) and (x6 == 0):
            print("TRIANGULO ISOSCELES")
            x6 += 1

import math
maior = input().split(" ")
a, b, c = maior
m1 = (int(a) + int(b) + abs(int(a) - int(b)))/2
m2 = (m1 + int(c) + abs(m1 - int(c)))/2
print("%d eh o maior"% m2)

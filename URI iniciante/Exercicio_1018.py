nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0
nota_1 = 0

x = int(input())

while True:
    if x > 100:
        x -= 100
        nota_100 += 1
    elif x > 50:
        x -= 50
        nota_50 += 1
    elif x > 20:
        x -= 20
        nota_20 += 1
    elif x > 10:
        x -= 10
        nota_10 += 1
    elif x > 5:
        x -= 5
        nota_5 += 1
    elif x > 2:
        x -= 2
        nota_2 += 1
    elif x > 1:
        x -= 1
        nota_1 += 1
    else:
        break
        
print(x)
print("%d nota(s) de R$ 100,00"%nota_100)
print("%d nota(s) de R$ 50,00"%nota_50)
print("%d nota(s) de R$ 20,00"%nota_20)
print("%d nota(s) de R$ 10,00"%nota_10)
print("%d nota(s) de R$ 5,00"%nota_5)
print("%d nota(s) de R$ 2,00"%nota_2)
print("%d nota(s) de R$ 1,00"%nota_1)

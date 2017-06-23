nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0
moeda_1 = 0
moeda_050 = 0
moeda_025 = 0
moeda_010 = 0
moeda_05 = 0
moeda_01 = 0

x = float(input())
if x >= 0 and x <= 1000000.00:
    while True:
        if x >= 100:
            x -= 100
            nota_100 += 1
        elif x >= 50:
            x -= 50
            nota_50 += 1
        elif x >= 20:
            x -= 20
            nota_20 += 1
        elif x >= 10:
            x -= 10
            nota_10 += 1
        elif x >= 5:
            x -= 5
            nota_5 += 1
        elif x >= 2:
            x -= 2
            nota_2 += 1
        elif x >= 1:
            x -= 1
            moeda_1 += 1
        elif x >= 0.5:
            x -= 0.5
            moeda_050 += 1
        elif x >= 0.25:
            x -= 0.25
            moeda_025 += 1
        elif x >= 0.10:
            x -= 0.10
            moeda_010 += 1
        elif x >= 0.05:
            x -= 0.05
            moeda_05 += 1
        elif x >= 0.01 or x >= 0.00999999999999:
            x -= 0.01 or 0.00999999999999
            moeda_01 += 1
        else:
            break


print("NOTAS:")
print("%d nota(s) de R$ 100.00"%nota_100)
print("%d nota(s) de R$ 50.00"%nota_50)
print("%d nota(s) de R$ 20.00"%nota_20)
print("%d nota(s) de R$ 10.00"%nota_10)
print("%d nota(s) de R$ 5.00"%nota_5)
print("%d nota(s) de R$ 2.00"%nota_2)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00"%moeda_1)
print("%d moeda(s) de R$ 0.50"%moeda_050)
print("%d moeda(s) de R$ 0.25"%moeda_025)
print("%d moeda(s) de R$ 0.10"%moeda_010)
print("%d moeda(s) de R$ 0.05"%moeda_05)
print("%d moeda(s) de R$ 0.01"%moeda_01)

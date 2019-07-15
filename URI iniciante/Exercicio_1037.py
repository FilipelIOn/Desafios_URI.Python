x = float(input())

while True:
    if x >= 0.0 and x <= 25.0:
        print("Intervalo [0,25]")
        break
    elif x > 25.0 and x <= 50.0:
        print("Intervalo (25,50]")
        break
    elif x > 50.0 and x <= 75.0:
        print("Intervalo (50,75]")
        break
    elif x > 75.0 and x <= 100.0:
        print("Intervalo (75,100]")
        break
    else:
        print("Fora de intervalo")
        break

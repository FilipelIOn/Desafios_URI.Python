c = input().split(" ")
x, y = c

X = float(x)
Y = float(y)

if X == 0.0 and Y == 0.0:
    print("Origem")
elif (X == 0.0 and Y > 0.0) or (X == 0.0 and Y < 0.0):
    print("Eixo Y")
elif (X > 0.0 and Y == 0.0) or (X < 0.0 and Y == 0.0):
    print("Eixo X")
elif X > 0.0 and Y > 0.0:
    print("Q1")
elif X < 0.0 and Y > 0.0:
    print("Q2")
elif X < 0.0 and Y < 0.0:
    print("Q3")
else:
    print("Q4")

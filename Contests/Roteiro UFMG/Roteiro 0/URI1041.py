coordinates = list(map(float, input().split()))

if coordinates[0] + coordinates[1] == 0.0:
    print("Origem")
elif (coordinates[0] == 0.0) and not (coordinates[1] == 0.0):
    print("Eixo Y")
elif (coordinates[1] == 0.0) and not (coordinates[0] == 0.0):
    print("Eixo X")

else:
    if coordinates[1] > 0.0:
        if coordinates[0] > 0.0:
            print("Q1")
        else:
            print("Q2")
    else:
        if coordinates[0] < 0.0:
            print("Q3")
        else:
            print("Q4")
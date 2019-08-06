def soma_letras(letra):
    soma = 0
    for i in letra:
        soma += x.find(i) + 1
    return soma

x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    try:
        palavra = input()
        num = soma_letras(palavra)
        p = [numeros for numeros in range(1, num + 1) if num % numeros == 0]
        if len(p) > 2:
            print("It is not a prime word.")
        else:
            print("It is a prime word.")

    except EOFError:
        break
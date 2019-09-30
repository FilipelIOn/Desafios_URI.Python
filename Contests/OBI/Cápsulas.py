n, f = map(lambda x: int(x), input().split())
coins = list(map(lambda x: int(x), input().split()))

d = 1
while True:
    x = 0
    for i in coins:
        x += int(d/i)

    if x >= f:
        break
    d += 1

print(d)
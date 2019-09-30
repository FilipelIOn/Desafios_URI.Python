n, f = map(lambda x: int(x), input().split())
cicles = list(map(lambda x: int(x), input().split()))
min_day, max_day = 1, 10**9

#binary search
while min_day < max_day:
    mid = int((max_day+min_day)/2)
    total = 0

    for i in cicles:
        total += int(mid/i)

    if total >= f:
        max_day = mid
    else:
        min_day = mid + 1
    print(min_day,max_day)

print(min_day)
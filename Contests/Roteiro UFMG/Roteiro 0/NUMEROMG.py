def baseconvert(n):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    n = int(n)
    s = ""
    while int(n) > 0:
        r = n % 36
        s = digits[int(r)] + s
        n = n / 36

    return s

while True:
    num = input().split()
    if (num[0] and num[1]) == "0":
        break
    else:
        num = int(num[0], 36) + int(num[1],36)
        print(baseconvert(num))
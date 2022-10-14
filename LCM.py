a, b = map(int, input().split()) # 17 997
x = max(a, b)
i = 1
while True:
    m = x * i # 17 * 1 -> 17
    if m%a == 0 and m % b == 0:
        print(m)
        break
    i += 1
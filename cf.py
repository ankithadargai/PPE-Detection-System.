for i in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    x.append(1)
    m = []
    for i in range(n):
        cp = a[i] % k
        if not cp and len(x):
            a[i] = k
        else:
            a[i] = cp
        if len(x):
            m.append((a[i], -i))
    m.sort(reverse=True)
    for y in m:
        k = y[1]
        k = -k
        k += 1
        print(k, end=" ")
    print()
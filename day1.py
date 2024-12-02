with open("day1data.txt", 'r') as f:
    data = f.read().splitlines()
    a = []
    b = []
    total = 0
    for line in data:
        i, j = line.split()
        a.append(int(i))
        b.append(int(j))
    a.sort()
    b.sort()
    for i in range(len(a)):
        total += abs(a[i] - b[i])
    print(total)
        
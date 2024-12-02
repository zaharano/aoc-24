with open("day1data.txt", 'r') as f:
    data = f.read().splitlines()
    a = []
    b = []
    for line in data:
        i, j = line.split()
        a.append(int(i))
        b.append(int(j))
    a.sort()
    b.sort()
    similarity = 0
    for i in range(len(a)):
        similarity += b.count(a[i]) * a[i]
    print(similarity)
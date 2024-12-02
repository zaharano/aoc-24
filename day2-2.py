safe = 0
TOLERANCE = 1

def diffs(r):
    if len(r) < 2:
        return []
    return [r[1] - r[0]] + diffs(r[1:])

def test_consistency(diffs, fails, dir):
    if diffs == []:
        return True
    if diffs[0] * dir <= 0:
        fails += 1
        if fails > TOLERANCE:
            return False           
    else:
        return test_consistency(diffs[1:], fails, dir)


with open("day2data.txt", 'r') as f:
    data = f.read().splitlines()
    for line in data:
        report = line.split()
        report = [int(num) for num in report]
        if test_consistency(diffs(report), 0, 1) or test_consistency(diffs(report), 0, -1):
            safe += 1


print("Safe: " + str(safe))
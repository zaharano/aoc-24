safe = 0
TOLERANCE = 1

def diffs(r):
    if len(r) < 2:
        return []
    return [r[1] - r[0]] + diffs(r[1:])

def test_consistency(report, diffs, fails, dir):
    if diffs == []:
        return True
    if diffs[0] * dir <= 0 or diffs[0] * dir > 3:
        fails += 1
        if fails > TOLERANCE:
            return False
        else: 
            return test_consistency(report, diffs[1:], fails, dir)
    else:
        return test_consistency(report, diffs[1:], fails, dir)


with open("day2data-test.txt", 'r') as f:
    data = f.read().splitlines()
    for line in data:
        report = [int(num) for num in line.split()]
        if test_consistency(report, diffs(report), 0, 1) or test_consistency(report, diffs(report), 0, -1):
            safe += 1
            print(diffs(report), " success")
        else:
            print(diffs(report), " fail")


print("Safe: " + str(safe))
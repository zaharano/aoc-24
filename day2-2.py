safe = 0
# TOLERANCE = 1
# was close with doing this the elegant way but just way too much easier to do it the brute

def get_diffs(r):
    if len(r) < 2:
        return []
    return [r[1] - r[0]] + get_diffs(r[1:])

def test(diffs, dir):
    if diffs == []:
        return True
    if diffs[0] * dir <= 0 or diffs[0] * dir > 3:
        return False
    else:
        return test(diffs[1:], dir)


with open("day2data.txt", 'r') as f:
    data = f.read().splitlines()
    for line in data:
        report = [int(num) for num in line.split()]
        if len(report) <= 0:
            continue
        diffs = get_diffs(report)
        print(diffs)
        if test(diffs, 1) or test(diffs, -1):
            safe += 1
            continue
        for i in range(len(report)):
            damp_report = report[:i] + report[i+1:]
            diffs = get_diffs(damp_report)
            if test(diffs, 1) or test(diffs, -1):
                safe += 1
                break
            
        
print("Safe: " + str(safe))
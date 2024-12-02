safe = 0

def test(direction, r):
  if len(r) < 2:
    return True
  if direction == 0:
    if r[0] > r[1]:
      direction = -1
    elif r[0] < r[1]:
      direction = 1
    else:
      return False
  diff = (r[1] - r[0]) * direction
  if diff < 1 or diff > 3:
    return False
  return test(direction, r[1:])

with open("day2data.txt", 'r') as f:
    data = f.read().splitlines()
    for line in data:
        report = line.split()
        report = [int(num) for num in report]
        if test(0, report):
            safe += 1


print("Safe: " + str(safe))
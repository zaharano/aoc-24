SEARCH = "XMAS"

p = []

with open("day4data.txt", 'r') as f:
    data = f.read().splitlines()
    for line in data:
      row = []
      for c in line:
        row.append(c)
      p.append(row)

w = len(p[0])
h = len(p)

# reverse the x and y of the matrix to fit x, y coordinates
p = list(map(list, zip(*p)))

def check_bounds(x, y):
  if x < 0 or x >= w:
    return False
  if y < 0 or y >= h:
    return False
  return True

def find_directions(x, y):
  directions = []
  for i in range(-1, 2):
    for j in range(-1, 2):
      if i == 0 and j == 0:
        continue
      if check_bounds(x + i, y + j):
        if p[x + i][y + j] == SEARCH[1]:
          directions.append((i, j))
  return directions

def check_remaining(x, y, d):
  for i in range(2, len(SEARCH)):
    if not check_bounds(x + d[0] * i, y + d[1] * i):
      return False
    if p[x + d[0] * i][y + d[1] * i] != SEARCH[i]:
      return False
  return True

def search():
  count = 0
  for i in range(w):
    for j in range(h):
      if p[i][j] == SEARCH[0]:
        directions = find_directions(i, j)
        if directions != []:
          for d in directions:
            if check_remaining(i, j, d):
              count = count + 1
  print(count)
    
search()
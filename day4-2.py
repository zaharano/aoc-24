p = []

# just realized that because of how strings work in python, I don't need lists. oh well.
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

def check_space(x, y):
  if x > 0 and x < w - 1 and y > 0 and y < h - 1:
    return True

# the range is comically useless here oh well
def check_MAS(x, y):
  for i in [-1, 1]:
    for j in [-1, 1]:
      if p[x + i][y + j] == "M":
        if p[x - i][y - j] == "S":
          if p[x + i][y - j] == "M":
            if p[x - i][y + j] == "S":
              return True
          if p[x - i][y + j] == "M":
            if p[x + i][y - j] == "S":
              return True
  return False

def search():
  count = 0
  for i in range(w):
    for j in range(h):
      if p[i][j] == "A" and check_space(i, j):
        if check_MAS(i, j):
          count = count + 1
  print(count)

search()
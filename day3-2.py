import re

total = 0
cursor = 0
enabled = True
MUL_EXP = r'mul\(\d{1,3},\d{1,3}\)'
DO_EXP = r'do\(\)'
DO_NOT_EXP = r'don\'t\(\)'

with open("day3data.txt", 'r') as f:
  data = f.read()
  
  while True:
    search = re.search("|".join([MUL_EXP, DO_EXP, DO_NOT_EXP]), data)
    print(search)
    if search is None:
      break
    if search.group().startswith('mul') and enabled:
      s = search.group().replace('mul(', '').replace(')', '')
      s = s.split(',')
      val = int(s[0]) * int(s[1])
      total += val
    elif search.group().startswith('don'):
      print('don\'t')
      enabled = False
    elif search.group().startswith('do'):
      print('do')
      enabled = True

    data = data[search.end():]

print(total)
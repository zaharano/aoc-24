import re

total = 0

with open("day3data.txt", 'r') as f:
  search = re.findall(r'mul\(\d{1,3},\d{1,3}\)', f.read())
  for s in search:
    s = s.replace('mul(', '').replace(')', '')
    s = s.split(',')
    val = int(s[0]) * int(s[1])
    total += val

print(total)
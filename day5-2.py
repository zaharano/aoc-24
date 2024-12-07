f = open("day5-data-rules.txt", 'r')
data = f.read().strip().splitlines()
f.close()

rules = []
for line in data:
    rules.append(line.split("|"))

f = open("day5-data-updates.txt", 'r')
data = f.read().strip().splitlines()
f.close()

updates = []
for line in data:
    updates.append(line.split(","))

def check_rule(rule, update):
    if all(page in update for page in rule):
        return update.index(rule[0]) < update.index(rule[1])
    return True

def check_update(update):
    for rule in rules:
        if not check_rule(rule, update):
            return False
    return True

bad_updates = []
for update in updates:
  if not check_update(update):
    bad_updates.append(update)

def merge_sort(array):
  if len(array) == 1:
    return array
  left = merge_sort(array[:round(len(array) / 2)])
  right = merge_sort(array[round(len(array) / 2):])
  return merge(left, right)

def merge(left, right):
  result = []
  left_index = 0
  right_index = 0
  while left_index < len(left) and right_index < len(right):
    if check_update([left[left_index], right[right_index]]):
      result.append(left[left_index])
      left_index += 1
    else:
      result.append(right[right_index])
      right_index += 1
  result += left[left_index:]
  result += right[right_index:]
  return result

corrected_updates = []

def correct_update(update):
  return merge_sort(update)
  
for update in bad_updates:
  corrected_updates.append(correct_update(update))

total = 0
for update in corrected_updates:
  middle = int(len(update) / 2)
  total += int(update[middle])

print(total)




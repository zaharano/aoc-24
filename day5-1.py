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

correct_updates = []
for update in updates:
    if check_update(update):
        correct_updates.append(update)

total = 0
for update in correct_updates:
  # this needs to round up by 8.5 = 8 in this fakakta lang
  # maybe it's fine though
  middle = int(len(update) / 2)
  total += int(update[middle])

print(total)
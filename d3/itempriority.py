import string
from collections import defaultdict

sample = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

def def_val():
  return 0

def get_compartments(s):
  split_ind = int(len(s) / 2)
  return s[0:split_ind], s[split_ind:len(s)]

def get_item_counts(compartment):
  counts = defaultdict(def_val)
  for item in compartment:
    counts[item] += 1
  return counts

lower_priorities = {letter: i for i, letter in enumerate(string.ascii_lowercase, start=1)}
upper_priorities = {letter: i for i, letter in enumerate(string.ascii_uppercase, start=27)}
PRIORITIES = lower_priorities | upper_priorities

def get_item_priority(item):
  return PRIORITIES[item]

GROUP_LEN = 3

f_rucksacks = open('rucksacks.txt', 'r').read()

total_sum = 0
rucksacks = f_rucksacks.split('\n')
for i in range(0, len(rucksacks), GROUP_LEN):
  group = rucksacks[i:i+GROUP_LEN]
  items = [set(rucksack) for rucksack in group]

  badge_set = items[0]
  for item in items[1:]:
    badge_set = badge_set.intersection(item)
  
  badge = list(badge_set)[0]
  total_sum += get_item_priority(badge)

print(total_sum)



# print(total_sum)






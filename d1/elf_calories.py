class Elf():

  def __init__(self, inventory):
    self.inventory = inventory
    self.total_calories = sum(self.inventory)

  def get_total_calories(self):
    return self.total_calories

f = open("elf_inventory.txt", "r")
elf_inventories = f.read().split('\n\n')

elfs = []
for inventory_str in elf_inventories:
  inventory = [int(calories) for calories in inventory_str.split('\n')]
  elfs.append(Elf(inventory))

elfs.sort(key=lambda x: x.total_calories, reverse=True)

#part 1
print(elfs[0].get_total_calories())

#part 2
print(sum([elf.get_total_calories() for elf in elfs[0:3]]))

  
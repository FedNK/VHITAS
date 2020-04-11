import random

print("Введите количество символов списка")
Amount = int(input())
NumbersList = list()
for i in range(Amount):
  RandomNumber = random.randint(0, 100)
  NumbersList.append(RandomNumber)
print(NumbersList)
for Element in NumbersList:
  if not Element % 2 == 0:
    NumbersList.remove(Element)
print(NumbersList)
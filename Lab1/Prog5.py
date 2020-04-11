from math import sqrt

print("Введите число:")
Num = int(input())
Sum = 0
for i in range(Num - 1):
  Rez = False
  i = i + 2
  KvKoren = int(sqrt(i))
  d = 2
  while d <= KvKoren:
    if i % d == 0:
      Rez = True
      break
    d = d + 1
  if Rez == False:
    Sum = Sum + i
print(Sum)
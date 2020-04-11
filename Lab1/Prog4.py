print("Введите число: ")
Num = int(input())
Sum = 0
for i in range(Num):
  i = i + 1
  if i % 10 == 3:
    Sum = Sum + i
print("Сумма чисел заканчивающихся на 3: " + str(Sum))
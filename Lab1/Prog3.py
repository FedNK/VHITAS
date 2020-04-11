print("Введите ваш возраст:")
Years = int(input())
print("Введите ваш пол (м/ж):")
Sex = input()
if Sex == "м":
  Result = 65 - Years
else:
  Result = 60 - Years
if Result > 0:
  print("Лет до пенсии: " + str(Result))
elif Result == 0:
  print("В этом году вы выходите/вышли на пенсию")
else:
  print("Вы уже вышли на пенсию")
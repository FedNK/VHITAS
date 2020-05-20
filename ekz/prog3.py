print("Введите данные: ")
stroka = input()
otkr = stroka.count("(")
zakr = stroka.count(")")
if otkr == zakr:
  print("Количество скобок сбалансировано")
elif otkr > zakr:
  print("Открывающих скобок больше на " + str(otkr - zakr))
else:
  print("Закрывающих скобок больше на " + str(zakr - otkr))
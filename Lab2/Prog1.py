print("Добавьте элементы списка (end - закончить ввод)")
Spisok = list()
Result = ""
i = 0
LastElement = False
while LastElement == False:
  NewValue = input()
  if not NewValue == "end":
   Spisok.append(NewValue)
  else:
    LastElement = True
    for Element in Spisok:
      if i % 2 == 0 and not i == 0:
        Result = Result + Element + " "
      i = i + 1
    print(Result)
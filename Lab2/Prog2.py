print("Добавьте элементы списка (end - закончить ввод)")
Spisok = list()
LastElement = False
while LastElement == False:
  NewValue = input()
  if not NewValue == "end":
   Spisok.append(NewValue)
  else:
    LastElement = True
    for Element in reversed(Spisok):
        print(Element)
print("Введите фамлию: ")
fam = input()
print("Введите имя: ")
name = input()
print("Введите отчество: ")
otch = input()
famcount = 0
namecount = 0
otchcount = 0
for letter in fam:
  if letter.lower() in "аоэиуыеёюя":
    famcount = famcount + 1
for letter in name:
  if letter.lower() in "бвгджзйклмнпрстфхцчшщ":
    namecount = namecount + 1
for letter in otch:
   otchcount = otchcount + 1
multiplied = famcount * namecount * otchcount
print(str(multiplied % 10 + 1))
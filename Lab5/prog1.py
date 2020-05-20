file = open("text.txt")
stramount = 0
for line in file:
    if not len(line) == 1:
        stramount = stramount + 1
        print(line)
print("Количество непустых строк: " + str(stramount))

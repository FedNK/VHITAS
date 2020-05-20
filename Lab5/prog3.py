import csv
with open('numbers.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    numberslist = list()
    for row in spamreader:
        row.append(str(int(row[0]) + int(row[1])))
        numberslist.append(row)
file = open("numbers.csv", "w")
for row in numberslist:
    for numbers in row:
        file.write(str(numbers) + ";")
    file.write("\n")
file.close()

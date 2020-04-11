from math import sqrt

print("Введите x координату 1 точки: ")
FirstPointX = int(input())
print("Введите y координату 1 точки: ")
FirstPointY = int(input())
print("Введите x координату 2 точки: ")
SecondPointX = int(input())
print("Введите y координату 2 точки: ")
SecondPointY = int(input())
Data = tuple()
Data = (FirstPointX, FirstPointY, SecondPointX, SecondPointY)
Distanse = round(sqrt((Data[2] - Data[0])**2 + (Data[3] - Data[1])**2), 2)
print(Distanse)
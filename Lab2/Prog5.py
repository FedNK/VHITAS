FirstDict = dict()
SecondDict = dict()

FirstDict["key1"] = "abc"
FirstDict["key2"] = "qwerty"

SecondDict["key1"] = "abc"
SecondDict["key2"] = "qwerty"

Items1 = FirstDict.items()
Items2 = SecondDict.items()
#print(Items1)
#print(Items2)
if Items1 == Items2:
  print("Словари равны")
else:
  print("Словари не равны")
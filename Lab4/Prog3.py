class Train:
  Loco = ""
  Vagons = list()
  def __init__(self, TrainType):
    self.TrainType = TrainType
 
  def SetLoco(self, Loco):
    self.Loco = Loco

  def AddVagon(self, VagonName):
    self.Vagons.append(VagonName)

  def __str__(self):
    AllVagons = ""
    for element in self.Vagons:
      AllVagons = AllVagons + str(element)
    return str(self.Loco) + AllVagons

class Locomotiv:
  def __init__(self, LocomotivType):
    self.LocomotivType = LocomotivType
  def __str__(self):
    if self.LocomotivType == "Паровоз":
     return "(==ТТ"
    elif self.LocomotivType == "Электровоз":
      return "/\/\ТТ"
    else:
      return "ooТТ"

class Vagon:
  def __init__(self, VagonType):
    self.VagonType = VagonType
  def __str__(self):
    if self.VagonType == "Пассажирский":
     return "•(_ _)"
    elif self.VagonType == "Товарный":
      return "•[_ _]"

Train1 = Train("Пассажирский поезд")

Locomotiv1 = Locomotiv("Паровоз")
Train1.SetLoco(Locomotiv1)

Vagon1 = Vagon("Пассажирский")
Train1.AddVagon(Vagon1)

print(Train1)
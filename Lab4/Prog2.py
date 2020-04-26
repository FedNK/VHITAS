class Train:
  Loco = ""
  Vagons = list()
  def __init__(self, TrainType):
    self.TrainType = TrainType
 
  def SetLoco(self, Loco):
    self.Loco = Loco

  def AddVagon(self, VagonName):
    self.Vagons.append(VagonName)

  def Run(self):
    TotalMass = 0
    for element in self.Vagons:
      TotalMass = TotalMass + element.VagonMass
    if self.Loco.MaxMass >= TotalMass:
      print("Ок")
    else:
      print("Масса поезда больше, чем может везти локомотив")

class Locomotiv:
  def __init__(self, LocomotivType, MaxMass):
    self.LocomotivType = LocomotivType
    self.MaxMass = MaxMass

class Vagon:
  def __init__(self, VagonType, VagonMass):
    self.VagonType = VagonType
    self.VagonMass = VagonMass

Train1 = Train("Пассажирский поезд")

Locomotiv1 = Locomotiv("Паровоз", 70)
Train1.SetLoco(Locomotiv1)

Vagon1 = Vagon("Пассажирский", 20)
Train1.AddVagon(Vagon1)

Train1.Run()
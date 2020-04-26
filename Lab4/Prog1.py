class Train:
  Loco = ""
  Vagons = list()
  def __init__(self, TrainType):
    self.TrainType = TrainType
 
  def SetLoco(self, Loco):
    self.Loco = Loco

  def AddVagon(self, VagonName):
    self.Vagons.append(VagonName)

class Locomotiv:
  def __init__(self, LocomotivType):
    self.LocomotivType = LocomotivType

class Vagon:
  def __init__(self, VagonType):
    self.VagonType = VagonType

Train1 = Train("Пассажирский поезд")

Locomotiv1 = Locomotiv("Паровоз")
Train1.SetLoco(Locomotiv1)

Vagon1 = Vagon("Пассажирский")
Train1.AddVagon(Vagon1)

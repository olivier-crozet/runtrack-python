class Personne:
  def __init__(self, name, prenom):
    self.name = name
    self.prenom = prenom

  def Sepresenter(self):
    print("Hello my name is " + self.name + " " + self.prenom)

obj1 = Personne("John","enculer")
obj1.Sepresenter()





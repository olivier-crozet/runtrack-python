class Personne:
  def __init__(self, name, prenom):
    self.name = name
    self.prenom = prenom

  def myfunc(self):
    print("Hello my name is " + self.name + " " + self.prenom)

p1 = Personne("John","enculer")
p1.myfunc()





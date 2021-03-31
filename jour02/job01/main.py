class Personne:
  def __init__(self, name, prenom):
    self.name = name
    self.prenom = prenom

  def sepresenter(self):
    print("Hello my name is " + self.name + " " + self.prenom)

  def get_name(self):
    return(self.name +" "+ self.prenom)
    

  def set_name(self, name, prenom):
    self.name = name
    self.prenom = prenom

obj1 = Personne("toto","coco")

obj1.set_name("mimi", "mumu")
print(obj1.get_name())


from Actions import *


class GameObject:
  class_name = ""
  desc = ""
  objects = {}
  characters = {}
  count = 0
  

  def __init__(self, name):
    print('Another character has appeared')
    self.alive = True
    self.name = name
    self._health = 3
    GameObject.objects[self.name] = self
    GameObject.characters[self.name] = self.class_name
    GameObject.count += 1

  def get_desc(self):
    return self.desc

  @property
  def health(self):
    return self._health

  @health.setter
  def health(self, value):
    self._health = value

class Goblin(GameObject):
  def __init__(self, name):
    self.class_name = "goblin"
    self._health = 3
    self.strength = 6
    self._desc = "A foul creature"
    super().__init__(name)

  @property
  def desc(self):
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "{} has a wound on their knee.".format(self.name)
    elif self.health == 1:
      health_line = "{}'s left arm has been cut off!".format(self.name)
    elif self.health <= 0:
      health_line = "{} is dead.".format(self.name)
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
    self._desc = value


class Witch(GameObject):
  def __init__(self, name):
    self.class_name = "witch"
    self._health = 3
    self.strength = 7
    self._desc = "An olf crone"
    super().__init__(name)
    
  @property
  def desc(self):
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "{} has a broken nose.".format(self.name)
    elif self.health == 1:
      health_line = "{}'s ear is missing".format(self.name)
    elif self.health <= 0:
      health_line = "{} is dead.".format(self.name)
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
    self._desc = value

  @desc.deleter
  def desc(self):
    del self._desc 

class Knight(GameObject):
  def __init__(self, name):
    self.class_name = "knight"
    self._health = 3
    self.strength = 10
    self._desc = "The hero in our story"
    super().__init__(name)
 
  @property
  def desc(self):
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "{} has a cut accross the chest.".format(self.name)
    elif self.health == 1:
      health_line = "{}'s hand has been chopped off".format(self.name)
    elif self.health <= 0:
      health_line = "{} is dead.".format(self.name)
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
    self._desc = value

  @desc.deleter
  def desc(self):
    del self._desc

def test():


  a = Goblin('Rupert')
  print(say('Hello'))
  print(list())
  print(hit(a))
  print(examine(a))
  print(create('goblin'))
  Witch("Matilda")
  Knight("Rupert")
  Goblin("Gobbly")
  Goblin("Bob")
  print(health(a))


    


if __name__=='__main__': test()

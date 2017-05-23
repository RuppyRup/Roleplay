
class GameObject:
  class_name = ""
  desc = ""
  objects = {}
  characters = {}
  count = 0

  def __init__(self, name):
    self.name = name
    GameObject.objects[self.name] = self
    GameObject.characters[self.name] = self.class_name
    GameObject.count += 1

  def get_desc(self):
    return self.class_name + "\n" + self.desc

class Goblin(GameObject):
  def __init__(self, name):
    self.class_name = "goblin"
    self.health = 3
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

  @desc.deleter
  def desc(self):
    del self._desc

class Witch(GameObject):
  def __init__(self, name):
    self.class_name = "witch"
    self.health = 3
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
    self.health = 3
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

def get_input():
  command = input(": ").split()
  try:
      verb_word = command[0]
  except:
      return
    
  if verb_word in verb_dict:
    verb = verb_dict[verb_word]
  else:
    print("Unknown verb {}". format(verb_word))
    return

  if len(command) >= 2:
    noun_word = command[1]
    print(verb(noun_word))
  elif command[0] == 'exit':
    print('closing down')
    close()
  else:
    print(verb("nothing"))

def say(noun):
  return 'You said "{}"'.format(noun)

def examine(noun):
  if noun in GameObject.characters:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)

def list_(noun):
      for k, v in GameObject.characters.items():
          print("{} is a {}".format(k,v))
      return '\n'
    #GameObject.objects[noun].get_desc()


def create(noun):
  new_character = noun + str(GameObject.count + 1)
  name = input("input {} name: ".format(new_character))
  if name in GameObject.characters:
      return '{} already exists'.format(name)

  if noun == 'witch':
      Witch(name)
      return "{} is now a witch".format(name)
  elif noun == 'knight':
      Knight(name)
      return "{} is now a knight".format(name)
  elif noun == 'goblin':
      Goblin(name)
      return "{} is now a goblin".format(name)
  else:
      return('Character type doesn\'t exist')

def health(noun):
  if noun in GameObject.characters:
    return GameObject.objects[noun].health
  else:
    return "There is no {} here.".format(noun)   

def whatis(noun):
  if noun in GameObject.characters:
    return GameObject.characters[noun]
  else:
    return "There is no {} here.".format(noun)

def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    #if type(thing) == Goblin:
    thing.health = thing.health - 1
    if thing.health <= 0:
      msg = "You killed {}".format(thing.name)
    else: 
      msg = "You hit {}".format(thing.name)
  else:
    msg ="There is no {} here.".format(noun) 
  return msg

def close():
  global closing
  closing = True

verb_dict = {
  "say": say,
  "examine" :examine,
  "whatis" : whatis,
  "exit" : close,
  "create" : create,
  "health" : health,
  "list" : list_,
  "hit" : hit
}

#def main():

closing = False #needs to be global

Witch("Matilda")
Knight("Rupert")
Goblin("Gobbly")
Goblin("Bob")
    
while not closing:
  get_input()

#if __name__=='__main__': main()

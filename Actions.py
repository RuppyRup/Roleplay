
from game_objects import *


def hit(character_object):
    character_object.health -= 1
    if character_object.health > 0:
        return 'You hit {}'.format(character_object.name)
    else:
        character_object.alive = False
        return 'You killed {}'.format(character_object.name)
        

def kill(character_object):
    character_object.alive = False
    #del character_object
    return 'You killed {}'.format(character_object.name)

def alive(character_object):
    return '{} alive is {}'.format(character_object.name, character_object.alive)

def say(noun):
    return 'You said {}'.format(noun)

def examine(character_object):
    description = character_object.get_desc()
    if character_object.alive == False:
        return'{} is Dead'.format(character_object.name)
    elif character_object.alive == True:
        return '{} is a {} \n{}\nHealth: {}'.format(character_object.name, character_object.class_name,
                                    description, character_object.health)
    else:
        return'{} has never existed'.format(character_object.name)

def create(new_object):
    player = new_object.lower()
    name = input('Input name for new character: ')
    print(new_object)
    if player == 'witch':
        print('creating new {}'.format(player))
        Witch(name)
        return '{} is now an witch'.format(name)
    elif player == 'knight':
        print('creating new {}'.format(player))
        Knight(name)
        return '{} is now an knight'.format(name)
    elif player == 'goblin':
        print('creating new {}'.format(player))
        Goblin(name)
        return '{} is now an goblin'.format(name)
    else:
        return 'Not a character'
    
def list_():
    for k, v in GameObject.characters.items():
        print('{} is a {}'.format(k,v))
    return 'Finished'
    
def health(character_object):
    character_object.health += 1
    return 'You gave {} some more health'.format(character_object.name)

def test():

  a = Goblin('Rupert')
  print(hit(a))
  print(examine(a))
  print(health(a))
  print(create('knight'))
  print(say('Hello'))
  print(list_())
  print(kill(a))
  print(examine(a))
  print(alive(a))

    


if __name__=='__main__': test()

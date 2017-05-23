
from Actions import *
from game_objects import *
from random import randint, choice



def close():
    global closing
    closing = True

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
    noun = command[1]
    if noun in GameObject.objects:
        if not GameObject.objects[noun].alive:
            print('{} is dead'.format(noun))
            return
        else:
            print(verb(GameObject.objects[noun]))
    else:
      print(verb(noun))
  elif command[0] == 'close':
    print('closing down')
    close()
  elif command[0] == 'list':
    print('Characters:')
    list_()
  else:
    print(verb("nothing"))

  if randint(0,9) >= 7:
      
      character_list = []
      for k in GameObject.characters.keys():
          character_list.append(k)
          
      random_verb = choice(action_list)
      random_character = choice(character_list)
      verb = verb_dict[random_verb]
      print('Ubuntu>>>{} {}'.format(random_verb, random_character))
      print(verb(GameObject.objects[random_character]))
  

verb_dict = {
  "say": say,
  "examine" :examine,
  "close" : close,
  "create" : create,
  "health" : health,
  "list" : list_,
  "hit" : hit,
  "kill" : kill,
  "alive" : alive
}

action_list = ['hit', 'examine', 'health', 'examine', 'hit', 'kill', 'health',]

closing = False #needs to be global



Witch("Matilda")
Knight("Rupert")
Goblin("Gobbly")
Goblin("Bob")


while not closing:
  get_input()
  



#def main():

#  a = Knight('Rupert')
#  b = Goblin("Gobbly")
#  print(say('Hello'))
#  print(list())
#  print(hit(a))
#  print(examine(a))
#  print(examine(b))
#  print(create('witch'))
#  print(list_())


    


#if __name__=='__main__': main()

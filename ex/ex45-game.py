from sys import exit
from random import randint


class Scene(object):

   def enter(self):
      print "This scene is not yet configured. Subclass it and implement enter()."
      exit(1)


class Engine(object):

   def __init__(self, scene_map):
      self.scene_map = scene_map

   def play(self):
      current_scene = self.scene_map.opening_scene()

      while True:
         print "\n----------"
         next_scene_name = current_scene.enter()
         current_scene = self.scene_map.next_scene(next_scene_name)

class Liberation(Scene):

   quips = [
         "Your body dissolves and you enter the pure realm of Shambhala.",
         "The entirety of society realizes its basic goodness.",
         "You awaken to the wisdom with which you were born."
   ]

   def enter(self):
      print Liberation.quips[randint(0, len(self.quips)-1)]
      return 'finished'

class Finished(Scene):

   def enter(self):
      exit(1)

class Samsara(Scene):

   def __init__(self):
      self.count = 0

   def enter(self):
      if self.count == 0:
         print "Your life is filled with suffering."

      else: 
         print "Your life is still filled with suffering."

      self.count += 1
      print "You can party, meditate, or gain merit."  
      print "What do you do?"

      action = raw_input("> ")

      if action == "party":
         print "You party.  It seems awesome for a time, but it only results in pain."
         return 'non_virtue'

      elif action == "meditate":
         print "Your samadhi strengthens and you achieve greater peace."
         return 'wisdom'

      elif action == "gain merit":
         print "You benefit beings and your virtue increases."
         return 'virtue'

      else:
         print "You're speaking in tongues. Try again."
         return 'samsara'

class NonVirtue(Scene):

   def enter(self):
      return 'samsara'

class Wisdom(Scene):

   def enter(self):
      return 'liberation'

class Virtue(Scene):

   def enter(self):
      return 'liberation'

class Map(object):

   scenes = {
      'non_virtue' : NonVirtue(),
      'wisdom' : Wisdom(),
      'virtue' : Virtue(),
      'samsara' : Samsara(),
      'liberation' : Liberation(),
      'finished' : Finished()
   }

   def __init__(self, start_scene):
      self.start_scene = start_scene

   def next_scene(self, scene_name):
      return Map.scenes.get(scene_name)

   def opening_scene(self):
      return self.next_scene(self.start_scene)

a_map = Map('samsara')
a_game = Engine(a_map)
a_game.play()


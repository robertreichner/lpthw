 
def scan(stuff):
   return Scanner().scan(stuff)

class Scanner(object):

   def __init__(self):
      self.directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 
                         'right', 'back']
      self.verbs = ['go', 'stop', 'kill', 'eat']
      self.stops = ['the', 'in', 'of', 'from', 'at', 'it']
      self.nouns = ['door', 'bear', 'princess', 'cabinet']


   def scan(self,stuff):
      words = stuff.split()
      results = []
      while (len(words) > 0): 
         lookup_word = words.pop(0)
         if lookup_word in self.directions:
            results.append(('direction', lookup_word))
         elif lookup_word in self.verbs:
            results.append(('verb', lookup_word))
         elif lookup_word in self.stops:
            results.append(('stop', lookup_word))
         elif lookup_word in self.nouns:
            results.append(('noun', lookup_word))
         elif isinstance(lookup_word, int): 
            results.append(('number', lookup_word))
         else:
            results.append(('error', lookup_word))
            
      return results




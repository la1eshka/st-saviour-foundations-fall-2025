
class Bunny:
    def __init__(self, name: str, tail: bool, color: str):
        self.name = name 
        self.color = color
        self.tail = tail
        self.legs = 4

    #TODO what does horrible accident do?
    def horrible_accident(self) -> str:
        if self.legs <= 0:
           return f'You\'ve broken all your legs!'
        else :
          self.legs -= 1
          return f'{self.name} the {self.color} bunny was in a horrible accident and now has {self.legs} legs left!'
        
if __name__ == '__main__':
   baloo = Bunny('Baloo', True, 'brown')
   print(baloo.horrible_accident())

   bugs = Bunny('Bugs', True, 'gray and white')
   print(bugs.horrible_accident())

   
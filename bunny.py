
class Bunny:
    def __init___(self, name: str, tail: str, color: bool):
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
          return f'The {self.color} bunny was in a horrible accident and now has {self.legs} left!'

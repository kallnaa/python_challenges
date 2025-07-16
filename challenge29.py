#Create a class Ghost, Ghost objects are instantiated without any arguments.
#Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

import random 
class Ghost(object):
   colors=["white","yellow","purple","red"] #create a list of all our available colours
   def __init__(self): #create our constructor
        self.color=random.choice(self.colors) #initialize our ghost's color with a random pick from the list of our available colors
g=Ghost() #calls the constructor
print(g.color) #prints the color

from transition import *

class State:
    def __init__(self, id, mode = ''):
        self.id = id
        self.mode = mode
        self.transition = None

    def setTransition(self, transition):
        self.transition = transition

    def process(self, character):
        proceed = self.transition.process(character)
        if proceed:
            return proceed
        elif proceed == None and self.getMode() == 'final':
            print("Saida = {}".format(character))

    def getMode(self):
        return self.mode

    def getId(self):
        return self.id

    def getTransition(self):
        if self.transition:
            return self.transition
        else:
            return self.getId()

    def __str__(self):
        return str(self.getId())+':'+self.getMode()
    

from transition import *

class State:
    def __init__(self, id, mode = 0):
        self.id = id
        self.mode = mode
        self.transitions = []

    def setTransition(self, transition):
        self.transitions.append(transition)

    def process(self, character):
        proceed = None
        for transition in self.transitions:
            proceed = transition.process(character)
            if proceed:
                return proceed
        if not proceed:
            print("Saida = {}".format(character))

    def getMode(self):
        return self.mode

    def getId(self):
        return self.id

    def getTransitions(self):
        return self.transitions
    

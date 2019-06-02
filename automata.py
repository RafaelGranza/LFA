from state import *

class DFA:
    def __init__(self):
        self.states = []

    def defineStates(self, states):
        self.states = states

    def processInput(self, word):
        print(self.findInitial())
        initialState = self.states[self.findInitial()]
        print(self.states[initialState.process(word)].process(word))
        self.states[initialState.process(word)].process(word)
            

    def findInitial(self):
        for state in self.states:
            if(state.getMode() == -1):
                return state.getId()
        return None
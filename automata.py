from state import *

class DFA:
    def __init__(self):
        self.states = []

    def defineStates(self, states):
        self.states = states

    def processInput(self, word):
        initialState = self.findInitial()
        output = []
        initialState.process(word)
        return output
            
    def findInitial(self):
        for state in self.states:
            if(state.getMode() == 'initial'):
                return state
        return None

    def __str__(self):
        s = 'Automata\n\n'
        for state in self.states:
            if state.getMode() == 'final':
                final = (str(state.getId())+'|')        
            else:
                s += (str(state.getId())+
                      '->'+
                      str(state.getTransition().getGoalState())+
                      ':'+
                      str(state.getTransition().getCharacter())+'\n')        
        return s+final
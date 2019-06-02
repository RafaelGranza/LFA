class Transition:
    def __init__(self):
        self.startState = dict()

    def defineTransition(self, startState, goalState, character):
        self.startState[character] = goalState

    def process(self, character):
        if character in self.startState:
            return self.startState.get(character)
        else:
            return None

    def getCharacters(self):
        return self.startState.keys
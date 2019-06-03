class Transition:
    def __init__(self, goalState, character):
        self.goalState = goalState
        self.character = character

    def process(self, character):
        if character == self.character:
            return self.goalState
        else:
            return self

    def getGoalState(self):
        return self.goalState.getId()

    def getCharacter(self):
        return self.character
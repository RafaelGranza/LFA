from transition import *
from state import *
from automata import *

q0 = State(0,-1)
q1 = State(1,1)
a1 = Transition()
a1.defineTransition(0,1,'a')
q0.setTransition(a1)
automato1 = DFA()
automato1.defineStates([q0,q1])
automato1.processInput('a')
print("O automato está trabalhando MUITO")
print("MUITO MESMO!!!")

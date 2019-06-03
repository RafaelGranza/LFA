from transition import *
from state import *
from automata import *

q0 = State('q0','initial')
q1 = State('q1','final')
q2 = State('q2','transitorial')
a1 = Transition(q1,'a')
a2 = Transition(q1,'b')
q0.setTransition(a1)
q2.setTransition(a2)
automato1 = DFA()
automato1.defineStates([q0,q1,q2])
print(automato1)
s = automato1.processInput('abc')
print(s)

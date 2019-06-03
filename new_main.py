from DFA import *
from utils import *

alphabet, states, delta_function, start_state, final_states = read_quintuple_from_data('DFA')
automata = DFA(alphabet, states, delta_function, start_state, final_states)

word = input()
automata.run_with_word(word)
print(word)
print(automata.get_output())
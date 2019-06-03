from DFA import *
from utils import *

automata = DFA(*read_quintuple_from_data('DFA'))

word = input('Demanda: ')
if automata.run_with_word(word):
    print("Aceito")
else:
    print("Rejeitado")
print(automata.get_output())
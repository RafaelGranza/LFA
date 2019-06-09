from class_factory import Factory
from class_assembly_line import Assembly_Line
from class_maestro import Maestro
from class_DFA import DFA
from class_moore import Moore
from utils import *

valida_entrada = DFA(*read_quintuple_from_data('DFA'))
fabrica1 = Factory('moore')

word = input('Demanda: ')
valida_entrada.run_with_word(word)

maestro = Maestro([fabrica1])
maestro.set_words(valida_entrada.get_output())
maestro.pooling()
maestro.show_outputs()
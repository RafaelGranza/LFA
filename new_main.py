from class_factory import Factory
from class_assembly_line import Assembly_Line
from class_maestro import Maestro
from class_DFA import DFA
from utils import *

valida_entrada = DFA(*read_quintuple_from_data('DFA'))
fabrica1 = Factory('tipo_b')
fabrica2 = Factory('tipo_w')

word = input('Demanda: ')
valida_entrada.run_with_word(word)

maestro = Maestro([fabrica1,fabrica2])
maestro.set_words(valida_entrada.get_output())
maestro.pooling()
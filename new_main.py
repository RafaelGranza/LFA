from class_factory import Factory
from class_assembly_line import Assembly_Line
from class_maestro import Maestro
from class_DFA import DFA
from class_moore import Moore
from utils import *

valida_entrada = DFA(*read_quintuple_from_data('DFA'))
fabrica1 = Factory('tipo_b')
fabrica2 = Factory('tipo_w')

word = input('Demanda: ')
if valida_entrada.run_with_word(word):
    print("Demanda validada!\nTamanho da demanda:",len(valida_entrada.get_output()),"carros")

maestro = Maestro([fabrica1,fabrica2])
maestro.set_words(valida_entrada.get_output())
maestro.pooling()
print(maestro.show_outputs())
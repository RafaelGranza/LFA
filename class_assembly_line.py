from utils import *
from class_DFA import DFA

class Assembly_Line:

    available = True

    def __init__(self, assembly_type):
        self.automaton = DFA(*read_quintuple_from_data(assembly_type))
        self.type = self.automaton.name

    def set_status(self, status):
        self.available = status

    
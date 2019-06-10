from class_assembly_line import Assembly_Line

class Factory:

    errors = 0

    def __init__(self, assembly_type):
        self.line = Assembly_Line(assembly_type)
        self.name = self.line.type
        self.lines = [Assembly_Line(assembly_type) for lines in range(len(self.line.automaton))]
        self.status = [0 for lines in range(len(self.line.automaton))]
        self.produced = list()
    
    def __len__(self):
        return len(self.lines)

    def __str__(self):
        return 'Linha tipo {}\nCarros nessa linha {}'.format(self.name,self.count_busy())

    def find_available(self):
        index = 0
        for busy in self.status:
            if not busy:
                return index
            index += 1

    def set_busy(self):
        index = self.find_available()
        self.status[index] = len(self.line.automaton)

    def update_status(self):
        for busy in range(len(self.status)):
            if self.status[busy]:
                self.status[busy] -= 1
            self.produced.append(self.lines[busy].automaton.output)
            self.lines[busy].automaton.output = ''

    def count_busy(self):
        count = 0
        for busy in self.status:
            if busy:
                count += 1
        return count

    def count_produced(self):
        sucess = list()
        count = 0
        for output in self.produced:
            if output:
                if 'e' in output:
                    self.errors += 1
                else:
                    sucess.append(output)
                    count += 1
        self.produced = sucess
        return count
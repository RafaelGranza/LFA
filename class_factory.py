from class_assembly_line import Assembly_Line

class Factory:

    errors = 0

    def __init__(self, assembly_type):
        line = Assembly_Line(assembly_type)
        self.lines = [Assembly_Line(assembly_type) for lines in range(line.automaton.get_size())]
        self.name = line.type
    
    def __len__(self):
        return len(self.lines)

    def find_available(self):
        for line in self.lines:
            if line.available:
                return line

    def count_busy(self):
        count = 0
        for line in self.lines:
            if not line.available:
                count += 1
        return count

    def get_name(self):
        return self.name

    def actual_state(self):
        in_line = ''
        for line in self.lines:
            if not line.available:
                in_line += line.automaton.current_letter
        
        return "{} carros na linha {}. Estados atuais {}".format(self.count_busy(), self.get_name(), in_line)
    
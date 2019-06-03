class DFA:

    current_state = None

    def __init__(self,
                 alphabet,
                 states,
                 delta_function,
                 start_state,
                 final_states):
        self.alphabet = alphabet
        self.states = states
        self.delta_function = delta_function
        self.start_state = start_state
        self.final_states = final_states
        self.current_state = start_state
        self.output = ''
        return

    def transition_to_state_with_input(self, letter):
        if ((self.current_state, letter) not in self.delta_function.keys()):
            self.current_state = None
            return
        self.current_state = self.delta_function[(self.current_state, letter)]
        self.output += letter
        return
    
    def in_accept_state(self):
        return self.current_state in self.final_states
    
    def go_to_initial_state(self):
        self.current_state = self.start_state
        return
    
    def get_output(self):
        return self.output
        
    def run_with_word(self, word):
        self.go_to_initial_state()
        for letter in word:
            self.transition_to_state_with_input(letter)
            continue
        return self.in_accept_state()
    pass
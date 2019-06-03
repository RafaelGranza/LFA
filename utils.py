def read_quintuple_from_data(file):
        f = open(file, "r")
        alphabet = set([symbol for symbol in f.readline().split()])
        states = set([int(state) for state in f.readline().split()])
        number_transitions = int(f.readline())
        delta_function = dict()
        for transition in range(number_transitions):
            r_input = f.readline()
            r_input = (r_input.replace(':','->').replace('\n','')).split('->')
            delta_function[(int(r_input[0]),r_input[2])] = r_input[1]
        start_state = int(f.readline())
        final_states = set([int(state) for state in f.readline().split()])
        f.close()

        return alphabet, states, delta_function, start_state, final_states

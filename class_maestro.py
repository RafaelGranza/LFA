class Maestro:

    def __init__(self, factory_list):
        self.factory_list = factory_list
        self.list_words = [[] for factory_type in self.factory_list]

    def set_words(self, words):
        for word in words:
            index = self.find_factory(word)
            self.list_words[index].append(word)    

    def pooling(self):
        controller = 1
        while(self.remaing_words()):
            index = 0
            for words in self.list_words:
                for word in words:
                    if controller:
                        controller = self.controller()
                    factory = self.factory_list[index]
                    line = factory.lines[factory.find_available()]
                    factory.set_busy()
                    print("Mandando o carro {}".format(word))
                    line.automaton.run_with_word(word)
                    self.update_factories()
                    print(factory)
                    words.pop(0)
                    break
                index += 1
    
    def find_factory(self, word):
        index = 0
        for factory in self.factory_list:
            if word.startswith(factory.name):
                return index
            index += 1

    def update_factories(self):
        for factory in self.factory_list:
            factory.update_status()

    def remaing_words(self):
        for words in self.list_words:
            if len(words) > 0:
                return True
        return False

    def controller(self):
        stop = input("Digite 'a' para avançar ao proximo estágio ou 'f' para acelerar ao final\n ->")
        return 1 if stop == 'a' else 0

    def menu(self):
        op = input("Digite '1' para mostrar o estado atual de todas as linhas de produção\n"+
                   "Digite '2 x' sendo x a linha que quer consultar\n"+
                   "Digite '3' para consultar quantos carros foram produzidos até o momento\n ->")
        if op == '1':
            for factory in self.factory_list:
                print(factory.actual_state())

    def show_outputs(self):
        for factory in self.factory_list:
            for line in factory.lines:
                print('Fita:',line)
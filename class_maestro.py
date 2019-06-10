class Maestro:

    def __init__(self, factory_list):
        self.factory_list = factory_list
        self.list_words = [[] for factory_type in self.factory_list]

    def set_words(self, words):
        for word in words:
            index = self.find_factory(word)
            self.list_words[index].append(word)    

    def pooling(self):
        controller,show = self.controller(True)
        while(self.remaing_words()):
            index = 0
            for words in self.list_words:
                for word in words:
                    factory = self.factory_list[index]
                    line = factory.lines[factory.find_available()]
                    factory.set_busy()
                    line.automaton.run_with_word(word)
                    self.update_factories()
                    #print(factory)
                    words.pop(0)
                    if controller:
                        controller,show = self.controller(False)
                    if show: print("Mandando o carro {}".format(word))
                    break
                index += 1
        for factory in self.factory_list:
            while(factory.count_busy()):
                self.update_factories()
    
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

    def controller(self, menu):
        if menu:
            stop = ord(input("Digite 'a' para avançar ao proximo estágio ou 'f' para acelerar ao final\n ->"))%2
            show = ord(input("Deseja acompanhar as entradas na linha? 's' ou 'n'\n ->"))%2
        else:
            stop = ord(input(" ->"))%2
            show = 0
        return stop,show

    def show_outputs(self):

        ans = ''
        for factory in self.factory_list:
            count = factory.count_produced()
            ans += "Linha {}\n  Carros produzidos = {}\n".format(factory.name,count)
        return ans
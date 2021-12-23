import copy
class Place:
    def __init__(self, name, tokens=0):
        self.tokens = tokens
        self.name = name

    def amount(self):
        return self.tokens

    def consume(self, amount=1):
        assert self.tokens >= amount
        self.tokens = self.tokens - amount

    def produce(self, amount=1):
        self.tokens = self.tokens + amount

class Transition:
    def __init__(self, name, preset=[], postset=[]):
        assert len(postset) > 0
        self.preset  = preset
        self.postset = postset
        self.name = name

    def fireable(self):
        for p in self.preset:
            if p.amount() == 0:
                return False
        return True

    def fire(self):
        if self.fireable():
            for p in self.preset:
                p.consume()
            for p in self.postset:
                p.produce()
    
    
class PetriNet:
    def __init__(self, transition=[]):
        self.transition = transition

        placelist = []
        for t in transition:
            placelist = placelist + t.preset + t.postset
        self.place = list(set(placelist))

        

    def run(self, firing_sequence):
        for t in firing_sequence:
            if t.fireable():
                t.fire()
                self.print_marking()
            else:
                raise PetriFiringError(t)
    
    def fire_one_transition(self, trans_name): # this method is to help pass by value easier(in reachable function)
        trans = [t for t in self.transition if t.name == trans_name]
        trans[0].fire()
    
    def reachable(self):
        marking_list = []
        marking_list.append(self.get_marking()) # initial marking
        self.print_marking()
        self.__help_reachable(copy.deepcopy(self), marking_list) # pass by value
        return marking_list

    def __help_reachable(self, petri, marking_list, name=''): # depth first search
        if name != '':
            petri.fire_one_transition(name)
            if not petri.get_marking() in marking_list:
                petri.print_marking()
                marking_list.append(petri.get_marking())
            else:
                return

        enabled_list = [t.name for t in petri.transition if t.fireable()]
        if(len(enabled_list) == 0):
            print('Terminal marking')
        
        for name in enabled_list:
            self.__help_reachable(copy.deepcopy(petri), marking_list, name)

    
    def print_marking(self):
        # first method: a little hard to trace the token
        # tokenlist = [p.tokens for p in self.place]
        # print(tokenlist)

        # second method: more readable and easier to trace
        tokenlist = [p.name +'^'+ str(p.tokens) for p in self.place if p.tokens]
        print(tokenlist)

    def get_marking(self):
        return [p.tokens for p in self.place] # for faster process of other operation

    def print_place(self):
        placelist = [p.name for p in self.place]
        print(placelist)

    def print_transition(self):
        translist = [t.name for t in self.transition]
        print(translist)
    

class PetriFiringError(Exception):
    def __init__(self, transition):
        self.message = f"\'{transition}\' is not fireable"
        super().__init__(self.message)
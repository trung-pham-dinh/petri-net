
class Place:
    def __init__(self, tokens):
        self.tokens = tokens

class Transition:
    def __init__(self, preset, postset):
        pass
    def fire(self):
        pass
    def isEnabled(self):
        pass
    
class PetriNet:
    def __init__(self, transition):
        self.transition = transition
    def run(self, firing_sequence):
        pass
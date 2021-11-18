class Place:
    def __init__(self, tokens=0):
        self.tokens = tokens

    def tokens(self):
        return self.tokens

    def consume(self, amount=1):
        assert self.tokens >= amount
        self.tokens = self.tokens - amount

    def produce(self, amount=1):
        self.tokens = self.tokens + amount

class Transition:
    def __init__(self, preset=[], postset=[]):
        assert len(postset) > 0
        self.preset  = preset
        self.postset = postset

    def fireable(self):
        for p in self.preset:
            if p.tokens() == 0:
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

    def run(self, firing_sequence):
        pass
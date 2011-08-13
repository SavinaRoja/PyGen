from random import randint

class Flower(object):

    '''A flower class, contains methods for mutation, mating, and
    calculating fitness.'''

    def __init__(self, traits = False):
        if not traits: #If no traits are given, they are randomly generated
            self.traits = [randint(0,1) for i in range(32)]
        else: #If traits are given, they are used
            self.traits = traits
            
        self.fitness = self.calcfitness()
        
    def mutate(self, traitlist):
        for i in range(2): #In a list of traits, create some mutations
            traitlist[randint(0,len(traitlist)-1)] = randint(0, 1)
        return traitlist #Return the mutated version of the traits list
        
    def mate(self, partner):
        
        #Take a mutated list of genes from the first parent
        selfset = self.mutate(self.traits[:16])
        #Take a mutated list of genes from the second parent
        partnerset = partner.mutate(partner.traits[16:])
        
        #Create a new flower from the combined, mutated parent genes
        newFlower = Flower(traits = selfset + partnerset)
        
        #Return the new flower
        return newFlower
        
    def calcfitness(self):
        #Fitness is a sum of all the traits
        return sum(self.traits)

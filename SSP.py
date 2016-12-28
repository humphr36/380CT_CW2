from random import randint, sample
from itertools import chain, combinations
from time import time


class SSP():
    def __init__(self, S=[], t=0):
        self.S = S #Set
        self.t = t #Target
        self.n = len(S) #Number of items in set
        #
        self.decision = False
        self.total    = 0
        self.selected = []

    def __repr__(self):
        return "SSP instance: S="+str(self.S)+"\tt="+str(self.t)
    
    def random_instance(self, n, bitlength=10):
        """Method creates a set and sets a random target for the SubsetSum Problem. Result could be true or false"""
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = randint(0,n*max_n_bit_number)
        self.n = len( self.S )

    def random_yes_instance(self, n, bitlength=10):
        """Method creates a set in which the result of the SubsetSum Problem is True"""
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = sum( sample(self.S, randint(0,n)) )
        self.n = len( self.S )

    #Exhaustive Search
    def exhaustive_search(self):
        """Method searches through all the possible candidates in order
        it checks to see if they equal the target and if they do it prints
        true"""
        candidates=[]
        candidate=[]
        #Create an array of all possible subsets
        for j in range(0, self.n+1):
          for subset in combinations(self.S, j):
            candidates.append(subset)
        #Search through the possible subsets to find if one matches the target
        summedcandidates=[sum(tup) for tup in candidates]
        for k in summedcandidates:
            if k==self.t:
                return True
        return False

    #Dynamic Programming

    #Greedy

    #Grasp

    
    #Random Search
    def try_at_random(self):
        """Method creates an empty array as the candidate variable,
        sets the total to 0 and then loops and randomly searches subsets
        until it finds one which adds up to the target, as it tries each
        subset it prints which subset it has tried and what the sum of
        that subset is"""
        candidate = []
        total = 0
        while total != self.t:
            candidate = sample(self.S, randint(0,self.n))
            total     = sum(candidate)
            print( "Trying: ", candidate, ", sum:", total )
            
start_time = time() #Starts monitoring time
instance = SSP()
instance.random_yes_instance(20)
print (instance.exhaustive_search())
print( instance )
#instance.try_at_random()
print("--- %s seconds ---" % (time() - start_time)) #Prints execution time

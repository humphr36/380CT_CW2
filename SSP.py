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
        if self.n==0 and self.t!=0: #if the set is empty and the target is not 0, return false
            return False
        if self.t==0: #if the target is 0 return true (as an empty set is a subset of all sets and adds up to 0)
            return True
        else:
            #Search through the possible subsets to find if one matches the target
            for j in range(0, self.n+1):
              for subset in combinations(self.S, j):
                  if sum(subset)==self.t:
                      return True
            return False

    #Dynamic Programming
    def dynamic_programming(self):
        """Method"""
        if self.n==0 and self.t!=0: #if the set is empty and the target is not 0, return false
            return False
        if self.t==0: #if the target is 0 return true (as an empty set is a subset of all sets and adds up to 0)
            return True
        else:
            #Create an array storing whether the each integer between 0 and t can calculated from the set
            options=[False]*(self.t+1)
            options[0]=True
            for k in range(0,self.n): #For each element of the set
                changingvars=[]
                for l in range(0,self.t+1): #for every integer between 0 and the total
                    z=l-self.S[k]
                    if options[l]==False and z>=0 and options[z]==True: #if the integer is false and if the number - the element is true
                        changingvars.append(l)
                for var in changingvars:
                    options[var]=True
                changingvars=[]
            return options[self.t]

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
instance = SSP()
for e in range(0,1):
    instance.random_instance(50,14)
    print( instance )
    start_time = time() #Starts monitoring time
    #print (instance.exhaustive_search())
    print (instance.dynamic_programming())
    #instance.dynamic_programming()
    #instance.try_at_random()
    print("--- %s seconds ---" % (time() - start_time)) #Prints execution time

# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"



        
        print(self.values)
        reward={}
        states = self.mdp.getStates()
        itr=0

        for st in states:
            reward[st]=0
            if self.mdp.isTerminal(st)==False:
                for act in self.mdp.getPossibleActions(st):
                    for nextState in self.mdp.getTransitionStatesAndProbs(st,act):
                        reward[st] += self.mdp.getReward(st, act, nextState)

        while(itr< self.iterations):
            itr+=1
            utility=self.values.copy()
            for st in states:
                if self.mdp.isTerminal(st)==False:
                    value=self.getQValue(st,self.getAction(st))
                    value = value * self.discount
                    utility[st]=reward[st]+value
                    
                    # utility[st]=reward[st]+self.discount*self.getQValue(st,self.getAction(st))
            self.values=utility
            

        



    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        
        reachState = self.mdp.getTransitionStatesAndProbs(state, action)
        

        count=0

        for st in reachState:
            nextState=st[0]
            probOfNextState= st[1]

            utilityOfNextState = self.getValue(nextState)
            count = count + (utilityOfNextState*probOfNextState)
        
        return count




        

    def computeActionFromValues(self, state):
        
        "*** YOUR CODE HERE ***"
        if self.mdp.isTerminal(state):
            return None

        possibleAction = self.mdp.getPossibleActions(state)
        print(possibleAction)
        maxi=-999999
        act = 0

        for action in possibleAction:
            val = self.getQValue(state,action)
            if(self.getQValue(state,action) > maxi):
                act = action
                maxi = max (self.getQValue(state,action),maxi)
                
        return act



    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

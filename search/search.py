# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import *

gotGoal=False
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]






goalState=None
visitedList=[]
moves=[]

def DFS(problem,currentState):
    
    global visitedList
    global moves
    global goalState

    visitedList.append(currentState)

    if problem.isGoalState(currentState):
        goalState=currentState
        return True

    for stateInfo in problem.getSuccessors(currentState):
        state=stateInfo[0]
        
        if state not in visitedList:
            if DFS(problem,state):
                moves.append(stateInfo[1])
                return True

    return False




def depthFirstSearch(problem):

    global visitedList
    global moves

    visitedList=[]
    moves=[]
    startState= problem.getStartState()    
    
    if DFS(problem,startState):
        moves.reverse()
        return moves
    
    


def breadthFirstSearch(problem):
    goalState=0
    visitedList=[]
    moves=[]
    parList={}

    parList[problem.getStartState()]=None

    visitedList.append(problem.getStartState())

    q = Queue()

    q.push(problem.getStartState())

    while not q.isEmpty():
        currentState = q.pop()

        if problem.isGoalState(currentState):
            goalState=currentState
            break

        # for state in problem.getSuccessors(currentState):
        #     if state[0] not in visitedList:
        #         visitedList.append(state[0])
        #         parList[state[0]]=currentState
        #         q.push(state[0])


        for state in problem.getSuccessors(currentState):
            if state[0] not in visitedList:
                visitedList.append(state[0])
                parList[state[0]]= (currentState,state[1])
                q.push(state[0])

    getDirection(problem,goalState,moves,parList)
    moves.reverse()
    print(moves)
    return moves


# def getDirection(problem,currentState,moves,parList):
    
#     if parList[currentState] == None:
#         return

#     for state in problem.getSuccessors(parList[currentState]):
#         if state[0]==currentState:
#             moves.append(state[1])
#             return getDirection(problem,parList[currentState],moves,parList)
            
def getDirection(problem,currentState,moves,parList):
    
    if parList[currentState] == None:
        return

    moves.append(parList[currentState][1])
    getDirection(problem,parList[currentState][0],moves,parList)
 


def iterativeDeepningSearch(problem):
    global visitedList
    global moves

    visitedList=[]
    moves=[]
    startState= problem.getStartState()    
    
    i=0

    while True:
        visitedList=[]
        moves=[]
        
        if DDFS(problem,startState,i,0):
            moves.reverse()
            print (moves)
            return moves
        i=i+1
        

def DDFS(problem,currentState,maxDepth, currentDepth):
    
    global goalState
    global visitedList
    global moves
    global gotGoal

    visitedList.append(currentState)

    

    if problem.isGoalState(currentState):
        goalState=currentState
        return True

    if maxDepth==currentDepth:
        return False

    for stateInfo in problem.getSuccessors(currentState):
        state=stateInfo[0]
        
        if state not in visitedList:
            if DDFS(problem,state,maxDepth,currentDepth+1):
                moves.append(stateInfo[1])
                return True

    return False


    
    





def uniformCostSearch(problem):
    goalState=0
    visitedList=[]
    moves=[]
    parList={}
    cost={}

    parList[problem.getStartState()]=None

    visitedList.append(problem.getStartState())

    cost[problem.getStartState()]=0

    q = PriorityQueue()

    q.push(problem.getStartState(),0)

    while not q.isEmpty():
        currentState = q.pop()

        if problem.isGoalState(currentState):
            goalState=currentState
            break

        for state in problem.getSuccessors(currentState):
            

            # if state[0] not in cost.keys():
            #     cost[state[0]]=cost[currentState]+state[2]
            #     parList[state[0]]=currentState
            #     q.push(state[0],cost[state[0]])


            # elif cost[state[0]]>cost[currentState]+state[2]:
            #     cost[state[0]]=cost[currentState]+state[2]
            #     parList[state[0]]=currentState
            #     q.push(state[0],cost[state[0]])

            if state[0] not in cost.keys():
                cost[state[0]]=cost[currentState]+state[2]
                parList[state[0]]=(currentState,state[1])
                q.push(state[0],cost[state[0]])
                


            elif cost[state[0]]>cost[currentState]+state[2]:
                cost[state[0]]=cost[currentState]+state[2]
                parList[state[0]]=(currentState,state[1])
                q.push(state[0],cost[state[0]])

    getDirection(problem,goalState,moves,parList)
    moves.reverse()
    print(moves)
    return moves



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0



def bestFirstSearch(problem,heuristic=nullHeuristic):
    goalState=0
    visitedList=[]
    moves=[]
    parList={}

    parList[problem.getStartState()]=None

    visitedList.append(problem.getStartState())

    q = PriorityQueue()

    #q.push(problem.getStartState())
    q.push(problem.getStartState(),heuristic(problem.getStartState(),problem))

    while not q.isEmpty():
        currentState = q.pop()

        if problem.isGoalState(currentState):
            goalState=currentState
            break


        for state in problem.getSuccessors(currentState):
            if state[0] not in visitedList:
                visitedList.append(state[0])
                parList[state[0]]= (currentState,state[1])
                q.push(state[0],heuristic(state[0],problem))
                

    getDirection(problem,goalState,moves,parList)
    moves.reverse()
    print(moves)
    return moves






def aStarSearch(problem, heuristic=nullHeuristic):
    

    goalState=0
    visitedList=[]
    moves=[]
    parList={}
    cost={}

    parList[problem.getStartState()]=None

    visitedList.append(problem.getStartState())

    cost[problem.getStartState()]=0

    q = PriorityQueue()

    q.push(problem.getStartState(),heuristic(problem.getStartState(),problem))

    while not q.isEmpty():
        currentState = q.pop()

        if problem.isGoalState(currentState):
            goalState=currentState
            break

        for state in problem.getSuccessors(currentState):
            

            # if state[0] not in cost.keys():
            #     cost[state[0]]=cost[currentState]+state[2]
            #     parList[state[0]]=currentState
            #     q.push(state[0],cost[state[0]])


            # elif cost[state[0]]>cost[currentState]+state[2]:
            #     cost[state[0]]=cost[currentState]+state[2]
            #     parList[state[0]]=currentState
            #     q.push(state[0],cost[state[0]])

            if state[0] not in cost.keys():
                cost[state[0]]=cost[currentState]+state[2]
                parList[state[0]]=(currentState,state[1])
                q.push(state[0],cost[state[0]]+heuristic(state[0],problem))
                


            elif cost[state[0]]>cost[currentState]+state[2]:
                cost[state[0]]=cost[currentState]+state[2]
                parList[state[0]]=(currentState,state[1])
                q.push(state[0],cost[state[0]]+heuristic(state[0],problem))

    getDirection(problem,goalState,moves,parList)
    moves.reverse()
    print(moves)
    return moves



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
bestfs=bestFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepningSearch
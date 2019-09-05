import queue
import copy
X=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
domA=[1,2,3,4]
domB=[1,2,3,4]
domC=[1,2,3,4]
domD=[1,2,3,4]
domE=[1,2,3,4]
domF=[1,2,3,4]
domG=[1,2,3,4]
domH=[1,2,3,4]
domI=[1,2,3,4]
domJ=[1,2,3,4]
domK=[1,2,3,4]
domL=[1,2,3,4]
domM=[1,2,3,4]
domN=[1,2,3,4]
domO=[1,2,3,4]


adjA=['B','D','E','J']
adjB=['A','C','E']
adjC=['B','E','F']
adjD=['A','G','H','I']
adjE=['A','B','C','F','H']
adjF=['C','E','I','L']
adjG=['D','H','I','M','K']
adjH=['D','E','G','J','L','K']
adjI=['D','F','G','J','K']
adjJ=['A','H','I','L','M']
adjK=['G','H','I','L','N','O']
adjL=['H','F','J','M','N','O','K']
adjM=['G','J','N','O','L']
adjN=['O','M','L','K']
adjO=['L','M','N','K']

csp = {X[0]: [domA,adjA,len(adjA)] , X[1]: [domB,adjB,len(adjB)] ,
         X[2]: [domC,adjC,len(adjC)] ,X[3]: [domD,adjD,len(adjD)],
         X[4]: [domE,adjE,len(adjE)],X[5]: [domF,adjF,len(adjF)],
         X[6]: [domG,adjG,len(adjG)],X[7]: [domH,adjH,len(adjH)],
         X[8]: [domI,adjI,len(adjI)], X[9]: [domJ,adjJ,len(adjJ)],
         X[10]: [domK,adjK,len(adjK)],X[11]: [domL,adjL,len(adjL)],
         X[12]: [domM,adjM,len(adjM)],X[13]: [domN,adjN,len(adjN)],
         X[14]: [domO,adjO,len(adjO)] }

# constraintList= ['A!=B', 'A!=D', 'A!=E', 'A!=J', 'B!=C', 'B!=E', 'C!=E', 'C!=F','D!=G','D!=H','D!=I','E!=F','E!=H',
#         'F!=I','G!=H','G!=I','H!=J','I!=J','K!=I','K!=G','K!=H','K!=L','K!=O','K!=N','L!=H','L!=F','L!=J',
#         'L!=M','L!=N','L!=O','M!=G','M!=J','M!=N','M!=O','N!=O']

assignment={}                               #this map contains current assignment of domain e.g: {'A':2,'B':1}


def Inference(csp,var,value):

    temp={}
    
    for item in csp[var][1]:                    #for each neighbours of var
        if item not in assignment.keys():       #if neighbour is not assigned
            li=[]
            for dom in csp[item][0]:            #for each domain of neighbour
                if value == dom:                #if constraint is not satisfied then remove that domain of neighbour
                    li.append(dom)

            for dom in li:
                csp[item][0].remove(dom)
            if len(csp[item][0])==0:
                return False
    for var in X:
        print(csp[var][0])
    return True


def take_var(csp):
    minRemVal=9999
    minRemVariable=0
    maxDegree=  -1

    for var in X:                                   #variable choosing heuristic
        if var not in assignment.keys():            #if node is not assigned then check for MRV heuristic
            if len(csp[var][0])<minRemVal:          #check len(dom of current variable) < minRemainingValue
                minRemVal=len(csp[var][0])
                minRemVariable=var
                maxDegree=csp[var][2]

            elif len(csp[var][0]) == minRemVal and maxDegree < csp[var][2]:         #check for Degree heuristic
                minRemVal=len(csp[var][0])
                minRemVariable=var
                maxDegree=csp[var][2]

    return minRemVariable




def justCheck():
    for var in X:
        for nei in csp[var][1]:
            if assignment[var]==assignment[nei]:
                return False
    return True


def backtrack(csp):
    if len(assignment)==len(X):                       #if all node is assigned then return DONE
        return True

    var=take_var(csp)    
    print("VAR :"+ var) 
    #for var1 in X:
     #   print(csp[var1][0])
    print ('\n')                      #choose variable using heuristic
    
    for value in csp[var][0]:
        print ("start",var,value)     
        csp1=copy.deepcopy(csp)                    #take a domain value and add it to assignment
        assignment[var]=value
        inf=Inference(csp1,var,value)                        #check if this domain can reduce neighbours domain
        if inf:
            if backtrack(csp1):
                return True
            print(var,value," backtrack")
            #for var1 in X:
             #   print(csp[var1][0])
        assignment.pop(var)

    return False


print(backtrack(csp))
print(assignment)
print(justCheck())




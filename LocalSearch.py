import queue
import random
X=['A','B','C','D','E','F','G','H','I','J']
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


adjA=['B','D','E','J']
adjB=['A','C','E']
adjC=['B','E','F']
adjD=['A','G','H','I']
adjE=['A','B','C','F','H']
adjF=['C','E','I']
adjG=['D','H','I']
adjH=['D','E','G','J']
adjI=['D','F','G']
adjJ=['A','H']

csp = {X[0]: [domA,adjA,len(adjA)] , X[1]: [domB,adjB,len(adjB)] ,
         X[2]: [domC,adjC,len(adjC)] ,X[3]: [domD,adjD,len(adjD)],
         X[4]: [domE,adjE,len(adjE)],X[5]: [domF,adjF,len(adjF)],
         X[6]: [domG,adjG,len(adjG)],X[7]: [domH,adjH,len(adjH)],
         X[8]: [domI,adjI,len(adjI)], X[9]: [domJ,adjJ,len(adjJ)] }

# constraintList= ['A!B','A!D','A!E','A!J',
#                      'B!A' , 'B!C' , 'B!E',
#                       'C!B' , 'C!E', 'C!F',
#                       'D!A','D!G','D!H','D!I',
#                       'E!A','E!B','E!C','E!F','E!H',
#                       'F!C','F!E','F!I',
#                       'G!D','G!H','G!I',
#                       'H!D','H!E','H!G','H!J',
#                       'I!D','I!F','I!G',
#                       'J!A','J!H' ]

assignment={}                               #this map contains current assignment of domain e.g: {'A':2,'B':1}







conflicted=[]

def isSolution(current):

    flag=False

    for key in current.keys():
        for dom in csp[key][1]:
            if current[key]== current[dom]:
                flag=True
                if key not in conflicted:
                    conflicted.append(key)
                if key not in conflicted:
                    conflicted.append(dom)
                
    if(flag):
        return False
    return True



def checkConflicts(current,rand_conf_var):

    if(isSolution(current)):
        return True,len(conflicted)

    return False,len(conflicted)




def localSearch():

    current={}
    cur_var=0
    cur_dom=0
    for val in X:
        current[val]=random.choice(csp[val][0])


    for i in range(1,5):
        if isSolution(current):
            return current
        current_conflicted=len(conflicted)

        rand_conf_var=random.choice(conflicted)

        for dom in csp[rand_conf_var][0]:
            current[rand_conf_var]=dom
            conflicted.clear()
            retValue,lenOfConflicted=checkConflicts(current,rand_conf_var)
            if retValue:
                print(current)
                return True
            if lenOfConflicted<current_conflicted:
                cur_dom=dom
                current_conflicted=lenOfConflicted
        
        current[rand_conf_var]=cur_dom
    

        
        

        
print(localSearch())
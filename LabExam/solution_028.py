


#This is for solving 8-queen problem. Max iteration=1000,

import queue
import random
import time



X=[1,2,3,4,5,6,7,8]


domA=[1,2,3,4,5,6,7,8]
domB=[1,2,3,4,5,6,7,8]
domC=[1,2,3,4,5,6,7,8]
domD=[1,2,3,4,5,6,7,8]
domE=[1,2,3,4,5,6,7,8]
domF=[1,2,3,4,5,6,7,8]
domG=[1,2,3,4,5,6,7,8]
domH=[1,2,3,4,5,6,7,8]

adjA=[2,3,4,5,6,7,8]
adjB=[1,3,4,5,6,7,8]
adjC=[1,2,4,5,6,7,8]
adjD=[1,2,3,5,6,7,8]
adjE=[1,2,3,4,6,7,8]
adjF=[1,2,3,4,5,7,8]
adjG=[1,2,3,4,5,6,8]
adjH=[1,2,3,4,5,6,7]



csp = {X[0]: [domA,adjA,len(adjA)] , X[1]: [domB,adjB,len(adjB)] ,
         X[2]: [domC,adjC,len(adjC)] ,X[3]: [domD,adjD,len(adjD)],
         X[4]: [domE,adjE,len(adjE)],X[5]: [domF,adjF,len(adjF)],
         X[6]: [domG,adjG,len(adjG)],X[7]: [domH,adjH,len(adjH)] }


conflicted=[]

def isSolution(current):

    flag=False

    for key in current.keys():
        for dom in csp[key][1]:
            # if current[key]== current[dom] or abs(ord(key)-ord(dom))==abs(current[key]-current[dom]):
            col=abs(key-dom)
            col1=abs(current[key]-current[dom])

            if current[key]== current[dom] or abs(key-dom)==abs(current[key]-current[dom]):
                flag=True
                if key not in conflicted:
                    conflicted.append(key)
                if dom not in conflicted:
                    conflicted.append(dom)
                
    if(flag):
        return False
    return True




def printGrid(current):
    array=[]
    #print('Placement of queen')
    for i in range(1,9):
        print('(',current[i],',',i,')')

file=open('output_028.txt','w')
def printGridFile(current):
    array=[]
    #file.write('Placement of queen\n')
    for i in range(1,9):
        file.write('('+str(current[i])+','+str(i)+')'+'\n')


def checkConflicts(current,rand_conf_var):

    if(isSolution(current)):
        return True,len(conflicted)

    return False,len(conflicted)




def localSearch():
    stTime=time.time()

    current={}
    cur_var=0
    cur_dom=0
    for val in X:
        current[val]=random.choice(csp[val][0])
    file.write("First Placement\n")
    printGridFile(current)
    print("First PLacement:")
    printGrid(current)
    
    
    #fole.write()

    count=0
    for i in range(1,1000):
        if isSolution(current):
            return current
        current_conflicted=len(conflicted)
        

        rand_conf_var=random.choice(conflicted)
        cur_dom=current[rand_conf_var]

        for dom in csp[rand_conf_var][0]:
            
            current[rand_conf_var]=dom
            conflicted.clear()
            retValue,lenOfConflicted=checkConflicts(current,rand_conf_var)
            if retValue:
                print("Final Placement:")
                printGrid(current)
                file.write("Final Placement:\n")
                printGridFile(current)
                print('Steps: ',count)
                file.write('Steps: '+str(count)+'\n')
                print('Execution Time: ', time.time()-stTime)
                file.write("Execution Time: "+ str(time.time()-stTime))
                #print(current)
                return True
            if lenOfConflicted<current_conflicted:
                count+=1
                cur_dom=dom
                current_conflicted=lenOfConflicted
        
        current[rand_conf_var]=cur_dom
    

        
        

print(localSearch())
   

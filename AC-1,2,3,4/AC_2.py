import queue
import copy

import time
# X=['A','B','C']
# domA=[1,2,3,4,5,6]
# domB=[1,2,3,4,5,6]
# domC=[1,2,3,4,5,6]
# adjA=['B','C']
# adjB=['A','C']
# adjC=['A','B']
# csp = {X[0]: [domA,adjA] , X[1]: [domB,adjB] , X[2]: [domC,adjC]}

# constraintList= ['A>B', 'B<A' , 'B<C' , 'C>B' , 'A!C' , 'C!A' ]




def revise(arc):
    revised= False

    for Di in csp[arc[0]][0][:]:
        cnt=False
        sign=arc[1]
        DomList=csp[arc[2]][0]
        for k in range(0,len(DomList)):
            if (sign=='>' and Di > DomList[k]) or (sign=='<' and Di < DomList[k]) or (sign=='!' and Di != DomList[k]) or (sign=='^' and Di == (DomList[k])**2) or (sign=='*' and Di**2 == DomList[k]) or (sign=='+' and Di == DomList[k]+2) or (sign=='-' and Di-2 == DomList[k]):
                cnt=True

        if cnt==False:
            csp[arc[0]][0].remove(Di)
            revised=True
    
    return revised


def AC_2():
    Q=queue.Queue()
    Q1=queue.Queue()
    for i in range(0,len(X)):

        for cons in constraintList:
            length=len(cons)
            if (X[i]> cons[length-1]):
                Q.put(cons)
                for rev in constraintList:
                    if(rev[0]== cons[length-1] and rev[len(rev)-1]== cons[0]):
                        Q1.put(rev)

            while Q.empty()==False:
                while Q.empty()==False:
                    arc=Q.get()
                    k=arc[0]
                    m=arc[len(arc)-1]
                    if revise(arc):

                        if len(csp[arc[0]][0])==0:                         #added later
                            return False


                        for val in constraintList:
                            if val[len(val)-1]==k and val[0]<= X[i] and val[0] != m:
                                Q1.put(val)

                while Q.empty()==False:
                    Q.get()

                # Q=copy.deepcopy(Q1)
                while Q1.empty()==False:
                    Q.put(Q1.get())

    return True





stTime=time.time()
with open('Test.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

fileLength=len(content)
#print(fileLength)
itr=0
while(itr<fileLength):

    constraintList=[]
    X=[]
    csp={}

    number=int(content[0+itr])
    #print(number)
    # for i in range(1+itr,itr+number+1):
    for i in range(1,number+1):
        X.append(str(i))
    #print(X)
    
    for i in range(itr+1,itr+number+1):
        cnt=0
        dom1=[]
        st=[]

        dom1=content[i].split(' ')
        node=dom1.pop(0)
        dom1 = list(map(int, dom1))
        csp[str(node)]=[dom1,[]]
    
        #print(dom1)

    edge=content[itr+number+1]
    #print(int(edge))
    for i in range(itr+number+2,itr+int(edge)+number+2):
        temp=content[i].split(' ')
        #print(temp)
        var1=temp[0]
        var2=temp[1]
        sign=temp[2]
        csp[var1][1].append(var2)
        constraintList.append((var1,sign,var2))
    #print(file[i][0],file[i][2])
    #print(csp)

    #print(constraintList)
    itr=itr+int(edge)+number+2



    stTime=time.time()
    print(AC_2())

    for val in csp.keys():
        print(csp[val][0])
    print('Time: ',time.time()-stTime)

import queue
import math
import time
import copy


#revise function
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


#AC-1 starts here
def AC_1():
    flag=False
    
    while(flag==False):
        flag=True
        for cons in constraintList:
            if revise(cons)==True:
                flag=False


#AC-2 starts here
def AC_2():
    Q=queue.Queue()
    Q1=queue.Queue()
    lenX=len(X)
    for i in range(0,lenX):
        for j in range(0,i):
            if (X[i],X[j]) in tempDict.keys():
                touple=(X[i],tempDict[(X[i],X[j])],X[j])
                Q.put(touple)
                touple=(X[j],tempDict[(X[j],X[i])],X[i])
                Q1.put(touple)

            while Q.empty()==False:
                while Q.empty()==False:
                    arc=Q.get()
                    k=arc[0]
                    m=arc[len(arc)-1]
                    if revise(arc)==True:
                        for l in range(0,i+1):
                            vari1=X[l]
                            vari2=X[i]
                        
                            if (vari1!=m):
                                if (vari1,k) in tempDict.keys():
                                    touple=(X[l],tempDict[(X[l],k)],k)
                                    Q1.put(touple)

                
                while Q1.empty()==False:
                    Q.put(Q1.get())



#AC-3 starts here
def AC_3():
    
    q= queue.Queue()
    t=len(constraintList)

    for i in range(0,t):
        q.put(constraintList[i])

    while q.empty() == False :
        arc=q.get()
        if revise(arc) == True:
            Di=len(csp[arc[0]][0])
            if Di==0:
                return False
           
            for i in range(0,len(csp[arc[0]][1])):
                t=len(constraintList)
                for k in range(0,t):

                    if constraintList[k][0]==arc[0]:
                        if constraintList[k][2]==arc[2]:
                            continue
                    
                        if(constraintList[k][1]=='>'):
                            q.put((constraintList[k][2],'<',constraintList[k][0]))

                        elif(constraintList[k][1]=='<'):
                            q.put((constraintList[k][2],'>',constraintList[k][0]))
                        
                        elif(constraintList[k][1]=='!'):
                            q.put((constraintList[k][2],'!',constraintList[k][0]))

                        elif(constraintList[k][1]=='^'):  
                            q.put((constraintList[k][2],'*',constraintList[k][0]))

                        elif(constraintList[k][1]=='+'):
                            q.put((constraintList[k][2],'-',constraintList[k][0]))

                        elif(constraintList[k][1]=='-'):   
                            q.put((constraintList[k][2],'+',constraintList[k][0]))

                        elif(constraintList[k][1]=='*'):                               
                            q.put((constraintList[k][2],'^',constraintList[k][0]))

    return True



#AC-4 starts here
def AC_4():
    Q=queue.Queue()
    S={}
    counter={}
    for Rij in constraintList:
        first=Rij[0]
        last=Rij[len(Rij)-1]
        for dom1 in csp[first][0]:
            for dom2 in csp[last][0]:
                S[(last,dom2)]=[]
                counter[(first,dom1,last)]=0

    for Rij in constraintList:
        first=Rij[0]
        last=Rij[len(Rij)-1]
        for dom1 in csp[first][0][:]:
            for dom2 in csp[last][0]:

                if Rij[1]=='>' and dom1 > dom2:
                    counter[(first,dom1,last)]+= 1
                    S[(last,dom2)].append((first,dom1))

                if Rij[1]=='<' and dom1 < dom2:
                    counter[(first,dom1,last)]+= 1
                    S[(last,dom2)].append((first,dom1))

                if Rij[1]=='!' and dom1 != dom2:
                    counter[(first,dom1,last)]+= 1
                    S[(last,dom2)].append((first,dom1))

                if Rij[1]=='+' and dom1 == dom2+2:
                    counter[(first,dom1,last)]+= 1
                    S[(last,dom2)].append((first,dom1))

                if Rij[1]=='-' and dom1-2 == dom2:
                    counter[(first,dom1,last)]+= 1
                    S[(last,dom2)].append((first,dom1))

                if Rij[1]=='*' and dom1**2 == dom2:
                    counter[(first,dom1,last)]+= 1
                    S[(last,dom2)].append((first,dom1))
                
                if Rij[1]=='^' and dom1 == dom2**2:
                    counter[(first,dom1,last)]+= 1
                    S[(last,dom2)].append((first,dom1))

            if counter[(first,dom1,last)]==0:
                Q.put((first,dom1))
                csp[first][0].remove(dom1)


    while not Q.empty():
        varDom=Q.get()
        vj=varDom[0]
        aj=varDom[1]
        for value in S[(vj,aj)]:
            vi=value[0]
            ai=value[1]
            if ai in csp[vi][0]:
                counter[(vi,ai,vj)]-=1
                if counter[(vi,ai,vj)]==0:
                    Q.put((vi,ai))
                    csp[vi][0].remove(ai)
    

#main code for graphs from Test.txt
stTime=0

file_exeTime=open('file_exeTime_028.txt','w')
file_domain=open('file_domain_028.txt','w')

with open('Test_028.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content] 

fileLength=len(content)
itr=0

while(itr<fileLength):
    constraintList=[]
    X=[]
    csp={}
    tempDict={}

    number=int(content[0+itr])

    for i in range(1,number+1):
        X.append(str(i))
    
    for i in range(itr+1,itr+number+1):
        cnt=0
        dom1=[]
        st=[]

        dom1=content[i].split(' ')
        node=dom1.pop(0)
        dom1 = list(map(int, dom1))
        csp[str(node)]=[dom1,[]]
    
    edge=content[itr+number+1]

    for i in range(itr+number+2,itr+int(edge)+number+2):
        temp=content[i].split(' ')
        var1=temp[0]
        var2=temp[1]
        sign=temp[2]
        csp[var1][1].append(var2)
        constraintList.append((var1,sign,var2))

        tempDict[(var1,var2)]=sign
    
    cspTmp=copy.deepcopy(csp)
    constraintListTmp=copy.deepcopy(constraintList)
    itr=itr+int(edge)+number+2

#Total domain count is in totalCount
    totalCount=0
    timeString=''

    for val in csp.keys():
        for tmp in csp[val][0]:
            totalCount+=1



#AC-1 execution time and domain reduction
    stTime=time.time()    
    print('----------')
    print("\nAC-1")
    AC_1()

    count1=0
    temp=0
    for val in csp.keys():
        count1=count1+len(csp[val][0])
        

    print('Time: ',(time.time()-stTime))
    timeString=str(number)+' '+str((time.time()-stTime))+' '

#Initialization from Temporary list,dict and variables
    csp=copy.deepcopy(cspTmp)
    constraintList=copy.deepcopy(constraintListTmp)


#AC-2 execution time and domain reduction
    stTime=time.time()
    print("\nAC-2")
    AC_2()
    
    count2=0
    temp=0
    for val in csp.keys():
        count2=count2+len(csp[val][0])
        

    print('Time: ',(time.time()-stTime))
    timeString=timeString+str((time.time()-stTime))+' '
#####

    csp=copy.deepcopy(cspTmp)
    constraintList=copy.deepcopy(constraintListTmp)


#AC-3 execution time and domain reduction
    stTime=time.time()
    print("\nAC-3")
    print(AC_3())

    count3=0
    temp=0
    for val in csp.keys():
        count3=count3+len(csp[val][0])
        
    print('Time: ',(time.time()-stTime))
    timeString=timeString+str((time.time()-stTime))+' '
####


    csp=copy.deepcopy(cspTmp)
    constraintList=copy.deepcopy(constraintListTmp)


#AC-4 execution time and domain reduction
    stTime=time.time()
    print("\nAC-4")
    AC_4()
    count4=0
    temp=0
    for val in csp.keys():
        count4=count4+len(csp[val][0])
        

    print('Time: ',(time.time()-stTime))
    timeString=timeString+str((time.time()-stTime))
####

#writing exe time and number of domain reduction in file
    file_domain.write(str(number)+' '+str(totalCount-count1)+' '+str(totalCount-count2)+' '+str(totalCount-count3)+' '+str(totalCount-count4)+'\n')
    file_exeTime.write(timeString+'\n')

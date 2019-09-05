import queue
import math
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



# print(constraintList)

#file=open("input.txt",'r')





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



def AC_3():
    
    q= queue.Queue()

    for i in range(0,len(constraintList)):
        q.put(constraintList[i])

    while q.empty() == False :
        arc=q.get()
        if revise(arc) == True:
            Di=len(csp[arc[0]][0])
            if Di==0:
                return False
           
            for i in range(0,len(csp[arc[0]][1])):
                for k in range(0,len(constraintList)):

                    if constraintList[k][0]==arc[0]:
                        if constraintList[k][2]==arc[2]:
                            continue
                    
                        if(constraintList[k][1]=='>'):
                            
                            strh=(constraintList[k][2],'<',constraintList[k][0])
                            q.put(strh)

                        elif(constraintList[k][1]=='<'):
                            
                            strh=(constraintList[k][2],'>',constraintList[k][0])
                            #print(strh)
                            q.put(strh)
                        
                        elif(constraintList[k][1]=='!'):
                            strh=(constraintList[k][2],'!',constraintList[k][0])
                            #print(strh)
                            q.put(strh)

                        elif(constraintList[k][1]=='^'):    # ^ used for square 
                            
                            strh=(constraintList[k][2],'*',constraintList[k][0])
                            #print(strh)
                            q.put(strh)

                        elif(constraintList[k][1]=='+'):    # ^ used for X=Y+2 
                            
                            strh=(constraintList[k][2],'-',constraintList[k][0])
                            #print(strh)
                            q.put(strh)

                        elif(constraintList[k][1]=='-'):    # ^ used for Y=X-2
                            
                            strh=(constraintList[k][2],'+',constraintList[k][0])
                            #print(strh)
                            q.put(strh)

                        elif(constraintList[k][1]=='*'):    # ^ used for square root 
                            
                            strh=(constraintList[k][2],'^',constraintList[k][0])
                            #print(strh)
                            q.put(strh)

            
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
    print(AC_3())

    for val in csp.keys():
        print(csp[val][0])
    print('Time: ',time.time()-stTime)








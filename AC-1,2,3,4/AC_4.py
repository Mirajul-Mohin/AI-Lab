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

Q=queue.Queue()
S={}
counter={}

def AC_4():
    
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


                if len(csp[first][0])==0:      #added later
                        return False
    
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


                    if len(csp[vi][0])==0:      #added later
                        return False

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
    print(AC_4())

    for val in csp.keys():
        print(csp[val][0])
    print('Time: ',time.time()-stTime)


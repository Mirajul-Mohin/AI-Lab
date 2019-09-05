import numpy as np

N=10

file=open("Test_028.txt",'w')
for variableSize in range(10,301,10):
    constraintList=[]
    edgeExist=False
    dom={}
    edgeNumber =1.5*variableSize
    edge=1
    X=[]

    for i in range(1,variableSize+1):
        X.append(i)


    while (edge<=edgeNumber):
        n1=np.random.randint(1,variableSize+1)
        n2=np.random.randint(1,variableSize+1) 
        if n1==n2:
            continue
            
        for val in constraintList:
            if (val[0]==str(n1) and val[2]==str(n2)) or (val[0]==str(n2) and val[2]==str(n1)):
                edgeExist=True
                break

        if edgeExist==False:
            cons=np.random.randint(1,4)
            edge+=1

            dom[n1]=[]
            dom[n2]=[]

            sizeOfDomain1=np.random.randint(5,36)
            sizeOfDomain2=np.random.randint(5,36) 
            itr=1

            while itr<=sizeOfDomain1:
                valueOfDomain=np.random.randint(1,101)
                if valueOfDomain not in dom[n1]:
                    dom[n1].append(valueOfDomain)
                    itr+=1
            itr=1

            while itr<=sizeOfDomain2:
                valueOfDomain=np.random.randint(1,101)
                if valueOfDomain not in dom[n2]:
                    dom[n2].append(valueOfDomain)
                    itr+=1

            if (max(dom[n1])<15 and min(dom[n2])>=15):
                constraintList.append((str(n1),'^',str(n2)))
                constraintList.append((str(n2),'*',str(n1)))

            elif (max(dom[n2])<15 and min(dom[n1])>=15):
                constraintList.append((str(n1),'*',str(n2)))
                constraintList.append((str(n2),'^',str(n1)))

            elif cons==1:
                constraintList.append((str(n1),'>',str(n2)))
                constraintList.append((str(n2),'<',str(n1)))

            elif cons==2:
                constraintList.append((str(n1),'<',str(n2)))
                constraintList.append((str(n2),'>',str(n1)))

            elif cons==3:
                constraintList.append((str(n1),'!',str(n2)))
                constraintList.append((str(n2),'!',str(n1)))

        edgeExist=False

    file.write(str(variableSize)+'\n')

    for val in X:
        if val not in dom.keys():
            dom[val]=[]
            sizeOfDomain=np.random.randint(5,36)
            itr=1

            while itr<=sizeOfDomain:
                valueOfDomain=np.random.randint(1,101)
                if valueOfDomain not in dom[val]:
                    dom[val].append(valueOfDomain)
                    itr+=1

        file.write(str(val))

        for value in dom[val]:
            file.write(' '+str(value))
        file.write('\n')

    file.write(str(len(constraintList))+'\n')
    for val in constraintList:
        file.write(val[0]+' '+val[2]+ ' '+val[1]+'\n')


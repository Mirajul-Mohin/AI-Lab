from munkres import Munkres, print_matrix, make_cost_matrix
import sys
import random

counter = 0
L = []
A = []
M = []
e = []
flag=True
available_vertex = []
V_matrix = []
temp = []
H_matrix = []



n = raw_input("Enter n: ")
n=int(n)

c = raw_input("Enter c: ")
c = int(c)
for i in range(0,n):
    available_vertex.append(i)

print("Enter Valuation matrix (cn x n):")
for i in range(0,c*n):
    for j in range(0,n):
        x = raw_input()
        x=int(x)
        temp.append(x)
        
    V_matrix.append(temp)
    temp = []
print('Valuation:')
for val in V_matrix:    
    print(val)



print("Enter Happiness matrix (cn x cn):")
for i in range(0,c*n):
    for j in range(0,c*n):
        x = raw_input()
        x=int(x)
        temp.append(x)
        
    H_matrix.append(temp)
    temp = []
print('Happiness:')
for val in H_matrix:    
    print(val)


########  Start Hungarian method 
def hungarian(valu_mat,str):
    global counter
    global L
    global A
    global M
    global e
    global flag
    global available_vertex
    global V_matrix
    global temp
    cost_matrix = make_cost_matrix(valu_mat, lambda cost: sys.maxint - cost)
    m = Munkres()
    indexes = m.compute(cost_matrix)
    print_matrix(valu_mat, msg=str)
    total = 0
    for row, column in indexes:
        value = valu_mat[row][column]
        total += value
        print '(%d, %d) -> %d' % (row, column, value)
        M.append((row,column))
    print 'total profit=%d' % total

######### End Hungarian Method


def OnlineMatching(str):
    
    global counter
    global L
    global A
    global M
    global e
    global flag
    global available_vertex
    global H_matrix
    global V_matrix

    print(str)
    for i in range(0,n):
        v=raw_input()
        v = int(v)

        L.append(v)
        counter = counter +1

        if counter >= n/5 :
            for val in M:
                if val[0] == v:
                    e.append(val)
                    #print(e[0])
            
            if(len(A) != 0 and len(e)!= 0): 
                for val in A:
                    if val[1] == e[0][1]:
                        flag = False
            
            if flag == True and len(e) != 0:
                A.append(e[0])
                available_vertex.remove(e[0][1])
                e.pop()
                

            else:
                v_prime = random.choice(available_vertex)
                A.append((v,v_prime))
                available_vertex.remove(v_prime)
                if len(e) !=0:
                    e.pop()
                #print("Is in else")

            flag=True


        else:
            v_prime = random.choice(available_vertex)
            A.append((v,v_prime))
            
            available_vertex.remove(v_prime)


        print("Current Allocation: ",A)
          
    return A

hungarian(V_matrix,'Lowest cost through this matrix:')


M1 = OnlineMatching("Input First N agent in any order")

def OnlineRoommate(t,str):
    global counter
    global L
    global A
    global M
    global e
    global flag
    global available_vertex
    global V_matrix
    global H_matrix

    for i in range(t,t+n):
    
        for r in range(0,n):
            for val in A:
                if (val[1]==r):
                    temp=val
                    break;

            V_matrix[i][r] = V_matrix[i][r] + H_matrix[i][temp[0]] + H_matrix[temp[0]][i]

    
    
    L=[]
    counter=0
    A=[]
    M=[]
    e=[]
    flag=True
    for i in range(0,n):
        available_vertex.append(i)
    
    hungarian(V_matrix,'\nLowest cost after adding Happiness value:')
    #print(M)
    C=OnlineMatching(str)
    return C


for g in range(1,c):
    M2 = OnlineRoommate(n*g,'Input '+str(g+1)+'th N agent in any order')
    for val in M2:
        M1.append(val)
    M2=[]
print(M1)

temp=[]
map={}
for t in range(0,n):
    for val in M1:
        if(val[1]==t):
            temp.append(val[0])
    print(temp, ' ---> ',t)
    temp=[]

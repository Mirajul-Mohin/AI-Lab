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

for i in range(0,n):
    available_vertex.append(i)

print("Enter Valuation matrix (2n x n):")
for i in range(0,2*n):
    for j in range(0,n):
        x = raw_input()
        x=int(x)
        temp.append(x)
        
    V_matrix.append(temp)
    temp = []
print('Valuation:')
for val in V_matrix:    
    print(val)



print("Enter Happiness matrix (2n x 2n):")
for i in range(0,2*n):
    for j in range(0,2*n):
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

hungarian(V_matrix,'Maximum Valuation through Valuation matrix:')


M1 = OnlineMatching("Input First N agent in any order")

def OnlineRoommate():
    global counter
    global L
    global A
    global M
    global e
    global flag
    global available_vertex
    global V_matrix
    global H_matrix

    for i in range(n,2*n):
    
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
    
    hungarian(V_matrix,'\nMaximum Valuation after adding Happiness value:')
    #print(M)
    C=OnlineMatching("Input Second N agent in any order")
    return C

    
    
M2 = OnlineRoommate()

print("Final Assignment: ")
for val in M1:
    for ad in M2:
        if(val[1]==ad[1]):
            print('('+str(val[0])+','+str(ad[0])+')'+'->'+str(val[1]))

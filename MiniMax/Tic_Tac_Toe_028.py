from random import choice
import time
from os import system
from math import inf as infinity
import platform



board = [[0, 0, 0],[0, 0, 0],[0, 0, 0],]
HUMAN = -1
COMP = +1



def evaluate(state):
  

    if wins(state, HUMAN):
        score = -1
        return score

    elif wins(state, COMP):
        score = +1
        return score
    
    else:
        score = 0
        return score

    return score


def wins(state, player):
   
    row1=[state[0][0], state[0][1], state[0][2]]
    row2=[state[1][0], state[1][1], state[1][2]]
    row3=[state[2][0], state[2][1], state[2][2]]
    col1=[state[0][0], state[1][0], state[2][0]]
    col2=[state[0][1], state[1][1], state[2][1]]
    col3=[state[0][2], state[1][2], state[2][2]]
    dig1=[state[0][0], state[1][1], state[2][2]]
    dig2=[state[2][0], state[1][1], state[0][2]]


    win_state = [row1,col1,row2,col2,row3,col3,dig1,dig2]

    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    
    c_win=wins(state,COMP)
    if c_win:
        return wins(state, COMP)
    return wins(state,HUMAN)


def empty_cells(state):
    
    cells = []


    for row in range(0, len(board)):
        length=len(board[row])
        for col in range(0,len(board[row])):
            
            if board[row][col]==0:
                cells.append([row,col])

    return cells


def valid_move(x, y):
   
    move=False
    listt=empty_cells(board)
    if [x, y] not in listt:
        return move
    else:
        move=True
        return move


def set_move(x, y, player):
   
    if valid_move(x, y)==False:
        return False
        
    elif valid_move(x, y)==True:
        board[x][y] = player
        return True


def minimax(state, depth, player):
   
    if player == HUMAN:
        best = [-1, -1, +infinity]
    elif player==COMP:
        best = [-1, -1, -infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        l=[-1, -1, score]
        return l

    for cell in empty_cells(state):
        x = cell[0]
        y = cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0] = x
        score[1] = y

        if (player==HUMAN ) and (score[2] < best[2]):
            best = score
        elif (player==COMP) and score[2] > best[2]:
            best=score


    return best





def render(state, c_choice, h_choice):
   

    chars = {-1: h_choice,+1: c_choice,0: ' '}

    print('\n' + '---------------')


    for row in range(0, len(board)):
        for col in range(0,len(board[row])):
            symbol = chars[board[row][col]]
            print(f'| {symbol} |', end='')
        print('\n' + '---------------')
            
      

def ai_turn(c_choice, h_choice):
  
    depth = len(empty_cells(board))
    if len(empty_cells(board)) == 0:
        return
    if game_over(board):
        return
    
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth != 9:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]
        
    elif depth==9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        

    set_move(x, y, COMP)
    time.sleep(1)

 


def human_turn(c_choice, h_choice):
 
    depth = len(empty_cells(board))
    if len(empty_cells(board)) == 0:
        return
    if game_over(board):
        return

    
    moves = {1: [0, 0], 2: [0, 1], 3: [0, 2],4: [1, 0], 5: [1, 1], 6: [1, 2],7: [2, 0], 8: [2, 1], 9: [2, 2],}
    move = -1
    print(f'Human turn [{h_choice}]')
    flag=True
    coor=[]
    render(board, c_choice, h_choice)

    while(1):
        if(move < 1 or move > 9):
            try:
                move = (input('Use number [1,9]: '))
                move = int(move)
                coord = moves[move]
                flag = set_move(coord[0], coord[1], HUMAN)
                can_move=flag
                if not can_move:
                    print('Bad move')
                    move = -1
         
            except (KeyError, ValueError):
                print('Bad choice')

        else:
            break


def main():
  
    
    h_choice = ''  
    c_choice = ''  
    first = ''  

    h_choice='x'
    c_choice='o'


    print('You will use x for move')

    while(1):
        first = input('Want to start first? [y/n]: ').upper()
        if (first =='Y' or first == 'N'):
            break
        
        else:
            print('Bad Input')
            continue


    while(1):
        if(len(empty_cells(board)) > 0 and not game_over(board)):
            if first == 'Y':
                human_turn(c_choice, h_choice)
                first = ''

            ai_turn(c_choice, h_choice)
            human_turn(c_choice, h_choice)

        else:
            break


    if wins(board, COMP):
        print(f'Computer turn [{c_choice}]')
        render(board, c_choice, h_choice)
        print('YOU LOSE!')

    elif wins(board, HUMAN):
        print(f'Human turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    
    else:
        
        render(board, c_choice, h_choice)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()
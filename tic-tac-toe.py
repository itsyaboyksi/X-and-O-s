import itertools

def game_play(game):


    def check(l):
        if l.count(l[0])==len(l) and l[0]!=0:
            return True
        else:
            return False    

    #Front Diagonal
    front_diags=[]
    for i in range(len(game)):
        front_diags.append(game[i][i])
    if check(front_diags):
        print(f"Player {front_diags[0]} is the winner diagonally (\\)!")
        return True

    #Back Diagonal
    back_diags=[]
    for rows,cols in enumerate(reversed(range(len(game)))):
        back_diags.append(game[rows][cols])
    if check(back_diags):
       print(f"Player {back_diags[0]} is the winner diagonally (/)!")
       return True

    #Horizontal Match
    for i in game:
        print(i)
        if check(i):
            print(f"Player {i[0]} is the winner horizontally!")
            return True

    #Verticle Match
    for j in range(len(game)):
        a=[]
        for i in game:
            a.append(i[j])
        if check(a):
            print(f"Player {a[0]} is the winner vertically!")
            return True
    return False

def game_board(board,player=0,row=0,column=0, just_display=False):


    try:
        if board[row][column]!=0:
            print("This position is occupied!")
            return board, False
        print("   "+"  ".join([str(i) for i in range(len(board))]))
        if not just_display:
            board[row][column]=player
        for i in enumerate(board):
                print(*i)
        return board, True 
    
    except IndexError as e:
        print("Error: Make sure your input row/column as 0, 1 or 2?", e)
        return board, False
    
    except Exception as e:
        print("Something went wrong!", e)
        return board, False

play=True
players=[1,2]

while play:
    board=int(input("What size game of tic-tac-toe you want to play?"))
    board=[[0 for i in range(board)] for i in range(board)]
    game_won=False
    board, _ =game_board(board, just_display=True)
    player_p=itertools.cycle([1,2])
    
    while not game_won:
        curr=next(player_p)
        print(f"Current Player: {curr}")
        played=False
        
        while not played:
            column=int(input("Enter The Column where you want to place the value:"))
            row=int(input("Enter The Row where you want to place the value:"))
            game, played=game_board(board, curr,row, column)
        
        if game_play(board):
            game_won=True
            restart=input("Do you want to play again? (y/n)")
            
            if restart.lower()=="y":
                print("Restarting.....")
            
            elif restart.lower()=="n":
                print("Byeeeeeeeeeeeee")
                play=False
            
            else:
                print("Invalid input, See ya later aligator")
                play=False   
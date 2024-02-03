
class Board():
    def __init__(self):
        self.ceills = [" "," "," "," "," "," "," "," "," "," ",]
    def diplay(self):
        print(f" {self.ceills[1]}  |  {self.ceills[2]}  |  {self.ceills[3]} ")
        print("------------------")    
        print(f" {self.ceills[4]}  |  {self.ceills[5]}  |  {self.ceills[6]} ")
        print("------------------")    
        print(f" {self.ceills[7]}  |  {self.ceills[8]}  |  {self.ceills[9]} ")
        print("------------------")    
    def update_cell(self , x_chois , player):
        if self.ceills[x_chois] == " ":
            self.ceills[x_chois] = player
    def is_winner(self,player):
       for coll in [[1,2,3] , [4,5,6],[7,8,9] , [1,4,7] , [2,5,8] , [3,6,9] , [1,5,9] , [3,5,7]]:
            result = True
            for col in coll:
                if self.ceills[col] != player:
                    result = False
            if result == True:
                return True
       return False    
    def reset(self):
        self.ceills=[" "," "," "," "," "," "," "," "," "," ",]
    def is_tie(self):
        used_cells = 0 
        for cells in self.ceills :
            if cells != " ":
                used_cells+=1
            if used_cells == 9:
                return True
            else:
                return False
                   
    def ai_move(self , player):
        
        if player == "X":
            enemy = "O"
        if player == "O":
            enemy = "X"
              
        #random choise
        for i in range(1,10):
            if self.ceills[i] == " ":
                self.update_cell(i, player)
                break
        
board =  Board()

def print_header():
    print ("Tic-Tac-Toe Game > ")

def refresh_screen():
       print_header()
       board.diplay()

while True:
    refresh_screen()
    x_chois= int(input("X) Please Choise Number between 1 >  9 |"))
    board.update_cell(x_chois ,  "X")
    
    if board.is_winner('X'):
        print("\nX Wins \n")
        play_again = input("Do You want Play another game (Y/N)").upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
           break
    if board.is_tie():
             print("\n Tie Game \n")
             play_again = input("Do You want Play another game (Y/N)").upper()
             if play_again == 'Y':
                 board.reset()
                 continue
             else:
                break     
    board.ai_move("O")
    refresh_screen()      


   # o_chois= int(input("O) Please Choise Number between 1 >  9|"))
    # board.update_cell(o_chois ,  "O")   
    if board.is_winner('O'):
           print("\n O Wins \n")
           play_again = input("Do You want Play another game (Y/N)").upper()
           if play_again == 'Y':
               board.reset()
               continue
           else:
              break   
    if board.is_tie():
          print("\n Tie Game! \n")
          play_again = input("Do You want Play another game (Y/N)").upper()
          if play_again == 'Y':
              board.reset()
              continue
          else:
             break      

import tkinter
import os

class Sokoban:
    def __init__(self, level):
        self.level=level
        self.x, self.y=self.getCurrentPosition()
        
        os.system("clear")
        self.display()

    def display(self):
        for i in range(0, len(self.level)):
            for j in range(0, len(self.level[0])):
                if(self.level[i][j]=='W'):
                    print('▩', ' ', end='') 
                elif(self.level[i][j]=='P'):
                    print('☖', ' ', end='')
                elif(self.level[i][j]=='T'):
                    print('☖', ' ', end='')
                elif(self.level[i][j]=='B'):
                    print('▢', ' ', end='')
                elif(self.level[i][j]=='G'):
                    print('•', ' ', end='')
                elif(self.level[i][j]=='C'):
                    print('⊠', ' ', end='')
                else:
                    print(' ', ' ', end='')
            print('')
        print('')


    def getCurrentPosition(self):
        for i in range(0, len(self.level)):
            for j in range(0, len(self.level[0])):
                if(self.level[i][j]=='P'):
                    return i, j
    

    def move_player_up(self):
        if(self.level[self.x][self.y]=='P'):                    #If Player is on an Empty Space
            self.level[self.x][self.y]=' '
        elif(self.level[self.x][self.y]=='T'):                  #If Player is on a Goal
            self.level[self.x][self.y]='G'
        self.x=self.x-1

    def up(self):
        if self.level[self.x-1][self.y]==' ':                   #If top tile is an Empty Space
            self.level[self.x-1][self.y]='P'
            self.move_player_up()
            return True
        
        elif self.level[self.x-1][self.y]=='G':                 #If top tile is a Goal tile
            self.level[self.x-1][self.y]='T'
            self.move_player_up()
            return True

        elif self.level[self.x-1][self.y]=='W':                 #If top tile is a Wall
            return False

        elif self.level[self.x-1][self.y]=='B':                 #If top tile is a Box
            if self.level[self.x-2][self.y]==' ':                   #If tile above Box is an Empty Space
                self.level[self.x-2][self.y]='B'
                self.level[self.x-1][self.y]='P'
                self.move_player_up()
                return True

            elif self.level[self.x-2][self.y]=='G':                 #If tile above Box is a Goal
                self.level[self.x-2][self.y]='C'
                self.level[self.x-1][self.y]='P'
                self.move_player_up()
                return True

            elif self.level[self.x-2][self.y] in ['W', 'B', 'C']:   #If tile above Box is a Wall, another Box, or Box@Goal
                return False

        elif self.level[self.x-1][self.y]=='C':                 #If top tile is a Box@Goal
            if self.level[self.x-2][self.y]==' ':                   #If tile above Box@Goal is an Empty Space
                self.level[self.x-2][self.y]='B'
                self.level[self.x-1][self.y]='T'
                self.move_player_up()
                return True

            elif self.level[self.x-2][self.y]=='G':                 #If tile above Box@Goal is a Goal
                self.level[self.x-2][self.y]='C'
                self.level[self.x-1][self.y]='T'
                self.move_player_up()
                return True

            elif self.level[self.x-2][self.y] in ['W', 'B', 'C']:    #If tile above Box@Goal is a Wall, another Box, or Box@Goal
                return False
            
    def move_player_down(self):
        if(self.level[self.x][self.y]=='P'):                    #If Player is on an Empty Space
            self.level[self.x][self.y]=' '
        elif(self.level[self.x][self.y]=='T'):                  #If Player is on a Goal
            self.level[self.x][self.y]='G'
        self.x=self.x+1
    
    def down(self):
        if self.level[self.x+1][self.y]==' ':                   #If top tile is an Empty Space
            self.level[self.x+1][self.y]='P'
            self.move_player_down()
            return True
        
        elif self.level[self.x+1][self.y]=='G':                 #If top tile is a Goal tile
            self.level[self.x+1][self.y]='T'
            self.move_player_down()
            return True

        elif self.level[self.x+1][self.y]=='W':                 #If top tile is a Wall
            return False

        elif self.level[self.x+1][self.y]=='B':                 #If top tile is a Box
            if self.level[self.x+2][self.y]==' ':                   #If tile above Box is an Empty Space
                self.level[self.x+2][self.y]='B'
                self.level[self.x+1][self.y]='P'
                self.move_player_down()
                return True

            elif self.level[self.x+2][self.y]=='G':                 #If tile above Box is a Goal
                self.level[self.x+2][self.y]='C'
                self.level[self.x+1][self.y]='P'
                self.move_player_down()
                return True

            elif self.level[self.x+2][self.y] in ['W', 'B', 'C']:   #If tile above Box is a Wall, another Box, or Box@Goal
                return False

        elif self.level[self.x+1][self.y]=='C':                 #If top tile is a Box@Goal
            if self.level[self.x+2][self.y]==' ':                   #If tile above Box@Goal is an Empty Space
                self.level[self.x+2][self.y]='B'
                self.level[self.x+1][self.y]='T'
                self.move_player_down()
                return True

            elif self.level[self.x+2][self.y]=='G':                 #If tile above Box@Goal is a Goal
                self.level[self.x+2][self.y]='C'
                self.level[self.x+1][self.y]='T'
                self.move_player_down()
                return True

            elif self.level[self.x+2][self.y] in ['W', 'B', 'C']:    #If tile above Box@Goal is a Wall, another Box, or Box@Goal
                return False

    def move_player_left(self):
        if self.level[self.x][self.y]=='P':                     #If Player is on an Empty Space
            self.level[self.x][self.y]=' '
        elif self.level[self.x][self.y]=='T':                   #If Player is on a Goal
            self.level[self.x][self.y]='G'
        self.y=self.y-1

    def left(self):
        if self.level[self.x][self.y-1]==' ':                   #If left tile is an Empty Space
            self.level[self.x][self.y-1]='P'
            self.move_player_left()
            return True

        elif self.level[self.x][self.y-1]=='G':                 #If left tile is a Goal
            self.level[self.x][self.y-1]='T'
            self.move_player_left()
            return True
        
        elif self.level[self.x][self.y-1]=='W':
            return False
        
        elif self.level[self.x][self.y-1]=='B':                 #If left tile is a Box
            if self.level[self.x][self.y-2]==' ':                   #If tile left of Box is an Empty Space
                self.level[self.x][self.y-2]='B'
                self.level[self.x][self.y-1]='P'
                self.move_player_left()
                return True

            elif self.level[self.x][self.y-2]=='G':                 #If tile left of Box is a Goal
                self.level[self.x][self.y-2]='C'
                self.level[self.x][self.y-1]='P'
                self.move_player_left()
                return True
            
            elif self.level[self.x][self.y-2] in ['W', 'B', 'C']:   #If tile left of Box is a Wall, another Box, or Box@Goal
                return False
        
        elif self.level[self.x][self.y-1]=='C':                 #If left tile is a Box@Goal
            if self.level[self.x][self.y-2]==' ':                   #If tile left of Box@Goal is an Empty Space
                self.level[self.x][self.y-2]='B'
                self.level[self.x][self.y-1]='T'
                self.move_player_left()
                return True
            
            elif self.level[self.x][self.y-2]=='G':                 #If tile left of Box@Goal is a Goal
                self.level[self.x][self.y-2]='C'
                self.level[self.x][self.y-1]='T'
                self.move_player_left()
                return True
            
            elif self.level[self.x][self.y-2] in ['W', 'B', 'C']:   #If tile left of Box@Goal is a Wall, Box, or Box@Goal
                return False
    

    def move_player_right(self):
        if self.level[self.x][self.y]=='P':                     #If Player is on an Empty Space
            self.level[self.x][self.y]=' '
        elif self.level[self.x][self.y]=='T':                   #If Player is on a Goal
            self.level[self.x][self.y]='G'
        self.y=self.y+1
            
    def right(self):
        
        if self.level[self.x][self.y+1]==' ':                   #If right tile is an Empty Space
            self.level[self.x][self.y+1]='P'
            self.move_player_right()
            return True

        elif self.level[self.x][self.y+1]=='G':                 #If right tile is a Goal
            self.level[self.x][self.y+1]='T'
            self.move_player_right()
            return True
        
        elif self.level[self.x][self.y+1]=='W':
            return False
        
        elif self.level[self.x][self.y+1]=='B':                 #If right tile is a Box
            if self.level[self.x][self.y+2]==' ':                   #If tile right of Box is an Empty Space
                self.level[self.x][self.y+2]='B'
                self.level[self.x][self.y+1]='P'
                self.move_player_right()
                return True

            elif self.level[self.x][self.y+2]=='G':                 #If tile right of Box is a Goal
                self.level[self.x][self.y+2]='C'
                self.level[self.x][self.y+1]='P'
                self.move_player_right()
                return True
            
            elif self.level[self.x][self.y+2] in ['W', 'B', 'C']:   #If tile right of Box is a Wall, another Box, or Box@Goal
                return False
        
        elif self.level[self.x][self.y+1]=='C':                 #If right tile is a Box@Goal
            if self.level[self.x][self.y+2]==' ':                   #If tile right of Box@Goal is an Empty Space
                self.level[self.x][self.y+2]='B'
                self.level[self.x][self.y+1]='T'
                self.move_player_right()
                return True
            
            elif self.level[self.x][self.y+2]=='G':                 #If tile right of Box@Goal is a Goal
                self.level[self.x][self.y+2]='C'
                self.level[self.x][self.y+1]='T'
                self.move_player_right()
                return True
            
            elif self.level[self.x][self.y+2] in ['W', 'B', 'C']:   #If tile right of Box@Goal is a Wall, Box, or Box@Goal
                return False




# P ☖ Player
# T ☖ Player on top of Goal
#   Empty Space
# G • Goal
# W ▩ Wall 
# B ▢ Box
# C ⊠ Box@Goal


level=[[' ', ' ', 'W', 'W', 'W', 'W', 'W', ' '],
       ['W', 'W', 'W', ' ', ' ', ' ', 'W', ' '],
       ['W', 'G', 'P', 'B', ' ', ' ', 'W', ' '],
       ['W', 'W', 'W', ' ', 'B', 'G', 'W', ' '],
       ['W', 'G', 'W', 'W', 'B', ' ', 'W', ' '],
       ['W', ' ', 'W', ' ', 'G', ' ', 'W', 'W'],
       ['W', 'B', ' ', 'C', 'B', 'B', 'G', 'W'],
       ['W', ' ', ' ', ' ', 'G', ' ', ' ', 'W'],
       ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]


game=Sokoban(level)  

window = tkinter.Tk()
window.geometry("0x0")
window.resizable('False', 'False')

def up(event):
    os.system("clear")
    game.up()
    game.display()

def down(event):
    os.system("clear")
    game.down()
    game.display()

def left(event):
    os.system("clear")
    game.left()
    game.display()

def right(event):
    os.system("clear")
    game.right()
    game.display()

def exit_game(event):
    window.destroy()
    os.system("clear")

def restart_game(event):
    window.destroy()
    os.system("clear")
    os.system("python3 Sokoban.py")

window.bind("w", up)
window.bind("s", down)
window.bind("a", left)
window.bind("d", right)

window.bind("<Up>", up)
window.bind("<Down>", down)
window.bind("<Left>", left)
window.bind("<Right>", right)

window.bind("<space>", restart_game)
window.bind("<Escape>", exit_game)
    
window.mainloop()


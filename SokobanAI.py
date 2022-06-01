from cmath import inf
import random
import tkinter
import os
import time
import sys
import copy

class Sokoban:
    def __init__(self, level_no):
        self.level_no=level_no
        self.update_level(level_no)
              
        self.x, self.y=self.get_current_position()
        
        self.cost=0
        self.prev_state=None
        
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
                    print('◆', ' ', end='')
                else:
                    print(' ', ' ', end='')
            print('')
        print("========================================================================================")
        self.is_goal_reached()


    def is_goal_reached(self):
        for i in range(0, len(self.level)):
            for j in range(0, len(self.level[i])):
                if self.level[i][j] in ['G', 'T']:
                    return False
        return True

    def update_level(self, level_no):
        self.level_no=level_no

        # P ☖ Player
        # T ☖ Player on top of Goal
        #     Empty Space
        # G • Goal
        # W ▩ Wall 
        # B ▢ Box
        # C ◆ Box@Goal

        if level_no==1:
            self.level=[['W', 'W', 'W', 'W', 'W', 'W'],
                        ['W', 'W', 'W', ' ', ' ', 'W'],
                        ['W', ' ', 'B', 'G', ' ', 'W'],
                        ['W', ' ', 'B', 'G', ' ', 'W'],
                        ['W', 'P', ' ', ' ', 'W', 'W'],
                        ['W', 'W', 'W', 'W', 'W', 'W']]
        elif level_no==2:    
            self.level=[['W', 'W', 'W', 'W', 'W', 'W', 'W'],
                        ['W', 'G', 'W', 'W', 'W', 'G', 'W'],
                        ['W', ' ', 'B', 'P', 'B', ' ', 'W'],
                        ['W', ' ', ' ', ' ', ' ', ' ', 'W'],
                        ['W', ' ', 'B', ' ', 'B', ' ', 'W'],
                        ['W', 'G', 'W', 'W', 'W', 'G', 'W'],
                        ['W', 'W', 'W', 'W', 'W', 'W', 'W']]
        elif level_no==3:    
            self.level=[['W', 'W', 'W', 'W', 'W', 'W', 'W'],
                        ['W', 'G', ' ', 'W', ' ', 'P', 'W'],
                        ['W', ' ', ' ', 'W', 'B', ' ', 'W'],
                        ['W', 'G', ' ', ' ', 'B', ' ', 'W'],
                        ['W', ' ', ' ', 'W', 'B', ' ', 'W'],
                        ['W', 'G', ' ', 'W', ' ', ' ', 'W'],
                        ['W', 'W', 'W', 'W', 'W', 'W', 'W']]
        elif level_no==4:
            self.level=[['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                        ['W', 'G', 'G', 'G', ' ', 'W', 'W', 'W'],
                        ['W', ' ', 'G', ' ', 'B', ' ', ' ', 'W'],
                        ['W', ' ', ' ', 'B', 'B', 'B', ' ', 'W'],
                        ['W', 'W', 'W', 'W', ' ', ' ', 'P', 'W'],
                        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]
        elif level_no==5:
            self.level=[[' ', ' ', 'W', 'W', 'W', 'W', 'W', ' '],
                        ['W', 'W', 'W', ' ', ' ', ' ', 'W', ' '],
                        ['W', 'G', 'P', 'B', ' ', ' ', 'W', ' '],
                        ['W', 'W', 'W', ' ', 'B', 'G', 'W', ' '],
                        ['W', 'G', 'W', 'W', 'B', ' ', 'W', ' '],
                        ['W', ' ', 'W', ' ', 'G', ' ', 'W', 'W'],
                        ['W', 'B', ' ', 'C', 'B', 'B', 'G', 'W'],
                        ['W', ' ', ' ', ' ', 'G', ' ', ' ', 'W'],
                        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]
        elif level_no==6:
            self.level=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', 'W', ' ', ' ', ' ', 'W', ' ', 'W', ' ', 'W', ' ', 'W', ' ', 'W', ' ', ' ', ' ', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', 'W', ' ', 'B', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', 'W', 'W', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', 'W', 'W', 'W', ' ', 'B', 'W', ' ', 'W', ' ', ' ', 'W', ' ', 'W', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                        [' ', ' ', 'W', ' ', ' ', 'B', ' ', ' ', 'W', ' ', ' ', 'B', 'W', ' ', 'W', ' ', 'B', 'B', ' ', 'W', ' ', ' ', ' ', 'W', ' ', 'W', ' ', ' ', 'W'],
                        [' ', 'W', 'W', ' ', 'W', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 'W', ' ', ' ', ' ', ' ', 'B', ' ', 'W', ' ', 'W', ' ', ' ', 'W'],
                        [' ', 'W', ' ', ' ', 'W', 'B', ' ', ' ', ' ', 'W', ' ', 'W', 'W', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', 'B', 'B', 'W', ' ', 'W', ' ', ' ', 'W'],
                        [' ', 'W', ' ', ' ', ' ', ' ', 'B', 'W', 'W', ' ', 'B', ' ', ' ', 'W', ' ', ' ', ' ', 'W', 'W', ' ', 'B', ' ', ' ', 'W', ' ', 'W', ' ', 'W', 'W'],
                        ['W', 'W', 'W', 'W', 'B', ' ', 'B', ' ', 'W', ' ', ' ', ' ', ' ', 'W', 'W', ' ', ' ', 'W', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', 'G', 'G', 'W'],
                        ['W', ' ', ' ', 'W', ' ', ' ', ' ', ' ', 'W', 'W', 'W', ' ', 'W', ' ', 'B', ' ', 'B', ' ', 'W', 'W', 'W', ' ', ' ', 'W', 'W', 'W', 'G', 'C', 'W'],
                        ['W', ' ', ' ', ' ', ' ', ' ', 'W', 'W', ' ', ' ', 'B', 'B', ' ', 'P', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 'G', 'G', 'G', 'G', 'W'],
                        ['W', ' ', ' ', 'W', 'W', ' ', ' ', 'W', 'W', ' ', ' ', ' ', 'B', ' ', ' ', 'W', 'B', 'W', ' ', ' ', 'W', 'W', 'G', 'G', 'G', 'G', 'C', 'G', 'W'],
                        ['W', 'W', ' ', 'W', ' ', ' ', 'B', ' ', ' ', 'W', ' ', 'W', ' ', 'B', 'W', 'W', ' ', ' ', 'W', 'W', 'G', 'G', 'G', 'G', 'C', 'G', 'W', 'W', 'W'],
                        ['W', 'W', ' ', 'W', 'W', ' ', ' ', 'B', ' ', ' ', 'W', ' ', 'B', ' ', 'W', ' ', ' ', 'W', 'G', 'G', 'G', 'G', 'C', 'G', 'W', 'W', 'W', ' ', ' '],
                        ['W', ' ', ' ', ' ', ' ', 'B', ' ', 'W', 'W', 'W', 'W', ' ', ' ', ' ', 'W', ' ', 'G', 'G', 'G', 'G', 'C', 'G', 'W', 'W', 'W', ' ', ' ', ' ', ' '],
                        ['W', ' ', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'G', 'G', 'C', 'G', 'W', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' '],
                        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.x, self.y=self.get_current_position()
        


    def get_current_position(self):
        for i in range(0, len(self.level)):
            for j in range(0, len(self.level[0])):
                if(self.level[i][j]=='P'):
                    return i, j
       
    
    def __gt__(self, other):
        return self.heuristic()>other.heuristic()

    def __lt__(self, other):
        return self.heuristic()<other.heuristic()

    def __eq__(self, other):
        return self.level==other.level

    def move_player_up(self):
        if(self.level[self.x][self.y]=='P'):                    #If Player is on an Empty Space
            self.level[self.x][self.y]=' '
        elif(self.level[self.x][self.y]=='T'):                  #If Player is on a Goal
            self.level[self.x][self.y]='G'
        self.x=self.x-1

    def up(self):
        if self.level[self.x-1][self.y]==' ':                   #If top tile is an Empty Space
            self.prev_state=copy.deepcopy(self)
            self.level[self.x-1][self.y]='P'
            self.move_player_up()
            return True
        
        elif self.level[self.x-1][self.y]=='G':                 #If top tile is a Goal tile
            self.prev_state=copy.deepcopy(self)
            self.level[self.x-1][self.y]='T'
            self.move_player_up()
            return True

        elif self.level[self.x-1][self.y]=='W':                 #If top tile is a Wall
            return False

        elif self.level[self.x-1][self.y]=='B':                 #If top tile is a Box
            if self.level[self.x-2][self.y]==' ':                   #If tile above Box is an Empty Space
                self.prev_state=copy.deepcopy(self)
                self.level[self.x-2][self.y]='B'
                self.level[self.x-1][self.y]='P'
                self.move_player_up()
                return True

            elif self.level[self.x-2][self.y]=='G':                 #If tile above Box is a Goal
                self.prev_state=copy.deepcopy(self)
                self.level[self.x-2][self.y]='C'
                self.level[self.x-1][self.y]='P'
                self.move_player_up()
                return True

            elif self.level[self.x-2][self.y] in ['W', 'B', 'C']:   #If tile above Box is a Wall, another Box, or Box@Goal
                return False

        elif self.level[self.x-1][self.y]=='C':                 #If top tile is a Box@Goal
            if self.level[self.x-2][self.y]==' ':                   #If tile above Box@Goal is an Empty Space
                self.prev_state=copy.deepcopy(self)
                self.level[self.x-2][self.y]='B'
                self.level[self.x-1][self.y]='T'
                self.move_player_up()
                return True

            elif self.level[self.x-2][self.y]=='G':                 #If tile above Box@Goal is a Goal
                self.prev_state=copy.deepcopy(self)
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
            self.prev_state=copy.deepcopy(self)
            self.level[self.x+1][self.y]='P'
            self.move_player_down()
            return True
        
        elif self.level[self.x+1][self.y]=='G':                 #If top tile is a Goal tile
            self.prev_state=copy.deepcopy(self)
            self.level[self.x+1][self.y]='T'
            self.move_player_down()
            return True

        elif self.level[self.x+1][self.y]=='W':                 #If top tile is a Wall
            return False

        elif self.level[self.x+1][self.y]=='B':                 #If top tile is a Box
            if self.level[self.x+2][self.y]==' ':                   #If tile above Box is an Empty Space
                self.prev_state=copy.deepcopy(self)
                self.level[self.x+2][self.y]='B'
                self.level[self.x+1][self.y]='P'
                self.move_player_down()
                return True

            elif self.level[self.x+2][self.y]=='G':                 #If tile above Box is a Goal
                self.prev_state=copy.deepcopy(self)
                self.level[self.x+2][self.y]='C'
                self.level[self.x+1][self.y]='P'
                self.move_player_down()
                return True

            elif self.level[self.x+2][self.y] in ['W', 'B', 'C']:   #If tile above Box is a Wall, another Box, or Box@Goal
                return False

        elif self.level[self.x+1][self.y]=='C':                 #If top tile is a Box@Goal
            if self.level[self.x+2][self.y]==' ':                   #If tile above Box@Goal is an Empty Space
                self.prev_state=copy.deepcopy(self)
                self.level[self.x+2][self.y]='B'
                self.level[self.x+1][self.y]='T'
                self.move_player_down()
                return True

            elif self.level[self.x+2][self.y]=='G':                 #If tile above Box@Goal is a Goal
                self.prev_state=copy.deepcopy(self)
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
            self.prev_state=copy.deepcopy(self)
            self.level[self.x][self.y-1]='P'
            self.move_player_left()
            return True

        elif self.level[self.x][self.y-1]=='G':                 #If left tile is a Goal
            self.prev_state=copy.deepcopy(self)
            self.level[self.x][self.y-1]='T'
            self.move_player_left()
            return True
        
        elif self.level[self.x][self.y-1]=='W':
            return False
        
        elif self.level[self.x][self.y-1]=='B':                 #If left tile is a Box
            if self.level[self.x][self.y-2]==' ':                   #If tile left of Box is an Empty Space
                self.prev_state=copy.deepcopy(self)
                self.level[self.x][self.y-2]='B'
                self.level[self.x][self.y-1]='P'
                self.move_player_left()
                return True

            elif self.level[self.x][self.y-2]=='G':                 #If tile left of Box is a Goal
                self.prev_state=copy.deepcopy(self)
                self.level[self.x][self.y-2]='C'
                self.level[self.x][self.y-1]='P'
                self.move_player_left()
                return True
            
            elif self.level[self.x][self.y-2] in ['W', 'B', 'C']:   #If tile left of Box is a Wall, another Box, or Box@Goal
                return False
        
        elif self.level[self.x][self.y-1]=='C':                 #If left tile is a Box@Goal
            if self.level[self.x][self.y-2]==' ':                   #If tile left of Box@Goal is an Empty Space
                self.prev_state=copy.deepcopy(self)
                self.level[self.x][self.y-2]='B'
                self.level[self.x][self.y-1]='T'
                self.move_player_left()
                return True
            
            elif self.level[self.x][self.y-2]=='G':                 #If tile left of Box@Goal is a Goal
                self.prev_state=copy.deepcopy(self)
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
            self.prev_state=copy.deepcopy(self)
            self.level[self.x][self.y+1]='P'
            self.move_player_right()
            return True

        elif self.level[self.x][self.y+1]=='G':                 #If right tile is a Goal
            self.prev_state=copy.deepcopy(self)
            self.level[self.x][self.y+1]='T'
            self.move_player_right()
            return True
        
        elif self.level[self.x][self.y+1]=='W':
            return False
        
        elif self.level[self.x][self.y+1]=='B':                 #If right tile is a Box
            if self.level[self.x][self.y+2]==' ':                   #If tile right of Box is an Empty Space
                self.prev_state=copy.deepcopy(self)
                self.level[self.x][self.y+2]='B'
                self.level[self.x][self.y+1]='P'
                self.move_player_right()
                return True

            elif self.level[self.x][self.y+2]=='G':                 #If tile right of Box is a Goal
                self.prev_state=copy.deepcopy(self)
                self.level[self.x][self.y+2]='C'
                self.level[self.x][self.y+1]='P'
                self.move_player_right()
                return True
            
            elif self.level[self.x][self.y+2] in ['W', 'B', 'C']:   #If tile right of Box is a Wall, another Box, or Box@Goal
                return False
        
        elif self.level[self.x][self.y+1]=='C':                 #If right tile is a Box@Goal
            if self.level[self.x][self.y+2]==' ':                   #If tile right of Box@Goal is an Empty Space
                self.prev_state=copy.deepcopy(self)
                self.level[self.x][self.y+2]='B'
                self.level[self.x][self.y+1]='T'
                self.move_player_right()
                return True
            
            elif self.level[self.x][self.y+2]=='G':                 #If tile right of Box@Goal is a Goal
                self.prev_state=copy.deepcopy(self)
                self.level[self.x][self.y+2]='C'
                self.level[self.x][self.y+1]='T'
                self.move_player_right()
                return True
            
            elif self.level[self.x][self.y+2] in ['W', 'B', 'C']:   #If tile right of Box@Goal is a Wall, Box, or Box@Goal
                return False


    def possibleNextStates(self):
        stateList=[]
        
        up_state=copy.deepcopy(self)
        if up_state.up():
            up_state.cost+=1
            stateList.append(up_state)

        down_state=copy.deepcopy(self)
        if down_state.down():
            down_state.cost+=1
            stateList.append(down_state)
            
        left_state=copy.deepcopy(self)
        if left_state.left():
            left_state.cost+=1
            stateList.append(left_state)

        right_state=copy.deepcopy(self)
        if right_state.right():
            right_state.cost+=1
            stateList.append(right_state)

        return stateList

    def manhattan_distance(self):
        total_distance=0
        for i in range(0, len(self.level)):
            for j in range(0, len(self.level[0])):
                if self.level[i][j]=='B':
                    distance=0

                    n=0
                    for k in range(0, len(self.level)):
                        for l in range(0, len(self.level[0])):
                            if self.level[k][l] in ['G', 'T']:
                                distance+=abs(k-i)+abs(l-j)
                                n+=1
                    #distance/=n
                    total_distance+=distance
                    #print(f'avg distance for box at {i},{j}={distance}')
        #print(f'Total manhattan distance={total_distance}')
        return total_distance
        
    def any_box_in_corner(self):
        punish=0
        for i in range(0, len(self.level)):
            for j in range(0, len(self.level[0])):
                if self.level[i][j]=='B':
                    
                    if self.level[i-1][j] in ['W'] or self.level[i+1][j] in ['W']:
                        if self.level[i][j-1] in ['W'] or self.level[i][j+1] in ['W']:
                            punish+=1000
                            #print(f'Box at {i},{j} is in corner. Punish={punish}')
        
        #print(f'total punish={punish}')
        return punish

    def heuristic(self):
        man_heuristic=self.manhattan_distance()

        punish_heuristic=self.any_box_in_corner()

        heuristic_val=man_heuristic+punish_heuristic
        #print(heuristic_val)
        return heuristic_val

def constructPath(goalState):
    print("The solution path from Goal to Start")
    while goalState is not None:
        goalState.display()
        goalState=goalState.prev_state

#############################################################################################

#A star algorithm
open=[]
closed=[]
def A_star(state):
    open.append(state)
    while open:
        thisState=open.pop(0)
        thisState.display()
        if thisState not in closed:
            closed.append(thisState)
        if thisState.is_goal_reached():
            print("Goal state found.. stopping search")
            constructPath(thisState)
            break
        else:
            nextStates=thisState.possibleNextStates()
            for eachState in nextStates:
                if eachState not in open and eachState not in closed:
                    open.append(eachState)
                    open.sort()
                elif eachState in open:
                    index=open.index(eachState)
                    if open[index].cost+open[index].heuristic()>eachState.cost+eachState.heuristic():
                        open.pop(index)
                        open.append(eachState)
                        open.sort()
                elif eachState in closed:
                    index=closed.index(eachState)
                    if closed[index].cost+closed[index].heuristic()>eachState.cost+eachState.heuristic():
                        closed.pop(index)
                        closed.append(eachState)
                        propogateImprovement(eachState)

def propogateImprovement(state):
    nextStates=state.possibleNextStates()
    for eachState in nextStates:
        if eachState in open:
            index=open.index(eachState)
            if open[index].heuristic()>eachState.heuristic():
                open.pop(index)
                open.append(eachState)
                open.sort()
        if eachState in closed:
            index=closed.index(eachState)
            if closed[index].heuristic()>eachState.heuristic():
                closed.pop(index)
                closed.append(eachState)
                propogateImprovement(eachState)

#########################################################################

#TKINTER MAINLOOP
win = tkinter.Tk()
win.geometry("0x0")
win.resizable('False', 'False')
#############################################

#INITIALIZE VALUES
start_time=time.time()
game=Sokoban(int(sys.argv[1]))
A_star(game)
exec_time=time.time()-start_time
print(f'Time taken to solve={exec_time}')
##############################################

#KEYBIND EVENTS
def up(event):
    os.system("clear")
    game.up()
    game.display()
    print(f'{game.cost}+{game.heuristic()}')

def down(event):
    os.system("clear")
    game.down()
    game.display()
    print(f'{game.cost}+{game.heuristic()}')

def left(event):
    os.system("clear")
    game.left()
    game.display()
    print(f'{game.cost}+{game.heuristic()}')

def right(event):
    os.system("clear")
    game.right()
    game.display()
    print(f'{game.cost}+{game.heuristic()}')


def next_level(event):
    if game.level_no!=6:
        win.destroy()
        os.system("python3 SokobanAI.py "+ str(game.level_no+1))

def previous_level(event):
    if game.level_no!=1:
        win.destroy()
        os.system("python3 SokobanAI.py "+ str(game.level_no-1))

def go_to_main_screen(event):
    win.destroy()
    os.system("python3 MainScreen.py")

def restart_game(event):
    win.destroy()
    os.system("python3 SokobanAI.py "+ str(game.level_no))


def exit_game(event):
    win.destroy()
    os.system("clear")

win.bind("n", next_level)
win.bind("b", previous_level)
win.bind("<BackSpace>", go_to_main_screen)
win.bind("<space>", restart_game)
win.bind("<Escape>", exit_game)
##############################################
    
win.mainloop()
#########################################################################
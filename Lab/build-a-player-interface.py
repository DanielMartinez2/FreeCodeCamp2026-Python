from abc import ABC, abstractmethod
import random

class Player(ABC):
    
    def __init__(self) -> None:
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]
    
    
    def make_move(self) -> tuple:
        random_move = random.choice(self.moves)
        x = self.position[0]
        y = self.position[1]
        new_move = (x+random_move[0], y+random_move[1])
        #self.position = tuple(random_move[i] + self.position[i] for i in range(len(random_move)))
        self.position = new_move
        self.path.append(self.position)
        return self.position
    
    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self) -> None:
        super().__init__()
        x = self.position[0]
        y = self.position[1]
        self.moves = [(x,y+1), (x,y-1), (x-1,y), (x+1,y)]

    def level_up(self):        
        x = self.position[0]
        y = self.position[1]
        new_moves = [(x+1,y+1), (x-1,y-1), (x+1,y-1), (x-1,y+1)]
        self.moves += new_moves


#make horse, bishop, queen, king classes
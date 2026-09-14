from enum import Enum

class GameStatus(Enum):
    IN_Progress = 'In Progress'
    Draw = 'Draw'
    X_Wins = 'X Wins'
    O_Wins = 'O Wins'
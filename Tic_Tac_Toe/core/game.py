

from Tic_Tac_Toe.entities.board import Board
from Tic_Tac_Toe.enums.game_status import GameStatus
import threading
from Tic_Tac_Toe.enums.symbol import Symbol

class Game:
    def __init__(self,player1,player2,board_size:int):
        self._player1 = player1
        self._player2 = player2
        self._board = Board(board_size)
        self._game_status = GameStatus.IN_Progress
        self._lock = threading.Lock()
        self._current_player_index = 0  # Index to track the current player (0 for player1, 1 for player2)

    def make_move(self,row,col,symbol:Symbol):
        with self._lock:
            if self._game_status!= GameStatus.IN_Progress:
                raise ValueError("Game is already over")
            if self._game_status == GameStatus.Draw:
                raise ValueError("Game is already a draw")

            if not self._board.is_cell_empty(row,col):
                raise ValueError("Cell is already occupied")

            if self._current_player_index == 0 and symbol != Symbol.X:
                raise ValueError("It's Player 1's turn. Please use Symbol X.")
            elif self._current_player_index == 1 and symbol != Symbol.O:
                raise ValueError("It's Player 2's turn. Please use Symbol O.")
            
            self._board.place_symbol(row,col,symbol)
    
            if self.check_winner(row,col,symbol):
                self._game_status = GameStatus.X_Wins if self._current_player_index == 0 else GameStatus.O_Wins

            elif self._board.is_full():
                self._game_status = GameStatus.Draw

            else:
                self._current_player_index = 1 - self._current_player_index  # Switch to the other player

    def check_winner(self,row=None,col=None,symbol=None):
        size = len(self._board._cells)
        if not symbol:
            raise ValueError("Symbol must be provided to check for a winner")

        # Check the row
        if all(self._board.get_cell(row,c).symbol == symbol for c in range(size)):
            return True

        # Check the column
        if all(self._board.get_cell(r,col).symbol == symbol for r in range(size)):
            return True

        # Check the main diagonal
        if row == col and all(self._board.get_cell(i,i).symbol == symbol for i in range(size)):
            return True

        # Check the anti-diagonal
        if row + col == size - 1 and all(self._board.get_cell(i,size-1-i).symbol == symbol for i in range(size)):
            return True

        return False

    @property
    def board(self)->Board:
        return self._board

    @property
    def game_status(self)->GameStatus:
        return self._game_status

    @property
    def winner(self):
        if self._game_status ==GameStatus.X_Wins:
            print(f'winner is {self._player1}')
            
        elif self._game_status == GameStatus.O_Wins:
            print(f'winner is {self._player2}')
            

        elif self._game_status == GameStatus.Draw:
            print('The game is a draw.')
            
        else:
            print('The game is still in progress.')
           

    def print_board(self):
        self._board.print_board()


    
        

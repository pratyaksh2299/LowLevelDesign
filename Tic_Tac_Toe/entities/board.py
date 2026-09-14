
from Tic_Tac_Toe.entities.cell import Cell


class Board:
    def __init__(self,size):
        self._size = size
        self._cells = [[Cell() for _ in range(size)]for  _ in range(size)]

    def place_symbol(self,row,col,symbol):
        if row <0 or row >= self._size or col <0 or col >= self._size:
            raise ValueError("Invalid row or column")
        self._cells[row][col].set_symbol(symbol)

    def is_cell_empty(self,row,col):
        if row <0 or row >= self._size or col <0 or col >= self._size:
            raise ValueError("Invalid row or column")
        return self._cells[row][col].is_empty()

    def is_full(self):
        for row in range(self._size):
            for col in range(self._size):
                if self._cells[row][col].is_empty():
                    return False
        return True
    
    def print_board(self) -> None:
        print()
        for i, row in enumerate(self._cells):
            row_str = " | ".join(f" {cell.symbol.value} " for cell in row)
            print(row_str)
            if i < self._size - 1:
                print("-" * (self._size * 5 - 1))
        print()

    def get_cell(self, row: int, col: int) -> Cell:
        return self._cells[row][col]

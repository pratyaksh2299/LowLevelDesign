from Tic_Tac_Toe.enums.symbol import Symbol

class Cell:
    def __init__(self):
        self._symbol = Symbol.EMPTY

    @property
    def symbol(self):
        return self._symbol

    def set_symbol(self, symbol: Symbol):
        if self._symbol != Symbol.EMPTY:
            raise ValueError("Cell is already occupied")
        self._symbol = symbol

    def is_empty(self):
        return self._symbol == Symbol.EMPTY
    

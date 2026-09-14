from Tic_Tac_Toe.enums.symbol import Symbol

class Player:
    def __init__(self,name,symbol: Symbol):
        self._name = name
        if symbol == Symbol.EMPTY:
            raise ValueError("Player symbol cannot be Empty")

        self._symbol = symbol

    @property
    def get_name(self):
        return self._name

    @property
    def get_symbol(self):
        return self._symbol

    def __str__(self):
        return f"Player Name: {self._name},Player Symbol: {self._symbol}"
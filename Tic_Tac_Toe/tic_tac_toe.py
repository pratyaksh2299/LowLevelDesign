from Tic_Tac_Toe.entities.player import Player
from Tic_Tac_Toe.enums.symbol import Symbol
from Tic_Tac_Toe.core.game import Game
from Tic_Tac_Toe.enums.game_status import GameStatus

if __name__ == "__main__":

    alice = Player("Alice", Symbol.X)
    bob = Player("Bob", Symbol.O)

    game = Game(alice, bob, 3)

    moves = [
        (0, 0, Symbol.X),  # Alice
        (0, 1, Symbol.O),  # Bob
        (1, 1, Symbol.X),  # Alice
        (0, 2, Symbol.O),  # Bob
        (2, 2, Symbol.O),  # Alice wins
    ]

    for row,col,symbol in moves:
        try:
            print(f"{symbol.value}'s turn. Placing at ({row}, {col})")
            game.make_move(row,col,symbol)
            game.print_board()
            game.winner
        except ValueError as e:
            print(f"Error: {e}")



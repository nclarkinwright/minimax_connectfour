from minimax_connectfour import *

def single_game(io=True):
    # For naive versus random test

    game = Game([['-' for i in range(8)] for j in range(8)])   # 8x8 empty board
    if io:
        game.display()

    maxplayer = RandomAgent('R')
    minplayer = RandomAgent('B')

    while True:

        m = maxplayer.move(game)
        game = game.neighbor(m, maxplayer.color)
        if io:
            time.sleep(1)
            game.display()

        if game.winning_state() is not None:
            break

        m = minplayer.move(game)
        game = game.neighbor(m, minplayer.color)
        if io:
            time.sleep(1)
            game.display()

        if game.winning_state() is not None:
            break

    if game.winning_state() == float("inf"):
        print("RED WINS!")
    elif game.winning_state() == float("-inf"):
        print("BLACK WINS!")
    elif game.winning_state() == 0:
        print("TIE!")

    return game

if __name__ == '__main__':
    single_game(io=True)
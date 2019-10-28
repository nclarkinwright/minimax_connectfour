from minimax_connectfour import *

def main():
    
    game = Game([['-' for i in range(8)] for j in range(8)])

    game = game.neighbor(3, 'R')
    game = game.neighbor(5, 'R')
    game = game.neighbor(0, 'R')
    game = game.neighbor(0, 'R')
    game = game.neighbor(0, 'R')
    game = game.neighbor(0, 'R')
    game = game.neighbor(0, 'R')
    game = game.neighbor(0, 'R')
    game = game.neighbor(0, 'R')
    game = game.neighbor(0, 'R')

    game.display()
    print(game.black_moves)
    print(game.red_moves)

if __name__ == '__main__':
    main()
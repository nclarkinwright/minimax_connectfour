from minimax_connectfour import *

def main():
    
    game = Game([['-' for i in range(8)] for j in range(8)])

    game.neighbor(3, 'R')
    game.neighbor(5, 'R')

if __name__ == '__main__':
    main()
from minimax_connectfour import *

def main():

    game_one = Game([['-','-','-','-','-','-','-','-']
                    ,['-','-','-','-','-','-','-','-']
                    ,['-','-','-','-','-','-','-','-']
                    ,['-','-','-','-','-','-','-','-']
                    ,['-','-','-','-','-','-','-','-']
                    ,['-','-','-','-','-','-','-','-']
                    ,['-','R','R','-','-','-','-','-']
                    ,['B','B','B','R','-','-','-','-']])
    
    game_two = Game([['-','-','-','-','-','-','-','-']
                    ,['-','-','-','-','-','-','-','-']
                    ,['-','-','-','-','-','-','-','-']
                    ,['-','-','-','-','-','-','-','-']
                    ,['-','-','-','-','-','-','-','-']
                    ,['-','-','-','-','-','-','-','-']
                    ,['R','-','-','-','-','-','-','-']
                    ,['R','B','B','B','-','-','-','-']])

    game_three = Game([['-','-','-','-','-','-','-','-']
                    ,['-','-','-','-','-','-','-','-']
                    ,['-','-','-','-','-','-','-','-']
                    ,['-','-','-','-','-','-','-','-']
                    ,['-','-','-','R','-','-','-','-']
                    ,['-','-','R','B','-','-','-','-']
                    ,['-','R','R','B','-','-','-','-']
                    ,['-','B','R','B','-','-','-','-']])


    def check_game_state(game):
        
        util = game.utility()
        print('Utility: ' + str(util))
        if game.winning_state() == float("inf"):
            print("RED WINS!")
        elif game.winning_state() == float("-inf"):
            print("BLACK WINS!")
        elif game.winning_state() == 0:
            print("TIE!")
        elif game.winning_state() is None:
            print("NO WINNER!")
    
    # Check winning states
    print('Game One: ')
    check_game_state(game_one)
    print('\nGame Two: ')
    check_game_state(game_two)
    print('\nGame Three: ')
    check_game_state(game_three)

if __name__ == '__main__':
    main()
import copy
import time
import abc
import random

class Game(object):
    """A connect four game."""

    def __init__(self, grid, red_moves = [], black_moves = []):
        """Instances differ by their board."""
        self.grid = copy.deepcopy(grid)  # No aliasing!
        #
        self.red_moves = red_moves
        self.black_moves = black_moves
        self.last_move = ''
        # Added for win state checking
        # Each game board keeps version of grid with x and y coords reversed
        # and list of lists of diagonals
        self.vert_grid = self.make_vert_grid()
        #self.diag_grid = self.make_diag_grid()

    key = [[ 0,  1,  2,  3,  4,  5,  6,  7]
          ,[ 8,  9, 10, 11, 12, 13, 14, 15]
          ,[16, 17, 18, 19, 20, 21, 22, 23]
          ,[24, 25, 26, 27, 28, 29, 30, 31]
          ,[32, 33, 34, 35, 36, 37, 38, 39]
          ,[40, 41, 42, 43, 44, 45, 46, 47,]
          ,[48, 49, 50, 51, 52, 53, 54, 55,]
          ,[56, 57, 58, 59, 60, 61, 62, 63]]

    def display(self):
        """Print the game board."""
        for row in self.grid:
            for mark in row:
                print(mark, end='')
            print()
        print()

    def possible_moves(self):
        """Return a list of possible moves given the current board."""
        moves = []
        last = len(self.grid[0])

        # Use range, so index is easily appended
        # Last is not actually last, because range excludes 2nd var
        for column in range(0, last):
            if self.grid[0][column] == '-':
                moves.append(column)
        return moves

    def neighbor(self, col, color):
        """Return a Game instance like this one but with a move made into the specified column."""
        game = Game(self.grid)
        last_row = len(self.grid) - 1

        for row in range(last_row, -1, -1):
            if game.grid[row][col] == '-':
                game.grid[row][col] = color
                # Record move made
                if color == 'R':
                    game.red_moves.append((row, col))
                if color == 'B':
                    game.black_moves.append((row, col))
                game.last_move = color
                # Stop once move is made
                break
        return game

    def utility(self):
        """Return the minimax utility value of this game"""
        # YOU FILL THIS IN

    def winning_state(self):
        """Returns float("inf") if Red wins; float("-inf") if Black wins;
           0 if board full; None if not full and no winner"""
        # Get the coords of the last move made and get the color to check
        if self.last_move == 'R':
            move = self.red_moves[-1]
            color = 'R'
        if self.last_move == 'B':
            move = self.black_moves[-1]
            color = 'B'
        y = move[0]
        x = move[1]

        # Horizontal check
        matches = 1
        go_left = True
        go_right = True
        for z in range(1, 4):
            # Check for bounds and whether non-match was found
            # Stop checking if non-matching piece was found
            if z - x >= 0 and go_left:
                if self.grid[y][x - z] == color:
                    matches = matches + 1
                else:
                    go_left = False
            if z + x < len(self.grid) and go_right:
                if self.grid[y][x + z] == color:
                    matches = matches + 1
                else:
                    go_right = False
        if matches >= 4:
            if color == 'R':
                return float('inf')
            else:
                return float('-inf')

        # Vertical check
        matches = 1
        go_up = True
        go_down = True
        for z in range(1, 4):
            # Check for bounds and whether non-match was found
            # Stop checking if non-matching piece was found
            if z - y >= 0 and go_up:
                if self.grid[y - z][x] == color:
                    matches = matches - 1
                else:
                    go_up = False
            if z + y < len(self.grid) and go_down:
                if self.grid[y + z][x] == color:
                    matches = matches + 1
                else:
                    go_down = False
        if matches >= 4:
            if color == 'R':
                return float('inf')
            else:
                return float('-inf')

        # Diagonal check 1
        matches = 1
        go_up_left = True
        go_down_right = True
        for z in range(1, 4):
            # Check for bounds and whether non-match was found
            # Stop checking if non-matching piece was found
            if z - y >= 0 and z - x >= 0 and go_up_left:
                if self.grid[y - z][x - z] == color:
                    matches = matches - 1
                else:
                    go_up_left = False
            if z + y < len(self.grid) and z + x < len(self.grid) and go_down_right:
                if self.grid[y + z][x + z] == color:
                    matches = matches + 1
                else:
                    go_down_right = False
        if matches >= 4:
            if color == 'R':
                return float('inf')
            else:
                return float('-inf')

        # Diag check 2
        matches = 1
        go_up_right = True
        go_down_left = True
        for z in range(1, 4):
            # Check for bounds and whether non-match was found
            # Stop checking if non-matching piece was found
            if z - y >= 0 and z + x < len(self.grid) and go_up_right:
                if self.grid[y - z][x + z] == color:
                    matches = matches - 1
                else:
                    go_up_right = False
            if z + y < len(self.grid) and z - x >= 0 and go_down_left:
                if self.grid[y + z][x - z] == color:
                    matches = matches + 1
                else:
                    go_down_left = False
        if matches >= 4:
            if color == 'R':
                return float('inf')
            else:
                return float('-inf')
        
        # Check for tie
        if self.possible_moves() == []:
            return 0
        
        # No winner, board is not full
        return None

    

    # Reverse x y coords of grid
    def make_vert_grid(self):
        new_grid = []
        grid_len = len(self.grid)

        # Assuming square
        for y in range(grid_len):
            sub_grid = []
            for x in range(grid_len):
                sub_grid.append(self.grid[x][y])
            new_grid.append(sub_grid)

        return new_grid

    # Return list of diagonals
    #def make_diag_grid(self):


class Agent(object):
    """Abstract class, extended by classes RandomAgent, FirstMoveAgent, MinimaxAgent.
    Do not make an instance of this class."""

    def __init__(self, color):
        """Agents use either RED or BLACK chips."""
        self.color = color

    @abc.abstractmethod
    
    def move(self, game):
        """Abstract. Must be implemented by a class that extends Agent."""
        pass

class RandomAgent(Agent):
    """Naive agent -- always performs a random move"""

    def move(self, game):
        """Returns a random move"""
        # Get all possible moves to take, keep # of possible moves found
        poss_moves = game.possible_moves()
        num_of_moves = len(poss_moves)

        # Get random integer
        move_to_take = random.randint(0, num_of_moves - 1)
        # Random int determines which index to use of possible moves
        return poss_moves[move_to_take]

class FirstMoveAgent(Agent):
    """Naive agent -- always performs the first move"""

    def move(self, game):
        """Returns the first possible move"""
        poss_moves = game.possible_moves()
        return poss_moves[0]

class MinimaxAgent(Agent):
    """Smart agent -- uses minimax to determine the best move"""

    def move(self, game):
        """Returns the best move using minimax"""
        # YOU FILL THIS IN

def tournament(simulations=50):
    """Simulate connect four games, of a minimax agent playing
    against a random agent"""

    redwin, blackwin, tie = 0,0,0

    for i in range(simulations):
        game = single_game(io=False)
        print(i, end=" ")
        if game.winning_state() == float("inf"):
            redwin += 1
        elif game.winning_state() == float("-inf"):
            blackwin += 1
        elif game.winning_state() == 0:
            tie += 1

    print("Red %d (%.0f%%) Black %d (%.0f%%) Tie %d" % (redwin,redwin/simulations*100,blackwin,blackwin/simulations*100,tie))

    return redwin/simulations

def single_game(io=True):
    """Create a game and have two agents play it."""

    game = Game([['-' for i in range(8)] for j in range(8)])   # 8x8 empty board
    if io:
        game.display()

    maxplayer = MinimaxAgent('R')
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
    #tournament(simulations=50)
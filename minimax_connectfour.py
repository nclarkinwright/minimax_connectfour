import copy
import time
import abc
import random

class Game(object):
    """A connect four game."""

    def __init__(self, grid, red_moves = [], black_moves = []):
        """Instances differ by their board."""
        self.grid = copy.deepcopy(grid)  # No aliasing!
        # Added for win state checking
        self.red_moves = red_moves
        self.black_moves = black_moves
        self.last_move = ''

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
        top_row = self.grid[0]
        index = 0

        for column in top_row:
            if column == '-':
                moves.append(index)
            index = index + 1
        return moves

    def neighbor(self, col, color):
        """Return a Game instance like this one but with a move made into the specified column."""
        game = Game(self.grid)
        last_row = len(self.grid) - 1

        # Start from bottom, and look for first empty space
        for row in range(last_row, -1, -1):
            if game.grid[row][col] == '-':
                game.grid[row][col] = color
                # Stop once move is made
                return game

    def utility(self):
        """Return the minimax utility value of this game"""
        # YOU FILL THIS IN

    def winning_state(self):
        """Returns float("inf") if Red wins; float("-inf") if Black wins;
           0 if board full; None if not full and no winner"""
        
        # Checks for four of same color in a row
        def victory_check(line):
            black = 'BBBB'
            red = 'RRRR'
            
            if line.find(red) != -1:
                return float('inf')
            if line.find(black) != -1:
                return float('-inf')
            else:
                return None

        # Check horizontal dimension
        for row in self.grid:
            v_check = victory_check(''.join(row))
            if not v_check is None:
                return v_check

        # Check vertical dimension
        vert_grid = self.make_vert_grid()
        for column in vert_grid:
            v_check = victory_check(''.join(column))
            if not v_check is None:
                return v_check

        # Check diagonals and reverse diagonals
        diag_grid = self.make_diag_grid(4)
        for diag in diag_grid:
            v_check = victory_check(''.join(diag))
            if not v_check is None:
                return v_check

        # Check for tie
        if self.possible_moves() == []:
            return 0
        
        # No winner, board is not full
        return None
    
    # Reverse x y coords of board grid, so columns are now rows
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
    
    # Returns grid of diagonals with length >= min
    def make_diag_grid(self, min):
        new_grid = []
        m = len(self.grid)
        n = len(self.grid[0])

        # Left side
        for z in range(m):
            sub_grid = []
            y = z
            x = 0
            while y >= 0:
                sub_grid.append(self.grid[y][x])
                y = y - 1
                x = x + 1
            new_grid.append(sub_grid)

        # Bottom
        for z in range(1, n):
            sub_grid = []
            y = m - 1
            x = z
            while x <= n - 1:
                sub_grid.append(self.grid[y][x])
                y = y - 1
                x = x + 1
            new_grid.append(sub_grid)

        # Reverse right
        for z in range(m):
            sub_grid = []
            y = z
            # x starts at other side for reverse
            x = n - 1
            while y >= 0:
                sub_grid.append(self.grid[y][x])
                y = y - 1
                x = x - 1
            new_grid.append(sub_grid)

        # Reverse bottom
        for z in range(n - 1, -1, -1):
            sub_grid = []
            y = m - 1
            x = z
            while x >= 0:
                sub_grid.append(self.grid[y][x])
                y = y - 1
                x = x - 1
            new_grid.append(sub_grid)
        
        return new_grid


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
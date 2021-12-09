import chess

class MinimaxAI():
    def __init__(self, max_depth):
        self.max_depth = max_depth
        self.calls = 0

    #returns best move for current player
    def choose_move(self, board):
        move, v = self.minimax_decision(board, self.max_depth)
        print("Minimax AI recommending move " + str(move))
        print("Move value: " + str(v))
        print("Num calls: " + str(self.calls))
        return move

    #possible moves on given board
    def possible_moves(self, board):
        moves = list(board.legal_moves)
        return moves

    #run min and max value functions to determine best move
    def minimax_decision(self, board, depth):
        best_move = None
        best_move_val = None
        for m in self.possible_moves(board):
            board.push(m)
            val = self.min_value(board, depth)
            if((best_move == None) or (val > best_move_val)):
                best_move = m
                best_move_val = val
            board.pop()
        return best_move, best_move_val

    #get minimum utility for current player from given board
    def min_value(self, board, depth):
        self.calls = self.calls +1
        if self.cutoff_test(board, depth):
            return - self.utility(board)
        min_val = None
        #find min valued move
        for m in self.possible_moves(board):
            board.push(m)
            val = self.max_value(board, depth-1)
            if((min_val == None) or (val < min_val)):
                min_val = val
            board.pop()
        return min_val

    #get maximum utility for current player from given board
    def max_value(self, board, depth):
        self.calls = self.calls +1
        if self.cutoff_test(board, depth):
            return self.utility(board)
        max_val = None
        #find max valued move
        for m in self.possible_moves(board):
            board.push(m)
            val = self.min_value(board, depth-1)
            if((max_val == None) or (val > max_val)):
                max_val = val
            board.pop()
        return max_val

    #return true if terminal state
    #or if reached max depth
    def cutoff_test(self, board, depth):
        return ((depth < 1) or board.is_game_over())

    #get utility of a board
    #winning board worth 100
    #each pawn is worth 1, knight or bishop is worth 3, rook 5, and queen 9.
    #losing board worth 0
    #what about tie?
    def utility(self, board):
        #terminal board
        if board.is_game_over():
            #lost
            if board.is_checkmate():
                return -100
            #tie
            else:
                return 0
        #nonterminal board
        else:
            u1 = len(board.pieces(1, board.turn)) + 3*(len(board.pieces(2, board.turn)) + len(board.pieces(3, board.turn))) + 5*(len(board.pieces(4, board.turn))) + 9*(len(board.pieces(5, board.turn)))
            u2 = len(board.pieces(1, not(board.turn))) + 3*(len(board.pieces(2, not(board.turn))) + len(board.pieces(3, not(board.turn)))) + 5*(len(board.pieces(4, not(board.turn)))) + 9*(len(board.pieces(5, not(board.turn))))
            return u1 - u2




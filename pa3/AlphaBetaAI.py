import chess
from math import inf
#add move reordering
class AlphaBetaAI():
    def __init__(self, max_depth):
        self.max_depth = max_depth
        self.calls = 0

    #returns best move for current player
    def choose_move(self, board):
        move, v = self.minimax_decision(board)
        print("A-B Minimax AI recommending move " + str(move))
        print("Move value: " + str(v))
        print("Num calls: " + str(self.calls))
        return move

    #possible moves on given board
    def possible_moves(self, board):
        moves = list(board.legal_moves)
        #sort by utility
        utilities = {}
        for m in moves:
            board.push(m)
            utilities[m] = self.utility(board)
            board.pop()
        return sorted(moves, key=lambda m: utilities[m])

    #run min and max value functions to determine best move
    def minimax_decision(self, board):
        best_move = None
        best_move_val = float(-inf)
        for m in self.possible_moves(board):
            board.push(m)
            val = self.min_value(board, float(-inf), float(inf), self.max_depth)
            if(val > best_move_val):
                best_move = m
                best_move_val = val
            board.pop()
        return best_move, best_move_val

    #get minimum utility for current player from given board
    def min_value(self, board, alpha, beta, depth):
        self.calls = self.calls +1
        if self.cutoff_test(board, depth):
            return - (self.utility(board))
        min_val = float(inf)
        #find min valued move
        #do lowest utility moves first
        moves = self.possible_moves(board)
        moves.reverse()
        for m in moves:
            board.push(m)
            min_val = min(min_val, self.max_value(board, alpha, beta, depth-1))
            board.pop()
            #if already more than previous max value, can prune other branches 
            if(min_val <= alpha):
                return min_val
            #update beta as min
            beta = min(min_val, beta)
        return min_val

    #get maximum utility for current player from given board
    def max_value(self, board, alpha, beta, depth):
        self.calls = self.calls +1
        if self.cutoff_test(board, depth):
            return self.utility(board)
        max_val = float(-inf)
        #find max valued move
        #do highest utility moves first
        for m in self.possible_moves(board):
            board.push(m)
            max_val = max(max_val, self.min_value(board, alpha, beta, depth-1))
            #if already greater than previous min value, need not explore other branches
            board.pop()
            if(max_val >= beta):
                return max_val
            alpha = max(alpha, max_val)
        return max_val

    #return true if terminal state
    #or if reached max depth
    def cutoff_test(self, board, depth):
        return (depth < 1) or (board.is_game_over())

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


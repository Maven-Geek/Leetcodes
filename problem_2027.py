class Solution(object): 
    def minimumMoves(self, s): 
        moves = 0 
        i = 0
        while i < len(s):
            if s[i] == 'X':
                moves += 1
                i += 3
            else:
                i += 1
        return moves

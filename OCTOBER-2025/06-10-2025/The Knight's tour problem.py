class Solution:
    def knightTour(self, n):
        # code here
        if n == 1:
            return [[0]]
        if n <= 4:
            return []
        
        moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        
        board = [[-1 for _ in range(n)] for _ in range(n)]
        
        def is_safe(x, y):
            return 0 <= x < n and 0 <= y < n and board[x][y] == -1
        
        def get_degree(x, y):
            count = 0
            for dx, dy in moves:
                if is_safe(x + dx, y + dy):
                    count += 1
            return count
        
        def solve(x, y, move_count):
            board[x][y] = move_count
            
            if move_count == n * n - 1:
                return True
            
            next_moves = []
            for dx, dy in moves:
                next_x, next_y = x + dx, y + dy
                if is_safe(next_x, next_y):
                    degree = get_degree(next_x, next_y)
                    next_moves.append((degree, next_x, next_y))
            
            next_moves.sort() 
            
            for _, next_x, next_y in next_moves:
                if solve(next_x, next_y, move_count + 1):
                    return True
            
            board[x][y] = -1
            return False
        
        if solve(0, 0, 0):
            return board
        else:
            return []
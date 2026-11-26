# Simplified Chess Engine
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    
    num_games = int(next(iterator))
    
    # Board is 4x4: rows 0..3, cols 0..3
    # Piece encoding:
    # 0: empty
    # White: 1: 'Q', 2: 'R', 3: 'B', 4: 'N'
    # Black: -1: 'Q', -2: 'R', -3: 'B', -4: 'N'
    
    piece_map = {'Q': 1, 'R': 2, 'B': 3, 'N': 4}
    
    knight_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    rook_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    bishop_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    queen_dirs = rook_dirs + bishop_dirs
    
    out = []
    
    for _ in range(num_games):
        w = int(next(iterator))
        b = int(next(iterator))
        m = int(next(iterator))
        
        board = [[0]*4 for _ in range(4)]
        
        for _ in range(w):
            t = next(iterator)
            c = ord(next(iterator)) - ord('A')
            r = int(next(iterator)) - 1
            board[r][c] = piece_map[t]
            
        for _ in range(b):
            t = next(iterator)
            c = ord(next(iterator)) - ord('A')
            r = int(next(iterator)) - 1
            board[r][c] = -piece_map[t]
            
        # Minimax with alpha-beta / simple depth-limited search
        # m moves means White moves on moves 1, 3, 5... (1-indexed)
        # Total half-moves (plies) allowed is m.
        # Actually, "can White win in <= m moves" means at most m plies (turns of White/Black)?
        # Notice sample: m = 1, White takes Black's Queen in 1 move.
        # Wait, does m count full moves or half-moves (plies)?
        # In chess, "White wins in m moves" could mean m plies or m turns.
        # Let's check sample:
        # "White can win in 1 move by taking Knight to A4 and capturing Queen. Because it took 1 move to win and 1 <= 1, print YES."
        # What if White moves, Black moves, White moves? Is that 2 moves or 3 moves?
        # "each move made by any player counts as a single move." -> so each ply is 1 move!
        # "each move made by any player counts as a single move."
        # This explicitly states that 1 move = 1 ply!
        # So m is the maximum number of plies (half-moves).
        
        def can_white_win(plies_left):
            # White's turn
            # If plies_left <= 0, White cannot make a move
            if plies_left <= 0:
                return False
                
            # White wants to find AT LEAST ONE move that wins
            # Generate all moves for White
            white_moves = []
            # Check direct win first!
            for r in range(4):
                for c in range(4):
                    p = board[r][c]
                    if p > 0:
                        # Generate moves for this piece
                        if p == 1:
                            dirs = queen_dirs
                        elif p == 2:
                            dirs = rook_dirs
                        elif p == 3:
                            dirs = bishop_dirs
                        else:
                            dirs = None
                            
                        if dirs:
                            for dr, dc in dirs:
                                nr, nc = r + dr, c + dc
                                while 0 <= nr < 4 and 0 <= nc < 4:
                                    dest = board[nr][nc]
                                    if dest > 0:
                                        break
                                    if dest == -1: # Black Queen captured!
                                        return True
                                    white_moves.append((r, c, nr, nc, dest))
                                    if dest < 0: # captured black piece, can't move further
                                        break
                                    nr += dr
                                    nc += dc
                        else: # Knight
                            for dr, dc in knight_moves:
                                nr, nc = r + dr, c + dc
                                if 0 <= nr < 4 and 0 <= nc < 4:
                                    dest = board[nr][nc]
                                    if dest <= 0:
                                        if dest == -1:
                                            return True
                                        white_moves.append((r, c, nr, nc, dest))
            
            # If plies_left == 1 and no immediate win, White cannot win
            if plies_left == 1:
                return False
                
            # Try each move for White
            # Prioritize captures
            white_moves.sort(key=lambda m: 0 if m[4] < 0 else 1)
            
            for r, c, nr, nc, captured in white_moves:
                p = board[r][c]
                board[r][c] = 0
                board[nr][nc] = p
                
                # Now it's Black's turn. For White to win, Black must NOT be able to prevent it.
                # That means for ALL Black moves, White must still be able to win in plies_left - 2 (from White's perspective).
                # But wait: if Black has NO legal moves, is it stalemate or what?
                # The objective: "The goal of the game is to capture the opponent's Queen without losing your own."
                # Does Black ever lose their Queen by stalemate? No, you have to capture it.
                # Can Black capture White's Queen? If Black can, then this White move fails!
                
                black_can_prevent = black_turn(plies_left - 1)
                
                # Undo move
                board[r][c] = p
                board[nr][nc] = captured
                
                if not black_can_prevent:
                    return True
                    
            return False

        def black_turn(plies_left):
            # Black's turn. Returns True if Black can avoid/prevent White's win (i.e. White cannot force a win),
            # or if Black can capture White's Queen immediately.
            # First, check if Black can immediately capture White's Queen.
            black_moves = []
            has_moves = False
            for r in range(4):
                for c in range(4):
                    p = board[r][c]
                    if p < 0:
                        if p == -1:
                            dirs = queen_dirs
                        elif p == -2:
                            dirs = rook_dirs
                        elif p == -3:
                            dirs = bishop_dirs
                        else:
                            dirs = None
                            
                        if dirs:
                            for dr, dc in dirs:
                                nr, nc = r + dr, c + dc
                                while 0 <= nr < 4 and 0 <= nc < 4:
                                    dest = board[nr][nc]
                                    if dest < 0:
                                        break
                                    if dest == 1: # White Queen captured!
                                        return True # Black prevents White win
                                    black_moves.append((r, c, nr, nc, dest))
                                    if dest > 0:
                                        break
                                    nr += dr
                                    nc += dc
                        else: # Knight
                            for dr, dc in knight_moves:
                                nr, nc = r + dr, c + dc
                                if 0 <= nr < 4 and 0 <= nc < 4:
                                    dest = board[nr][nc]
                                    if dest >= 0:
                                        if dest == 1:
                                            return True
                                        black_moves.append((r, c, nr, nc, dest))

            # If Black has no moves, White doesn't immediately capture Queen unless next turn White can.
            # But Black must make a move if they have one. If Black has no moves, does game end or Black passes?
            # In chess, no moves = stalemate. Does that count as White winning? No, White must capture Queen.
            if not black_moves:
                return True

            # If plies_left <= 0, White ran out of moves, Black successfully prevented White from winning in <= m moves.
            if plies_left <= 0:
                return True

            # Black wants to find AT LEAST ONE move such that White CANNOT win.
            # So if there is ANY move by Black where can_white_win(plies_left - 1) is False,
            # Black can prevent White's win!
            # Prioritize captures
            black_moves.sort(key=lambda m: 0 if m[4] > 0 else 1)

            for r, c, nr, nc, captured in black_moves:
                p = board[r][c]
                board[r][c] = 0
                board[nr][nc] = p
                
                white_wins = can_white_win(plies_left - 1)
                
                board[r][c] = p
                board[nr][nc] = captured
                
                if not white_wins:
                    return True # Black found a move to prevent White's win
                    
            return False # White wins against ALL of Black's moves

        if can_white_win(m):
            out.append("YES")
        else:
            out.append("NO")

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()
# Gridland Metro
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])
    
    total_cells = n * m
    
    tracks_by_row = {}
    
    idx = 3
    for _ in range(k):
        r = int(input_data[idx])
        c1 = int(input_data[idx+1])
        c2 = int(input_data[idx+2])
        idx += 3
        
        if r not in tracks_by_row:
            tracks_by_row[r] = []
        tracks_by_row[r].append((c1, c2))
        
    occupied_cells = 0
    
    for r, intervals in tracks_by_row.items():
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        current_start, current_end = intervals[0]
        
        for next_start, next_end in intervals[1:]:
            if next_start <= current_end + 1:
                current_end = max(current_end, next_end)
            else:
                merged.append((current_start, current_end))
                current_start, current_end = next_start, next_end
        merged.append((current_start, current_end))
        
        for start, end in merged:
            occupied_cells += (end - start + 1)
            
    print(total_cells - occupied_cells)

if __name__ == '__main__':
    solve()
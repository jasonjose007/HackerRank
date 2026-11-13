# Cloudy Day 
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    town_pos = [int(x) for x in data[1:n+1]]
    town_pop = [int(x) for x in data[n+1:2*n+1]]
    
    m = int(data[2*n+1])
    cloud_pos = [int(x) for x in data[2*n+2:2*n+2+m]]
    cloud_range = [int(x) for x in data[2*n+2+m:2*n+2+2*m]]
    
    towns = sorted(zip(town_pos, town_pop))
    town_pos = [t[0] for t in towns]
    town_pop = [t[1] for t in towns]
    
    clouds = []
    for i in range(m):
        pos = cloud_pos[i]
        rng = cloud_range[i]
        clouds.append((pos - rng, pos + rng))
        
    events = []
    for i, (p, pop) in enumerate(zip(town_pos, town_pop)):
        events.append((p, 0, i, pop)) # 0 for town
        
    for j, (l, r) in enumerate(clouds):
        events.append((l, -1, j)) # cloud start
        events.append((r, 1, j)) # cloud end
        
    events.sort(key=lambda x: (x[0], x[1]))
    
    active_clouds = set()
    town_cloud_count = [0] * n
    town_covered_by = [-1] * n
    
    sunny_population = 0
    
    for event in events:
        if event[1] == -1: # cloud start
            active_clouds.add(event[2])
        elif event[1] == 1: # cloud end
            if event[2] in active_clouds:
                active_clouds.remove(event[2])
        else: # town
            idx = event[2]
            pop = event[3]
            count = len(active_clouds)
            town_cloud_count[idx] = count
            if count == 0:
                sunny_population += pop
            elif count == 1:
                town_covered_by[idx] = list(active_clouds)[0]
                
    cloud_saved_pop = [0] * m
    for i in range(n):
        if town_cloud_count[i] == 1:
            c_idx = town_covered_by[i]
            cloud_saved_pop[c_idx] += town_pop[i]
            
    max_saved = max(cloud_saved_pop) if cloud_saved_pop else 0
    print(sunny_population + max_saved)

if __name__ == '__main__':
    solve()
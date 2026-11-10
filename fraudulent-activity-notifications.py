# Fraudulent Activity Notifications
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def activityNotifications(expenditure, d):
    # Maximum possible expenditure value based on constraints (usually 200)
    MAX_VAL = 200
    
    count = [0] * (MAX_VAL + 1)
    
    # Initialize the frequency array for the first d days
    for i in range(d):
        count[expenditure[i]] += 1
        
    notifications = 0
    n = len(expenditure)
    
    def get_median(d, count):
        # Even d
        if d % 2 == 0:
            target1 = d // 2
            target2 = d // 2 + 1
            curr_sum = 0
            m1 = m2 = -1
            for i in range(len(count)):
                curr_sum += count[i]
                if m1 == -1 and curr_sum >= target1:
                    m1 = i
                if m2 == -1 and curr_sum >= target2:
                    m2 = i
                    break
            return (m1 + m2) / 2.0
        # Odd d
        else:
            target = d // 2 + 1
            curr_sum = 0
            for i in range(len(count)):
                curr_sum += count[i]
                if curr_sum >= target:
                    return float(i)
                    
    for i in range(d, n):
        median = get_median(d, count)
        if expenditure[i] >= 2 * median:
            notifications += 1
            
        # Slide the window
        count[expenditure[i - d]] -= 1
        count[expenditure[i]] += 1
        
    return notifications

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    d = int(input_data[1])
    expenditure = [int(x) for x in input_data[2:]]
    
    ans = activityNotifications(expenditure, d)
    print(ans)

if __name__ == '__main__':
    solve()
# Cipher
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

i = 0: `current_xor = 0`, `bit = 1^0 = 1`, `b = [1]`, `current_xor = 1`.
i = 1: `bit = 1^1 = 0`, `b = [1, 0]`, `current_xor = 1`.
i = 2: `bit = 1^1 = 0`, `b = [1, 0, 0]`, `current_xor = 1`.
i = 3: `bit = 0^1 = 1`, `b = [1, 0, 0, 1]`, `current_xor = 0`.
Loop finishes. Output: `1001`.
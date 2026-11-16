# Flipping bits
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

def flippingBits(n):
    return n ^ 0xFFFFFFFF

def main():
    q = int(input().strip())
    for _ in range(q):
        n = int(input().strip())
        print(flippingBits(n))

if __name__ == '__main__':
    main()
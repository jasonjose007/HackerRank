# Plus Minus
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for x in arr:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zero += 1
    print(f"{pos / n:.6f}")
    print(f"{neg / n:.6f}")
    print(f"{zero / n:.6f}")


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    plusMinus(arr)
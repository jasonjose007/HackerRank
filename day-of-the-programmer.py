# Day of the Programmer
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

def dayOfProgrammer(year):
    if year == 1918:
        return f"26.09.{year}"
    elif year < 1918:
        is_leap = (year % 4 == 0)
    else:
        is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    
    return f"12.09.{year}" if is_leap else f"13.09.{year}"

if __name__ == "__main__":
    year = int(input().strip())
    print(dayOfProgrammer(year))
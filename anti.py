# Example Antikythera puzzle solver
import sys

rowOne = [6, 10, 7, 19]
rowTwo = [3, 10, 10, 12]
rowThree = [33, 22, 25, 11]


def main():
    print("Row 1: " + str(addCol(1)))
    print("Row 2: " + str(addCol(2)))
    print("Row 3: " + str(addCol(3)))
    print("Row 4: " + str(addCol(4)))


def addCol(col):
    """Add columns"""
    if col == 1:
        sum = rowOne[0] + rowTwo[0] + rowThree[0]
    elif col == 2:
        sum = rowOne[1] + rowTwo[1] + rowThree[1]
    elif col == 3:
        sum = rowOne[2] + rowTwo[2] + rowThree[2]
    elif col == 4:
        sum = rowOne[3] + rowTwo[3] + rowThree[3]

    return sum


def scramble():
    """Scrambles puzzle in preparation for solving"""
    return 0


main()

def printMatrix():
    matrix = [ [1,2,3],[4,5,6],[7,8,9] ]
    for row in matrix:
        for col in row:
            print(col, end="")
        print()


if __name__ == "__main__":
    printMatrix()
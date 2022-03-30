import numpy as np
a = int(input("Enter the number of rows:"))
b = int(input("Enter the number of columns:"))
print("Enter the number in a single line separated by space:")
val = list(map(int, input().split()))
matrix = np.array(val).reshape(a,b)
print(matrix)

def matrix():
    matrix = [ [1,2,3],[4,5,6],[7,8,9] ]
    a = matrix[0][0], matrix[0][1], matrix[0][2]
    b = matrix[1][0], matrix[1][1], matrix[1][2]
    c = matrix[2][0], matrix[2][1], matrix[2][2]
    print(*a, sep=" ")
    print(*b, sep=" ")
    print(*c, sep=" ")
  
if __name__ == "__main__":
    matrix()
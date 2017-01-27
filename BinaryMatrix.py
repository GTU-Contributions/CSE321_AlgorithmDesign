import time

# Returns the minimum among 3 numbers
def getMinimum(num1, num2, num3):
    minimum = num1;
    if minimum > num2:
        minimum = num2 
    if(minimum > num3):
        minimum = num3
    
    return minimum

# Returns the size of the maximum square sub-matrix with all 1s
def findMaximumSizedSquareSize(matrix, rows, columns):
    # Current size of the maximum sub square
    size = 0
    # Sum matrix
    S = [[x for x in range(columns)] for y in range(rows)]

    # Copy first column of the matrix to the sum matrix
    for i in range(0, rows):
        S[i][0] = matrix[i][0]

    # Copy first row of the matrix to the sum matrix
    for i in range(0, columns):
        S[0][i] = matrix[0][i]

    for i in range(0, rows):
        for j in range(0, columns):
            if matrix[i][j] == 1:
                minNumber = getMinimum(S[i][j-1], S[i-1][j], S[i-1][j-1])
                S[i][j] = minNumber + 1
                # Update the size if bigger size is found
                if S[i][j] > size:
                    size = S[i][j]
            else: # when matrix[i][j] == 0
                S[i][j] = 0

    return size
    
def main():

    rows = 6
    columns = 5
    matrix = ([0, 1, 1, 0, 1], 
              [1, 1, 0, 1, 0], 
              [0, 1, 1, 1, 0],
              [1, 1, 1, 1, 0],
              [1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0])

    result = findMaximumSizedSquareSize(matrix, rows, columns)
    print("The maximum sized square size is:", result)
    time.sleep(5) # Sleep 5 seconds


main()

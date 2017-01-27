import time
import sys

def MatrixChainOrderOperations(a, size):
    # Allocate a 2D cash to hold the results
    # of minimum operations for subsequences
    cash = [[0 for x in range(size)] 
			for x in range(size)]
	
    # For multiplying one matrix the cost is zero
    for i in range(0, size):
        cash[i][i] = 0

    # matrixLength is the lenght of the matrices inside the parentheses
    # For example if we have ABCD
    # -> for matrixLength 2 = (AB)CD, A(BC)D, AB(CD)
    # The program saves the values of 2x2 multiplications in the cash
    # so when multiplying 3x3 the results of 2x2 is read from the cash
    # -> for matrixLength 3 = (ABC)D or A(BCD)
    for matrixLength in range(2, size):
        for i in range(1, size-matrixLength+1):
            j = i+matrixLength-1
            cash[i][j] = sys.maxsize
            
            for m in range(i, j):
                #Always the minimum cost is saved in the cash
                cost = cash[i][m] + cash[m+1][j] + a[i-1]*a[m]*a[j]
                if cost < cash[i][j]:
                    cash[i][j] = cost

    # Return the minimum number of operations from the cash
    return cash[1][size-1]

def main():

    #Example array of matrix sizes
    # A = 10x30
    # B = 30x5
    # C = 5x60
    array = [10, 30, 5, 60, 3]

    num = MatrixChainOrderOperations(array, len(array))
    print("Minimum number of operations is: " + str(num))
    time.sleep(5) # Sleep 5 seconds


main()

































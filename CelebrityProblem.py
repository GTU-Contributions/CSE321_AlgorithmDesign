import time

def CelebrityProblem():
    
    matrix = ([1, 0, 1, 1, 1],
              [0, 1, 1, 0, 1],
              [1, 1, 1, 0, 1],
              [0, 0, 1, 1, 1],
              [0, 0, 0, 0, 1])

    n = len(matrix)-1 # The maximum index for the matrix
    x, y, nextPerson = 0, 1, 2 

    # Eliminate all persons one by one until only 1 person remains
    while nextPerson <= n+1:
        if matrix[x][y] == 1: # If person x knows person y
            x = nextPerson # eliminate person x and assign next person
        else:
            y = nextPerson # eliminate person y and assign next person

        nextPerson += 1

    # Find who is the last checked person and make it candidate to be celebrity
    if x == n+1:
        candidate = y
    else:
        candidate = x

    # Set the value for candidate knows candidate to 0
    matrix[candidate][candidate] = 0
    
    celebrity = candidate
    # Check if the candidate knows any of the eliminated people or
    # Check if any of the eliminated people doesn't know the candidate
    for i in range(0, n+1):
        if matrix[candidate][i] or (not matrix[i][candidate] and i != candidate):
            celebrity = -1 # candidate knows somebody or he is not known by someone
            break;
    
    return celebrity
        
def main():

    print("The celebrity is:", CelebrityProblem())
    
    time.sleep(5) # Sleep 5 seconds
    
main()

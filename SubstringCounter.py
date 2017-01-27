import time

def BruteForceAlgorithm():
    theString = "CABAAXBYA"
    length = len(theString)
    num = 0
    for x in range(0, length):
        if theString[x] == 'A':
            for y in range(x+1, length):
                if theString[y] == 'B':
                    num += 1
    return num

def MoreEfficientAlgorithm():
    theString = "CABAAXBYA"
    length = len(theString)-1
    num = 0
    counter_B = 0
    
    for x in range(length, 0, -1):
        if theString[x] == 'A':
            num += counter_B
        if theString[x] == 'B':
            counter_B += 1
    
    return num
    
def main():

    print("BRUTE FORCE ALGORITHM")
    print("The number of substrings is:", BruteForceAlgorithm())
    print("MORE EFFICIENT ALGORITHM")
    print("The number of substrings is:", MoreEfficientAlgorithm())
    
    time.sleep(5) # Sleep 5 seconds
    
main()

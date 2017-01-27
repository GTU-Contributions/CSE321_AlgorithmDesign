import time

def makeFlip(pancakes, n):
    i = 0
    while i < n:
        swap = pancakes[i]
        pancakes[i] = pancakes[n]
        pancakes[n] = swap
        i += 1
        n -= 1

    return pancakes

def FlippingPancakes(pancakes):
    length = len(pancakes)

    if length < 2:
        return pancakes

    for i in range(length, 0, -1):
        maxIndex = 0
        for j in range(0, i):
            if(pancakes[j] > pancakes[maxIndex]):
                maxIndex = j

        if maxIndex == i-1:
            continue;

        if maxIndex:
            print("Making flip:", makeFlip(pancakes, maxIndex))

        print("Making flip:", makeFlip(pancakes, i-1))
    
def main():

    pancakes = [1, 2, 10, 7, 8, 3]

    print("Pancakes:", pancakes)
    FlippingPancakes(pancakes)
    print("Sorted pancakes:", pancakes)
    
    time.sleep(5) # Sleep 5 seconds
    
main()

import time

def CreateDisks(size):
    Disks = []
    for i in range(1, (2*size+1)):
        if i%2 != 0:
            Disks.append("1") # Append 1 for black disk
        else:
            Disks.append("0") # Append 0 for white disk

    return Disks

def AlternatingDisks(DisksList):
    startIndex = 0
    endIndex = len(DisksList)-1
    moves = 0
    swapped = 1
    while(swapped):
        swapped = 0
        
        for i in range(startIndex, endIndex, 2):
            DisksList[i], DisksList[i+1] = DisksList[i+1], DisksList[i] # swapp i and i+1 disk
            swapped = 1
            moves += 1

        startIndex += 1
        endIndex -= 1

    return moves
                    
def main():
    numOfDisks = int(input("Enter the number of the disks for one color: "))
    print("The number of disks entered for one color is:", numOfDisks)

    DisksList = CreateDisks(numOfDisks)
    print("Starting position of the disks:", DisksList)

    moves = AlternatingDisks(DisksList)
    print("Last position of the disks:", DisksList)
    print("The minimum moves needed is:", moves)

    time.sleep(5) # Sleep 5 seconds
    
main()

import time

# item = (ID, Weight, Value)
ITEMS = [("Green", 12, 4),
         ("Blue", 2, 2),
         ("Grey", 1, 2),
         ("Orange", 1, 1),
         ("Yellow", 4, 10)]

# Returns the value of an item
def value(item):
    return item[2]

# Returns the weight of an item
def weight(item):
    return item[1]

# Returns the density of an item (value per weight)
def density(item):
    return float(item[2])/float(item[1])

# Parameters:
# items: The items list
# maxWeight: The max weight of the knapsack
# keyFunc: Can be 'value', 'weight' or 'density'
def greedyKnapsack(items, maxWeight, keyFunc):
    # List to hold all the items we put in the knapsack
    knapsackList = []
    # Initialize knapsack value and weight to 0
    knapsackValue = 0
    knapsackWeight = 0
    # Sort the items according to the key function
    sorted_items = sorted(items, key = keyFunc)

    # While there are any unprocessed items
    while len(sorted_items) > 0:
        item = sorted_items.pop()
        # If the sum of the current weight of the bag and
        # the weight of the current item is not greater than
        # the max weight of the bag
        if knapsackWeight + weight(item) <= maxWeight:
            # Add the item to the bag
            knapsackList.append(item) 
            # Add the value of the current item to the total value of the bag
            knapsackValue += value(item)
            # Add the weight of the current item to the total weight of the bag
            knapsackWeight += weight(item)
            
    return knapsackList, knapsackWeight, knapsackValue

def main():
    # Max weight that can be taken by the knapsack
    maxWeight = 15

    print("The max value of the knapsack is: " + str(maxWeight))
    print("~~~~~ item = (ID, Weight, Value) ~~~~~")
    print("-------------------------------------------------------------")
    print("Items choosen according to the value: ")
    vKnapsack, vWeight, vValue = greedyKnapsack(ITEMS, maxWeight, value)
    print("Items: " + str(vKnapsack))
    print("Total value: " + str(vValue) + ", Total weight: " + str(vWeight))
    print("-------------------------------------------------------------")
    print("Items choosen according to the weight: ")
    wKnapsack, wWeight, wValue = greedyKnapsack(ITEMS, maxWeight, weight)
    print("Items: " + str(wKnapsack))
    print("Total value: " + str(wValue) + ", Total weight: " + str(wWeight))
    print("-------------------------------------------------------------")
    print("Items choosen according to the density: ")
    dKnapsack, dWeight, dValue = greedyKnapsack(ITEMS, maxWeight, density)
    print("Items: " + str(dKnapsack))
    print("Total value: " + str(dValue) + ", Total weight: " + str(dWeight))
    print("-------------------------------------------------------------")
    
    time.sleep(10) # Sleep 10 seconds

main()

# Print unordered pairs

def printUnorderedPairs(array):
    for i in range(0, len(array)+1):
        for j in range(i + 1, len(array)):
            print(array[i], ",", array[j])

printUnorderedPairs([1, 2, 3, 4, 5])
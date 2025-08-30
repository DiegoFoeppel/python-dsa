# Big O examples

# O(1) - Constant - A simple add numbers function
def add(a, b):
    return a + b

def multiplyNumber(n):
    return n * n

# O(n) - Linear - Loop through array items
def printValues(vet):

    for i in range(len(vet)):
        print(i)

# O(LogN) - Logarithmic - Find an element in a sorted array
# Creio que seja busca binária

def binarySearch(vet):
    return

#  O(n^2) - Quadratic - Nested Loops -> Matriz exemplo

def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        print(total)
        total += add(i, i+1)
    return total

print(pair_sum_sequence(5))

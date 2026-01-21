def missing_number(arr, n):
    return sum(list(range(1, n+1))) - sum(arr)

print(missing_number([2, 3, 4, 5, 6], 6))
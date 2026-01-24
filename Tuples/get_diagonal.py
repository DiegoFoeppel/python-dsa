def get_diagonal(tup):
    result = []
    
    for i in range(len(tup)):
        result.append(tup[i][i])

    return tuple(result)

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
print(tuple1 | tuple2)
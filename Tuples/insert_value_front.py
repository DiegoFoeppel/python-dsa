def insert_value_front(input_tuple, value_to_insert):

    # result = list(input_tuple)

    print(len(input_tuple))
    # if len(input_tuple) == 0:
    #     return (value_to_insert, )

    # for i in range(len(input_tuple)):
    #     if value_to_insert < input_tuple[i]:
    #         result.insert(0, value_to_insert)
    #         break
    
    return (value_to_insert, ) + input_tuple

input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)  # Expected output: (1, 2, 3, 4)
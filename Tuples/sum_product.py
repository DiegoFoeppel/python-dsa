def sum_product(tuple):

    sumTuple = 0
    product = 1

    for num in tuple:
        sumTuple += num
        product *= num
    
    return sumTuple, product

input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)  # Expected output: 10, 24

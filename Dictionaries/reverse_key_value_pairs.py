def reverse_dict(my_dict):
    result = {}
    
    for key, value in my_dict.items():
        result[value] = key
    
    return result

print(reverse_dict({'a': 1, 'b': 2, 'c':3}))
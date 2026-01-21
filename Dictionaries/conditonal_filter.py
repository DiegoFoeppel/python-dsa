
def filter_dict(my_dict, condition):
    
    result = {k: v for k, v in my_dict.items() if condition(k, v)}
    
    return result

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
filtered_dict = print(filter_dict(my_dict, lambda k, v: v % 2 == 0))

# {'b': 2, 'd': 4}

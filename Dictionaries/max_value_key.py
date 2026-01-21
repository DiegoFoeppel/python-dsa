def max_value_key(my_dict):
    # TODO
    maxValueKey = ""
    maxValue = 0
    
    for key, value in my_dict.items():
        
        if value > maxValue:
            maxValue = value
            maxValueKey = key
    
    return maxValueKey

my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))
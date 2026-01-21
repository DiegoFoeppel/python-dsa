
def merge_dicts(dict1, dict2):
    
    dictMerge = dict1

    # result = dict1.copy()
    
    for k, v in dict2.items():
        print(k, v)

        # result[key] = result.get(key, 0) + value
        
        if k in dict1:
            dict1[k] += v
        else:
            dictMerge[k] = v

    print(dictMerge)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)

# {'a': 1, 'b': 5, 'c': 7, 'd': 5}
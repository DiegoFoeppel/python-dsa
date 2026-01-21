def check_same_frequency(list1, list2):

    dict1 = {k: list1.count(k) for k in list1}
    dict2 = {k: list2.count(k) for k in list2}

    print(dict1, dict2)

    return dict1 == dict2

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))
    

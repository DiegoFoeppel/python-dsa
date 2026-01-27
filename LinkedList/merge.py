

def merge_lists(l1, l2):
    res = []

    # maior len 
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1 

    for i in range(len(l1)):
        if l1[i] == l2[i]:
            res.append(l1[i])
            res.append(l2[i])
        elif l1[i] > l2[i]:
            res.append(l2[i])
            res.append(l1[i])
        else:
            res.append(l1[i])
            res.append(l2[i])

    return res

# merge sorted_lists

print(merge_lists([], [0]))
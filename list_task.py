def remove_adjacent(lst):
  return [lst[i] for i in range(len(lst)) if i == 0 or lst[i-1] != lst[i]]
    


def linear_merge(lst1, lst2):
    res = []
    i = 0
    j = 0
    while ((i < len(lst1)) and (j < len(lst2))):
        if lst1[i] < lst2[j]:
            res.append lst1[i]
            i += 1
        else:
            res.append lst2[j]
            j += 1
    return res
        





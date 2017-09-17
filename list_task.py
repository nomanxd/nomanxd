def remove_adjacent(lst):
  return [lst[i] for i in range(len(lst)) if i == 0 or lst[i-1] != lst[i]]
    


def linear_merge(lst1, lst2):
    return sorted(lst1 + lst2);





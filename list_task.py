def remove_adjacent(lst):
  return [lst[i] for i in range(len(lst)) if i == 0 or lst[i-1] != lst[i]]
    


 def linear_merge(lst1, lst2):
      result = []
      while len(lst1) and len(lst2):
        if lst1[0] < lst2[0]:
          result.append(lst1.pop(0))
         else:
          result.append(lst2.pop(0))
      return result
        





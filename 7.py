def firstDescPair(ls):
  for i in range(len(ls)):
    if(ls[i] > ls[i+1]):
      return ls[i],ls[i+1]
      
  return None, None

print(firstDescPair([2, 5, 8, 12, -5, 10, 12, 8]))
print(firstDescPair([50, 57, 108, 123, 1000, 999, 998, 0]))
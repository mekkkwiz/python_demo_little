def missing_integer(data):
  refData = [0,1,2,3,4,5,6,7,8,9]
  difference_1 = set(refData).difference(set(data))
  return difference_1.pop()

def missing_integerV2(data):
  refData = [0,1,2,3,4,5,6,7,8,9,10]
  for val in refData:
    if (val not in data):
      return val

print(missing_integerV2([3, 2, 10, 8, 5, 0, 1, 7, 6, 4]))
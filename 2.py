def complement9(x):
  if(x > 0):
    digits = [int(i) for i in str(x)]
    resList = [str(9-i) for i in digits]
    return str(resList)


print(complement9(431609))

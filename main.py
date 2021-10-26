def maxlen(s):
  s = str(s)
  splitedList = s.split()
  lenOfSplitedList = [len(val) for val in splitedList]
  maxlenOfList = max(lenOfSplitedList) 

  print(maxlenOfList)
  for i in range(len(splitedList)):
    if (lenOfSplitedList[i] == maxlenOfList):
      print(splitedList[i])

maxlen("Row, row, row your boat")
maxlen("Gently down the stream")
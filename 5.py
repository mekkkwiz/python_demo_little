def is_anagram(str1, str2):
  stack = []
  for i in str1:
    stack.append(i)
  for j in str2:
    if (j in stack):
      stack.pop(stack.index(j))
    else:
      return False
    if(len(stack) == 0):
      return True
    
    
print(is_anagram("abcde","acebd"))
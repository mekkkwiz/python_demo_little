def is_quirksome(x, digit):
  x1 = int(x/(10**(digit-(digit/2))))
  x2 = int(x%(10**(digit-(digit/2))))

  # print(x1,x2)
  
  if ((x1+x2)**2 == x):
    return True
  else:
    return False


print(is_quirksome(1234,4))
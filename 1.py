def sumOE(x):

  digits = [int(i) for i in str(x)]
  odd = []
  even = []
  print(digits)

  for i in digits:
    if (i%2 == 0): #หาร 2 ลงตัว(เลขคู่)
      even.append(i)
    else: #หาร 2 แล้วเหลือเศษ (เลขคี่)
      odd.append(i)

  return sum(odd), sum(even)


x,y = sumOE(431257380)
print(x, y)

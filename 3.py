def is_abecedarian(s):
  # print(s,"".join(sorted(s)))
  if (s == "".join(sorted(s))):
    return True
  else:
    return False


print(is_abecedarian("duck"))
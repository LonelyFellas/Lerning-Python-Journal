"""
Author: dariwish
"""
def elsePassed(): 
  print("program start ....")
  n = 1
  while n < 10:
    n += 1
    print("n: ", n)
  else:
    print("program accoss 'else' end ...")
  
def breakEnd():
  print("program start ...")
  n = 1
  while n < 10:
    n += 1
    print("n: ", n)
    if n > 8:
      break
  else:
    print("progam accoss 'else' end ...")
breakEnd()
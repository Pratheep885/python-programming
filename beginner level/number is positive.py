numvarb=int(raw_input())
if(numvarb<=100000):  
  if(numvarb==0):
    print("zero")
  elif(numvarb<0):
    print("negative")
  else:
    print("positive")
else:
  print("number is greater than 100000")

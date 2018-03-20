N=int(raw_input())
if(N<=100000):  
  if(N>0):
    print("positive")
  elif(N==0):
    print("zero")
  else:
    print("negative")
else:
  print("number is greater than 100000")

N=int(raw_input())
if(N<=100000):  
  if(N==0):
    print("zero")
  elif(N<0):
    print("negative")
  else:
    print("positive")
else:
  print("number is greater than 100000")

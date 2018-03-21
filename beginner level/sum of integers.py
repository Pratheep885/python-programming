sl=int(raw_input())
wx=int(raw_input())
list=[]
sum=0
for i in range(0,sl):
  r=int(raw_input())
  list.append(r)
for j in range(0,wx):
  sum=sum+list[j]
print(sum)

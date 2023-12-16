A=list(map(str,input()))
newA=[]

temp=[]
for i in A:
  if i=='-' or i=='+':
    newA.append(int(''.join(temp)))
    temp.clear()
    newA.append(i)
    continue
  else:
    temp.append(i)

newA.append(int(''.join(temp)))
del A, temp
 
ans=0
isMinus=False
temp=[]
for i in newA:
  if i=='-':
    if isMinus:
      ans-=sum(temp)
    else:
      ans+=sum(temp)
    temp.clear()
    isMinus=True
  elif i=='+':
    continue
  else:
    temp.append(i)

if isMinus:
  ans-=sum(temp)
else:
  ans+=sum(temp)

print(ans)
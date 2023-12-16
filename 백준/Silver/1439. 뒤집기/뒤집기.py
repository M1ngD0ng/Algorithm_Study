S=list(map(int,input()))


A=[]

prev=S[0]
temp=[prev]

for i in S:
  if i!=prev: 
    temp.append(i)
    prev=i
cnt0=temp.count(0)
cnt1=temp.count(1)

print(min(cnt0,cnt1))
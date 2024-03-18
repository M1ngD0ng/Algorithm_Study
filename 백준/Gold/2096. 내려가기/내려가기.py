import sys

N=int(sys.stdin.readline()) 
_max=list(map(int,sys.stdin.readline().split()))
_min=[_max[0],_max[1],_max[2]]
for i in range(1,N):
  temp1=[_max[0],_max[1],_max[2]]
  temp2=[_min[0],_min[1],_min[2]]

  a,b,c=map(int,sys.stdin.readline().split())
  _max[0]=(max(temp1[0],temp1[1])+a)
  _max[1]=(max(temp1[0],temp1[1],temp1[2])+b)
  _max[2]=(max(temp1[1],temp1[2])+c)

  _min[0]=(min(temp2[0],temp2[1])+a)
  _min[1]=(min(temp2[0],temp2[1],temp2[2])+b)
  _min[2]=(min(temp2[1],temp2[2])+c)

print(max(_max),min(_min)) 
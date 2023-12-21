import sys
while True:
  A=list(map(int,sys.stdin.readline().split()))
  if A[0]==A[1]==A[2]==0:
    break
  A.sort(reverse=True)
  if A[0]>=(A[1]+A[2]):
    print("Invalid")
  else:
    temp=A.count(A[0])
    if temp==3:
      print("Equilateral")
    elif temp==2:
      print("Isosceles")
    else:
      temp=A.count(A[1])
      if temp==2:
        print("Isosceles")
      else:
        print("Scalene")
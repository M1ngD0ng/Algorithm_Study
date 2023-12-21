import sys
N=int(sys.stdin.readline())


if N==1:
  print(1)

else:
  cnt=2
  dp=7
  while True:
    if N<=dp:
      print(cnt)
      break
    else:
      dp+=(cnt*6)
      cnt+=1 
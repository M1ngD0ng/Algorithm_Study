import math
from collections import deque

def solution(prog, speeds):
    answer = []
    
    N=len(prog)
    q=deque()
    for i in range(N):
        day=math.ceil((100-prog[i])/speeds[i])
        q.append(day)
    
    cur=q.popleft()
    cnt=1
    while q:
        v=q.popleft()
        
        if v>cur:
            answer.append(cnt)
            cur=v
            cnt=1
        else:
            cnt+=1
            
    answer.append(cnt)
    return answer
import heapq

def solution(n, w):
    ans = 0
    if sum(w)<=n:
        return 0
    
    for i in range(len(w)):
        w[i]*=-1
    heapq.heapify(w)
        
    for i in range(n):
        v=heapq.heappop(w)
        heapq.heappush(w,v+1)
        
    for i in range(len(w)):
        ans+=(w[i]*w[i])
    
    return ans
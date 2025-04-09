def solution(want, number, discount):
    answer = 0
    
    d=dict()
    N=len(want)
    M=len(discount)
    
    for i in range(10):
        if discount[i] in d.keys():
            d[discount[i]]+=1
        else:
            d[discount[i]]=1
    
    left=0
    
    while True:
        isPossible=True
        for i in range(N):
            if want[i] in d.keys() and d[want[i]]>=number[i]:
                continue
            else:
                isPossible=False
                break
        if isPossible:
            answer+=1
        
        left+=1
        if left+9==M:
            break
        
        d[discount[left-1]]-=1
        if discount[left+9] in d.keys():
            d[discount[left+9]]+=1
        else:
            d[discount[left+9]]=1
        
        
    return answer
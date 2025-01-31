def solution(N, stages): 
    M=len(stages)
    
    dp=[0 for _ in range(N+2)]
    fail=dict()
    
    for i in range(M):
        dp[stages[i]]+=1
    
    print(dp)
    for i in range(1,N+1):
        if dp[i]!=0:
            fail[i]=dp[i]/(M-dp[i-1])
        else:
            fail[i]=0
        dp[i]+=dp[i-1]
    print(dp)
    answer=sorted(fail.keys(), key=lambda x:(-fail[x],x))
    return answer
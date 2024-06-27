import sys
sys.setrecursionlimit(10**6)

def solution(begin, target, words):
    answer = 1e8
    
    if target not in words:
        return 0
    
    li=[[] for _ in range(len(begin))]
    
    for i in range(len(begin)):
        for j in range(len(words)):
            li[i].append(words[j][i])
    
    begin=list(begin)
    target=list(target)
    visited=dict()
    def dfs(begin,cnt):
        nonlocal answer
        if begin==target:
            answer=min(answer,cnt)
            return
        for i in range(len(target)):
            if begin[i]==target[i]:
                continue

            temp=begin[i]
            for s in set(li[i]):
                begin[i]=s
                _str=''.join(begin)
                if _str in words:
                    if _str not in visited:
                        visited[_str]=cnt+1
                        dfs(list(_str), cnt+1)
                    else:
                        if visited[_str]>cnt+1:
                            visited[_str]=cnt+1
                            dfs(list(_str), cnt+1)
            begin[i]=temp

    dfs(begin,0)
    return answer
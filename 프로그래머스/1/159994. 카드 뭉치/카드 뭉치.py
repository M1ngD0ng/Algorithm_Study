def solution(c1, c2, goal):
    answer = ''
    
    idx1=0
    idx2=0
    
    N=len(c1)
    M=len(c2)
    for g in goal:
        if idx1<N and c1[idx1]==g:
            idx1+=1
        elif idx2<M and c2[idx2]==g:
            idx2+=1
        else:
            return 'No'
    return 'Yes'
    
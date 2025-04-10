def solution(genres, plays):
    answer = []
    
    gDict=dict()
    pDict=dict()
    
    N=len(genres)
    
    for i in range(N):
        if genres[i] in gDict.keys():
            gDict[genres[i]]+=plays[i]
        else:
            gDict[genres[i]]=plays[i]
            
        if genres[i] in pDict.keys():
            pDict[genres[i]].append([plays[i],i])
        else:
            pDict[genres[i]]=[[plays[i],i]]
            
    sort1=sorted(gDict.keys(), key=lambda x:(-gDict[x]))
    
    for s in sort1:
        sort2=sorted(pDict[s], key=lambda x:(-x[0], x[1]))
        for i in range(min(len(sort2),2)):
            answer.append(sort2[i][1])
    
    return answer
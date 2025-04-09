def solution(record):
    answer = []
    
    d=dict()
    history=[]
    for r in record:
        if r[0]=='E':
            A,B,C=r.split()
            d[B]=C
            history.append((B,True))
        elif r[0]=='L':
            A,B=r.split()
            history.append((B,False))
        else:
            A,B,C=r.split()
            d[B]=C
    
    for h in history:
        s=''
        if h[1]==True:
            s="님이 들어왔습니다."
        else:
            s="님이 나갔습니다."
        answer.append(d[h[0]]+s)
    
    return answer
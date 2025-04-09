

def solution(part, comp):
    answer = ''
    
    d=dict()
    
    for c in comp:
        if c in d.keys():
            d[c]+=1
        else:
            d[c]=1
    
    for p in part:
        if p in d.keys() and d[p]>0:
            d[p]-=1
        else:
            return p
            
    
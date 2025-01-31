def solution(answers):
    arr=[
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    d=dict()
    
    _max=-1
    ans=[]
    for i in range(3):
        N=len(arr[i])
        d[i+1]=0
        
        for j in range(len(answers)):
            temp=j%N
            if(arr[i][temp]==answers[j]): d[i+1]+=1
            
        if(d[i+1]>_max):
            _max=d[i+1]
            ans=[i+1]
        elif d[i+1]==_max:
            ans.append(i+1)
    
    return ans
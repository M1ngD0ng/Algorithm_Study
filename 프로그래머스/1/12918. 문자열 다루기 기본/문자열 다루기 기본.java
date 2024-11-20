class Solution {
    public boolean solution(String s) {
        boolean answer = true;
        int N=s.length();
        
        if(N==4 || N==6){
            for(int i=0;i<N;i++){
                int a=s.charAt(i);
                if(a>47 && a<58) continue;
                else return false;
            }
        }else return false;
        
        return answer;
    }
}
class Solution {
    public String solution(String s) { 
        int len=s.length();
        if(len%2==0){
            return s.substring((int)(len/2)-1,(int)(len/2)+1);
        }else{
            return s.substring((int)(len/2),(int)(len/2)+1);
        } 
    }
}
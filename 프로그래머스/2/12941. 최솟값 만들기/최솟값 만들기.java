import java.util.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        List<Integer> listA = new ArrayList<>();
        List<Integer> listB = new ArrayList<>();
        
        for(int i:A){
            listA.add(i);
        }
        
        for(int i:B){
            listB.add(i);
        }
        
        Collections.sort(listA);
        Collections.sort(listB, Collections.reverseOrder());
        
        for(int i=0;i<A.length;i++){
            answer+=listA.get(i)*listB.get(i);
        }
        return answer;
    }
}
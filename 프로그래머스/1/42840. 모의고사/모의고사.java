import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i=1;i<4;i++){
            map.put(i,0);
        }
        
        int[] temp = {1,2,3,4,5};
        for(int i=0;i<answers.length;i++){
            if(isCorrect(answers[i], temp[i%5])) map.put(1, map.get(1)+1);
        }
        
        int[] temp1 = {2,1,2,3,2,4,2,5};
        for(int i=0;i<answers.length;i++){
            if(isCorrect(answers[i], temp1[i%8])) map.put(2, map.get(2)+1);
        }
        
        int[] temp2 = {3,3,1,1,2,2,4,4,5,5};
        for(int i=0;i<answers.length;i++){
            if(isCorrect(answers[i], temp2[i%10])) map.put(3, map.get(3)+1);
        }
        
        ArrayList<Integer> arr = new ArrayList<>();
        int maxValue=0;
        
        for(int i=1;i<4;i++){
            if(map.get(i)>maxValue){
                maxValue=map.get(i);
                arr.clear();
                arr.add(i);
            } else if(map.get(i)==maxValue) arr.add(i);
        }
        
        return arr.stream().mapToInt(Integer::intValue).toArray();
    }
    
    public boolean isCorrect(int a, int b){
        return a==b;
    }
}
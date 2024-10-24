import java.util.*;
import java.io.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        StringTokenizer st= new StringTokenizer(s);
        int _min=Integer.MAX_VALUE;
        int _max=Integer.MIN_VALUE;
        while(st.hasMoreTokens()){
            int temp = Integer.parseInt(st.nextToken());
            if(temp<_min) _min=temp;
            if(temp>_max) _max=temp;
        }
        return Integer.toString(_min)+" "+Integer.toString(_max);
    }
}
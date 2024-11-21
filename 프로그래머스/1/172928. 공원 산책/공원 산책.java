class Solution {
    public int[] solution(String[] park, String[] routes) { 
        int N=park.length;
        int M=park[0].length();
        int[] dx={0,0,-1,1};
        int[] dy={-1,1,0,0}; // 좌우상하 WENS
        
        int sx=0;
        int sy=0;
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(park[i].charAt(j)=='S'){
                    sx=i;
                    sy=j;
                    break;
                }
            }
        }
        for(String s: routes){
            String[] code=s.split(" ");
            int direc = transToIdx(code[0].charAt(0));
            int dist = Integer.parseInt(code[1]);
            
            int nx=sx+dx[direc]*dist;
            int ny=sy+dy[direc]*dist;
            
            if(nx<0 || nx>=N || ny<0 || ny>=M) continue;
            
            int tx=sx;
            int ty=sy;
            
            boolean isPossible=true;
            
            for(int i=0;i<dist;i++){
                tx+=dx[direc];
                ty+=dy[direc];
                if(park[tx].charAt(ty)=='X'){
                    isPossible=false;
                    break;
                }
            }
            if(isPossible){
                sx=tx;
                sy=ty;
            }
            
        }
        int[] answer={sx,sy};
        return answer;
    }
    
    int transToIdx(char c){
        if(c=='W') return 0;
        else if(c=='E') return 1;
        else if(c=='N') return 2;
        else return 3;
    }
}
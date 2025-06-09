// public class Main {
//   public static void main(String[] args) {
//     System.out.println("Hello World!");
//   }
// }

import java.util.*;
import java.io.*;

public class Main {
  static class Node {
    int x;
    int y;

    Node(int x, int y) {
      this.x = x;
      this.y = y;
    }

    @Override
    public boolean equals(Object o){
      if(this==o) return true;
      if(o==null || getClass()!=o.getClass()) return false;

      Node node=(Node) o;
      return x==node.x && y==node.y;
    }

    @Override
    public int hashCode(){
      return Objects.hash(x,y);
    }
  }

  public static void main(String[] args) throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    int M = Integer.parseInt(br.readLine());
    Set<Node> hs1=new HashSet<>();
    Set<Node> hs2=new HashSet<>();


    st=new StringTokenizer(br.readLine());
    int x=Integer.parseInt(st.nextToken());
    int y=Integer.parseInt(st.nextToken());
    hs1.add(new Node(0,0));
    
    for(int i=0;i<M-1;i++){
      st=new StringTokenizer(br.readLine());
      int vx=Integer.parseInt(st.nextToken());
      int vy=Integer.parseInt(st.nextToken());
      hs1.add(new Node(x-vx,y-vy));
    }

    int N=Integer.parseInt(br.readLine());
    for(int i=0;i<N;i++){
      st=new StringTokenizer(br.readLine());
      int vx=Integer.parseInt(st.nextToken());
      int vy=Integer.parseInt(st.nextToken());
      hs2.add(new Node(vx,vy));
    }
    
    for(Node node:hs2){
      boolean isPossible=true;
      for(Node nd:hs1){
        if(!hs2.contains(new Node(node.x-nd.x, node.y-nd.y))){
          isPossible=false;
          break;
        }
      }
      if(isPossible){
        System.out.println((node.x-x)+" "+(node.y-y));
        break;
      }
    }
    
  }
}
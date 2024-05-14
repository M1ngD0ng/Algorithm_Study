#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    long long num =n;
    int ans = 0;
    if(num==1) return 0;
    while(true){
        if(num%2==0){
            num/=2;
        }else{
            num=num*3+1;
        }
        ans+=1;
        if (num==1) return ans;
        if (ans>500) return -1;
    }
    
    return -1;
}
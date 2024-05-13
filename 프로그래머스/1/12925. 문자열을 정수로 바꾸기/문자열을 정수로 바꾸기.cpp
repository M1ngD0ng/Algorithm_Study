#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    bool flag=true;
    int answer = 0;

    if (s[0]=='-'){
        s.erase(0,1);
        flag=false;
    } else if (s[0]=='+'){
        s.erase(0,1);
    }
    if (!flag) answer=stoi(s)*-1;
    else answer=stoi(s);
    
    
    return answer;
}
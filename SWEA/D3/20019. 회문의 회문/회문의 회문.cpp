#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case){
        string str;
        cin>>str;
        int N=str.length();
        int cnt=N-1;
        bool flag=true;
        
        for (int i=0;i<N;i++){
            if(str[i]!=str[cnt]){
                flag=false;
                break;
            } else cnt-=1;
        }
        if(!flag){
            cout<<'#'<<test_case<<" NO\n";
            continue;
        } 

        cnt=((N-1)/2)-1;
        for (int i=0;i<((N-1)/2);i++){
            if(str[i]!=str[cnt]){
                flag=false;
                break;
            } else cnt-=1;
        }
        if(!flag){
            cout<<'#'<<test_case<<" NO\n";
            continue;
        }
        
        cnt=N-1;
        for (int i=((N-1)/2)+1;i<N;i++){
            if(str[i]!=str[cnt]){
                flag=false;
                break;
            } else cnt-=1;
        }
        if(!flag) cout<<'#'<<test_case<<" NO\n";
        else cout<<'#'<<test_case<<" YES\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
#include<iostream>
#include<algorithm>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
    int N=8;
	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
	for(test_case = 1; test_case <= T; ++test_case) {
        char board[N][N];
        int row[N];
        int col[N];

        for(int i=0;i<N;i++){
            row[i]=0;
            col[i]=0;

            for(int j=0;j<N;j++){
                cin>>board[i][j];

            }
        }
        int ans=0;
        for (int i=0;i<N;i++){
            for (int j=0; j<N;j++){
                if (board[i][j]=='O'){
                    ans+=1;
                    row[i]+=1;
                    col[j]+=1;
                }
            }
        }
        if(ans!=8) {
            cout<<'#'<<test_case<<" no\n";
            continue;
        }
        bool flag=true;
        for (int i=0;i<N;i++){
            if(row[i]>1 || col[i]>1) {
                flag=false;
                break;
            }
        }
        if(!flag) cout<<'#'<<test_case<<" no\n";
        else cout<<'#'<<test_case<<" yes\n";
	}
	return 0;
}
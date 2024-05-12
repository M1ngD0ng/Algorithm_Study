#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case){
        int A[3];
        int ans=0;
        cin>>A[0]>>A[1]>>A[2]; 
        bool flag=true;
        
        for (int i=2;i>0;i--){
            if (A[i]>A[i-1]) continue;
            else {
                while(true){
                    A[i-1]-=1;
                    if(A[i]>A[i-1]){
                        if(A[i-1]==0){
                            flag=false;
                            break;
                        }
                        else{
                            ans+=1;
                            break;
                        }
                    }
                    ans+=1;
                }
            }
            if(!flag){
                ans=-1;
                break;
            }
        }
        cout<<'#'<<test_case<<' '<<ans<<'\n';
        
	}
	return 0;
}
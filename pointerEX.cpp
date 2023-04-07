/* Quiz #10 다음 이차원배열을 출력하세요.
int c[3][5] = { {1, 3, 5, 77, 9}, {10, 20, 3, 4, -1}, {0, 0, 8, 5, 3} };
(1) 이중 for문 이용
(2) 단일 for문 이용 (힌트: 포인터 사용)
*/
/*
#include<iostream>
using namespace std;
int main(){
    int c[3][5] = { {1, 3, 5, 77, 9}, {10, 20, 3, 4, -1}, {0, 0, 8, 5, 3} };
    for (int i=0; i<15; i++){
        cout<<c[i/5][i%5]<<" ";
        if((i+1)%5==0){
            cout << endl;
        }
    }
    return 0;
}
*/

#include<iostream>
using namespace std;
int main(){
    int c[3][5] = { {1, 3, 5, 77, 9}, {10, 20, 3, 4, -1}, {0, 0, 8, 5, 3} };
    int (*p)[5] = c; // 행을 5로하는 2차원 배열 생성
    for (int i=0; i<15; i++){
        cout<<p[i/5][i%5]<<" ";
        if((i+1)%5==0){
            cout << endl;
        }
    }
    return 0;
}
// (*(p+(i/5)))[i%5]
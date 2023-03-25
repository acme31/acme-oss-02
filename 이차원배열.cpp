#include<iostream>
using namespace std;

class ThreeMatrices {
    int a[3][5] = { {5, 10, 2, 7, 5}, {4, 6, 2, 2, 9}, {1, 9, 2, 8, 4} };
    int b[3][5] = { {5, 2, 7, 4, 5}, {10, 6, 9, 2, 3}, {2, 6, 4, 7, 1} };
    int c[3][5];
public:
    ThreeMatrices(); // 배열값을 초기화 하기 위한 생성지
    void printC(); // 맴버함수
    void biggerC(); // 배열 값 큰 거 골라내는 멤버함수
    void smallerC(); // 배열 값 작은 거 골라내는 멤버함수
    // 전부 매개변수가 존재하지 않는 생성자임
}; // public 의 마지막에선 세미콜론 추가 필요
ThreeMatrices::ThreeMatrices(){ // 생성자 선언 구문
    for(int i=0; i<=2; i++){
        for(int k=0; k<=4 ; k++){
            c[i][k] = 0;
        }
    } // 2차원 배열 0으로 초기화
} 
void ThreeMatrices::printC(){ // 출력 위한 멤버함수
    for(int i=0; i<=2; i++){
        for(int k=0; k<=4 ; k++){
            cout << c[i][k] << " ";
        }
        cout << endl;
    }
}
void ThreeMatrices::biggerC(){ // 큰 값 걸러내기 위한 멤버함수
    for(int i=0; i<=2; i++){
        for(int k=0; k<=4 ; k++){
            if(a[i][k]>b[i][k]){
                c[i][k] = a[i][k];
            }
            else{
                c[i][k] = b[i][k];
            }
        }
    }
}
void ThreeMatrices::smallerC(){ // 작은 값 걸러내기 위한 멤버함수
    for(int i=0; i<=2; i++){
        for(int k=0; k<=4 ; k++){
            if(a[i][k]<b[i][k]){
                c[i][k] = a[i][k];
            }
            else{
                c[i][k] = b[i][k];
            }
        }
    }
    
}
int main(){
    ThreeMatrices m; // class 를 호출하기 위한 선언문
    cout << "initial..." << endl; m.printC(); // 모든 배열의 값이 0이 나오도록
    cout << "bigger..." << endl; m.biggerC(); m.printC(); // 큰거 거른 후 출력
    cout << "smaller..." << endl; m.smallerC(); m.printC(); // 작은 거 거른 호 출력
    return 0;
}
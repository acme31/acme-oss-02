#include<iostream>
#include<cmath>
using namespace std;
class Line
{
private:
    int sx, sy, ex, ey;
public:
    Line(){sx=0;sy=0;ex=0;ey=0;}
    void setTwoPoints();
    double getLineLength();
};
void Line::setTwoPoints(){ 
    cout << "시작점 좌표 정수 두 개를 입력하세요."<<endl;
    cin >> sx >> sy;
    cout << "끝점 좌표 정수 두 개를 입력하세요."<<endl;
    cin >> ex >> ey;
}
double Line::getLineLength(){
    return sqrt( pow(ex - sx, 2) + pow(ey - sy, 2) );
}
int main(){
    Line myline;
    myline.setTwoPoints();
    cout << "myline의 길이는 "<<myline.getLineLength()<<" 입니다."<<endl;
}

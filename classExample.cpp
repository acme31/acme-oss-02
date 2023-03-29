#include<iostream>
using namespace std;

class ConvertSecond {
private:    
    int h, m, s;
public:
    ConvertSecond(){h=0;m=0;s=0;};
    void setData();
    int getResult(){return h*3600+m*60+s;};
}; 
void ConvertSecond::setData(){
    cout << "시(hour) 입력: ";
    cin >> h;
    cout << "분(minute) 입력: ";
    cin >> m;
    cout << "초(second) 입력: ";
    cin >> s;
}

int main() {
    ConvertSecond a;
    a.setData(); 
    cout << "입력하신 시간은 총 " << a.getResult() << " 초 입니다." << endl;
    ConvertSecond b; 
    cout << "기본 시간은 총 " << b.getResult() << " 초 입니다." << endl;
    return 0;
}
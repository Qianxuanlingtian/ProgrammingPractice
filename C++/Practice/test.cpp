#include <stdlib.h>
#include <iostream>
#include "subfile.h"
using namespace std;

int main(void)
{
    int a,b,c;
    int flag = 1;
    char operator_flag;
    char continue_flag;
    cout << "Hello" << endl;
    while(flag){
        cout << "想进行何种运算（+、-、*、/）：" << endl;
        cin >> operator_flag;
        switch(operator_flag){
            case('+'):{
                cout << "请输入被加数：" << endl;
                cin >> a;
                cout << "请输入加数：" << endl;
                cin >> b;
                c = add(a, b);
                cout << "结果为：" << c << endl;
                cout << "继续么（Y/N）：" << endl;
                cin >> continue_flag;
                if(continue_flag == 'Y'){
                    flag = 1;
                }
                else if(continue_flag == 'N'){
                    flag = 0;
                }
                else{
                    flag = 0;
                }
            };
            break;
            case('-'):{
                cout << "请输入被减数：" << endl;
                cin >> a;
                cout << "请输入减数：" << endl;
                cin >> b;
                c = sub(a, b);
                cout << "结果为：" << c << endl;
                cout << "继续么（Y/N）：" << endl;
                cin >> continue_flag;
                if(continue_flag == 'Y'){
                    flag = 1;
                }
                else if(continue_flag == 'N'){
                    flag = 0;
                }
                else{
                    flag = 0;
                }
            };
            break;
            case('*'):{
                cout << "请输入被乘数：" << endl;
                cin >> a;
                cout << "请输入乘数：" << endl;
                cin >> b;
                c = mul(a, b);
                cout << "结果为：" << c << endl;
                cout << "继续么（Y/N）：" << endl;
                cin >> continue_flag;
                if(continue_flag == 'Y'){
                    flag = 1;
                }
                else if(continue_flag == 'N'){
                    flag = 0;
                }
                else{
                    flag = 0;
                }
            };
            break;
            case('/'):{
                cout << "请输入被除数：" << endl;
                cin >> a;
                cout << "请输入除数：" << endl;
                cin >> b;
                while(!b){
                    if(b == 0){
                    cout << "除数不能为0！请重新输入：" << endl;
                    cin >> b;
                    }
                }
                c = chu(a, b);
                cout << "结果为：" << c << endl;
                cout << "继续么（Y/N）：" << endl;
                cin >> continue_flag;
                if(continue_flag == 'Y'){
                    flag = 1;
                }
                else if(continue_flag == 'N'){
                    flag = 0;
                }
                else{
                    flag = 0;
                }
            };
            break;
        }
    }
    system("pause");
}
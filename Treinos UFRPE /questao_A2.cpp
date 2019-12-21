#include <bits/stdc++.h>

using namespace std;

int main(){
    map<int, string> dic;
    dic[0] = "zero";
    dic[1] = "one";
    dic[2] = "two";
    dic[3] = "three";
    dic[4] = "four";
    dic[5] = "five";
    dic[6] = "six";
    dic[7] = "seven";
    dic[8] = "eight";
    dic[9] = "nine";
    dic[10] = "ten";
    dic[11] = "eleven";
    dic[12] = "twelve";
    dic[13] = "thirteen";
    dic[14] = "fourteen";
    dic[15] = "fifteen";
    dic[16] = "sixteen";
    dic[17] = "seventeen";
    dic[18] = "eighteen";
    dic[19]	= "nineteen";
    dic[20] = "twenty";
    dic[30] = "thirty";
    dic[40] = "forty";
    dic[50] = "fifty";
    dic[60] = "sixty";
    dic[70] = "seventy";
    dic[80] = "eighty";
    dic[90] = "ninety";

    int entrada;
    cin >> entrada;
    if (entrada < 20){
        cout << dic[entrada] << endl;

    }else{
        if((entrada % 10) != 0){
            cout << dic[(entrada/10)*10] <<'-'<< dic[entrada%10] << endl;

        }else{
            cout << dic[entrada] << endl;
        }
    }
}

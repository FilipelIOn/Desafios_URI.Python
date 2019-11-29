#include <bits/stdc++.h>

using namespace std;

int maior, x;

int main(){
    for (int i=0; i<101; i++){
    cin >> x;
    if (x > maior){
        maior = x;
    }else if (x == 0){
        break;
    }
    }
    cout << maior << endl;
    return 0;
}
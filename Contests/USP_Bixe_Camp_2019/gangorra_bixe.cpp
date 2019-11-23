#include <bits/stdc++.h>

using namespace std;

int main(){
    int p1, c1, p2, c2, l, r;
    cin >> p1 >> c1 >> p2 >> c2;
    l = p1 * c1;
    r = p2 * c2;

    if(l==r){
        cout << 0 << endl;
    } else if (l>r){
        cout << -1 << endl;
    }else{
        cout << 1 << endl;
    }
    return 0;
    
    
}
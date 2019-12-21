#include <bits/stdc++.h>

using namespace std;
int x, y, z, a, b, c;
string saida;

int main(){
    cin >> x >> y >> z >> a >> b >> c;
    saida = "NO";
    if (x <= a){
        if (x + y <= a+b){
            if (x + y + z <= a+b+c){
                saida = "YES";
            }
        }
    }
    cout << saida << endl;
}
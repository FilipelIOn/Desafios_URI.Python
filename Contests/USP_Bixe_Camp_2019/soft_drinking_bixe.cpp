#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, k, l, c, d, p, nl, np, x;
    cin >> n>> k>> l>> c>> d>> p>> nl>> np;
    int v[] = {(k*l)/nl, c*d, (p/np)};
    x = *min_element(v, v+3);

    cout << x/n << endl;
    return 0;
}
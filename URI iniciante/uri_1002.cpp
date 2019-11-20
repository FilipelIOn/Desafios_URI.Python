#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    double pi,x,area;
    pi = 3.14159;
    cin>>x;
    area = pi* (x*x);
    cout << fixed << setprecision(4);
    cout << "A=" << area << endl;
    return 0;
}

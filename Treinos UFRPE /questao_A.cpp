#include <bits/stdc++.h>

using namespace std;
int moedas, capsulas, min_day = 1, max_day = 1e8;
int const max_ciclos = 1e6;
int ciclos[max_ciclos];

int main(){
    min_day = 1;
    max_day = 1e8;
    cin >> moedas >> capsulas;
    for (int i = 0; i < moedas; i++){
        cin >> ciclos[i];
    }

//inicio da busca binaria

    while (min_day < max_day){
        int mid = (max_day+min_day)/2;
        int total = 0;

        for (int i = 0; i < moedas; i++){
            total += (mid/ciclos[i]);
        }
        if (total >= capsulas){
            max_day = mid;
        }else{
            min_day = mid + 1;
        }
        //cout << min_day << " " << max_day << endl;
    }
    cout << min_day << endl;
  
}
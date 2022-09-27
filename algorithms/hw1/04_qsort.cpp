#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>

using namespace std;

void print_vector(vector<int>& vec, string msg){

    cout << msg << endl;
    for (const auto& item: vec )
        cout << item << " ";
    cout << endl;
}


int split(vector<int>& v, int left_idx, int right_idx, int treshold){ // [left_idx, right_idx)
    int m = left_idx;
    for (int i = left_idx; i < right_idx; ++i){
        if (v[i] < treshold){
            if ( i != m){
                int buf = v[i];
                v[i] = v[m];
                v[m] = buf;
            }
            m++;
        }
    }
    return m;
}


void quicksort(vector<int>& v, int left_idx, int right_idx){
    if (right_idx - left_idx <= 1)
        return 
}


int main(){
    int n;
    long long num_inversions = 0;
    cin >> n;
    vector<int> v(n);
    
    for(auto& item: v){
        cin >> item;
    }

    split(v, 0, n, 3);
    print_vector(v, "");
    system("pause");
    return 0; 
}
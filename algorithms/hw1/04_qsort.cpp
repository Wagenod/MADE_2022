#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <ctime>
#include <tuple>

using namespace std;

void print_vector(vector<int>& vec, string msg){
    cout << endl << msg << endl;
    for (const auto& item: vec )
        cout << item << " ";
    cout << endl;
}

void swap_items(vector<int>& v, int i, int j){
    int buf = v[i];
    v[i] = v[j];
    v[j] = buf;
}


tuple<int, int> split(vector<int>& v, int left_idx, int right_idx, int treshold){ // [left_idx, right_idx)
    int m1 = left_idx, m2 = left_idx;
    for (int i = left_idx; i < right_idx; ++i){
        if (v[i] < treshold){
            if (m2 > m1){
                swap_items(v, m1, i);
                swap_items(v, m2, i);
            } else if (i != m1){
                swap_items(v, m1, i);
            }
            m1++;
            m2++;
        } else if (v[i] == treshold) {
            swap_items(v, m2, i);
            m2++;
        }  
    }
    return {m1, m2};
}


void quicksort(vector<int>& v, int left_idx, int right_idx){
    if (right_idx - left_idx <= 1)
        return;

    srand(time(NULL));
    int rand_idx = left_idx + rand() % (right_idx - left_idx);
    int treshold = v[rand_idx];
    int m1, m2;
    tie(m1, m2) = split(v, left_idx, right_idx, treshold);
    quicksort(v, left_idx, m1);  // [left_idx; m1)
    quicksort(v, m2, right_idx); // [m2; right_idx)
}


int main(){
    int n;
    cin >> n;
    vector<int> v(n);
    
    for(auto& item: v){
        cin >> item;
    }

    quicksort(v, 0, n);
    print_vector(v, "");
    system("pause");
    return 0; 
}
#include <iostream>
#include <vector>
#include <tuple>
#include <ctime> // for rand
#include <utility> // for tie
#include <algorithm> // for copy
#include <iterator> // for back_inserter


using namespace std;

void print_vector(vector<int>& vec){
    cout << endl;
    for (const auto& item: vec )
        cout << item << " ";
    cout << endl;
}


tuple<int, int> split(vector<int>& v, int left_idx, int right_idx, int treshold){ // [left_idx, right_idx)
    int m1 = left_idx, m2 = left_idx;
    for (int i = left_idx; i < right_idx; ++i){
        if (v[i] < treshold){
            swap(v[m1], v[i]);
            if (m2 != m1){
                swap(v[m2], v[i]);
            } 
            m1++;
            m2++;
        } else if (v[i] == treshold) {
            swap(v[m2], v[i]);
            m2++;
        }  
    }
    return {m1, m2}; // [m1, m2)
}


int find_k_order_stat(vector<int>& a, int l_idx, int r_idx, int k){ // [l,r)
    if (r_idx - l_idx <= 1)
        return a[l_idx];

    srand(time(NULL));
    int random_idx = l_idx + rand() % (r_idx - l_idx);

    int m1, m2;
    tie(m1, m2) = split(a, l_idx, r_idx, a[random_idx]);
    
    if (k < m1){
        return find_k_order_stat(a, l_idx, m1, k);
    } else if (k >= m2){
        return find_k_order_stat(a, m2, r_idx, k);
    }

    return a[k];
}

int main(){
    int n, m;

    cin >> n;
    vector<int> a(n);
    vector<int> working_arr;
    for (int& i: a){
        cin >> i;
    }

    copy(a.begin(), a.end(), back_inserter(working_arr));

    cin >> m;
    for (int num = 0; num < m; num++){
        int i, j, k;
        cin >> i >> j >> k;
        cout << find_k_order_stat(working_arr, i - 1, j, k - 1 + i - 1) << endl;
        copy(a.begin() + i - 1, a.begin() + j, working_arr.begin() + i - 1);
    } 

    system("pause");
    return 0;
}
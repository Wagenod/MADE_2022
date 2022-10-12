#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int ALPHABET_CAPACITY = 26;

template<typename T>
void print_vector(const vector<T>& vec){
    cout << endl;
    for (const T& item: vec )
        cout << item << " ";
    cout << endl;
}

vector<int> radix_sort(const vector<string>& vstr, int k, int m, int n){
    vector<int> P(n); // вектор перестановок для исходных строк
    for (size_t j = 0; j < n; j++){
        P[j] = j;
    }

    for (int i = 1; i <= k; i++){
        vector<int> cnt(ALPHABET_CAPACITY);
        for (size_t l = 0; l < n; l++){
            
            cnt[int(vstr[P[l]][m - i] - 'a')]++;
        }

        vector<int> shifts(ALPHABET_CAPACITY);
        for (size_t j = 1; j < shifts.size(); j ++){
            shifts[j] = shifts[j - 1] + cnt[j - 1];
        }

        vector<int> P_old(P.begin(), P.end());
        for (size_t l = 0; l < n; l++){
            int cnt_idx = int(vstr[P_old[l]][m - i]) - 'a';
            P[shifts[cnt_idx]++] = P_old[l];
        }
    }
    return P;
}



int main(){
    int n, m, k;
    cin >> n >> m >> k;
    cin.ignore(1);
    vector<string> strs(n);

    for (string& item: strs){
        getline(cin, item);
    }

    vector<int> P = radix_sort(strs, k, m, n);

    for(const int& p: P){
        cout << strs[p] << endl;
    }
    
    system("pause");
    return 0;
}
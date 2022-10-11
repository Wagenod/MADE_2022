#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int ALPHABET_CARD = 26;
const int ASCII_BEGIN_CODE = 97;
const int ASCII_END_CODE = 122;

template<typename T>
void print_vector(const vector<T>& vec){
    cout << endl;
    for (const T& item: vec )
        cout << item << " ";
    cout << endl;
}

void radix_sort(const vector<string>& vstr, int k){
    for (int i = 1; i <= k; i++){
        vector<int> cnt(ALPHABET_CARD);
        for (const string& str: vstr){
            cnt[int(str[str.size() - i]) - ASCII_BEGIN_CODE]++;
        }
        print_vector(cnt);
    }
    
}



int main(){
    int n, m, k;
    cin >> n >> m >> k;
    cin.ignore(1);
    vector<string> strs(n);

    for (string& item: strs){
        getline(cin, item);
    }

    radix_sort(strs, k);
    // for (int l = 0; l < m; l++){

    // }


    return 0;
}
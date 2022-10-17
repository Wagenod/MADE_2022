#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int ALPHABET_CAPACITY = 26;

template<typename T>
void print(const vector<T>& vec){
    cout << endl;
    for (const T& item: vec )
        cout << item << " ";
    cout << endl;
}


int main(){
    int n, m;
    cin >> n >> m;

    string s, t;
    cin >> s >> t;

    vector<int> cnt(ALPHABET_CAPACITY);
    for (const char& ch: t){
        cnt[int(ch - 'a')]++;
    }

    int substr_count = 0;
    vector<int> tmp_cnt(ALPHABET_CAPACITY);
    int dk = 0;
    bool flag = false;
    for (int i = 0;i < n; i++){
        for (int k = i + dk; k < n; k++){
            int chr_idx = int(s[k] - 'a');
            tmp_cnt[chr_idx]++;

            // cout << "-----------------------------";
            // print(tmp_cnt);
            // print(cnt);
            // cout << "-----------------------------";

            if (tmp_cnt[chr_idx] > cnt[chr_idx]){

                tmp_cnt[int(s[i] - 'a')]--; // i
                tmp_cnt[chr_idx]--; // k

                // cout << "-----------------------------";
                // print(tmp_cnt);
                // print(cnt);
                // cout << "-----------------------------";

                substr_count += k - i - 1;
                dk = k - i - 1; 
                break;
            } 

            if (k == n - 1){
                flag = true;
                substr_count += (n - i - 1)*(n - i)/2;
            }
            substr_count++;
        }

        if (flag){
            break;
        }
    }
    cout << substr_count;
    system("pause");
    return 0;
}
#include <iostream>
#include <vector>

using namespace std;

void print_vector(vector<int>& vec){
    cout << endl;
    for (const auto& item: vec )
        cout << item << " ";
    cout << endl;
}



const int M = 101;

void counting_sort(vector<int>& v){
    vector<int> cnt(M);

    for (int& item: v){
        cnt[item]++;
    }

    int i = 0;
    for(int j = 0; j < M; j++){
        while (cnt[j] > 0){
            v[i++] = j;
            cnt[j]--;
        }
    }
}

int main(){
    vector<int> v;

    int tmp;
    while (cin.peek() != '\n' && cin >> tmp)
    {   
        v.push_back(tmp);
    }
    
    counting_sort(v);

    print_vector(v);

    return 0;
}
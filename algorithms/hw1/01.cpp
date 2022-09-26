#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> v(n);
    
    for(auto& item: v){
        cin >> item;
    }

    for (int i = 0; i < v.size() - 1; i++){
        for (int j = i + 1; j < v.size(); j++){
            if (v[j] < v[i]){
                int tmp = v[i];
                v[i] = v[j];
                v[j] = tmp;
            }
        }
    }

    //cout << "sorted array:" << endl;
    for (const auto& item: v )
        cout << item << " ";
    return 0;
}
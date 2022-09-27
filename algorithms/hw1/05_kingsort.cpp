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


int main(){
    int n;
    long long num_inversions = 0;
    cin >> n;
    vector<int> v(n);
    
    for(auto& item: v){
        cin >> item;
    }


    print_vector(v, "");
    system("pause");
    return 0; 
}
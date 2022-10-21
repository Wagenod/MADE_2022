#include <iostream>
#include <vector>

using namespace std;


int main(){

    vector<int> P = {1 ,2, 3};
    vector<int> Q(P.begin(), P.end());
    P[0] = 0;
    cout << Q[0];
    system("pause");
    return 0;
}
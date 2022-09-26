#include <iostream>
#include <vector>
#include <string>

using namespace std;

void print_vector(vector<int>& vec, string msg){
    cout << msg << endl;
    for (const auto& item: vec )
        cout << item << " ";
    cout << endl;
}

vector<int> merge(vector<int>& vec1, vector<int>& vec2, long long& n_inversions){
    cout << n_inversions << endl;

    int merged_size = vec1.size() + vec2.size();
    vector<int> merged_vect(merged_size);
    int i = 0, j = 0;

    while (i + j < merged_size) {
        if ((j == vec2.size()) || (i < vec1.size() && vec1[i] <= vec2[j])) {
            merged_vect[i + j] = vec1[i];
            i++;
        } else {
            merged_vect[i + j] = vec2[j];
            n_inversions += vec1.size() - i;
            j++;
        }
    }
    return merged_vect;
}

vector<int> merge_sort(vector<int>& numbers, long long& n_inversions){

    if (numbers.size() == 1)
        return numbers;

    cout << n_inversions << endl;
    vector<int> left_part(numbers.begin(), numbers.begin() + numbers.size()/2);
    vector<int> right_part(numbers.begin() + numbers.size()/2, numbers.end());

    left_part = merge_sort(left_part, n_inversions);
    right_part = merge_sort(right_part, n_inversions);

    return merge(left_part, right_part, n_inversions);
}



int main(){
    int n;
    long long num_inversions = 0;
    cin >> n;
    vector<int> v(n);
    
    for(auto& item: v){
        cin >> item;
    }

    vector<int> sorted_vec = merge_sort(v, num_inversions);
    cout << num_inversions << endl;
    system("pause");
    return 0; 
}
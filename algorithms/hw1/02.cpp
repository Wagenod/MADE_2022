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

vector<int> merge(vector<int>& vec1, vector<int>& vec2){
    int merged_size = vec1.size() + vec2.size();
    vector<int> merged_vect(merged_size);
    int i = 0, j = 0;

    while (i + j < merged_size)
    {
        if ((i == vec1.size()) || (j < vec2.size() && vec2[j] < vec1[i])){
            merged_vect[i + j] = vec2[j];
            j++;
        } else {
            merged_vect[i + j] = vec1[i];
            i++;
        }
    }
    return merged_vect;
}

vector<int> merge_sort(vector<int>& numbers){

    if (numbers.size() == 1)
        return numbers;

    vector<int> left_part(numbers.begin(), numbers.begin() + numbers.size()/2);
    vector<int> right_part(numbers.begin() + numbers.size()/2, numbers.end());

    left_part = merge_sort(left_part);
    right_part = merge_sort(right_part);

    return merge(left_part, right_part);
}



int main(){
    int n;
    cin >> n;
    vector<int> v(n);
    
    for(auto& item: v){
        cin >> item;
    }

    vector<int> sorted_vec = merge_sort(v);

    for (const auto& item: sorted_vec)
        cout << item << " ";

    // print_vector(sorted_vec, "sorted array:");
    //system("pause");
    return 0; 
}
#include <iostream>
#include <string>
#include <map>
#include <sstream>
#include <algorithm> // sort
#include <vector>
#include <cstring>

using namespace std;

const map<char, int> ROMA_TO_ARABIC = {{'I', 1},{'V', 5}, {'X', 10}, {'L', 50}};

struct RomaKing{
    string king_name;
    string number;
};

void print_vector(const vector<RomaKing>& v){
    for (const RomaKing& king: v){
        cout << king.king_name << " " << king.number << endl;
    }
}

int parse_roma(const string& roma_num){
    int arabic_num = 0, last_arabic_digit = -1;

    for (const char& roma_digit: roma_num){
        int current_arabic_digit = ROMA_TO_ARABIC[roma_digit];
        if (last_arabic_digit < 0){
            last_arabic_digit = current_arabic_digit;
        } else {
            if (last_arabic_digit < current_arabic_digit){
                last_arabic_digit *= -1; 
            }
            arabic_num += last_arabic_digit;
            last_arabic_digit = current_arabic_digit;
        }
    }
    return arabic_num + last_arabic_digit;
}


bool operator< (const RomaKing& left_king, const RomaKing& right_king){
    if (left_king.king_name == right_king.king_name){
        return parse_roma(left_king.number) < parse_roma(right_king.number);
    }
    return left_king.king_name < right_king.king_name;
}



int main(){
    int n;
    cin >> n;
    cin.ignore();

    vector<RomaKing> kings(n);
    for (int i = 0; i < n; i++){
        string king_name, king_num;
        getline(cin, king_name, ' ');
        getline(cin, king_num);
        kings[i] = {king_name, king_num};
    }

    sort(kings.begin(), kings.end());
    print_vector(kings);

    system("pause");
    return 0; 
}
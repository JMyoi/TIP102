#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
using namespace std;

int max_number_of_string_pairs(vector<string> signals){
    unordered_map<string, int> pairs;
    int totalPairs = 0;
    for(int i = 0; i < signals.size(); ++i){
        string reversed(signals.at(i).rbegin(), signals.at(i).rend());
        cout<<"reversed at: "<< i<<": "<<reversed<<endl;
        if(pairs.count(reversed) == 1){// if found then incriment the frequency and total pairs
            if(pairs[reversed] == 2){// if pair was already accounted for then reset it to 1
                pairs[reversed] = 1;
            }
            else{
                pairs[reversed]++;
                totalPairs++;
            }
        }
        else{// no pair found, just insert
            pairs[signals.at(i)] = 1;
        }
    }
    return totalPairs;
}

vector<vector<int>> find_difference(vector<int> signals1, vector<int> signals2){
    //construct 2 sets
    unordered_set<int> S1;
    for(int n: signals1)
        S1.insert(n);
    unordered_set<int> S2;
    for(int n: signals2)
        S2.insert(n);

    //difference of signals1 - signals2
    vector<int> diff1;
    for(int n: S1)
        if(!S2.count(n)) diff1.push_back(n); // if n is not in set 2 then insert
    vector<int> diff2;
    for(int n: S2)
        if(!S1.count(n)) diff2.push_back(n);

    vector<vector<int>> ans;
    ans.push_back(diff1);
    ans.push_back(diff2);
    return ans;
}


int main(){
    // Q7 Signal pairs
    // vector<string> signals1 = {"cd", "ac", "dc", "ca", "zz"};
    // int ans = max_number_of_string_pairs(signals1);
    // cout<<"Answer: "<<ans<<endl;

    /*
    Q8
    vector<int> S1 = {1,2,3};
    vector<int> S2 = {2,4,6};
    vector<vector<int>> ans = find_difference(S1, S2);
    for(int i = 0; i < ans.size(); ++i){
        cout<<"[";
        for(int j = 0; j < ans.at(i).size(); ++j){
            cout<<ans.at(i).at(j);
            if(j != ans.at(i).size()-1)
                cout<<",";
            else
                continue;
        }
        cout<<"]";
    }
    */

    return 0;
}


/*
pairs[i] // access value, but will insert 0 if not there?
pairs.at(k) // safe? returns iteratior or .end() if not found?
pairs.count(k)// 1 or 0

*/
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
using namespace std;

int max_number_of_string_pairs(vector<string> signals);

vector<vector<int>> find_difference(vector<int> signals1, vector<int> signals2);

int* find_common_signals(vector<int> signals1, vector<int> signals2);

int* find_common_signals_usingSet(vector<int> signals1, vector<int> signals2);

vector<int> frequency_sort(vector<int> signals);

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
   /*
   Q9 and 10
   vector<int> signals1 = {4,3,2,4,1};
   vector<int> signals2 = {2,2,5,2,3,6};
   int* arr = find_common_signals_usingSet(signals1, signals2);
   cout<< arr[0]<<", "<<arr[1]<<endl;
   delete[] arr;
   */
  /*
    Q11
  */




    return 0;
}


/*
pairs[i] // access value, but will insert 0 if not there?
pairs.at(k) // safe? returns iteratior or .end() if not found?
pairs.count(k)// 1 or 0

*/

vector<int> frequency_sort(vector<int> signals){
    unordered_map<int, int> freq;
    for(int s: signals){
        if(freq.count(s))
            freq[s]++;
        else
            freq[s] = 1;
    }

    //return a sorted array based on frequency in increasing order of frequency, if frequency are same, sort in decreasing order by key
    vector<int> sorted(signals.size());
    
    for(auto it = freq.begin(); it != freq.end(); it++){
        it->first;
        it->second;
        //implement via insertion sort 
    }

}


int* find_common_signals(vector<int> signals1, vector<int> signals2){
    int answer1 = 0;
    int answer2 = 0;
    for(int n1: signals1){
        for(int n2: signals2){
            if (n1 == n2){
                answer1++;
                break;
            }
        }
    }
    for(int i = 0; i < signals2.size(); ++i){
        for(int j = 0; j < signals1.size(); ++j){
            if(signals2.at(i) == signals1.at(j)){
                answer2++;
                break;
            }
        }
    }
    int* ans = new int[]{answer1, answer2};
    return ans;

}

int* find_common_signals_usingSet(vector<int> signals1, vector<int> signals2){
    unordered_set<int> Seen1;
    unordered_set<int> Seen2;
    int answer1 = 0;
    int answer2 = 0;

    for(int n2: signals2){
        Seen2.insert(n2);
    }
    for(int n1: signals1){
        if(Seen2.count(n1)){
            answer1++;
        }
    }

    for(int n1: signals1){
        Seen1.insert(n1);
    }
    for(int n2: signals2){
        if(Seen1.count(n2)){
            answer2++;
        }
    }

    int* ans = new int[]{answer1, answer2};
    return ans;


}

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
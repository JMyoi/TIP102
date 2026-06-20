#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <string>
using namespace std;

int count_endangered_species(string endangered_species, string observed_species);

int main(){
    /*
    Problem 2
    string endangered_species1 = "aA";
    string observed_species1 = "aAAbbbb";
    cout<< count_endangered_species(endangered_species1, observed_species1)<<endl;
    */

    

    return 0;
}


int count_endangered_species(string endangered_species, string observed_species){
    int totalEndangered = 0;
    unordered_map<char, int> endangeredFreq;
    for(char c: endangered_species){
        endangeredFreq[c] = 0;
    }
    for(int i = 0; i < observed_species.size(); ++i){
        if(endangeredFreq.count(observed_species.at(i))){
            endangeredFreq[observed_species.at(i)]++;
            totalEndangered++;
        }
    }
    cout<<" Endangered Freq = "<<endl;
    for(auto it = endangeredFreq.begin(); it != endangeredFreq.end(); it++){
        cout<<(*it).first<<": "<<it->second<<endl;
    }
    return totalEndangered;

}
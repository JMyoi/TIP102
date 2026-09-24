#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <unordered_set>
#include <string>
using namespace std;

int count_endangered_species(string endangered_species, string observed_species);
vector<string> prioritize_observations(vector<string> observed_species, vector<string> priority_species);
/*
make a priorityFreq of all priority animals and set to zero

priorityFreq = {
    cardinal: 0,
    "sparrow": 0,
    ...
}
    iterate through every animal in observed Species and if it is in Priority freq then incirment, 
    if not then add it to a non priority list 

    at the end, make a vector of priority freq with all animals there
    then in the non priority list sort by ascending alphabetic order, 
    combine the two vectors and return it
*/
int main(){
    /*
    Problem 2
    string endangered_species1 = "aA";
    string observed_species1 = "aAAbbbb";
    cout<< count_endangered_species(endangered_species1, observed_species1)<<endl;
    */

    vector<string> observed_species2 = {"bluejay", "sparrow", "cardinal", "robin", "crow"};
    vector<string> priority_species2 = {"cardinal", "sparrow", "bluejay"};

    vector<string> result = prioritize_observations(observed_species2, priority_species2);
    for(string species: result){
        cout<<species<<" ";
    }


    return 0;
}

vector<string> prioritize_observations(vector<string> observed_species, vector<string> priority_species){

    unordered_map<string, int> priorityFreq;
    for(string species: priority_species){ // for P elements, one O(1) avg hash insert each → O(P)

        priorityFreq[species] = 0;
    }
    vector<string> nonPriority;
    for(string species: observed_species){ // iterate N elements, one O(1) avg hash lookup each → O(N)

        if(priorityFreq.count(species)){
            priorityFreq[species]++;
        }
        else{
            nonPriority.push_back(species);
        }
    }
    vector<string> observedPrioritySpecies;
    /*
        outer loop: P iterations
        inner loop: runs priorityFreq[species] times per species
        total inner iterations across all species ≤ N (can't exceed observed count)
        → O(N) total
    */
    for(string species: priority_species){ 
        for(int i = 0; i < priorityFreq[species]; ++i){
            observedPrioritySpecies.push_back(species);
        }
    }
    //nonPriority has at most N-P elements → O((N-P) log(N-P))
    sort(nonPriority.begin(), nonPriority.end());

    // copies N-P elements → O(N-P)
    observedPrioritySpecies.insert(observedPrioritySpecies.end(), nonPriority.begin(), nonPriority.end());
    return observedPrioritySpecies;
    /*
    O(P) + O(N) + O(N) + O((N-P)log(N-P)) + O(N-P)
    = O(N + (N-P)log(N-P))

    In the worst case where P is small (few or no priority species), this simplifies to O(N log N), dominated by the sort. If P ≈ N (almost everything is priority), the sort shrinks toward O(1) and it approaches O(N).

Space: O(N) — for nonPriority, observedPrioritySpecies, and the map.

    */
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
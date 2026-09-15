#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> leftRightDifference(vector<int> nums){
    /*
    for each index, calculate left sum and right sum, subtract them and push them to return vector*/
    vector<int> Difference;
    for(int i = 0; i < nums.size(); i++){
        int rightSum = 0; 
        int leftSum = 0;
        //calculate left diff
        for(int l = i-1; l>=0; l--){
            leftSum +=nums.at(l);
        }
        for(int r = i+1; r< nums.size(); r++){
            rightSum += nums.at(r);
        }
        cout<<"for iteration: "<<i<<" Left sum - Right Sum: "<<leftSum<<" - "<<rightSum<<"="<<leftSum-rightSum<<endl;
        Difference.push_back(leftSum - rightSum);
    }
    return Difference;
}

vector<string> common_elements(vector<string> lst1, vector<string> lst2){
    vector<string> Output;
    for(int i = 0; i < lst1.size(); ++i){
        for(int j = 0; j < lst2.size(); ++j){
            if(lst1.at(i) == lst2.at(j)){
                Output.push_back(lst1.at(i));
            }
        }
    }
    return Output;
}




int main(){
    /*
    Left and Right Sum Difference, Problem 8
    vector<int> nums = {10,4,8,3};
    vector<int> ans = leftRightDifference(nums);
    for(int n: ans){
        cout<<n<<" ";
    }
    */

    /*
    common cause
    vector<string> lst1 = {"super strength", "super speed", "x-ray vision"};
    vector<string> lst2 = {"martial arts", "stealth", "master detective"};

    vector<string> out = common_elements(lst1, lst2);

    for(string s: out){
        cout<<s<<" ";
    }
    */

    



    return 0;
}
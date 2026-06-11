#include <iostream>
#include <vector>
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


int main(){
    vector<int> nums = {10,4,8,3};
    vector<int> ans = leftRightDifference(nums);
    for(int n: ans){
        cout<<n<<" ";
    }
    return 0;
}
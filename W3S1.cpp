#include <iostream>
#include <stack>
#include <queue>
#include <vector>
using namespace std;

int time_required_to_stream(vector<int> movies, int k);
struct movie{
    int index;
    int streams;
};

int main(){

    cout << time_required_to_stream({5, 1, 1, 1}, 0) << endl;


    return 0;
}

int time_required_to_stream(vector<int> movies, int k){
    queue<movie> movieQueue;
    for(int i = 0; i < movies.size(); ++i){
        movieQueue.push(movie{i, movies.at(i)});
    }

    int totalTime = 0; 

    while(!movieQueue.empty()){
        movie currMovie = movieQueue.front();
        movieQueue.pop();
        currMovie.streams--;
        totalTime++;
        if(currMovie.streams != 0){
            movieQueue.push(currMovie);
        }
        else if (currMovie.index == k && currMovie.streams == 0){
            return totalTime;
        }
    }
    return -1;
}

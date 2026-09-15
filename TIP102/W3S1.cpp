#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;

int time_required_to_stream(vector<int> movies, int k);

struct movie{
    int index;
    int streams;
};

vector<string> reverse_watchlist(vector<string> watchlist);
string remove_duplicate_shows(string schedule);
float minimum_average_view_count(vector<int> view_counts);

int main(){

    // cout << time_required_to_stream({5, 1, 1, 1}, 0) << endl;

    /*
    Q.2
    vector<string> watchlist = {"Breaking Bad", "Stranger Things", "The Crown", "The Witcher"};
    watchlist = reverse_watchlist(watchlist);
    for(string watch: watchlist){
         cout<<watch<<", ";
    }
    */

   //cout<< remove_duplicate_shows("abbaca") << endl;
    cout << minimum_average_view_count({7, 8, 3, 4, 15, 13, 4, 1});


    return 0;
}

float minimum_average_view_count(vector<int> view_counts){
    sort(view_counts.begin(), view_counts.end());
    int left = 0; 
    int right = view_counts.size()-1;
    vector<float> average;
    while( left < right ){
        float avg = (view_counts.at(left) + view_counts.at(right)) / 2.0;
        average.push_back(avg);
        left++;
        right--;
    }
    auto it = min_element(average.begin(), average.end());
    return *it;
}


string remove_duplicate_shows(string schedule){
    stack<char> S;
    for(char show: schedule){
        if(S.empty()){
            S.push(show);
        }
        else if(S.top() == show){
            S.pop();
        }
        else 
            S.push(show);
    }
    string result;
    while(!S.empty()){
        result+=S.top();
        S.pop();
    }
    reverse(result.begin(), result.end());
    return result;
}

vector<string> reverse_watchlist(vector<string> watchlist){
    int left = 0; 
    int right = watchlist.size() - 1;
    while(left < right){
        string temp = watchlist.at(left);
        watchlist.at(left) = watchlist.at(right);
        watchlist.at(right) = temp;
        left++;
        right--;
    }
    return watchlist;
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


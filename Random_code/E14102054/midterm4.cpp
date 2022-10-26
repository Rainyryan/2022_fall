#include<iostream>

using namespace std; 

int main(){
    int arr[10] = {3, 5, 6, 2, 4, 8, 9, 10, 0, 90};

    int max_ = INT32_MIN, min_ = INT32_MAX, idxM = 0, idxm = 0;

    for(int i = 0; i < 10; ++i){
        if(arr[i] > max_){
            max_ = arr[i];
            idxM = i;
        }
        if(arr[i] < min_){
            min_ = arr[i];
            idxm = i;
        }
    }  
    cout<<"max: "<<max_<<" with index "<<idxM<<"\nmin: "<<min_<<" with index "<<idxm<<'\n';
}
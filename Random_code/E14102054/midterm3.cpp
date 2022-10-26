#include<iostream>
#include<stdlib.h>
#include<time.h>

using namespace std; 

int main(){
    double arr[10][8] = {0};
    srand(time(NULL));

    for(int i = 0; i < 10; ++i){
        for(int j = 0; j < 8; ++j){
            arr[i][j] = ((double)rand() * 21.00/ RAND_MAX - 10.5);
        }
    }
    
    for(int i = 0; i < 10; ++i){
        for(int j = 0; j < 8; ++j){
            printf("%20.10f ",arr[i][j]);
        }
        cout<<'\n';
    }

}
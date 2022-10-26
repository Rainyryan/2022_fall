#include <iostream> 

using namespace std;

//using tree structure that has parent (i-1)/2 and child 2*i+1 and 2*i+2

void heapify(int* A, int i, int n){
    if(2*i+1 > n) return;
    else if(A[2*i+1] > A[2*i+2] && A[2*i+1] > A[i]){
        swap(A[2*i+1], A[i]);
        heapify(A, 2*i+1, n);
    }else if(2*i+2 > n) return;
    else if(A[2*i+2] > A[2*i+1] && A[2*i+2] > A[i]){
        swap(A[2*i+2], A[i]);
        heapify(A, 2*i+2, n);
    }
}

void buildheap(int *A, int n){
    for(int i = (n-1)/2; i >= 0; --i){
        heapify(A, i, n);
    }
} 
void heapsort(int *A, int n){
    buildheap(A, n);
    for(int i = n; i > 0; --i){
        swap(A[0], A[i]);
        heapify(A, 0, i);
    }
}

int main(){
    int A[10] = {8, 3, 4, 5, 6, 10, 34, 3, 7, 1};
    for(int i = 0; i < 10; ++i) cout<<A[i]<<' ';
    cout<<'\n';
    heapsort(A, 9);
    for(int i = 0; i < 10; ++i) cout<<A[i]<<' ';
    return 0;
}


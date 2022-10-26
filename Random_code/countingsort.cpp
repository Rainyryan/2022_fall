#include <iostream>

using namespace std;

//A kind of cool sorting algorithm that uses the concept of linear hashin
int* countingsort(int A[], int size, int Max){
    int* C = new int[Max], *B = new int[size];
    for(int i = 0; i < size; ++i) ++C[A[i]];
    for(int i = 1; i < Max; ++i) C[i] += C[i-1];
    for(int i = 0; i < size; ++i){
        B[C[A[i]-1]] = A[i];
        --C[A[i]];
    }
    return B;
}
int main(){
    int A[10] = {8, 3, 4, 5, 6, 10, 34, 3, 7, 1}; 
    for(int i = 0; i < 10; ++i) cout<<A[i]<<' ';
    cout<<'\n';
    int *B = countingsort(A, 10, 34); 
    for(int i = 0; i < 10; ++i) cout<<B[i]<<' ';
    return 0;
}


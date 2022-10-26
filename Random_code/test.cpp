#include<iostream>

using namespace std;

int main(){
    double beans[10] = {};
    char words[][50] = {"Pars repair", "using a", "posterior", "approach", "was", "performed", "the patient", "on a", "Jackson", "spine table"};
    string str[2] = {};//= {"London", "Birmingham", " Edinburgh", " Durum"};

    cout<<sizeof(beans[5])<<'\n';
    cout<<sizeof(words[5])<<'\n';
    cout<<sizeof(str[5])<<'\n';

    float temperatures[5] = {30.7, 32.2, 35.2, 36.5, 44.0}; 

    int max = 10; cin >> max;
    int* values = new int[max];
    //delete[] values;
}
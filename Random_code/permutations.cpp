#include <iostream>
#include <string>

using namespace std;

void perm(string s, int a, int b){
    if(a == b) cout<<s.substr(0,b)<<'\n';
    for(int i = a; i < b; ++i){
        swap(s[a], s[i]);
        perm(s, a+1, b);
        swap(s[a], s[i]);
    }
}
// ABC
// ACB
// BAC
// BCA
// CBA
// CAB

int main(){
    string s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int n;
    cin>>n;
    perm(s,0,n);
}
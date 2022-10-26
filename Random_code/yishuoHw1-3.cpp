#include<iostream>

using namespace std;

class queue{
    int *arr, front, back, size, capacity;
    
public:
    queue(int size = 5);
    ~queue();
    void push(int);
    int top();
    int pop();
    bool empty();
};
queue::queue(int size){
    arr = new int[size];
    capacity = size;
    front = 0;
    back = -1;
    this->size = 0;
}
queue::~queue(){
    delete[] arr;
}
bool queue::empty(){
    return size == 0;
}
void queue::push(int item){
    ++back %= capacity;
    arr[back] = item;
    ++size;
}
int queue::pop(){
    int ret = arr[front];
    ++front %= capacity;
    --size;
    return ret;
}
int queue::top(){
    return arr[front];
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    queue Q;
    int time = 0;

    int T[5], C[5], prevPlayer = -1, next, front;
    cout<<"enter arrival times\n";
    for(int i = 0; i < 5; ++i) cin>>T[i];
    cout<<"enter coin amounts\n";
    for(int i = 0; i < 5; ++i) cin>>C[i];
    for(;;++time){
        for(int i = 0; i < 5; ++i) if(T[i] == time) Q.push(i);
        if(!Q.empty()){
            front = Q.top();
            if(--C[front]){
                if(prevPlayer == Q.top()) Q.push(Q.pop());
            }else{
                Q.pop();
            }
            prevPlayer = front;
        }
        
    }


}
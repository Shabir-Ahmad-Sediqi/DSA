
#include <bits/stdc++.h>

using namespace std;

int main(){
    // Deque Data Structure

    deque<int> d;
    d.push_back(5);
    d.push_back(2);
    d.pop_back();
    d.push_front(8);
    d.pop_front();

    // its a little bit slower than vector because its internal implementation is
    // mush more complex than vector 
}
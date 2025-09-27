#include <bits/stdc++.h>

using namespace std;

void multilsetDS(){
    // this is another kind of set that accepts repetated value

    multilset<int> s;

    s.insert(5);
    s.insert(5); // Totally valid but if you try to remove an element all instances
    s.insert(5); // of that element will be removed except this method
                 // s.erase(s.find(anyElement)) 
}

int main(){
    // its set data structure

    set<int> numbers = {1,2,3,5};
    cout<<numbers.size()<<"\n";

    numbers.insert(6);
    numbers.count(2);
    numbers.erase(6);

    for (auto i : numbers){
        cout << i;
    }

}
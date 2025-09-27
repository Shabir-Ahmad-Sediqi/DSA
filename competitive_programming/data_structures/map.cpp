#include <bits/stdc++.h>

using namespace std;

int main(){
    map<string, int> m;

    m["Ali"] = 3;
    m["Shabir"] =6;
    m["Ahmad"] = 5;

    cout<< m["Shabir"]<<"\n";

    // check if a key is exist

    cout<<m["Ali"];

    // prints all the key and the value

    for (auto x : m){
        cout<<x.first << " " << x.second << "\n";
    }
}
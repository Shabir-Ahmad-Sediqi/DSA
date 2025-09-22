
 #include <bits/stdc++.h>
 using namespace std;

 int main(){
    int sum = 0;
    int best = 0;

    vector<int> arr = {-1,2,4,-3,5,2,-5,2};

    for (int i : arr){
        sum = max(i, sum + i);
        best = max(best, sum);
    }

    cout<<best<<"\n";
 }



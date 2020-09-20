# DDD

#include <bits/stdc++.h>

using namespace std;
const int max_inf = 0x3f3f3f3f;
int fa[50005];

int main() {
    ios::sync_with_stdio(false);
    int n,q;
    cin >> n >> q;
    for(int i=2;i<n;++i){
        cin >> fa[i];
    }
    int a,b;
    fa[1] = 0;
    while(--q){
        cin >> a >> b;
        while(a && --b){
            a = fa[a];
        }
        cout <<a <<endl;
    }
    
    return 0;
}

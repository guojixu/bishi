#include <bits/stdc++.h>
using namespace std;
#include <iostream>
typedef pair<int, int> pa;

int dp[220][5050];
pa a[202];
int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    cin>>n>>m;
    int res = 0;


    int t = m;
    for (int i = 1; i <= n; i++) {
        scanf("%d%d", &a[i].first, &a[i].second);
        cin>>a[i].first>>a[i].second;
        if (a[i].first < 0) {
            t -= a[i].first;
        }
    }
    sort(a + 1, a + 1 + n, greater<pa>());
    for (int i = 1; i <= n; ++i) {
        if (a[i].first > 0) {
            for (int j = a[i].first; j <= t; ++j) {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i].first] + a[i].second);
            }
        }
        else {
            for (int j = 0; j <= t + a[i].first; j++) {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i].first] + a[i].second);
            }
        }
    }
    for (int i = 0; i <= m; ++i) {
        res = max(res, dp[n][i]);
    }
//    printf("%d\n", res);
    cout<<ans<<endl;
    return 0;
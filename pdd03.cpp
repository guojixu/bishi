#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pii;

int dp[202][5005];
pii a[202];
int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    int nm = m;
    for (int i = 1; i <= n; ++i) {
        scanf("%d%d", &a[i].first, &a[i].second);
        if (a[i].first < 0) {
            nm -= a[i].first;
        }
    }
    sort(a + 1, a + 1 + n, greater<pii>());
    for (int i = 1; i <= n; ++i) {
        if (a[i].first > 0) {
            for (int j = a[i].first; j <= nm; ++j) {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i].first] + a[i].second);
            }
        }
        else {
            for (int j = 0; j <= nm + a[i].first; ++j) {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i].first] + a[i].second);
            }
        }
    }
    int ans = 0;
    for (int i = 0; i <= m; ++i) {
        ans = max(ans, dp[n][i]);
    }
    printf("%d\n", ans);
    return 0;
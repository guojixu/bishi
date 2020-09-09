#include <iostream>
#include <unordered_set>
using namespace std;

const int N = 1e5 + 10, M = 1e6 + 10;

int n, m;
char p1[N], p2[N], s1[M], s2[M];
int ne1[N], ne2[N];

int main() {
    cin >> n;
    for (int i = 1; i <= n; i ++) cin >> p1[i];
    for (int i = 1; i <= n; i ++) cin >> p2[i];

    cin >> m;
    for (int i = 1; i <= m; i ++) cin >> s1[i];
    for (int i = 1; i <= m; i ++) cin >> s2[i];

    // 求ne数组, ne[1] = 0 此时求的过程也是一个完美的递归过程
    for (int i = 2, j = 0; i <= n; i ++) {
        while (j && p1[i] != p1[j + 1])  j = ne1[j];
        if (p1[i] == p1[j + 1]) j ++;
        ne1[i] = j;
    }

    for (int i = 2, j = 0; i <= n; i ++) {
        while (j && p2[i] != p2[j + 1])  j = ne2[j];
        if (p2[i] == p2[j + 1]) j ++;
        ne2[i] = j;
    }

    unordered_set<int> res;
    int start = 0;
    for (int i = 1, j = 0; i <= m; i ++) {
        while (j && s1[i] != p1[j + 1]) j = ne1[j];
        if (s1[i] == p1[j + 1]) j ++;
        if (j == n) {
            // 匹配成功
            res.insert(i - n);
            j = ne1[j];
        }
    }

    for (int i = 1, j = 0; i <= m; i ++) {
        while (j && s2[i] != p2[j + 1]) j = ne2[j];
        if (s2[i] == p2[j + 1]) j ++;
        if (j == n) {
            // 匹配成功
            if (res.count(i - n)) {
                start = i - n + 1;
                break;
            }
            j = ne2[j];
        }
    }

    cout << start << endl;

    return 0;
}
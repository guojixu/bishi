#include <bits/stdc++.h>
using namespace std;
unordered_map<int, vector<int>> mp;
vector<int> w;
int res;

void dfs(int u, vector<int>& path) {
    int x = w[u];
    res = max(res, x);
    for (int i = path.size() - 1; i >= 0; i --) {
        x ^= w[i];
        res = max(res, x);
    }
    path.push_back(w[u]);
    for (auto v: mp[u]) {
        dfs(v, path);
    }
    path.pop_back();
}

int main() {
    int n;
    cin >> n;
    w = vector<int>(n + 1);
    vector<bool> has_fathers(n + 1, false);

    for(int i=0;i<n;i++) {
        int id, weight, left, right;
        cin >> id >> weight >> left >> right;
        w[id] = weight;
        if (left != -1) mp[id].push_back(left), has_fathers[left] = true;
        if (right != -1) mp[id].push_back(right), has_fathers[right] = true;
    }

    int root = 1;
    for (int i = 1; i <= n; i ++) {
        if (!has_fathers[i]) {
            root = i;
            break;
        }
    }
    vector<int> path;
    dfs(root, path);
    cout << res << endl;
    return 0;
}
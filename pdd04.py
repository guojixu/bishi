#include <bits/stdc++.h>
using namespace std;
unordered_map<int, vector<int>> graphs;
vector<int> weights;
int res;

void dfs(int u, vector<int>& path) {
    res = max(res, weights[u]);
    for (auto x: path) res = max(res, weights[u] ^ x);
    path.push_back(weights[u]);
    for (auto v: graphs[u]) {
        dfs(v, path);
    }
    path.pop_back();
}

int main() {
    int n;
    cin >> n;
    weights = vector<int>(n + 1);
    vector<bool> has_fathers(n + 1, false);

    for (int i = 0; i < n; i ++) {
        int id, weight, left, right;
        cin >> id >> weight >> left >> right;
        weights[id] = weight;
        if (left != -1) graphs[id].push_back(left), has_fathers[left] = true;
        if (right != -1) graphs[id].push_back(right), has_fathers[right] = true;
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
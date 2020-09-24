# 3
```python
res = 0
from collections import defaultdict


def dfs(u, path: list):
    global res
    x = w[u]
    res = max(res, x)
    for i in range(len(path) - 1, -1, -1):
        x ^= w[i]
        res = max(res, x)
    path.append(w[u])
    for v in mp[u]:
        dfs(v, path)
    path.pop()


N = int(input())
w = [0] * (N + 1)
mp = defaultdict(list)
has_father = [False] * (N + 1)
for _ in range(N):
    id, weight, left, right = [int(_) for _ in input().split()]
    w[id] = weight
    if left != -1:
        mp[id].append(left)
        has_father[left] = True
    if right != -1:
        mp[id].append(right)
        has_father[right] = True

root = None
for i in range(1, N + 1):
    if not has_father[i]:
        root = i
        break
path = []
dfs(root, path)
print(res)

```

# 4
```cpp
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
```

# 4
```python
def kmp(mom_string, son_string):
    pos1 = []
    test = ''
    if type(mom_string) != type(test) or type(son_string) != type(test):
        pos1.append(-1)
        return -1
    if len(son_string) == 0:
        pos1.append(0)
        return 0
    if len(mom_string) == 0:
        pos1.append(-1)
        return -1
    next = [-1] * len(son_string)
    if len(son_string) > 1:
        next[1] = 0
        i, j = 1, 0
        while i < len(son_string) - 1:
            if j == -1 or son_string[i] == son_string[j]:
                i += 1
                j += 1
                next[i] = j
            else:
                j = next[j]
    m = s = 0
    while (s < len(son_string) and m < len(mom_string)):
        if s == -1 or mom_string[m] == son_string[s]:
            m += 1
            s += 1
        else:
            s = next[s]

    if s == len(son_string):
        pos1.append(m - s)
    pos1.append(-1)
    return pos1


k = int(input())
pat1 = "".join(input().strip().split())
pat2 = "".join(input().strip().split())
n = int(input())
st1 = "".join(input().strip().split())
st2 = "".join(input().strip().split())

pos11 = kmp(st1, pat1)
pos22 = kmp(st2, pat2)
k = [i for i in pos11 if i in pos22 and i != -1]
if k == -1 or len(k) == 0:
    print(0)
else:
    print(k[0] + 1)
```
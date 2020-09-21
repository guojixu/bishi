#2
class TreeAncestor:

    def __init__(self, n: int, parent):
        self.cols = 20  # log(50000) < 20

        self.dp = [[-1] * self.cols for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = parent[i]
        # 动态规划设置祖先, dp[node][j] 表示 node 往前推第 2^j 个祖先
        for j in range(1, self.cols):
            for i in range(n):
                if self.dp[i][j - 1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]
        return

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.cols - 1, -1, -1):
            if k & (1 << i):
                node = self.dp[node][i]
                if node == -1:
                    break
        return node


if __name__ == '__main__':
    n, q = [int(_) for _ in input().split()]
    parent = [-1] + [int(_) - 1 for _ in input().split()]
    ta = TreeAncestor(n, parent)
    for _ in range(q):
        x, k = [int(_) for _ in input().split()]
        print(ta.getKthAncestor(x - 1, k) + 1)

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

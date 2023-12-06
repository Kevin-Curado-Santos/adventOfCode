#include <bits/stdc++.h>

using namespace std;
typedef long long i64;

bool isValid(int x, int y, vector<string> &grid, int h, int w) {
    pair<int, int> neighbors[] = {
        {x - 1, y}, {x + 1, y}, {x, y - 1}, {x, y + 1},
        {x - 1, y - 1}, {x - 1, y + 1}, {x + 1, y - 1}, {x + 1, y + 1},
    };
    for (auto nb: neighbors) {
        if (nb.first >= 0 && nb.first < h && nb.second >= 0 && nb.second < w) {
            if (!isdigit(grid[nb.first][nb.second])
                && grid[nb.first][nb.second] != '.') {
                return true;
            }
        }
    }
    return false;
}

void part1() {
    ifstream file("3.in");
    string line;
    vector<string> grid;
    while(getline(file, line)){
        grid.push_back(line);
    }
    int w = grid[0].size();
    int h = grid.size();

    int ans = 0;
    for(int i=0; i<h;i++){
        int j = 0;
        while(j<w){
            if(isdigit(grid[i][j])){
                int num = 0;
                bool valid = false;
                while(isdigit(grid[i][j])){
                    num = num * 10 + (grid[i][j] - '0');
                    valid = valid || isValid(i, j, grid, h, w);
                    j++;
                }
                if(valid){
                    ans += num;
                }
            }else{
                j++;
            }
        }
    }
    cout << ans << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    part1();
    return 0;
}
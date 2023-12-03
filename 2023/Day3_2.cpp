#include <bits/stdc++.h>

using namespace std;
typedef long long i64;

pair<int, int> gearPos(int x, int y, vector<string> &grid, int h, int w) {
    pair<int, int> neighbors[] = {
        {x - 1, y}, {x + 1, y}, {x, y - 1}, {x, y + 1},
        {x - 1, y - 1}, {x - 1, y + 1}, {x + 1, y - 1}, {x + 1, y + 1},
    };
    for (auto nb: neighbors) {
        if (nb.first >= 0 && nb.first < h && nb.second >= 0 && nb.second < w) {
            if (grid[nb.first][nb.second] == '*') {
                return {nb.first, nb.second};
            }
        }
    }
    return {-1, -1};
}

void part2(){
    ifstream file("3.in");
    string line;
    vector<string> grid;
    map<pair<int, int>, vector<int>> cn;
    while(getline(file, line)){
        grid.push_back(line);
    }
    int w = grid[0].size();
    int h = grid.size();

    int ans = 0;

    for(int i=0; i<h; i++){
        int j = 0;
        while(j<w){
            if(isdigit(grid[i][j])){
                int num = 0;
                set<pair<int, int>> gears;
                while(isdigit(grid[i][j])){
                    num = num * 10 + (grid[i][j] - '0');
                    auto pos = gearPos(i, j, grid, h, w);
                    if(pos!=make_pair(-1, -1)){
                        gears.insert(pos);
                    }
                    j++;
                }
                for(auto gear: gears){
                    cn[gear].push_back(num);
                }
            }else{
                j++;
            }
        }
    }

    for(auto it : cn){
        if(it.second.size()==2)
            ans += it.second[0] * it.second[1];
    }
    cout << ans << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    part2();
    return 0;
}
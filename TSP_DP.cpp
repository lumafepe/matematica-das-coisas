#include <iostream>
#include <vector>
#include <filesystem>
#include <string>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <chrono>

using namespace std;

/*int graph[][N] = { { 0, 10, 15, 20 },
                       { 10, 0, 35, 25 },
                       { 15, 35, 0, 30 },
                       { 20, 25, 30, 0 } };
*/

#define MAXN 20

int graph[MAXN][MAXN];

int N;

//N, 2^N
int dp[MAXN][1 << MAXN];

vector<int> answer;

void printAnswer() {
    for (int i = 0; i < answer.size(); i++) {
        cout << answer[i] << "-";
    }

    cout << 0;
}

bool isSet(int i, int bitmask) {
    return bitmask & (1 << i);
}

int remove_(int i, int bitmask) {
    if (isSet(i, bitmask))
        bitmask -= (1 << i);

    return bitmask;
}

int tsp(int n, int bitmask, int depth) {

    if (dp[n][bitmask] != -1)
        return dp[n][bitmask];

    int ans = 1e9;

    cout << n << " " << depth << endl;

    for (int i = 1; i < N; i++) {
        if (!isSet(i, bitmask) || i == n)
            continue;

        int newBitmask = remove_(i, bitmask);

        if(graph[i][n] != -1)
            ans = min(ans, tsp(i, newBitmask, depth + 1) + graph[i][n]);
    }

    if (ans == 1e9)
        ans = graph[0][n];

    dp[n][bitmask] = ans;

    return ans;
}


void rebuild(int n, int bitmask) {
    answer.push_back(n);


    int ans = 1e9;

    int j = -1;

    for (int i = 1; i < N; i++) {
        if (!isSet(i, bitmask) || i == n)
            continue;

        int newBitmask = remove_(i, bitmask);

        if (graph[i][n] != -1) {
            int temp = tsp(i, newBitmask, 0) + graph[i][n];

            if (temp < ans) {
                ans = temp;
                j = i;
            }
        }
    }

    if (j != -1)
        rebuild(j, remove_(j, bitmask));
}

int main()
{
    cin >> N;

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> graph[i][j];

    auto start = std::chrono::high_resolution_clock::now();
    //Set the dp array to all -1
    memset(dp, -1, sizeof(dp));

    int ans = 1e9;


    int bitmask = pow(2, N) - 2;

    for (int i = 1; i < N; i++) {
        if (graph[i][0] != -1) {
            int temp = tsp(i, remove_(i, bitmask), 0) + graph[i][0];

            if (temp < ans) {
                ans = temp;
                answer = vector<int>();
                rebuild(i, remove_(i, bitmask));
            }
        } 
    }
    answer.push_back(0);
    reverse(answer.begin(), answer.end());

    auto finish = std::chrono::high_resolution_clock::now();

     auto microseconds = std::chrono::duration_cast<std::chrono::milliseconds>(finish-start);

    cout << "RESPOSTA: " << ans << endl;
    cout << "CAMINHO: ";
    printAnswer();
    cout << endl;

    cout << "DURACAO: " << microseconds.count() <<endl;

    return 0;
}
 //https://github.com/sth144/christofides-algorithm-cpp/blob/master/tsp.cpp

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <chrono>

using namespace std;



#define N 1000

int graph[N][N];


void compute_shortestPath(int V) {
    vector<int> visited(V,0);

    vector<int> path(1,0);
    int current = 0;
    int count = 1;
    int cost = 0;

    visited[0] = 1;

    while(count < V) {
        int min = 1e9, index = -1;

        for(int i = 0; i < V; i++) {
            if(!visited[i] && graph[current][i] < min) {
                min = graph[current][i];
                index = i;
            }
        }
        cout << index << " " << count << endl;
        visited[index] = 1;
        path.push_back(index);
        current = index;
        ++count;
        cost += min;
    }

    cout << "RESPOSTA: " << cost << endl;
    cost += graph[current][0];
    cout << "CAMINHO: " << endl;
    for(int i = 0; i < V; i++) {
        cout << path[i] << " ";
    }
    cout << endl;
}


int main() {

    int n;

    cin >> n;

    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            cin >> graph[i][j];

    auto start = std::chrono::high_resolution_clock::now();

    compute_shortestPath(n);

    auto finish = std::chrono::high_resolution_clock::now();

    auto microseconds = std::chrono::duration_cast<std::chrono::milliseconds>(finish-start);

    cout << "DURACAO: " << microseconds.count() <<endl;

    return 0;
}
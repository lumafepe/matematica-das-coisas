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


int tsp(const std::vector<int>& v,int minimo){
    int ea=0;
    int minat=0;
    for (int e : v){
        if (ea!=0)
            minat+=graph[ea][e];
        else ea=e;
    }
    if (minat<minimo) return minat;
    else return minimo;
}



int main(){




    cin >> N;
    int arr[N];

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> graph[i][j];

    for (int i = 0; i < N; i++) arr[i]=i;
    int n = sizeof(arr)/sizeof(arr[0]);
    std::vector<int> a(arr,arr+n);
    int min=1410065408;
    auto start = std::chrono::high_resolution_clock::now();
    do{
        min=tsp(a,min);
    } while (std::next_permutation(a.begin(),a.end()));


    auto finish = std::chrono::high_resolution_clock::now();
    auto microseconds = std::chrono::duration_cast<std::chrono::milliseconds>(finish-start);
    cout << endl;
    cout << "DURACAO: " << microseconds.count() <<endl;

    return 0;
}
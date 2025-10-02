#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <filesystem>

using namespace std;
namespace fs = std::filesystem;

vector<int> balancearr(vector<int>& arr, int l, int r) {
    if (l > r) return {};
    int mid = l + (r - l) / 2;
    vector<int> result = {arr[mid]};
    vector<int> left = balancearr(arr, l, mid - 1);
    vector<int> right = balancearr(arr, mid + 1, r);
    result.insert(result.end(), left.begin(), left.end());
    result.insert(result.end(), right.begin(), right.end());
    return result;
}

void generateInput(int n) {
    vector<int> arr(n);
    for (int i = 0; i < n; i++) arr[i] = rand();

    fs::create_directory("inputs");

    // random (unsorted)
    ofstream out("inputs/inputnotsorted_" + to_string(n) + ".txt");
    out << n << "\n";
    for (auto x : arr) out << x << "\n";
    out.close();

    // ascending
    sort(arr.begin(), arr.end());
    out.open("inputs/inputsortedincreasing_" + to_string(n) + ".txt");
    out << n << "\n";
    for (auto x : arr) out << x << "\n";
    out.close();

    vector<int> balanced = balancearr(arr, 0, n - 1);
    out.open("inputs/inputbalanced_" + to_string(n) + ".txt");
    out << n << "\n";
    for (auto x : balanced) out << x << "\n";
    out.close();

    // descending
    sort(arr.begin(), arr.end(), greater<int>());
    out.open("inputs/inputsorteddecreasing_" + to_string(n) + ".txt");
    out << n << "\n";
    for (auto x : arr) out << x << "\n";
    out.close();

    cout << "Created input files for n = " << n << endl;
}

int main() {
    srand(time(0));
    vector<int> inputs = {1000, 2500, 5000, 7500, 10000, 25000, 50000, 75000, 100000};

    for (int n : inputs) {
        generateInput(n);
    }

    return 0;
}

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>

using namespace std;

int partition(vector<int> &arr, int low, int high) {
    int pivot = arr[low];
    swap(arr[low], arr[high]); // move pivot to end
    int left = low - 1;
    for (int right = low; right < high; right++) {
        if (arr[right] <= pivot) {
            left++;
            swap(arr[left], arr[right]);
        }
    }
    swap(arr[left + 1], arr[high]);
    return left + 1;
}

void quickSort(vector<int> &arr, int low, int high) {
    if (low < high) {
        int mid = partition(arr, low, high);
        quickSort(arr, low, mid - 1);
        quickSort(arr, mid + 1, high);
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        cout << "Usage: " << argv[0] << " inputfile.txt" << endl;
        return 1;
    }

    string filename = argv[1];
    ifstream file(filename);
    if (!file.is_open()) {
        cout << "Error: Cannot open input file." << endl;
        return 1;
    }

    int n;
    file >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++)
        file >> arr[i];
    file.close();

    auto start = chrono::steady_clock::now();
    quickSort(arr, 0, n - 1);
    auto end = chrono::steady_clock::now();

    cout << chrono::duration_cast<chrono::microseconds>(end - start).count() << endl;
    return 0;
}

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>

using namespace std;

void heapify(vector<int> &arr, int n, int i)
{
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    int largest = i;

    if (left < n && arr[left] > arr[largest])
    {
        largest = left;
    }

    if (right < n && arr[right] > arr[largest])
    {
        largest = right;
    }

    if (largest != i)
    {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(vector<int> &arr, int n)
{
    for (int i = (n / 2) - 1; i >= 0; i--)
    {
        heapify(arr, n, i);
    }

    for (int i = n - 1; i >= 0; i--)
    {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        cout << "Usage: " << argv[0] << " inputfile.txt" << endl;
        return 1;
    }

    string filename = argv[1];
    ifstream file(filename);
    if (!file.is_open())
    {
        cout << "Error: Cannot open input file." << endl;
        return 1;
    }

    int n;
    file >> n;
    vector<int> arr(n);

    for (int i = 0; i < n; i++)
    {
        file >> arr[i];
    }
    file.close();

    auto start = chrono::steady_clock::now();
    heapSort(arr, n);
    auto end = chrono::steady_clock::now();

    auto duration = chrono::duration_cast<chrono::microseconds>(end - start).count();

    string inputType, nStr;
    cout << duration << endl;

    return 0;
}
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>

using namespace std;

void countSort(vector<int> &arr, int n, int place)
{
    int count[10];
    for (int i = 0; i < 10; i++)
        count[i] = 0;
    for (int i = 0; i < n; i++)
        count[(arr[i] / place) % 10]++;
    for (int i = 1; i < 10; i++)
        count[i] = count[i - 1] + count[i];

    vector<int> res(n);
    for (int i = n - 1; i >= 0; i--)
    {
        res[count[(arr[i] / place) % 10] - 1] = arr[i];
        count[(arr[i] / place) % 10]--;
    }
    for (int i = 0; i < n; i++)
    {
        arr[i] = res[i];
    }
}

void radixSort(vector<int> &arr, int n)
{
    int maxElement = arr[0];
    for (int i = 1; i < n; i++)
    {
        maxElement = max(maxElement, arr[i]);
    }

    for (int place = 1; (maxElement / place) > 0; place *= 10)
    {
        countSort(arr, n, place);
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
    radixSort(arr, n);
    auto end = chrono::steady_clock::now();

    auto duration = chrono::duration_cast<chrono::microseconds>(end - start).count();

    string inputType, nStr;
    cout << duration << endl;

    return 0;
}

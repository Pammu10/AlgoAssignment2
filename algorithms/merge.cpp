#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>

using namespace std;

void merge(vector<int> &arr, int low, int mid, int high)
{
    vector<int> temp(high - low + 1);
    int left = low;
    int right = mid + 1;
    int k = 0;
    while (left <= mid && right <= high)
    {
        if (arr[left] < arr[right])
        {
            temp[k] = arr[left];
            left++;
            k++;
        }
        else
        {
            temp[k] = arr[right];
            right++;
            k++;
        }
    }

    while (left <= mid)
    {
        temp[k++] = arr[left];
        left++;
    }

    while (right <= high)
    {
        temp[k++] = arr[right];
        right++;
    }

    for (int i = low; i <= high; i++)
    {
        arr[i] = temp[i - low];
    }
}

void mergeSort(vector<int> &arr, int low, int high)
{
    if (low >= high)
        return;
    int mid = low + (high - low) / 2;
    mergeSort(arr, low, mid);
    mergeSort(arr, mid + 1, high);
    merge(arr, low, mid, high);
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
    mergeSort(arr, 0, n - 1);
    auto end = chrono::steady_clock::now();

    auto duration = chrono::duration_cast<chrono::microseconds>(end - start).count();

    string inputType, nStr;
    cout << duration << endl;

    return 0;
}

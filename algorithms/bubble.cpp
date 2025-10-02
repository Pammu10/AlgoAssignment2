#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>

using namespace std;

void bubbleSort(vector<int> &arr, int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        bool swap = false;
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swap = true;
            }
        }
        if (!swap)
            break;
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
    bubbleSort(arr, n);
    auto end = chrono::steady_clock::now();

    auto duration = chrono::duration_cast<chrono::microseconds>(end - start).count();

    string inputType, nStr;

    cout << duration << endl;

    return 0;
}

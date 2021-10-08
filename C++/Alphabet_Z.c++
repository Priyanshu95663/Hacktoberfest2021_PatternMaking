#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cout << "Enter a number: ";
    cin >> n;
    for (int row = 0; row < n; row++)
    {
        for (int column = 0; column < n; column++)
        {
            if (row == 0 || row == n - 1 || column == n - 1 - row)
            {
                cout << "*";
            }
            else
            {
                cout << " ";
            }
        }
        cout << endl;
    }
    return 0;
}

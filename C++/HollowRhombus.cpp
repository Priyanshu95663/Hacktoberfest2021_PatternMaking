#include <iostream>
using namespace std;

int n;  // No. of rows or columns
cin>>n;
for (int i=1; i<=n; i++)
{   
    for (int j=1; j<=n-i; j++)
    {
        cout<<" ";
    }
    for (int j=1; j<=n; j++)
    {
        if (i == 1 || i == n)
        {
            cout<<"*";
        }
        else if (j == 1 || j == n)
        {
            cout<<"*";
        }
        else
        { 
            cout<<" ";
        }
    }
    cout<<endl;
}

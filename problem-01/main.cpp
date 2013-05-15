#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int a, b, c, ans = 0;
    cin>>a>>b;
    c = max(a, b);
    for (int i = 2; i <= c; ++i)
        if (a % i == b % i)
            ++ans;
    cout<<ans<<endl;
}

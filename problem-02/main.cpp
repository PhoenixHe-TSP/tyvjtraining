#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>

using namespace std;

char ma[103][103];
int F[4][2]={ 0,1,1,0,0,-1,-1,0 };

int main()
{
    int n, m, x=0, y=0, d=0;
    char letter = '#';
    string s;
    memset(ma, 'o', sizeof(ma));
    cin>>n>>m>>s;
    for (string::iterator i = s.begin(); i != s.end(); ++i)
    {
        switch (*i)
        {
            case 'F':
                ma[x][y] = letter;
                x += F[d][0];
                y += F[d][1];
                x = (x + n) % n;
                y = (y + m) % m;
                break;
            case 'L':
                d = (d + 3) % 4;
                break;
            case 'R':
                d = (d + 1) % 4;
                break;
            case 'C':
                letter = *(++i);
        }

    }
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
            putchar(ma[i][j]);
        putchar('\n');
    }
}

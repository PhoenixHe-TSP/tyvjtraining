#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
int main()
{
     int i,n;
     scanf("%d",&n);
     long long sum1=(1LL+n)*n/2;
     long long sum2=1LL*n*(n+1)/2*(2*n+1)/3;
     int x;
     for(i=1;i<=n-2;++i)
     {
         scanf("%d",&x);
         sum1-=x;
         sum2-=x*x;
     }    
     int num1=(sum1+sqrt(2*sum2-sum1*sum1))/2;
     int num2=(sum1-sqrt(2*sum2-sum1*sum1))/2;
     printf("%d %d\n", min(num1,num2), max(num1,num2));
     return 0;
}

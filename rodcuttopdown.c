#include<stdio.h>
#include<limits.h>
int max(int a, int b)
{
    return (a > b)? a : b;
}


int rodcuttopdown(int price[], int n,int r[])
{
int maxval;
  if(r[n]>=0)
        return r[n];

  if(n==0)
    maxval=0;
  else
  {

    maxval= INT_MIN;
    for(int i=1; i<=n; i++)
    {
        maxval= max(maxval,price[i]+rodcuttopdown(price,n-i,r));
    }

  }
 r[n]=maxval;

 return maxval;
}


int rodcut(int price[],int n)
{
    int r[n];
    int i=1;
    while(i<=n)
    {
         r[i]=INT_MIN;
         i++;
    }
    return rodcuttopdown(price,n,r);
}



int main(int argc, char *argv[])
{

    int n = 6;
    int arr[] = {INT_MIN, 10, 23};
	printf("Max Value is %d",rodcut(arr,n));

	return 0;
}

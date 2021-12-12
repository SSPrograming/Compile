#include <stdio.h>
#include <stdlib.h>

int sum(int *a, int n)
{
    int _sum = 0;
    n = n - 1;
    while (n >= 0)
    {
        _sum = _sum + a[n];
        n = n - 1;
    }
    return _sum;
}

int main()
{
    int a[3];
    a[0] = 0;
    a[1] = 1;
    a[2] = 2;
    printf("sum(0, 1, 2) = %d\n", sum(a, 3));
    return 0;
}

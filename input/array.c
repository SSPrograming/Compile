#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n = 3;
    int a[3];
    a[0] = 0;
    a[1] = -(10 + 2);
    a[2] = a[1];
    printf("a[0] = %d\n", a[0]);
    printf("a[1] = %d\n", a[1]);
    printf("a[2] = %d\n", a[2]);
    
    return 0;
}

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    int a[3];
    a[0] = 0;
    a[1] = -(10 + 2);
    a[2] = a[1];
    printf("a[0] = %d\n", a[0]);
    printf("a[1] = %d\n", a[1]);
    printf("a[2] = %d\n", a[2]);
    
    n = 5;
    int* b = (int*)malloc(n);
    b[0] = 0;
    b[1] = 4;
    b[2] = 2;
    b[4] = 4;
    b[5] = 6;
    while(n + 1 > 0) {
        printf("b[%d] = %d\n", n, b[n]);
        n = n - 1;
    }

    return 0;
}

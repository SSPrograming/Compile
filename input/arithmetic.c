#include <stdio.h>

int main()
{
    int a = 1;
    int b = 2;
    printf("%d + %d = %d\n", a, b, a + b);
    a = 4;
    b = 2;
    printf("%d - %d = %d\n", a, b, a - b);
    a = 3;
    b = 4;
    printf("%d * %d = %d\n", a, b, a * b);
    a = 10000;
    b = 5000;
    printf("%d / %d = %d\n", a, b, a / b);
    return 0;
}

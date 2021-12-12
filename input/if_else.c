#include <stdio.h>

int main()
{
    int a = 20;
    printf("a = ");
    if (a > 10)
    {
        printf("%d > 10\n", a);
    }
    else if (a <= 10 && a > 5)
    {
        printf("%d > 5\n", a);
    }
    else if (a > 1)
    {
        printf("%d > 1\n", a);
    }
    else if (a == 1)
    {
        printf("%d > 0\n", a);
    }
    else if (a <= -1)
    {
        printf("%d <= -1\n", a);
    }
    else
    {
        printf("%d = 0\n", a);
    }
    return 0;
}

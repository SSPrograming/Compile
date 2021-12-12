#include <stdio.h>

int main()
{
    int n = 0;
    while (1)
    {
        if (n > 5)
        {
            break;
        }
        else
        {
            printf("%d\n", n);
            n = n + 1;
            continue;
        }
    }
    return 0;
}

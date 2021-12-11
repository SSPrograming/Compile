#include <stdlib.h>
#include <stdio.h>

void sort(int *arr, int n)
{
    if (n < 0)
    {
        return;
    }
    int i = n - 1;
    int j = 0;
    int change = 0;
    while (i >= 0)
    {
        j = 0;
        while (j < i)
        {
            if (arr[j] > arr[j + 1])
            {
                arr[j] = arr[j + 1] + arr[j];
                arr[j + 1] = arr[j] - arr[j + 1];
                arr[j] = arr[j] - arr[j + 1];
                change = 1;
            }
            j = j + 1;
        }
        if (change == 0)
        {
            break;
        }
        i = i - 1;
    }
    return;
}

int main()
{
    int n;
    scanf("%d", &n);
    int *arr = (int *)malloc(4 * n);
    int i = 0;
    printf("n = %d\n", n);
    while (i < n)
    {
        scanf("%d", arr + i);
        printf("%d\n", arr[i]);
        i = i + 1;
    }
    sort(arr, n);
    i = 0;
    while (i < n)
    {
        printf("%d ", arr[i]);
        i = i + 1;
    }
    printf("\n");
    free((char *)arr);
    return 0;
}

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
    int a[5];
    a[0] = 2;
    a[1] = 4;
    a[2] = 6;
    a[3] = 1;
    a[4] = 4;
    int k = 0;
    printf("初始 a = {");
    while (k < 5)
    {
        if (k == 4)
        {
            printf("%d", a[k]);
        }
        else
        {
            printf("%d, ", a[k]);
        }
        k = k + 1;
    }
    printf("}\n");
    sort(a, 5);
    k = 0;
    printf("排序 a = {");
    while (k < 5)
    {
        if (k == 4)
        {
            printf("%d", a[k]);
        }
        else
        {
            printf("%d, ", a[k]);
        }
        k = k + 1;
    }
    printf("}\n");

    int n;
    printf("请输入数组的元素个数：");
    scanf("%d", &n);
    int *arr = (int *)malloc(sizeof(int) * n);
    int i = 0;
    printf("n = %d\n", n);
    printf("请输入元素：");
    while (i < n)
    {
        scanf("%d", arr + i);
        i = i + 1;
    }
    sort(arr, n);
    printf("数组排序结果：");
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

#include <stdio.h>

int main()
{
    int a;
    int b;
    printf("请输入两个数字：");
    scanf("%d %d", &a, &b);
    printf("您输入的数字的和是：%d + %d = %d\n", a, b, a + b);
    return 0;
}

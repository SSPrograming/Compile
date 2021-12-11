#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

//-1表示小于，0表示等于，1表示大于
int operatorCmp(char operator1, char operator2)
{
    if (operator1 == '+' || operator1 == '-')
    {
        if (operator2 == '*' || operator2 == '/' || operator2 == '(')
        {
            return -1;
        }
        else
        {
            return 1;
        }
    }
    if (operator1 == '*' || operator1 == '/')
    {
        if (operator2 == '(')
        {
            return -1;
        }
        else
        {
            return 1;
        }
    }
    if (operator1 == '(')
    {
        if (operator2 == ')')
        {
            return 0;
        }
        else
        {
            return -1;
        }
    }
    if (operator1 == ')')
    {
        exit(-1);
    }
    if (operator1 == '\0')
    {
        if (operator2 == '\0')
        {
            return 0;
        }
        else
        {
            return -1;
        }
    }
}

double calculate(double number_1, char operator, double number_2)
{
    if (operator== '+')
    {
        return number_1 + number_2;
    }
    if (operator== '-')
    {
        return number_1 - number_2;
    }
    if (operator== '*')
    {
        return number_1 * number_2;
    }
    if (operator== '/')
    {
        return number_1 / number_2;
    }
    exit(-1);
}

double evaluate(char *S)
{
    double opnd[1024];
    char optr[1024];
    int opnd_p = 0; //运算数栈指针
    int optr_p = 0; //运算符栈指针
    optr_p = optr_p + 1;
    optr[optr_p] = '\0';
    while (optr_p > 0)
    {
        if (isdigit((int)*S))
        {
            int number = 0;
            while (isdigit((int)*S))
            {
                number = number * 10 + (int)(*S) - '0';
                S = S + 1;
            }
            opnd_p = opnd_p + 1;
            opnd[opnd_p] = (double)number;
        }
        else
        {
            int cmpResult = operatorCmp(optr[optr_p], *S);
            if (cmpResult == -1)
            {
                optr_p = optr_p + 1;
                optr[optr_p] = *S;
                S = S + 1;
            }
            if (cmpResult == 0)
            {
                optr_p = optr_p - 1;
                S = S + 1;
            }
            if (cmpResult == 1)
            {
                char op_top = optr[optr_p];
                optr_p = optr_p - 1;
                double number_2 = opnd[opnd_p];
                opnd_p = opnd_p - 1;
                double number_1 = opnd[opnd_p];
                opnd_p = opnd_p - 1;
                double cal_res = calculate(number_1, op_top, number_2);
                opnd_p = opnd_p + 1;
                opnd[opnd_p] = cal_res;
            }
        }
    }
    return opnd[opnd_p];
}

int main()
{
    char str[1024];
    scanf("%s", str);
    double res = evaluate(str);
    printf("%d\n", res);
    return 0;
}

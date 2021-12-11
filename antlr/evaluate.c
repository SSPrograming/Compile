#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int calculate(int number_1, char operator, int number_2) {
    if (operator == '+') {
        return number_1 + number_2;
    }
    else if (operator == '-') {
        return number_1 - number_2;
    }
    else if (operator == '*') {
        return number_1 * number_2;
    }
    else if (operator == '/') {
        return number_1 / number_2;
    }
    exit(-1);
}

//-1表示小于，0表示等于，1表示大于
int operatorCmp(char operator1, char operator2) {
    if (operator1 == '+' || operator1 == '-') {
        if(operator2 == '*' || operator2 == '/' || operator2 == '(') {
            return -1;
        }
        else {
            return 1 ;
        }
    }
    else if (operator1 == '*' || operator1 == '/') {
        if (operator2 == '(') {
            return -1;
        }
        else
        {
            return 1;
        }
    }
    else if (operator1 == '(') {
        if (operator2 == ')') {
            return 0;
        }
        else
        {
            return -1;
        }
    }
    else if (operator1 == ')') {
        exit(-1);
    }
    else if (operator1 == '\0') {
        if (operator2 == '\0') {
            return 0;
        }
        else
        {
            return -1;
        }
    }
}

int evaluate(char* S)
{
    int opnd[1024];
    char optr[1024];
    int opnd_p = 0;     //运算数栈指针
    int optr_p = 0;     //运算符栈指针
    optr_p = optr_p + 1;
    optr[optr_p] = '\0';
    while (optr_p > 0) 
    {
        if(isdigit(*S))
        {
            int number = 0;
            while (isdigit(*S)) {
                number = number * 10 + *S - '0';
                S = S + 1;
            }
            opnd_p = opnd_p + 1;
            opnd[opnd_p] = number;
        }
        else
        {
            int cmpResult = operatorCmp(optr[optr_p], *S);
            if (cmpResult == -1) {
                optr_p = optr_p + 1;
                optr[optr_p] = *S;
                S = S + 1 ;
            }
            else if (cmpResult == 0) {
                optr_p = optr_p - 1;
                S = S + 1;
            }
            else if (cmpResult == 1) {
                char op_top = optr[optr_p];
                optr_p = optr_p - 1;
                int number_2 = opnd[opnd_p];
                opnd_p = opnd_p - 1;
                int number_1 = opnd[opnd_p];
                opnd_p = opnd_p - 1;  
                int cal_res = calculate(number_1, op_top, number_2);
                opnd_p = opnd_p + 1;
                opnd[opnd_p] = cal_res;
            }
        }
    }
    return opnd[opnd_p];
}

int main()
{
    char str [1024];
    scanf("%s", str);
    int res = evaluate(str);
    printf("%d\n", res);
    return 0;
}
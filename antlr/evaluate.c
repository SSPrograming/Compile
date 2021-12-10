#include<stdio.h>
#include<ctype.h>

int operatorOrder(char operator)
{
    if (operator == '+') {
        return 0;
    }
    else if (operator == '-') {
        return 1;
    }
    else if (operator == '*') {
        return 2;
    }
    else if (operator == '/') {
        return 3;
    }
    else if (operator == '(') {
        return 4;
    }
    else if (operator == ')') {
        return 5;
    }
    else if (operator == '\0') {
        return 6;
    }
    exit(1);
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
    optr[++optr_p] = '\0';
    while (optr_p > 0) 
    {
        if(isdigit(*S))
        {
            int number = 0;
            while (isdigit(*S)) {
                number = number * 10 + *S - '0';
                S = S + 1;
            }
            opnd[++opnd_p] = number;
        }
        else
        {
            int cmpResult = operatorCmp(optr[optr_p], *S);
            if (cmpResult == -1) {
                optr[++optr_p] = *S;
                S = S + 1;
            }
            else if (cmpResult == 0) {
                optr_p = optr_p - 1;
                S = S + 1;
            }
            else if (cmpResult == 1) {
                char op_top = optr[optr_p];
                optr_p = optr_p - 1;
                 
            }
        }
    }
}
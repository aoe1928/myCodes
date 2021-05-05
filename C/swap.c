#include<stdio.h>

void swap(int*, int*);
int main()
{
    int a, b;
    a = 10;
    b = 20;
    swap(&a, &b);
    printf("%d %d\n", a, b);
    return 0;
}
void swap(int *a, int *b)
{
    // int tmp;
    // tmp = *b;
    // printf("%d\n", tmp);
    // *b = *a;
    // *a = tmp;
    *a += *b;
    *b = *a - *b;
    *a -= *b;
}
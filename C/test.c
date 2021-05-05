#include <stdio.h>
int main()
{
    int num = 10;
    int *p = &num;
    *p = 20;
    printf("%d\n", num);
    printf("%d\n", *&num);
    return 0;
}

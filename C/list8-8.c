#include<stdio.h>
int add_point(int *p);

int main()
{
    int all_point;
    int point[3] = {10, 20, 50};
    all_point = add_point(point);
    printf("now point is %d\n", all_point);
    return 0;
}
int add_point(int *p)
{
    int sum = 0;
    for (int i = 0; i < 3; i++){
        sum += *(p + i);
    }
    return sum;
}
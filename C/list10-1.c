#include <stdio.h>
int main()
{
    int a, b, c, x;
    FILE *fp;
    fp = fopen("data.txt", "r");
    fscanf(fp, "%d %d %d", &a, &b, &c);
    fclose(fp);
    x = 2 * a + 3 * b + 5 * c;
    fp = fopen("calc.txt", "w+");
    fprintf(fp, "a=%d, b=%d, c=%d --> \n", a, b, c);
    fprintf(fp, "2a + 3b + 5c = %3d\n", x);
    fclose(fp);
    return 0;
}
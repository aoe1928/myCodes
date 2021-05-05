#include<stdio.h>
#include<string.h>

int main()
{
    typedef struct
    {
        char subject[10];
        int score;
        char result;
    } TEST;
    TEST kamoku, *p;
    p = &kamoku;
    strcpy(p->subject, "English");
    p->score = 85;
    p->result = 'A';

    printf("subj : %s ", p->subject);
    printf("score : %d, hyouka : %c\n", p->score, p->result);
    return 0;
}
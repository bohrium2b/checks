#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

bool isodd(int n);

int main(int argc, string argv[])
{
    int number = atoi(argv[1]);
    bool out = isodd(number);
    if (out == TRUE)
    {
        printf("Odd\n");
    }
    else
    {
        printf("Even\n");
    }
}

#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // This program adds 2 numbers
    printf("This program adds 2 integers\n");
    int num1 = get_int("1st number: ");
    int num2 = get_int("2nd number: ");
    int total = num1 + num2;
    // Print out total
    printf("%i\n", total);
    return 0;
}
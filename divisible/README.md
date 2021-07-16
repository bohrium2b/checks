# Divisible
In divisible, your task is to print out every number between `1` and `100` that is divisible
by 6. The first numbers in the sequence should be `6`, `12`, `18` ...  
You **don't** need `<cs50.h>`!

# How to get started
1. Create a new directory (`mkdir divisible`) and `cd` into it (`cd divisible`).
2. Execute `wget https://github.com/daltongit/checks/raw/c/divisible/divisible.c` to download the distribution code

# Understanding
**You should fill in all of the blanks and add code under the `TODO`'s. If you want to add or delete lines of code, you can.** 
 - The program starts by repeating between every number from 1 to 100. You should determine if the `for` loop should be `<=` or `<` 100 though.
 - We define a variable `____` with type `float`. You should replace this with a better (**more descriptive**) variable name.
 - We then set `____` to the current number (`i`) divided by `6`. **You may find this to be helpful when you are filling in the `if` statement below.** 
 - We then set an if loop. **You have to fill in the condition though.** The condition should check if **`i` divided by 6 is a whole number/integer**.
 - If `i` divided by 6 is a whole number above is true, then we print out `i`.


# Implementation Details
How should you check if a number is divisible by six? Well, you can repeat through every number
and check, **does dividing it by six output a whole number**?
If so, then that number is divisible by 6, and you should `print` it out.

# Testing
Run
`check50 daltongit/checks/c/divisible`.

# How to submit
Ready to submit? Once you are ready, run
`submit50 daltongit/checks/c/divisible`.

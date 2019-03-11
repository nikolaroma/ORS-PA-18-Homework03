"""
===================   TASK 1   ====================
* Name: Sum Number Digits
*
* Write a function `sum_digits` that will return
* sum of digits for given integer number.
* If passed value is invalid, function should
* return -1 which indicates something went wrong.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def sum_digits(n):

    s = 0
    while n :
            s += n % 10
            n //= 10
            return s
#ja ne umijem -1 da napravim




def main():

    int_number = 1234
    digit_sum = sum_digits(int_number)
    print("Sum of digits for given numbers is: ", digit_sum)

main()

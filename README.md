# function_to_check_fibonacchi
This is a function that checks for fibonacchi sequence.

In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, the Fibonacci sequence, in which each number is the sum of the two preceding ones. The sequence commonly starts from 0 and 1, although some authors omit the initial terms and start the sequence from 1 and 1 or from 1 and 2. Starting from 0 and 1, the next few values in the sequence are:[1]

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
The Fibonacci numbers were first described in Indian mathematics,[2][3][4] as early as 200 BC in work by Pingala on enumerating possible patterns of Sanskrit poetry formed from syllables of two lengths. They are named after the Italian mathematician Leonardo of Pisa, later known as Fibonacci, who introduced the sequence to Western European mathematics in his 1202 book Liber Abaci.

'''
In the Fibonacchi sequence, the first numbers are zero and one.
the next number in the sequence is the sum of the numbers that preced it.
'''


# Declare the function
def CheckIfFibonacci():
    # Prompt the user for the number they want to check.
    numberToCheck = int(input("Enter Number: "))

# The first three values of the Fibonacci Sequence are 0, 1, 1
    first_num = 0
    second_num = 1
    Third_num = 1

# First, to check whether the user input is zero or one:

    if (numberToCheck == 0 or numberToCheck == 1):
        print("The Number is a part of Fibonacci Sequence")

# For values greater than 0 and 1
    else:
        while first_num < numberToCheck:
            first_num = second_num + Third_num
            Third_num = second_num
            second_num = first_num
        if first_num == numberToCheck:
            print("The number is in the Fibonacci Sequence")
        else:
            print("The number is not in the Fibonacci Sequence")

# Now th function has o be called to check a number.  
CheckIfFibonacci()

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
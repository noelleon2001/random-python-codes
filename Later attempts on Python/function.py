# Example1
def addingNumbers(num1,num2):
    """
    INPUT: It takes two numbers
    OUTPUT: Returns the sum of the numbers
    """
    return (num1+num2)
print(addingNumbers(5,5))
print(addingNumbers.__doc__)
sum = addingNumbers(5,5)
print(sum)

# Example 2
def isPrime(num):
    """
INPUT: It takes a number
OUTPUT: Whether number is prime or not
    """
    print(isPrime.__doc__)
    for n in range(2,num):
        if num % n==0:
            return ("Not prime")
        else:
            return ("The number is prime")
print(isPrime(6))


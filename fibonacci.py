#using python to write the fibonacci sequence of a given number



# function to get fibonacci sequence using a recursive method/function
def fibonaccisequence(no):
    if no == 0:
        return 0
    elif no == 1 or no == 2 :
        return 1
    else :
        return (fibonaccisequence(no-1) + fibonaccisequence(no -2))

number = int(input("Please input a number"))
fibonacci =  fibonaccisequence(number)
# to check the validity of the number
if number <= 0:
    print("Please enter a positive integer")
else:
    ("The fibonacci sequence is:")
    for i in range(number):
        print(fibonaccisequence(i))

# Calculate factorial using a function 
n = int(input("Enter the number : "))
def fact(n):
    if n ==0 or n ==1:
        return 1
    else:
        return n * fact(n -1)
a = fact(5)
print("Factorial of",n," is : ",a)


    
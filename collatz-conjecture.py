Written in python:

# Collatz Conjecture: This program implements 3n+1 algorithim. It prompts the user for n, where n is a positive integer,
# and outputs the length of the chain.

def Length(n):
    
    count = 0
    
    while n != 1:

        if n%2 == 0:
            n = n/2

        else :
            n = 3*n+1

        count = count + 1


    return count

print("\n'Mathematics may not be ready for such problems.'\n     -Paul Erdos on the Collatz Conjecture.\n")

n = int(input('Enter a value n:\n'))
n = Length(n)

print'\nThe length of the chain is:\n\n', n

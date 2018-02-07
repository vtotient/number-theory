Written in python:

# This program was adapted from exercises in Joseph H. Silverman's A Friendly Introduction to Number Theory.
# This is my first program in python.


#  This function takes in as parameters a & b and returns the greatest common divisor. This is done using the
#  Euclidean Algorithm

def gcd(a,b):

    while b != 0:
        a, b = b, a%b
    return a


a = int(input('Enter an integer a:'))
b = int(input('Enter an integer b:'))

x = gcd(a,b)

print ('The greatest common divisor is',x)

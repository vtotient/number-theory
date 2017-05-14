Written in python:

# This program computes pi(x) (pi(x) is a function that returns the number of primes lesser than x) and the ratio
# of pi(x)/(x/ln(x)) given x, where x/ln(x) is an approximation of pi(x).

import math

# This function checks primality of n and returns 1 if prime, 0 if not prime.
# Note: this can be made more efficient using methods like Fermant's Little Theorem, Miller-Rabin test, or the Chinese
# Remainder Theorem.
def checkPrime(n):

    k = 2

    # Divide n by k until k >= n
    while k < n:
        rem = n%k

        #if the remainder of n/k is 0 then n is divisble by k. Thus n is not prime since k does not equal 1 or n.
        if rem == 0:
            return 0

        k = k+1

    # if the the loop ends then no number 1<n divides n thus n is prime

    return 1


# Count the number of primes p, where p<=x. x is passed as a parameter and the function returns the value of pi(x).
def pi(x):

    count = 0
    n = 2                   # n starts at 2 since primes >=2

    while n<=x:
        r = checkPrime(n)

        if r == 1:
            count = count +1

        n = n + 1

    return count


# The Prime Number Theorem says when x is large, the number of primes less than x is approximately equal to x/ln(x).
# Compute x/ln(x). Parameters: x, returns value of x/ln(x):
def pnt(x):
    a = x/(math.log(x))
    return a


# Compute ratio of pi(x)/(x/ln(x))
def ratio(num,b):
    c = num/b
    return c


# Main program:

print '\n\nThe number of primes lesser than or equal to x can be approximated by x/ln(x). ' \
      'This approximation works best when x is large.'

A = input('\nEnter a positive integer:\n')
b = pnt(A)

print '\nThe approximation is: \n%s' % b

num = pi(A)

if num == 1:

    print '\nThe number %s itself is prime, thus pi(x)=1.' % A

else:
    print '\nThe number of primes lesser than or equal to %s is:' % A
    print num

print '\nThe ratio of pi(x)/approx is: \n%s' % ratio(num,b)
print '\nThe closer this ratio is to one the better the approximation.'

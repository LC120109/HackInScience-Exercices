import math
def is_prime(n):
    is_prime = False
    
    if n == 1:
        return False
    elif n > 1: 
        for i in range(2, int(math.sqrt(n))+1):
            if (n % i) == 0:
                is_prime = True
                break
        
    if is_prime == True:
        return False
    else:
        return True
 
def sum_primes(n):
    sum = 0
    for i in range(n):
        if is_prime(i):
            sum += i
    return sum
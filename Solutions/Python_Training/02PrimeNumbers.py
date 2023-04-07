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
 
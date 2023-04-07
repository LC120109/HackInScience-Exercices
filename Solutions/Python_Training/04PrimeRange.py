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
        
 
def print_prime(valueRange):
    prime_list = []
    for i in range(valueRange[0], valueRange[1]):
        if is_prime(i):
            prime_list.append(i)
    
    print(*prime_list, sep = ', ')


print_prime([10000, 10050])

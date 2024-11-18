def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """


    # Function implementation here ...
    import math
    from math import sqrt
    output = True

    if num <= 1:  
        output = False
    elif num <= 3:  
        output = True
    elif num % 2 == 0 or num % 3 == 0:  
        output = False
    else:
    
        for k in range(5, int(math.sqrt(num)) + 1, 6):  
            if num % k == 0 or num % (k + 2) == 0:
                output = False
                break  

    return output  
print(is_prime(10))
print(is_prime(1))
print(is_prime(5))
# # # Run code example
# boolean = is_prime(5)   # returns True
# print(boolean)
  
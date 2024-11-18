def is_golden_number(n):
#     # function implementation ...
    if n <= 1:
        return False

    for a in range(1, n):  
        b = n - a
        if b > 0 and (a * b) % 1000 == 0:  
            return True  
    #return boolean
    return False
print(is_golden_number(42))
print(is_golden_number(65))
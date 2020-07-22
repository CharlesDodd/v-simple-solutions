def is_prime(num):

    if num <= 0: return False
    if num == 1:return False
    if num == 2:return True

    if num%6 in [2,3,4]:
        return False
    max_div = int(num**0.5)

    for i in range(3,max_div+1,2):
        if num % i == 0:
            return False
    return True

print(is_prime(2**(31)-1))
    

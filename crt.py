import numpy as np

remainders = [3,1,6,2]
moduli = [5,7,8,11]

def crt(remainders,moduli): # Accept two arrays of same size. return solution using the Chinese Remainder Theorem.
    N_i = [ int(np.prod(moduli[:i])*np.prod(moduli[i+1:])) for i in range(len(moduli)) ]
    x_i = [ int(pow(N_i[i], -1, moduli[i])) for i in range(len(moduli)) ]
    return sum( [ remainders[i]*N_i[i]*x_i[i] for i in range(len(moduli))] ) % np.prod(moduli)

    

print(crt(remainders,moduli))
         


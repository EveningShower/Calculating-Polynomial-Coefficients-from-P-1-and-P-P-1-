import math
def get_coefficients(p1, pp1):
    # calculate degree of polynomial
    n = math.floor(math.log(pp1, p1))
    
    # initialize list for coefficients
    coefficients = [0 for i in range(n+1)]
    A = pp1
    for i in range(n, -1, -1):
        a = A // p1**i
        A -= a*p1**i
        coefficients[i] = a
    return coefficients

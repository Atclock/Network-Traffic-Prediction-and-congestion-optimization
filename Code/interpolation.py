import numpy as np
 # Newton's divided difference interpolation method
def newton_interpolation(x, y, x_target):

    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)

    n = len(x)

    coef = np.copy(y)

    for j in range(1,n):
        coef[j:n] = (coef[j:n] - coef[j-1:n-1]) / (x[j:n] - x[0:n-j])


    result = coef[n-1]
    for k in range(n - 2, -1, -1):
        result = result * (x_target - x[k]) + coef[k]
    
    return result


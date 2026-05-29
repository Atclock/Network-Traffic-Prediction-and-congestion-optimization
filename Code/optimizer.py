#Here we will implement the optimization algorithm to find the optimal traffic flow that minimizes delay. We will use the Newton-Raphson method to find the minimum of the delay function.

def delay_function(x):
    return (100 / x) +0.5 * x

def delay_derivative(x):
    return (-100 / (x ** 2)) + 0.5

def delay_second_derivative(x):
    return (200 / (x ** 3))

def newton_raphson(initial_guess, tolerance=1e-6, max_iter=100):

    x = initial_guess

    iterations = []

    for i in range(max_iter):

        fx = delay_derivative(x)
        f_prime = delay_second_derivative(x)

        x_new = x - (fx / f_prime)
        
        error = abs(x_new - x)

        iterations.append((i+1, x, x_new, error))

        if error < tolerance:
            return x_new, iterations
        
        x = x_new

    return x, iterations


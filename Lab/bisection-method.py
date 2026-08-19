def square_root_bisection(number, tolerance=0.01, max_iter=50):
    if not isinstance(number, (int,float)):
        raise TypeError('Must be a number')
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    else:
        low = 0
        high = max(1,number)
        for i in range(0, max_iter):
            middle = (high + low)/2   
            if middle**2 < number:
                low = middle 
            else:
                high = middle 
            if high - low <= tolerance:
                print(f"The square root of {number} is approximately {middle}")
                return middle
            
        print(f"Failed to converge within {max_iter} iterations")
        return None
square_root_bisection(0.001, 1e-7, 50)
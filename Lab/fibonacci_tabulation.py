def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError('Input must be a number!')
    if n < 0:
        raise ValueError('Number must be a positive integer')
    sequence = [0,1]
    if n <= 1:
        return n
    i = 2
    while i <= n:
        fib = sequence[i-1] + sequence[i-2]            
        sequence.append(fib)
        i+=1
    #print(sequence)
    return sequence[n] 

#print(fibonacci(10))
    
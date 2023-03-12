
def primosRange(start, end, step):
    primes = []
    for num in range(start, end+1, step):
        if num > 1:
            for i in range(2, int(num**(1/2))+1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes
primes = primosRange(0, 10, 1)
print(primes)
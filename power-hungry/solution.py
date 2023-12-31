def solution(xs):
    n_pos = 0
    n_neg = 0
    n_zero = 0
    n = len(xs)
    prod = 1
    maxNeg = -99999999999

    # one element
    if(n == 1):
        return str(xs[0])

    # get all count
    for i in range(n):
        if(xs[i] == 0):
            n_zero += 1
        else:
            if (xs[i] > 0):
                n_pos += 1
            else:
                maxNeg = max(maxNeg, xs[i])
                n_neg += 1
        
            prod = prod * xs[i]

    # case all zero
    if(n_zero == n):
        return str(0)
    
    # case negative
    if(n_pos == 0 and n_neg == 1):
        return str(0)
    
    # if odd negative
    if n_neg & 1:
        prod = int(prod / maxNeg)
    
    return str(prod)

print(solution([-2, -3, 4, -5]))
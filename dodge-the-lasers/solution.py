# https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s

def S(n):
    if n == 1:
        return 1
    if n < 1:
        return 0
    
    a = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
    n1 = (a - 1) * n // 10**100

    return n * n1 + n * (n + 1) / 2 - n1 * (n1 + 1)/2 - S(n1)

def solution(s):
    s = int(s)

    return str(S(s))
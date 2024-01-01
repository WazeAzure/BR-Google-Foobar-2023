from math import sqrt

# def rec(n):
#     ans = 0

#     if(n == 1):
#         return 0
#     elif(n == 2):
#         return 1
#     elif(n == 3):
#         return 2
    
#     if (n & 1 == 0):
#         temp = rec(n >> 1) + 1
#         ans += temp
#     else:
#         a = rec((n+1) >> 1) + 2
#         b = rec((n-1) >> 1) + 2
#         if(a < b):
#             ans += a
#         else:
#             ans += b

#     return ans


def solution(n):
    n = int(n)

    ans = 0
    while(n > 3):
        if (n & 1):
            if (n & 2):
                n = (n + 1) >> 2
                ans += 3
            # if odd
            else:
                n = (n-1) >> 1
                ans += 2
        else:
            # if even
            n = n >> 1
            ans += 1
    if n == 3:
        ans += 2
    elif n == 2:
        ans += 1
    return ans
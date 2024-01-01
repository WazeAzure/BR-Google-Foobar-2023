

def solution(l):
    c = [0] * len(l)
    n = len(l)
    ans = 0
    for i in range(n):
        for j in range(i):
            if(l[i] % l[j] == 0):
                c[i] += 1
                ans += c[j]    
    return ans

print(solution([1, 1, 1]))
print(solution([1, 2, 3, 4, 5, 6]))

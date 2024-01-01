
def solution(banana_list):
    def isValid(n):
        for i in range(n-1):
            for j in range(i+1, n):
                if(banana_list[i] ^ banana_list[j]):
                    # print(banana_list[i], banana_list[j])
                    banana_list.pop(i)
                    banana_list.pop(j-1)
                    return True
        return False

    ans = 0
    state = True
    while(state):
        if(len(banana_list) == 1):
            break
        n = len(banana_list)
        state = isValid(n)
        
    ans = len(banana_list)
    return ans

def solution(banana_list):
    n = len(banana_list)

    odd = 0
    even = 0
    for i in range(n):
        if(banana_list[i] & 1):
            odd += 1
        else:
            even += 1
    
    return max(odd, even) - min(odd, even)

print(solution([1, 7, 3, 21, 13, 19]))
print(solution([1, 1, 1, 1, 1]))
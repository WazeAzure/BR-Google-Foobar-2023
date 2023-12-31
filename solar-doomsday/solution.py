import math

def solution(area):
    ans = []

    while(area):
        temp = math.floor(math.sqrt(area))
        area -= (temp*temp)
        ans.append(temp*temp)
    
    return str(ans)
    

# print(solution(12))
# print(solution(15324))
        

#########################

solution_list = []


def solutionBench(area):

    low_root = int(math.sqrt(area))
    low_sq = low_root**2
    solution_list.append(low_sq)

    diff = area - low_sq

    if diff == 1:
        solution_list.append(1)
        return solution_list
    elif diff == 0:
        return solution_list
    else:
        return solution(diff)


if __name__ == "__main__":
    area = int(input("Enter area: "))
    print(solutionBench(area))
    print(solution(area))
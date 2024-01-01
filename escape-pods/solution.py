def solution(entrances, exits, path):
    ne = len(entrances)
    nx = len(exits)
    np = len(path)
    inter = path[ne:(np-nx)]
    ans = 0
    for i in range(np - ne - nx):
        sum_r = sum(inter[i])
        sum_e = 0
        for j in entrances:
            sum_e += path[j][ne+i]
        ans += min(sum_e, sum_r)
    return ans

print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))
print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
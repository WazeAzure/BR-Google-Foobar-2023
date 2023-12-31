def showMap(map):
    f = open('map.txt', 'w')
    
    for r in range(len(map)):
        for c in range(len(map[0])):
            f.write(str(map[r][c]) + ' ')
        f.write('\n')
    f.close()

def BFS(r, c, map):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    visited = [[0 for i in range(len(map[0]))] for j in range(len(map))]

    visited[r][c] = 1

    next = [(r, c)]
    while next:
        x, y = next.pop(0)
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < len(map) and 0 <= next_y < len(map[0]):
                if(not visited[next_x][next_y]):
                    visited[next_x][next_y] = visited[x][y] + 1
                    if (map[next_x][next_y]):
                        continue
                    next.append((next_x, next_y))
    
    return visited

def solution(map):
    start = BFS(0, 0, map)
    end = BFS(len(map)-1, len(map[0])-1, map)
    ans = float('inf')
    for i in range(len(map)):
        for j in range(len(map[0])):
            if(start[i][j] and end[i][j]):
                ans = min(ans, start[i][j] + end[i][j] - 1)
    return ans

temp1 = solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0], [0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0]])
temp2 = solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])

print(temp1, temp2)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_power2(x):
    return (x & (x-1) == 0) and x != 0

def inifite_loop(a, b):
    numerator = a + b
    denominator = gcd(a, b)
    result = numerator // denominator

    return not (is_power2(result))

def create_graph(banana_list):
    graph = {i: [] for i in range(len(banana_list))}
    
    for i in range(len(banana_list)):
        for j in range(i, len(banana_list)):
            if (i != j) and (inifite_loop(banana_list[i], banana_list[j])):
                graph[i].append(j)
                graph[j].append(i)
    return graph

def graph_comparator(graph):
    return lambda x: len(graph[x])

def distract(graph):
    ans = 0
    remain = len(graph)

    while (remain >= 1) and len(graph) > 1:
        min_length = min(graph, key=graph_comparator(graph))

        if(len(graph[min_length]) < 1):
            del graph[min_length]
        else:
            matched_pair = [len(graph[graph[min_length][0]]) + 1, 1]

            for node in graph[min_length]:
                if(len(graph[node]) < matched_pair[0]):
                    matched_pair = [len(graph[node]), node]
                
                for i in range(len(graph[node])):
                    if(graph[node][i] == min_length):
                        del graph[node][i]
                        break
                
            for node in graph[matched_pair[1]]:
                for i in range(len(graph[node])):
                    if graph[node][i] == matched_pair[1]:
                        del graph[node][i]
                        break
                
            del graph[min_length]
            del graph[matched_pair[1]]
            ans += 2

        if (len(graph) > 1):
            remain = len(graph)
    return ans

def solution(banana_list):
    num_trainers = len(banana_list)
    if num_trainers == 2 and banana_list[0] == banana_list[1]:
        return num_trainers
    
    graph = create_graph(banana_list)
    distracted = distract(graph)
    ans = len(banana_list) - distracted

    return ans


print(solution([1, 7, 3, 21, 13, 19]))
print(solution([1, 1, 1, 1, 1]))
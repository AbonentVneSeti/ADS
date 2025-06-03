import math

def tsp(graph):
    n = len(graph)
    if n == 0:
        return 0
    full_mask = (1 << n) - 1

    dp = [[math.inf] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue

            for j in range(n):
                if mask & (1 << j):
                    continue
                if graph[i][j] == math.inf:
                    continue

                new_mask = mask | (1 << j)
                new_cost = dp[mask][i] + graph[i][j]
                if new_cost < dp[new_mask][j]:
                    dp[new_mask][j] = new_cost

    min_cycle = math.inf
    for i in range(n):
        if dp[full_mask][i] != math.inf and graph[i][0] != math.inf:
            total = dp[full_mask][i] + graph[i][0]
            if total < min_cycle:
                min_cycle = total

    return min_cycle if min_cycle != math.inf else -1

if __name__ == "__main__":
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    print(tsp(graph))
def tsp(graph):
    n = len(graph)
    if n == 0 or n == 1:
        return 0

    INF = 10 ** 18
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1 << n):
        for i in range(n):
            if dp[mask][i] == INF:
                continue
            for j in range(n):
                if mask & (1 << j):
                    continue
                if graph[i][j] == INF:
                    continue
                new_mask = mask | (1 << j)
                new_cost = dp[mask][i] + graph[i][j]
                if new_cost < dp[new_mask][j]:
                    dp[new_mask][j] = new_cost

    full_mask = (1 << n) - 1
    ans = INF
    for i in range(n):
        if dp[full_mask][i] != INF and graph[i][0] != INF:
            candidate = dp[full_mask][i] + graph[i][0]
            if candidate < ans:
                ans = candidate

    return ans if ans != INF else -1


# Пример графа (матрица связности)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(tsp(graph))  # Вывод: 80 (кратчайший путь: 0->1->3->2->0)
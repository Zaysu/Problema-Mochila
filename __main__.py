import math

def knapsack_log_n(capacity, weights, values, n):
    return math.log(n)

def knapsack_n(capacity, weights, values, n):
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

def knapsack_nlogn(capacity, weights, values, n):
    sorted_items = sorted(zip(weights, values), key=lambda x: x[0])
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, sorted_items[i][0] - 1, -1):
            dp[w] = max(dp[w], dp[w - sorted_items[i][0]] + sorted_items[i][1])
    return dp[capacity]

def knapsack_n2(capacity, weights, values, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

def knapsack_w(capacity, weights, values, n):
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

def knapsack_nw(capacity, weights, values, n):
    return knapsack_n2(capacity, weights, values, n)

def knapsack_nm(capacity, weights, values, n, m):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for w in range(capacity, weights[i - 1] - 1, -1):
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
    return dp[n][capacity]

def read_data(file_name):
    with open(file_name, 'r') as file:
        capacity, n = map(int, file.readline().strip().split())
        weights = list(map(int, file.readline().strip().split()))
        values = list(map(int, file.readline().strip().split()))

        if len(weights) != n or len(values) != n:
            raise ValueError(f"Número de itens não corresponde ao número de pesos/valores: {n} itens declarados, "
                             f"{len(weights)} pesos fornecidos, {len(values)} valores fornecidos.")

    return capacity, weights, values, n

def test_knapsack(file_name):
    print(f"\nTestando com o arquivo: {file_name}")
    try:
        capacity, weights, values, n = read_data(file_name)

        print("Resultado O(log n):", knapsack_log_n(capacity, weights, values, n))
        print("Resultado O(n):", knapsack_n(capacity, weights, values, n))
        print("Resultado O(n log n):", knapsack_nlogn(capacity, weights, values, n))
        print("Resultado O(n²):", knapsack_n2(capacity, weights, values, n))
        print("Resultado O(W):", knapsack_w(capacity, weights, values, n))
        print("Resultado O(nW):", knapsack_nw(capacity, weights, values, n))
        print("Resultado O(nm):", knapsack_nm(capacity, weights, values, n, 2))
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    files = [
        'mochila.txt',
        'knapsack_random_small.txt',
        'knapsack_random_medium.txt',
        'knapsack_random_large.txt'
    ]

    for file_name in files:
        test_knapsack(file_name)

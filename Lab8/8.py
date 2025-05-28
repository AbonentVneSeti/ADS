def count_coin_combinations(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] += dp[j - coin]

    return dp[amount]

def main():
    print(count_coin_combinations(10, [2, 5, 3, 6]))

if __name__ == "__main__":
    main()
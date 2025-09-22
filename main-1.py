# main-1.py
from typing import Dict, List
import time, statistics as stats

COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount: int) -> Dict[int, int]:
    """
    Жадібний алгоритм видачі решти.
    Спочатку вибирає найбільші доступні номінали монет.
    """
    result = {}
    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount: int) -> Dict[int, int]:
    """
    Алгоритм динамічного програмування для мінімальної кількості монет.
    """
    dp: List[int] = [0] + [float("inf")] * amount
    prev: List[int] = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in COINS:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = coin

    result: Dict[int, int] = {}
    i = amount
    while i > 0 and prev[i] != -1:
        coin = prev[i]
        result[coin] = result.get(coin, 0) + 1
        i -= coin
    return result

def bench(fn, amount, repeats=5):
    """Вимірювання часу виконання функції."""
    times = []
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn(amount)
        times.append(time.perf_counter() - t0)
    return stats.median(times)

if __name__ == "__main__":
    amount = 113
    print("Сума:", amount)
    print("Greedy:", find_coins_greedy(amount))
    print("DP:", find_min_coins(amount))

    print("\nПорівняльна таблиця:")
    print(f"{'amount':>8} | {'greedy, ms':>10} | {'dp, ms':>8}")
    print("-"*34)
    for a in [10, 100, 1000, 5000, 10000]:
        tg = bench(find_coins_greedy, a) * 1000
        td = bench(find_min_coins, a) * 1000
        print(f"{a:8d} | {tg:10.3f} | {td:8.3f}")

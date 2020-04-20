n=int(input())
prices=list(map(int,input().split()))
if len(prices) <= 1:
    print(0)
else:
    max_profit = 0
    for i in range(1, n):
        diff = prices[i] - prices[i - 1]
        if diff > 0:
            max_profit += diff
    print(max_profit)

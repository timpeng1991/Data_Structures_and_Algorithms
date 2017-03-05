# Recursive Change
def RecursiveChange(money, coins):
    if money == 0:
        return 0
    # infinite
    MinNumCoins = float('inf')
    # find the min # among len(coins) choices
    for i in range(len(coins)):
        if money >= coins[i]:
            NumCoins = RecursiveChange(money - coin[i], coins)
            if NumCoins + 1 < MinNumCoins:
                MinNumCoins = NumCoins + 1
    return MinNumCoins

# DP Change
# store all the answers, small to large
def DPChange(money, coins):
    MinNumCoins = [0] * (money + 1)
    for m in range(1, money + 1):
        MinNumCoins[i] = float('inf')
        for i in range(len(coins)):
            if m >= coins[i]:
                NumCoins = MinNumCoins(m - coins[i]) + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
    return MinNumCoins

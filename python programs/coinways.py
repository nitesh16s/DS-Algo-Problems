# def change(amount, coins):
    
#     table = [[0 for i in range(amount+1)] for j in range(len(coins))]

#     for i in range(len(coins)):
#         table[i][0] = 1
    
#     for i in range(1, amount+1):
#         if i%coins[0]==0:
#             table[0][i] = 1
#         else:
#             table[0][i] = 0
        
#     for i in range(1, len(coins)):
#         for j in range(1, amount+1):
#             if coins[i] > j:
#                 table[i][j] = table[i-1][j]
#             else:
#                 table[i][j] = table[i-1][j] + table[i][j-coins[i]]
                
#     return table[-1][-1]

# print(change(5, [1,2,3]))
# print(change(3, [2]))

def change(amount, coins):
    l=len(coins)
    dp=[0 for _ in range(amount+1)]
    # print(dp)
    dp[0]=1
    for coin in coins:
        for j in range(coin,amount+1):
            dp[j]+=dp[j-coin]
            print(dp)
    # print(dp)
    return dp[amount]

print(change(5, [1,2,5]))
print(change(3, [2]))

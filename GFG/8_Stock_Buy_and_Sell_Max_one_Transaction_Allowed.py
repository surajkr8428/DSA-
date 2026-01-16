
def maximumProfit(prices):
    
    mn = float('inf')
    mx = 0
    
    for i in prices:
        mn = min(mn,i)
        mx = max(mx,i-mn)
        
    return mx

arr = [[7, 10, 1, 3, 6, 9, 2],[7, 6, 4, 3, 1],[1, 3, 6, 9, 11]]
for j in arr:
    print("Input: ",j)
    print("Maximum Profit: ",maximumProfit(j))
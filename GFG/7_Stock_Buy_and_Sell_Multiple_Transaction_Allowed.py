def BuySell(arr):
    
    buy = []
    sell = []
    l = len(arr)
    
    ## Finding Buy and Sell Days
    buy.append(arr[0])
    for i in range(l-1):
        if arr[i] > arr[i+1]:
            buy.append(arr[i+1])
            sell.append(arr[i])
            
        elif i == l-2 and arr[-1] > buy[-1]:
            sell.append(arr[i+1])
    
    ## Calculating Profit     
    p = 0
    for j in range(len(sell)):
        p += sell[j] - buy[j]
        
    return p
    
prices = [100, 180, 260, 310, 40, 535, 695]
print("Input: ",prices)
print("Profit: ",BuySell(prices))
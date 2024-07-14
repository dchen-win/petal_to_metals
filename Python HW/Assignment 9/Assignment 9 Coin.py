import time
start = time.process_time() 
def num_coins(amount,coins,count):
   for cents in range(amount+1):
      coinCount = cents
      for j in [c for c in coins if c <= cents]:
            if count[cents-j] + 1 < coinCount:
               coinCount = count[cents-j]+1
            #    print(coinCount)
      count[cents] = coinCount
    #   print(count[cents])
   return count[amount]
print(num_coins(65,[1,5,10,25],[0]*1001))
end = time.process_time() 
print("Time elapsed was " + str(end-start))
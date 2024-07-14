#reference code: http://www.openbookproject.net/books/pythonds/Recursion/DynamicProgramming.html
import time
import sys
start = time.time() 
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
amount = int(sys.argv[1])
a = []
coins = sys.argv[2:]
for coin in coins:
    a.append(int(coin))
print("Amount = ", amount)
print("coin = ", a)
# print(num_coins(65,[1,5,10,25],[0]*1001))
end = time.time() 
print("Time elapsed was " + str(end-start))
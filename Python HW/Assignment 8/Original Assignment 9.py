import time

start = time.time() 
def num_coins(amount, coins, count):
    if 1 not in coins:
        print("A penny for your thoughts on why you thought this would work with a penny?")
        return
    min_coins = None
    if amount == 0:
        return count
    for c in coins:
        if c <= amount:
            cur_count = num_coins(amount-c, coins, count+1)
            if min_coins is None or cur_count < min_coins:
                min_coins = cur_count
    return min_coins
print(num_coins(65, [1, 5, 10, 25],0))
end = time.time() 
print("Time elapsed was " + str(end-start))
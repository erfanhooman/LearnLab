"""
Problem:
    Rewrite the counting sorting algorithm to sort a bunch of coin including one, two, five, ten and fifty penny

* Input : A list of coins in the Value of 1 , 2, 5, 10 , 50
* Output : A sorted list of this coin
"""


# --- Pseudocode Code --- #

'''
- Create a list the possible value of the coins
- Create an list of empty lists for each coin Value

- For coin is the input coins:
    Put the coin in the relevant list of lists
    
- For each index i and value in coin_values
    For each element in the range from 0 to count[i]
      Append value to sorted_coins
'''


# --- Python Code --- #
def counting_sort_coins(coins):

    coin_values = [1, 2, 5, 10, 50]

    count = [0] * len(coin_values)

    for coin in coins:
        for i, value in enumerate(coin_values):
            if coin == value:
                count[i] += 1

    return [value for i, value in enumerate(coin_values) for _ in range(count[i])]


if __name__ == "__main__":

    coins = [1, 50, 2, 1, 10, 5, 2, 50, 10, 1]
    sorted_coins = counting_sort_coins(coins)
    print(sorted_coins)
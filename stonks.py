"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #11 - Stonks (stonks.py)


Author: Chris Lai

Difficulty Level: 8/10

Background: Paul recently got a nice bonus from work and wanted to invest it into the 
stock market. In order to maximize his profit, Paul analyzed some data from recent 
transactions in order to find out which combination of buying and selling stocks would 
net the highest earnings.

Prompt: Given a list of prices (prices[i]) collected throughout the day, find the highest 
profit that Paul can earn if he buys the stock during any hour of the day and then sells 
it during the same day. In total, Paul may buy/sell a total of two times per day, with 
the condition that he must sell everything before buying again.

Constraints: The number of prices “n” in the list are constrained to 24 >= n > 0 and 
the prices “i” must be constrained to 10^5 >= i >= 0.

Test Cases:
Input: [1, 2, 3, 4, 5, 0], Output: 4
Buy during hour 1 (price = 1), sell during hour 5 (price = 5), net profit = 5 - 1 = 4

Input: [7, 5, 3, 2, 1], Output: 0
DO NOT BUY (declining prices, no profit possible)

Input: [1, 3, 3, 5, 4, 0, 3, 8, 5, 5], Output: 12
Buy during hour 1 (price = 1), sell during hour 4 (price = 5), net profit = 5 - 1 = 4. 
Then, buy during hour 6 (price = 0), sell during hour 8 (price = 8), net profit = 8 - 0 = 8. 
Total profit = 4 + 8 = 12.


Demo: [7, 1, 5, 3, 4, 0], Output: 5
Buy during hour 2 (price = 1), sell during hour 3 (price = 5), net profit = 5 - 1 = 4.
Then, buy during hour 4 (price = 3), sell during hour 5 (price = 4), net profit = 4 - 3 = 1
Total profit = 4 + 1 = 5

What the code does:

----------------------------------- Window #1 -----------------------------------
Iterator        x               min_price_1     x - min_price_1     max_profit_1
0               7               7               7 - 7 = 0           0               
1               1               1               1 - 1 = 0           0
2               5               1               5 - 1 = 4           4
3               3               1               3 - 1 = 2 [X]       4
4               4               1               4 - 1 = 3 [X]       4
5               0               0               0 - 0 = 0 [X]       4

----------------------------------- Window #2 -----------------------------------
Iterator        x               max_price_2     max_price_2 - x     max_profit_2
5               0               0               0 - 0 = 0           0               
4               4               4               4 - 4 = 0           0
3               3               4               4 - 3 = 1           1
2               5               5               5 - 5 = 0 [X]       1
1               1               5               5 - 1 = 4           4
0               7               7               7 - 7 = 0 [X]       4

profit_1 = [0, 0, 4, 4, 4, 4]
profit_2 = [4, 4, 1, 1, 0, 0]
profit_s = [4, 4, 5, 5, 4, 4] <- maximum from this list is 5, therefore answer is 5
"""

class Solution:
    def stonks(self, prices):
        min_price_1 = 100000 
        profit_1 = []  
        max_profit_1 = 0 

        for x in prices: 
            if min_price_1 > x:
                min_price_1 = x
            else:
               
                max_profit_1 = max(max_profit_1, x - min_price_1)

            profit_1.append(max_profit_1)

        max_price_2 = 0 
        profit_2 = [0]*len(prices) 
        max_profit_2 = 0

        for i in range(len(prices) - 1, -1, -1): 
            x = prices[i]
            if x > max_price_2: 
               
                max_price_2 =  x
            else:
                max_profit_2 = max(max_profit_2, max_price_2 - x)

            profit_2[i] = max_profit_2

        max_profit = 0 

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.stonks(array)
    print(ans)

if __name__ == "__main__":
    main()

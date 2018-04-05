class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        """ compare
        1 5 4 3 6 2 9 7 6 8 9
        """
        
        if len(prices) < 2:
            return 0
        
        increase = True
        cur_profit = 0
        buy_point = prices[0]
        for p, p_1 in zip(prices[:-1], prices[1:]):
            
            if increase:
                if p_1 < p: # hit the top
                    increase = False
                    cur_profit += (p - buy_point)
                    buy_point = None
            else:
                if p_1 > p: # hit the bottom
                    increase = True
                    buy_point = p
        if increase:
            cur_profit += (prices[-1] - buy_point)
            
        return cur_profit


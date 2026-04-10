class StockSpanner:

    def __init__(self):
        self.stock_stack = []

    def next(self, price: int) -> int:
        self.stock_stack.append(price)
        count = 0
        for i in range(len(self.stock_stack) - 1, -1, -1):
            if self.stock_stack[i] <= price:
                count += 1
            else:
                break
            
        return count
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
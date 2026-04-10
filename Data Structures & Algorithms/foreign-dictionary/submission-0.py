from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {}
        for word in words:
            for letter in word:
                adj_list[letter] = []
        for i in range(len(words) - 1):
            first = words[i]
            second = words[i+1]
            for j in range(max(len(first), len(second))):
                if j >= len(second) and j < len(first):
                    return ""
                elif j >= len(first):
                    break
                else:
                    if first[j] != second[j]:
                        adj_list[first[j]].append(second[j])
                        break
        
        print(adj_list)
        colors = defaultdict(int)
        for key, value in adj_list.items():
            colors[key] = 0
        
        order_deque = deque()
        can_sort = True
        def dfs(node):
            nonlocal can_sort
            colors[node] = 1

            for adj in adj_list[node]:
                if colors[adj] == 1:
                    can_sort = False
                    return
                if colors[adj] == 0:
                    dfs(adj)
            
            colors[node] = 2
            order_deque.appendleft(node)
        
        for key, value in colors.items():
            if value == 0:
                dfs(key)
        
        if not can_sort:
            return ""
        
        return "".join(order_deque)

        


            
        


        
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        group_list = defaultdict(list)
        wordList.append(beginWord)
        wordList = list(set(wordList))

        if endWord not in wordList:
            return 0

        for word in wordList:
            for i in range(len(word)):
                group_list[word[0:i] + '*' + word[i+1:]].append(word)
        
        
        
        def bfs(beginWord):
            changes = 1
            q = deque([beginWord])
            visited = set()
            visited.add(beginWord)
            
            while q:
                for i in range(len(q)):
                    curr = q.popleft()
                    if curr == endWord:
                        return changes
                    neighbors = []
                    for j in range(len(curr)):
                        neighbors.extend(group_list[curr[0:j] + '*' + curr[j+1:]])
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)
                changes += 1
            
            return 0
        
        return bfs(beginWord)

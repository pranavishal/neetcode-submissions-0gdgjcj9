from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = defaultdict(list)
        wordList.append(beginWord)
        wordList = list(set(wordList))

        if endWord not in wordList:
            return 0

        for i in range(len(wordList)):
            word = wordList[i]
            for j in range(i + 1, len(wordList)):
                comp = wordList[j]
                diff_count = 0
                for k in range(len(word)):
                    if word[k] != comp[k]:
                        diff_count += 1
                if diff_count == 1:
                    adj_list[word].append(comp)
                    adj_list[comp].append(word)
        
        
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
                    for neighbor in adj_list[curr]:
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)
                changes += 1
            
            return 0
        
        return bfs(beginWord)

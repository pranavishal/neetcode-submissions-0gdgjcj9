class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.word = True
    
    def search(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.word
    
    def startsWith(self, prefix):
        curr = self.root
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_trie = PrefixTrie()
        for word in words:
            word_trie.insert(word)
        
        results = set()
        
        all_words = set(words)

        def dfs(pos, pre):
            i, j = pos
            curr = pre + board[i][j]
            if not word_trie.startsWith(curr):
                return
            
            if curr in all_words:
                results.add(curr)
            
            neighbors = []
            if i > 0:
                neighbors.append((i - 1, j))
            if i < len(board) - 1:
                neighbors.append((i + 1, j))
            if j > 0:
                neighbors.append((i, j - 1))
            if j < len(board[0]) - 1:
                neighbors.append((i, j + 1))

            for neighbor in neighbors:
                letter = board[i][j]
                board[i][j] = '#'
                dfs(neighbor, curr)
                board[i][j] = letter


        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs((i, j), "")
        
        return list(results)
                

        
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
        self.word_val = None

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
        curr.word_val = word
    
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

        def dfs(pos, node):
            i, j = pos
            letter = board[i][j]
            if letter not in node.children:
                return
            
            new_node = node.children[letter]
            if new_node.word:
                results.add(new_node.word_val)
                new_node.word = False
                new_node.word_val = None
            
            neighbors = []
            if i > 0:
                neighbors.append((i - 1, j))
            if i < len(board) - 1:
                neighbors.append((i + 1, j))
            if j > 0:
                neighbors.append((i, j - 1))
            if j < len(board[0]) - 1:
                neighbors.append((i, j + 1))

            letter = board[i][j]
            board[i][j] = '#'
            for neighbor in neighbors:
                dfs(neighbor, new_node)

            board[i][j] = letter


        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs((i, j), word_trie.root)
        
        return list(results)
                

        
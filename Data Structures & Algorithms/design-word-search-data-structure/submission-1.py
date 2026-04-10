class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.word = True
    
    def searchNode(self, node, word):
        curr = node
        for i, letter in enumerate(word):
            if letter != ".":
                if letter not in curr.children:
                    return False
                else:
                    curr = curr.children[letter]
            else:
                for key, val in curr.children.items():
                    if self.searchNode(val, word[i+1:]):
                        return True
                return False
        return curr.word
        

    def search(self, word: str) -> bool:
        curr = self.root
        for i, letter in enumerate(word):
            if letter != ".":
                if letter not in curr.children:
                    return False
                else:
                    curr = curr.children[letter]
            else:
                for key, val in curr.children.items():
                    if self.searchNode(val, word[i+1:]):
                        return True
                return False

        return True
        

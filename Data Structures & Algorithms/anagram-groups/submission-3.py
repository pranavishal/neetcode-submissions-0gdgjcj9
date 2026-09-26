from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            letter_list = [0] * 26
            for letter in word:
                letter_list[ord(letter) - ord('a')] += 1
            anagram_map[tuple(letter_list)].append(word)
        
        returnVal = []
        for key, val in anagram_map.items():
            returnVal.append(val)
        
        return returnVal
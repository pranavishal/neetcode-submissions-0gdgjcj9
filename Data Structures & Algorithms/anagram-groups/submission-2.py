from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_count_map = defaultdict(list)
        grouped_anagrams = []
        for word in strs:
            letter_counts = [0] * 26
            for s in word:
                letter_counts[ord(s) - ord('a')] += 1
            letter_count_map[tuple(letter_counts)].append(word)
        
        for key, val in letter_count_map.items():
            grouped_anagrams.append(val)
        
        return grouped_anagrams


        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # 1. make a map where a key represents 26 length tuple of lower case letters
        # 2. Iterate through strs, and generate this tuple for each string
        # 3. if this tuple exists in the map, append it to the value of the map (list of strs)
        # After that iterate through the map, and append all the values into a final list

        charTupleMap = {}

        for s in strs:
            sTuple = ([0] * 26)
            key = tuple(sTuple)
            for i in range(len(s)):
                sTuple[ord(s[i]) - ord('a')] += 1
                key = tuple(sTuple)
            if key in charTupleMap:
                charTupleMap[key].append(s)
            else:
                charTupleMap[key] = [s]
        
        finalList = []

        for key, value in charTupleMap.items():
            finalList.append(value)
        
        return finalList
        
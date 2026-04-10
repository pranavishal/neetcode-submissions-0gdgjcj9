class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answerList = []
        sortedNums = sorted(nums)
        print(sortedNums)

        seenIVals = set()
        for i in range(len(sortedNums)):
            if sortedNums[i] in seenIVals:
                continue
            
            seenIVals.add(sortedNums[i])
            j = i + 1
            k = len(sortedNums) - 1

            seenJSet = set()
            seenKSet = set()
            target = 0 - sortedNums[i]
            while j < k:
                val = sortedNums[j] + sortedNums[k]
                if val == target:
                    if not(sortedNums[j] in seenJSet or sortedNums[k] in seenKSet):
                        seenJSet.add(sortedNums[j])
                        seenKSet.add(sortedNums[k])
                        answerList.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    j += 1
                    k -= 1

                
                elif val > target:
                    k -= 1
                
                else:
                    j += 1
            
        return answerList

        
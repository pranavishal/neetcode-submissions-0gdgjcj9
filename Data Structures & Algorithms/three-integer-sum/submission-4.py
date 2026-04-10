class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answerList = []
        sortedNums = sorted(nums)
        print(sortedNums)

        for i in range(len(sortedNums)):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue
            j = i + 1
            k = len(sortedNums) - 1


            target = 0 - sortedNums[i]
            while j < k:
                val = sortedNums[j] + sortedNums[k]
                if val == target:
                    answerList.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    while j < k and sortedNums[j] == sortedNums[j + 1]:
                        j += 1
                    j += 1
                    
                    while k > j and sortedNums[k] == sortedNums[k - 1]:
                        k -= 1
                    k -= 1

                
                elif val > target:
                    k -= 1
                
                else:
                    j += 1
            
        return answerList

        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        SumSet = set()
        answerArray = []
        indexMap = {}
        for i in range(len(nums)):
            if nums[i] in indexMap:
                indexMap[nums[i]].append(i)
            else:
                indexMap[nums[i]] = [i]
        
        for i in range(len(nums)):
            target = 0 - nums[i]
            for j in range(i + 1, len(nums)):
                searchVal = target - nums[j]
                if searchVal in indexMap:
                    for val in indexMap[searchVal]:
                        if val == i or val == j:
                            continue
                        if tuple(sorted(list((nums[i], nums[j], nums[val])))) not in SumSet:
                            answerArray.append([nums[i], nums[j], nums[val]])
                            SumSet.add(tuple(sorted(list((nums[i], nums[j], nums[val])))))
                        
        
        return answerArray

                

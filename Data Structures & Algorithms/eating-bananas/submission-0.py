class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # We know that the minimum amount of bananas/hour is 1, and the maximum amount of 
        # bananas/hour is max(piles) since h is at least the amount of elements in piles,
        # and setting k to be max(piles) means we can eat a pile per hour

        # Maybe, we can do a binary search between these two number? start in the middle,
        # see if that amount of hours is doable under 9 hours, if so, that is your right
        # if its not, then its your left 

        # Keep going until you your left or right == your middle

        left = 1
        right = max(piles)
        middle = int((left + right) / 2)

        while True:
            if middle == left or middle == right:
                # check to see if left can work
                testH = 0
                for i in range(len(piles)):
                    testH += math.ceil(piles[i] / left)
                    if testH > h:
                        break
                if testH < h:
                    return left
                
                return right
            
            # see if current middle can work
            testH = 0
            for i in range(len(piles)):
                testH += math.ceil(piles[i] / middle)
                if testH > h:
                    break
            
            if testH > h:
                left = middle
            
            else:
                right = middle
            
            middle = int((left + right) / 2)
        
        return right

                    




            

        
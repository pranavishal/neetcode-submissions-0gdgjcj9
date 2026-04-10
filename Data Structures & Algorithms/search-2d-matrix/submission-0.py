class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        middle = int((left + right) / 2)

        while True:
            if target >= matrix[middle][0] and target <= matrix[middle][len(matrix[0]) - 1]:
                break
            
            if middle == left or middle == right:
                if target >= matrix[left][0] and target <= matrix[left][len(matrix[0]) - 1]:
                    middle = left
                    break
                
                if target >= matrix[right][0] and target <= matrix[right][len(matrix[0]) - 1]:
                    middle = right
                    break
                
                return False
            
            if matrix[middle][0] > target:
                right = middle
                
            
            elif matrix[middle][len(matrix[0]) - 1] < target:
                left = middle
            
            middle = int((left + right) / 2)

        # now binary search on this array

        theArray = matrix[middle]

        left = 0
        right = len(theArray) - 1
        middle = int((left + right) / 2)

        curr = theArray[middle]

        while True:
            if curr == target:
                return True
            
            if middle == left or middle == right:
                if target == theArray[left] or target == theArray[right]:
                    return True
                
                return False
            
            if curr > target:
                right = middle
            
            elif curr < target:
                left = middle
            
            middle = int((left + right) / 2)
            curr = theArray[middle]

        return False



        
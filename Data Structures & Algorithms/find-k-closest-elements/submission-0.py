class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1

        while (right - left + 1) > k:
            left_score, right_score = abs(arr[left] - x), abs(arr[right] - x)
            if left_score <= right_score:
                right -= 1
            elif right_score < left_score:
                left += 1
            else:
                print("BAD CASE: NOT FORSEEN")
        
        return arr[left:right + 1]
        
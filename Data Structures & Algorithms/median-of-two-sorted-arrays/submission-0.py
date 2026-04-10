class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1

        while True:
            mid = (l + r) // 2
            Aleft = A[mid] if mid >= 0 else float('-inf')
            Aright = A[mid + 1] if (mid + 1) < len(A) else float('inf')
            Bleft = B[half - mid - 2] if (half - mid - 2) >= 0 else float('-inf')
            Bright = B[half - mid - 1] if (half - mid - 1) < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                print(half)
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = mid - 1
            else:
                l = mid + 1
        
            
        
        
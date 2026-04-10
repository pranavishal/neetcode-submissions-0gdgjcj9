class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = 0
        right = len(matrix) - 1
        top = 0
        bottom = len(matrix) - 1

        while left < right:
            for i in range(left, right):
                curr = (top, i)
                num_steps = right - left
                curr_num = matrix[top][i]
                while True:
                    if curr[0] == top and curr[1] < right:
                        curr = (curr[0], curr[1] + 1)
                        
                    elif curr[0] < bottom and curr[1] == right:
                        curr = (curr[0] + 1, curr[1])
                    
                    elif curr[0] == bottom and curr[1] > left:
                        curr = (curr[0], curr[1] - 1)
                    
                    elif curr[0] > top and curr[1] == left:
                        curr = (curr[0] - 1, curr[1])
                    
                    num_steps -= 1
                    if num_steps == 0:
                        temp = matrix[curr[0]][curr[1]]
                        matrix[curr[0]][curr[1]] = curr_num
                        curr_num = temp
                        num_steps = right - left
                    
                    if curr == (top, i):
                        break
            
            left += 1
            right -= 1
            top += 1
            bottom -= 1
                    


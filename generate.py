"""
Pascal's Triangle
Link: https://leetcode.com/problems/pascals-triangle/
"""

def generate(self, numRows: int) -> List[List[int]]:
    arr = [[1]]
    for i in range(1, numRows):
        ## Idea: add 0 at leftmost and rightmost side. 
        temp = [0] + arr[i-1] + [0]
        cur_arr = []
        for j in range(i+1):
            cur_arr.append(temp[j] + temp[j+1])
        arr.append(cur_arr)
    return arr

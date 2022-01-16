"""
Two Sum II - Input Array Is Sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Time complexity: O(n)
"""

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    ## Idea: using two pointers.
    l, r = 0, len(numbers)-1
    while l < r:
        current_sum = numbers[l] + numbers[r]
        if target == current_sum:
            return [l+1, r+1]
        
        # if target larger than sum then shift left pointer to 1 position towards right side. 
        if target > current_sum:
            l += 1
        # if target smaller than sum then shift right pointer to 1 position towards left side. 
        if target < current_sum:
            r -= 1
    
    return None

if __name__ == '__main__':
    print(twoSum([1,3,4,5,7,10,11], 9))

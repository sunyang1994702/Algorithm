"""
Missing Number
Link: https://leetcode.com/problems/missing-number/
"""

def missingNumber_1(self, nums: List[int]) -> int:
    # Method1
    for i in range(len(nums)+1):
        if i in nums:
            continue
        else:
            return i


def missingNumber_2(self, nums: List[int]) -> int:
    # Method2. The summation about range(0, n) - summation about nums
    sum_num = sum([i for i in range(len(nums)+1)])

    return sum_num - sum(nums)


def missingNumber_3(self, nums: List[int]) -> int:
    # Method3. The summation about range(0, n) - summation about nums
    res = len(nums)
    for i in range(len(nums)):
        res += (i - nums[i])
    return res
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
def threeSum(self, nums: List[int]) -> List[List[int]]:

    """

    :param self:
    :param nums:
    :return:

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Input: nums = []
    Output: []

    Input: nums = [0]
    Output: []
    """
    r, d = set(), set()
    seen = {}
    for i, val_1 in enumerate(nums):

        if val_1 not in d: #This line can be deleted, but somehow it will incease the runtime, I dont understand
            d.add(val_1)
            for j, val_2 in enumerate(nums[i + 1:], i + 1):
                complement = -val_1 - val_2
                if complement in seen and seen[complement] == i: #The and condition is necessary to avoid (nums[i], nums[i], complement)
                    r.add(tuple(sorted((val_1, val_2, complement))))
                seen[val_2] = i
    return r


#Summary: This problem has the core idea of twoSum, just make the "target" dynamic

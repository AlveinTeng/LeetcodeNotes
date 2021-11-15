"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that
 adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses
 were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.
"""

###The idea is simple, we can just maximize up to the ith house, then it has the same logic has fibonacci sequences
### This solution is a bit faster than the solution on leetcode I think although the core idea is the same6
def rob(self, nums: list[int]) -> int:
    # Let dp be the array where stores the maximum when robs to the ith house

    # Base case
    l = len(nums)
    if l == 1:
        return nums[0]
    if l == 2:
        return max(nums[0], nums[1])
    dp = [0] * l
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, l):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[l - 1]
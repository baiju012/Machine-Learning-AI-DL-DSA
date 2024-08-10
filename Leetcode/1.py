# Given an array of integers (nums) and a target integer (target), find the indices of the two numbers in the array that add up to the target.

class Solution:
  def Twosum(self, num, target):
    num_hash = {}
    for i in range(len(num)):
      if target - num[i] in num_hash:
        return [num_hash[target - num[i]], i]
      num_hash[num[i]] = i




# class Solution:
#     def twoSum(self, nums, target):
#         nums_hash = {}  # Step 1: Initialize an empty hash map (dictionary)
        
#         for i in range(len(nums)):  # Step 2: Iterate through the list of numbers
#             if target - nums[i] in nums_hash:  # Step 3: Check if the complement of nums[i] is in the hash map
#                 return [nums_hash[target - nums[i]], i]  # Step 4: If found, return the indices
#             nums_hash[nums[i]] = i  # Step 5: Store the current number with its index in the hash map

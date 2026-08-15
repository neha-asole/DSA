class Solution(object):
    def maxSubArray(self, nums):
        sum=0
        maxSum =float('-inf')
        for i in range(len(nums)):
          if sum == 0:
            start=i
          sum=sum+nums[i]
          if sum>maxSum:
            maxSum=sum
          if sum<0:
            sum=0
        return maxSum        
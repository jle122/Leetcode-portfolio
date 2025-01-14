class Solution(object):
    def majorityElement(self, nums):
        counts = {}
        for i in nums: # fills dict with all values in nums and the amount of times each value appears
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
        maxCount = -1
        for i in nums: # finds the majority element 
            if counts[i] > maxCount and counts[i] > len(nums)/2:
                maxCount = i
        return maxCount
        
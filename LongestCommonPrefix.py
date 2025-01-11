class Solution(object):
    def longestCommonPrefix(self, strs):
        min = float('inf')
        shortestword = ""
        prefix = ""
        for i in strs: # finds the shortest word in the array
            if min > len(i):
                min = len(i)
                shortestword = i
        for i in range(min): # for loop checking for matching letters at correct locations
            hasLetter = True
            for j in strs:
                if j != shortestword and j[i] != shortestword[i]:
                    hasLetter = False
            if hasLetter == True:
                prefix += shortestword[i]
            else:
                break
        return prefix
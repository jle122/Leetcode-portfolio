class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        word = []
        while i >= 0: # finds the last character of the last word
            if s[i] != " ":
                break
            i -= 1
        j = i
        while j >= 0: # adds all characters of the word to a list
            if s[j] != " ":
                word += s[j]
                j -= 1
            else:
                break
        return len(word) # return length of list
        
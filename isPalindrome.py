class Solution(object):
    def isPalindrome(self, s):
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # set up strings that store acceptable characters
        lowercase = uppercase.lower()
        numbers = "0123456789"
        s = s.replace(" ", '') 
        for i in s: # lowercases and removes special characters
            if i in uppercase:
                s = s.replace(i, i.lower())
            elif i not in uppercase and i not in lowercase:
                if i in numbers:
                    continue
                else:
                    s = s.replace(i, '')
            else:
                continue
        mid = len(s) // 2
        for i in range(mid): # checks if it's a palindrome
            if s[i] != s[(len(s)-1) - i]:
                return False
        return True
        
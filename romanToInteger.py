class Solution(object):
    def romanToInt(self, s):
        numerals = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000} # stores roman numeral values for easy access
        sum = 0 # return value
        i = 0 #counter
        while i < len(s):
            if i != len(s) - 1: # all values before last roman numeral
                if s[i] == "C": # checks all possible values involving C (100)
                    if s[i + 1] == "M":
                        sum += 900
                        i += 2
                    elif s[i + 1] == "D":
                        sum += 400
                        i += 2
                    else:
                        sum += 100
                        i += 1
                elif s[i] == "X": # checks all possible values involving X (10)
                    if s[i + 1] == "C":
                        sum += 90
                        i += 2
                    elif s[i + 1] == "L":
                        sum += 40
                        i += 2
                    else:
                        sum += 10
                        i += 1
                elif s[i] == "I": # checks all possible values involving I (1)
                    if s[i + 1] == "X":
                        sum += 9
                        i += 2
                    elif s[i + 1] == "V":
                        sum += 4
                        i += 2
                    else:
                        sum += 1
                        i += 1
                else:
                    sum += numerals[s[i]]
                    i += 1
            else:
                sum += numerals[s[i]]
                i += 1
        return sum
        
class Solution(object):
    def plusOne(self, digits):
        all9 = True
        for i in digits: # checks the case if all the digits are 9
            if i != 9:
                all9 = False
                break
        if all9 == True: # calculates when all digits are 9 (the sum is 10^(len(digits)))
            arr = [1]
            for i in range(len(digits)):
                arr.append(0)
            return arr
        else:
            i = len(digits) - 1
            if digits[i] != 9: # checks for additions without carrying the 1
                digits[i] += 1
                return digits
            else:
                while i >= 0:
                    digits[i] += 1
                    if digits[i] == 10: # indicates a carry over if digits[i] = 10 (digits[i] was 9)
                        i -= 1
                    else: # stops when there is no more carry over needed
                        break
                for j in range(len(digits)): # changes all 10s to zeros to get correct digits
                    if digits[j] == 10:
                        digits[j] = 0
        return digits

            


            
         
            
                
        
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for i in range(len(matrix[0])): # iterates through the values of the last row, then goes diagonal upwards left
            r = len(matrix) - 1
            if r == len(matrix) - 1 and i == 0:
                continue
            elif i == len(matrix[0]) - 1: # once last value in row is reached, check all diagonals that don't begin on bottom row
                while r >= 0:
                    target = matrix[r][i]
                    j = r - 1
                    k = i - 1
                    while j >= 0 and k >= 0:
                        if matrix[j][k] != target:
                            return False
                        else:
                            j -= 1
                            k -= 1
                    r -= 1
            else:
                target = matrix[r][i]
                j = r - 1
                k = i - 1
                while j >= 0 and k >= 0:
                    if matrix[j][k] != target:
                        return False
                    else:
                        j -= 1
                        k -= 1
        return True
        
class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in matrix:
            for j in range(len(i)):
                if i[j]==target:
                    return True
                    break
        return False    
class Solution
    def diagonalSum(self, mat List[List[int]]) - int
        if len(mat) == 1
            return mat[0][0]
        temp = 0
        for i in range(len(mat))
            temp += mat[i][i]
            temp += mat[i][len(mat)-1-i]
        if(len(mat) %2 == 0)
            return temp
        else
            return temp - mat[len(mat)2][len(mat)2]
        
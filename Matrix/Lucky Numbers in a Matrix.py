
class Solution
    def luckyNumbers (self, matrix List[List[int]]) - List[int]
        rowMin = []
        colMax = []
        for i in range(len(matrix))
            rowMin.append(min(matrix[i]))
            
        for i in range(len(matrix[0]))
            colMax.append(max([matrix[j][i] for j in range(len(matrix))]))
        
        if(len(rowMin) = len(colMax))
            for i in rowMin
                if(i in colMax)
                    return [i]
        else 
            for i in colMax
                if i in rowMin
                    return [i]
        
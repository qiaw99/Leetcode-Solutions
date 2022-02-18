class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        indices = {}
        res = []
        zero = 0
        for i in range(len(mat)):
            if(zero in mat[i]):
                indices[i] = mat[i].index(0)
            else:
                indices[i] = len(mat[i])
        for key, value in sorted(indices.items(), key=lambda item: item[1]):
            res.append(key)
        del indices
        return res[:k]
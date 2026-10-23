class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euc_dist(l):
            return l[0]**2 + l[1]**2
        p_n_d = {}
        for coor in points:
            p_n_d[tuple(coor)] = euc_dist(coor)

        pnd = sorted(p_n_d, key = p_n_d.get)
        return [list(p) for p in pnd[:k]] 
        

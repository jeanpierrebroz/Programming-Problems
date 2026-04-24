class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #[1, 2, 3], [5, 5, 5], [8, 1, 2], [8, 4, 4]        #8, 3, 3
        #we know that if any merge would cause us to go over the bound for a, b, or c, then we can't do it
        #greedily find the minimum distance merge every time? or do we just prune
        a, b, c = target

        plausible = []

        for ta, tb, tc in triplets:
            if ta <= a and tb <= b and tc <= c:
                plausible.append([ta, tb, tc])
        
        if len(plausible) == 0:
            return False

        hit = [0, 0, 0]
        for ta, tb, tc in plausible:
            if ta == a:
                hit[0] = 1
            if tb == b:
                hit[1] = 1
            if tc == c:
                hit[2] = 1
        if sum(hit) == 3:
            return True
        return False
        

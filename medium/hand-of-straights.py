class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        hand.sort()

        count = defaultdict(int)
        for h in hand:
            count[h] += 1
        
        for h in hand:
            if count[h] == 0:
                continue
            target = h
            for _ in range(groupSize):
                if target not in count or count[target] == 0:
                    return False
                
                count[target] -= 1
                target += 1
            
        
        return True
        
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #minimum weight capacity will have to be the max of weights
        #the max weight capacity will have to be the sum of weights
        #optimize for w

        def runSimulation(weights, days, capacity):
            taken = 1
            curr_weight = 0
            for r in range(len(weights)):
                if curr_weight + weights[r] > capacity:
                    curr_weight = weights[r]
                    taken += 1
                else:
                    curr_weight += weights[r]
            return taken

        min_weight, max_weight = max(weights), sum(weights)

        while min_weight < max_weight:
            
            w = (max_weight + min_weight) // 2

            days_taken = runSimulation(weights, days, w)

            if days_taken <= days:
                max_weight = w
            else:
                min_weight = w + 1


        return min_weight
heap = []
        result = float('inf')

        arr = sorted([(w / q, q) for q, w in zip(quality, wage)])

        quality_sum = 0
        
        for ratio, quality in arr:

            heapq.heappush_max(heap, quality)
            quality_sum += quality

            if len(heap) > k:
                quality_sum -= heapq.heappop_max(heap)
            
            if len(heap) == k:
                result = min(result, quality_sum * ratio)
        
        return result
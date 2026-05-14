class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        #brute force would be to make a list of all positions in the array, then for each street light illuminate that one
        #however, we do a lot of work for this and we only need the smallest position
        counts = defaultdict(int)

        for position, r in lights:
            counts[position - r] += 1
            counts[position + r + 1] -= 1
        
        brightness, max_brightness, position = 0, 0, -float('inf')


        for light in sorted(counts.items()):
            brightness += light[1]
            if brightness > max_brightness:
                max_brightness = brightness
                position = light[0]
        
        return position
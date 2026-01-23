class Solution:
    def compress(self, chars: List[str]) -> int:
        #O(n) time, O(1) space

        read, write = 0,0
        while read < len(chars):
            char = chars[read]
            count = 0
            while read < len(chars) and char == chars[read]:
                read += 1
                count +=1 
            
            chars[write] = char
            write +=1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write
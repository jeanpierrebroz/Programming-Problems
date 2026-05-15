class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        #only construct paths if they're valid, don't brute force everything
        result = []
        s = [int(num) for num in s]
        
        def backtrack(idx, path, curr_num):
            if idx == len(s):
                if len(path) == 4:
                    result.append('.'.join([str(i) for i in path]))
                return
            
            if len(path) == 4: return

            curr_num = curr_num * 10 + s[idx]
            
            if curr_num < 256:
                path.append(curr_num)
                backtrack(idx + 1, path, 0)
                path.pop()
                
                if curr_num != 0:
                    backtrack(idx + 1, path, curr_num)
    
        backtrack(0, [], 0)
        return result
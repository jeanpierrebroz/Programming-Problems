class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                curr_str = ""
                while stack and stack[-1] != "[":
                    curr_str = stack.pop() + curr_str
                
                stack.pop()
                
                k_str = ""
                while stack and stack[-1].isdigit():
                    k_str = stack.pop() + k_str
                
                stack.append(int(k_str) * curr_str)
        
        return "".join(stack)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            #if it's a number, we know we want to add it to stack
            if t not in "+-*/":
                stack.append(int(t))
            
            
            else:
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    res = a + b
                elif t == "-":
                    res = a - b
                elif t == "*":
                    res = a * b
                else:
                    res = int(a / b)
                
                stack.append(res)
        
        return stack[0]
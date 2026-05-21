class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for i in tokens:
            if i in '+-*/':
                item1 = stack.pop()
                item2 = stack.pop()
                
                if i == '+':
                    result = item2+item1
                elif i == '-':
                    result = item2-item1
                elif i == '*':
                    result = item2*item1
                elif i == '/':
                    result = int(item2/item1)
                stack.append(result)
            
            else:
                stack.append(int(i))

            
        return int(stack[0])
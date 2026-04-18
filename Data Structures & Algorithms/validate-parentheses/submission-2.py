class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        for i in range(n):
            nte = len(stack) != 0

            if nte and stack[-1] == '(' and s[i] == ')':
                stack.pop()
            elif nte and stack[-1] == '{' and s[i] == '}':
                stack.pop()
            elif nte and stack[-1] == '[' and s[i] == ']':
                stack.pop()
            else:
                stack.append(s[i])

        if len(stack) == 0:
            return True
        else:
            return False


        
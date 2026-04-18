class Solution:
    def calPoints(self, operations: List[str]) -> int:
        length = len(operations)
        stack = []
        for i in range(length):
            if operations[i] == "C":
                stack.pop()

            elif operations[i] == "D":
                a = 2*stack[-1]
                stack.append(a)

            elif operations[i] == "+":
                a = int(stack[-1])
                b = int(stack[-2])
                stack.append(a+b)
            
            else:
                stack.append(int(operations[i]))

        total_sum = sum(stack)
        return total_sum
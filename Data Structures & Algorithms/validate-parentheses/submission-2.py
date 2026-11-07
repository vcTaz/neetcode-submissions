class Solution:
    def isClosing(self, s: str) -> bool:
        return s == ')' or s == ']' or s == '}'

    def isMatch(self, start: str, end: str) -> bool:
        if start == '(' and end == ')':
            return True
        elif start == '[' and end == ']':
            return True
        elif start == '{' and end == '}':
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if len(stack) == 0 and self.isClosing(char):
                return False
            elif self.isClosing(char):
                if self.isMatch(stack[-1], char):
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(char)
        
        return len(stack) == 0
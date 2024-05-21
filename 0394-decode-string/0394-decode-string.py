class Solution:
    def decodeString(self, s: str) -> str:
        stack=""
        for i in s:
            if i != ']':
                stack+=i
            else:
                number = ''
                curr = len(stack)-1
                while not stack[curr].isdigit():
                    curr -= 1 
                first = curr
                number += stack[curr]
                curr -= 1
                while stack[curr].isdigit():
                    number += stack[curr]
                    curr -= 1
                last = curr + 1 
                stack = stack[:last] + (int(number[::-1]) * stack[first+2:])
        return stack
        
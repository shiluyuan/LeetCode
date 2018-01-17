"""
implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
"""
def calculate(self, s):
    res, num, sign, stack = 0, 0, 1, [1]
    for i in s+"+":
        if i.isdigit():
            num = 10*num + int(i)
        elif i in "+-":
            res += num * sign * stack[-1]
            sign = 1 if i=="+" else -1
            num = 0
        elif i == "(":
            stack.append(sign * stack[-1])
            sign = 1
        elif i == ")":
            res += num * sign * stack[-1]
            num = 0
            stack.pop()
    return res


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        signs = [1, 1]
        i = 0

        while i < len(s):
            x = s[i]
            if x.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                res += signs.pop() * int(s[start:i])
                continue
            elif x in '(+-':
                signs += signs[-1] * (1, -1)[x == '-'],
            elif x == ')':
                signs.pop()

            i += 1

        return res
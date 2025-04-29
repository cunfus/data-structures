import sys
import os
sys.path.append(os.path.dirname(__file__))

from stack import Stack


def infix_to_postfix(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    s = Stack()

    for token in infix:
        if token.isspace():
            continue
        elif token.isdigit():
            output.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            operator = s.pop()
            while operator != '(':
                output.append(operator)
                operator = s.pop()
        elif token in "+-*/":
            while (s and s.peek() != '(' and precedence.get(s.peek(), 0) >= precedence[token]):
                output.append(s.pop())
            s.push(token)
    else:
        while s.is_empty() == False:
            output.append(s.pop())
    
    return ' '.join(output)




if __name__ == "__main__":
    """
    (6 * (5 + ((2 + 3) * 8) + 3))
    """
    
    result = infix_to_postfix("(6 * (5 + ((2 + 3) * 8) + 3))")
    print(result)